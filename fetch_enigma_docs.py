#!/usr/bin/env python3
"""
Script to fetch Enigma GraphQL API documentation and create individual markdown files.
"""

import requests
import time
import re
from pathlib import Path
from bs4 import BeautifulSoup
import html2text

# Base configuration
BASE_URL = "https://documentation.enigma.com/reference/graphql_api"
BASE_DIR = Path("/Users/benjamincrane/api-reference-docs-new/enigma/08-reference")

# Define all sections and their items
SECTIONS = {
    "00-overview": {
        "folder": "00-overview",
        "url_section": "",  # Overview is the main page
        "items": [
            ("graphql-api-reference", "")  # Already created, will populate
        ]
    },
    "01-directives": {
        "folder": "01-directives",
        "url_section": "directives",
        "items": [
            ("coalesce", "coalesce"),
            ("compact", "compact"),
            ("dadjoke", "dadjoke"),
            ("dateAccessible", "date-accessible"),
            ("include", "include"),
            ("join", "join"),
            ("lower", "lower"),
            ("map", "map"),
            ("skip", "skip"),
            ("slice", "slice"),
            ("trim", "trim"),
            ("upper", "upper"),
        ]
    },
    "02-enums": {
        "folder": "02-enums",
        "url_section": "enums",
        "items": [
            ("EnrichmentProvider", "enrichment-provider"),
            ("EntityType", "entity-type"),
            ("ListSearchField", "list-search-field"),
            ("ListType", "list-type"),
            ("OutputFormat", "output-format"),
            ("TinType", "tin-type"),
        ]
    },
    "03-inputs": {
        "folder": "03-inputs",
        "url_section": "inputs",
        "items": [
            ("AddressInput", "address-input"),
            ("CancelListMaterializationInput", "cancel-list-materialization-input"),
            ("ColumnMappingInput", "column-mapping-input"),
            ("Conditions", "conditions"),
            ("ConnectionConditions", "connection-conditions"),
            ("CreateListInput", "create-list-input"),
            ("CreateListMaterializationInput", "create-list-materialization-input"),
            ("DeleteListInput", "delete-list-input"),
            ("EnrichmentInput", "enrichment-input"),
            ("EntityIdentifier", "entity-identifier"),
            ("FieldAliasInput", "field-alias-input"),
            ("GetListMaterializationInput", "get-list-materialization-input"),
            ("ListConditionsInput", "list-conditions-input"),
            ("ListSearchInputInput", "list-search-input-input"),
            ("OutputSpec", "output-spec"),
            ("PersonInput", "person-input"),
            ("SearchFieldGroupInput", "search-field-group-input"),
            ("SearchInput", "search-input"),
            ("SearchListsInput", "search-lists-input"),
            ("SuggestionInput", "suggestion-input"),
            ("TinInput", "tin-input"),
            ("UpdateListInput", "update-list-input"),
            ("UpdateListMaterializationInput", "update-list-materialization-input"),
        ]
    },
    "04-interfaces": {
        "folder": "04-interfaces",
        "url_section": "interfaces",
        "items": [
            ("Entity", "entity"),
            ("NodeFunctions", "node-functions"),
        ]
    },
    "05-mutations": {
        "folder": "05-mutations",
        "url_section": "mutations",
        "items": [
            ("cancelListMaterialization", "cancel-list-materialization"),
            ("createList", "create-list"),
            ("createListMaterialization", "create-list-materialization"),
            ("createSuggestion", "create-suggestion"),
            ("deleteList", "delete-list"),
            ("updateList", "update-list"),
            ("updateListMaterialization", "update-list-materialization"),
        ]
    },
    "06-objects": {
        "folder": "06-objects",
        "url_section": "objects",
        "items": [
            # Core entities
            ("Account", "account"),
            ("Address", "address"),
            ("Brand", "brand"),
            ("LegalEntity", "legal-entity"),
            ("OperatingLocation", "operating-location"),
            ("Person", "person"),
            # Will fetch the objects section page to get the complete list
        ]
    },
    "07-queries": {
        "folder": "07-queries",
        "url_section": "queries",
        "items": [
            ("account", "account"),
            ("search", "search"),
            ("listMaterialization", "list-materialization"),
        ]
    },
    "08-scalars": {
        "folder": "08-scalars",
        "url_section": "scalars",
        "items": [
            ("Boolean", "boolean"),
            ("Date", "date"),
            ("DateTime", "date-time"),
            ("Float", "float"),
            ("ID", "id"),
            ("Int", "int"),
            ("JSON", "json"),
            ("JSONString", "json-string"),
            ("String", "string"),
            ("UUID", "uuid"),
        ]
    },
    "09-unions": {
        "folder": "09-unions",
        "url_section": "unions",
        "items": [
            ("SearchUnion", "search-union"),
        ]
    },
    "10-deprecated": {
        "folder": "10-deprecated",
        "url_section": "deprecated",
        "items": [
            # Will check if there are deprecated items
        ]
    },
}


def fetch_page_content(url):
    """Fetch content from a URL and convert to markdown."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        # Return raw HTML for now - we'll use a more sophisticated approach
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None


def extract_markdown_content(html):
    """Extract main content from HTML and convert to markdown."""
    try:
        # Parse HTML
        soup = BeautifulSoup(html, 'html.parser')

        # Remove script and style elements
        for script in soup(["script", "style", "nav", "header", "footer"]):
            script.decompose()

        # Get the main content area (adjust selector based on actual page structure)
        main_content = soup.find('main') or soup.find('article') or soup.body

        if not main_content:
            return None

        # Convert to markdown
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = False
        h.ignore_emphasis = False
        h.body_width = 0  # Don't wrap lines
        h.single_line_break = False

        markdown = h.handle(str(main_content))
        return markdown.strip()
    except Exception as e:
        print(f"Error converting HTML to markdown: {e}")
        return None


def create_file(folder, filename, content):
    """Create a markdown file with the given content."""
    file_path = BASE_DIR / folder / f"{filename}.md"
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return file_path


def main():
    """Main execution function."""
    print("Starting Enigma GraphQL API documentation fetch...")
    total_files = 0
    successful = 0
    failed = 0

    for section_key, section_data in SECTIONS.items():
        folder = section_data["folder"]
        url_section = section_data["url_section"]
        items = section_data["items"]

        if not items:
            print(f"\nSkipping {section_key} - no items defined")
            continue

        print(f"\n{'='*60}")
        print(f"Processing: {section_key}")
        print(f"{'='*60}")

        for filename, url_slug in items:
            total_files += 1

            # Construct URL
            if section_key == "00-overview":
                url = BASE_URL
            else:
                url = f"{BASE_URL}/{url_section}/{url_slug}"

            print(f"\nFetching: {filename}")
            print(f"URL: {url}")

            # Fetch content
            html_content = fetch_page_content(url)

            if html_content:
                # Convert to markdown
                markdown_content = extract_markdown_content(html_content)

                if markdown_content:
                    create_file(folder, filename, markdown_content)
                    print(f"✓ Created: {folder}/{filename}.md")
                    successful += 1
                else:
                    print(f"✗ Failed to convert: {folder}/{filename}.md")
                    failed += 1
            else:
                print(f"✗ Failed to fetch: {folder}/{filename}.md")
                failed += 1

            # Be nice to the server
            time.sleep(0.5)

    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"Total files: {total_files}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
