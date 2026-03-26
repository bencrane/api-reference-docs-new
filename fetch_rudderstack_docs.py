#!/usr/bin/env python3
"""
Fetch all RudderStack documentation pages and save as markdown files.
"""

import os
import re
import sys
import time
import requests
from bs4 import BeautifulSoup
import html2text
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_URL = "https://www.rudderstack.com/docs/"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rudderstack")

# Configure html2text
def get_converter():
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_emphasis = False
    h.body_width = 0  # Don't wrap lines
    h.protect_links = True
    h.wrap_links = False
    h.single_line_break = False
    return h


def url_to_filepath(url):
    """Convert a URL to a local file path."""
    parsed = urlparse(url)
    path = parsed.path
    # Remove /docs/ prefix
    path = re.sub(r'^/docs/?', '', path)
    # Remove trailing slash
    path = path.rstrip('/')

    if not path:
        return os.path.join(OUTPUT_DIR, "index.md")

    # Split into parts
    parts = path.split('/')

    # The last part becomes the filename
    filename = parts[-1] + ".md"

    # Everything else is the directory
    if len(parts) > 1:
        dirpath = os.path.join(OUTPUT_DIR, *parts[:-1])
    else:
        dirpath = OUTPUT_DIR

    return os.path.join(dirpath, filename)


def fetch_page(url, session):
    """Fetch a page and extract the main content as markdown."""
    try:
        resp = session.get(url, timeout=30)
        resp.raise_for_status()
    except Exception as e:
        return None, str(e)

    soup = BeautifulSoup(resp.text, 'html.parser')

    # Try to find the main content area
    # RudderStack docs use various content containers
    content = None

    # Try common selectors for doc content
    selectors = [
        'article',
        '[class*="content"]',
        'main',
        '.markdown-body',
        '.docs-content',
        '#content',
        '.page-content',
    ]

    for sel in selectors:
        content = soup.select_one(sel)
        if content:
            # Make sure it's not just a nav or sidebar
            text = content.get_text(strip=True)
            if len(text) > 200:
                break
            content = None

    if not content:
        # Fallback: get the body minus nav/sidebar/footer
        content = soup.find('body')
        if content:
            for tag in content.find_all(['nav', 'header', 'footer', 'aside']):
                tag.decompose()
            # Remove script and style
            for tag in content.find_all(['script', 'style']):
                tag.decompose()

    if not content:
        return None, "No content found"

    # Remove navigation elements, sidebars, etc.
    for tag in content.find_all(['nav', 'aside']):
        tag.decompose()
    for tag in content.find_all(class_=re.compile(r'sidebar|nav|menu|footer|cookie|banner')):
        tag.decompose()
    for tag in content.find_all(['script', 'style']):
        tag.decompose()

    # Convert to markdown
    converter = get_converter()
    markdown = converter.handle(str(content))

    # Clean up excessive whitespace
    markdown = re.sub(r'\n{4,}', '\n\n\n', markdown)
    markdown = markdown.strip()

    # Extract title
    title_tag = soup.find('h1')
    if not title_tag:
        title_tag = soup.find('title')
    title = title_tag.get_text(strip=True) if title_tag else ""

    # If the markdown doesn't start with a heading, add the title
    if title and not markdown.startswith('#'):
        markdown = f"# {title}\n\n{markdown}"

    return markdown, None


def load_urls(filepath):
    """Load URLs from file."""
    with open(filepath) as f:
        return [line.strip() for line in f if line.strip()]


def process_url(url, session):
    """Process a single URL: fetch, convert, and save."""
    filepath = url_to_filepath(url)

    # Skip if already exists
    if os.path.exists(filepath):
        return url, "skipped", filepath

    markdown, error = fetch_page(url, session)
    if error:
        return url, f"error: {error}", filepath

    if not markdown or len(markdown) < 50:
        return url, "empty", filepath

    # Create directory
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(markdown)

    return url, "ok", filepath


def main():
    url_file = "/tmp/rudderstack_urls.txt"
    urls = load_urls(url_file)

    print(f"Loaded {len(urls)} URLs")
    print(f"Output directory: {OUTPUT_DIR}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    })

    success = 0
    errors = 0
    skipped = 0
    empty = 0

    # Process with thread pool for speed
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(process_url, url, session): url for url in urls}

        for i, future in enumerate(as_completed(futures)):
            url, status, filepath = future.result()

            if status == "ok":
                success += 1
            elif status == "skipped":
                skipped += 1
            elif status == "empty":
                empty += 1
            else:
                errors += 1

            if (i + 1) % 50 == 0 or status.startswith("error"):
                print(f"[{i+1}/{len(urls)}] {status}: {url}")
                if status == "ok":
                    rel = os.path.relpath(filepath, OUTPUT_DIR)
                    print(f"  -> {rel}")

    print(f"\nDone! Success: {success}, Skipped: {skipped}, Empty: {empty}, Errors: {errors}")
    print(f"Total files in {OUTPUT_DIR}:")
    total = sum(1 for _, _, files in os.walk(OUTPUT_DIR) for f in files if f.endswith('.md'))
    print(f"  {total} markdown files")


if __name__ == "__main__":
    main()
