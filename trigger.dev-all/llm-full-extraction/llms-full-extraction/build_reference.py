#!/usr/bin/env python3
"""
Build structured reference files from split Trigger.dev documentation pages.
Reads source pages from pages/ directory and produces organized .md files.
"""

import os
import re
from pathlib import Path

BASE = Path("/Users/benjamincrane/conductor/workspaces/trigger-dev-github-repo/atlanta/llms-full-extraction")
PAGES = BASE / "pages"

# Mapping: output filename -> list of source page filenames (without .txt)
FILE_MAP = {
    # ── Core Reference ──
    "TASKS.md": [
        "tasks--overview", "writing-tasks-introduction", "tasks--schemaTask",
        "tasks--scheduled", "hidden-tasks", "context", "run-usage"
    ],
    "TRIGGERING.md": ["triggering"],
    "RUNS.md": ["runs"],
    "QUEUES_CONCURRENCY.md": ["queue-concurrency"],
    "WAITS_TOKENS.md": ["wait", "wait-for", "wait-until", "wait-for-token"],
    "ERRORS_RETRIES.md": ["errors-retrying"],
    "SCHEDULING.md": [
        "tasks--scheduled",
        "management--schedules--create", "management--schedules--update",
        "management--schedules--delete", "management--schedules--list",
        "management--schedules--retrieve", "management--schedules--activate",
        "management--schedules--deactivate", "management--schedules--timezones"
    ],
    "REALTIME.md": [
        "realtime--overview", "realtime--how-it-works", "realtime--run-object",
        "realtime--auth", "realtime--backend--overview",
        "realtime--backend--subscribe", "realtime--backend--streams"
    ],
    "STREAMS.md": [
        "tasks--streams", "realtime--backend--streams",
        "realtime--react-hooks--streams"
    ],
    "REACT_HOOKS.md": [
        "realtime--react-hooks--overview", "realtime--react-hooks--streams",
        "realtime--react-hooks--subscribe", "realtime--react-hooks--swr",
        "realtime--react-hooks--triggering", "realtime--react-hooks--use-wait-token"
    ],
    "METADATA_TAGS.md": ["runs--metadata", "tags", "runs--priority"],
    "IDEMPOTENCY.md": ["idempotency"],
    "MACHINES.md": ["machines"],
    "MAX_DURATION_HEARTBEATS.md": ["runs--max-duration", "runs--heartbeats"],
    "VERSIONING.md": ["versioning", "deployment--atomic-deployment"],

    # ── Configuration & Build ──
    "CONFIG.md": ["config--config-file"],
    "BUILD_EXTENSIONS.md": [
        "config--extensions--overview", "config--extensions--prismaExtension",
        "config--extensions--syncEnvVars", "config--extensions--puppeteer",
        "config--extensions--playwright", "config--extensions--ffmpeg",
        "config--extensions--aptGet", "config--extensions--additionalFiles",
        "config--extensions--additionalPackages", "config--extensions--pythonExtension",
        "config--extensions--esbuildPlugin", "config--extensions--emitDecoratorMetadata",
        "config--extensions--audioWaveform", "config--extensions--lightpanda",
        "config--extensions--custom"
    ],
    "LOGGING_TRACING.md": ["logging", "observability--dashboards", "observability--query"],

    # ── Deployment & Operations ──
    "DEPLOYMENT.md": [
        "deployment--overview", "deploy-environment-variables",
        "deployment--preview-branches", "deployment--atomic-deployment",
        "vercel-integration", "github-integration"
    ],
    "CLI.md": [
        "cli-introduction", "cli-dev", "cli-dev-commands", "cli-deploy-commands",
        "cli-init-commands", "cli-login-commands", "cli-logout-commands",
        "cli-whoami-commands", "cli-update-commands", "cli-promote-commands",
        "cli-preview-archive", "cli-switch", "cli-list-profiles-commands"
    ],
    "GITHUB_ACTIONS.md": ["github-actions"],
    "SELF_HOSTING.md": [
        "self-hosting--overview", "self-hosting--docker", "self-hosting--kubernetes",
        "self-hosting--env--supervisor", "self-hosting--env--webapp"
    ],

    # ── API Reference ──
    "API_OVERVIEW.md": [
        "management--overview", "management--authentication",
        "management--errors-and-retries", "management--auto-pagination",
        "management--advanced-usage"
    ],
    "API_TASKS.md": [
        "management--tasks--trigger", "management--tasks--batch-trigger",
        "management--tasks--trigger-batch"
    ],
    "API_RUNS.md": [
        "management--runs--list", "management--runs--retrieve",
        "management--runs--replay", "management--runs--cancel",
        "management--runs--reschedule", "management--runs--update-metadata",
        "management--runs--add-tags", "management--runs--retrieve-events",
        "management--runs--retrieve-trace", "management--runs--retrieve-result"
    ],
    "API_BATCHES.md": [
        "management--batches--create", "management--batches--retrieve",
        "management--batches--retrieve-results", "management--batches--stream-items"
    ],
    "API_QUEUES.md": [
        "management--queues--list", "management--queues--retrieve",
        "management--queues--pause", "management--queues--concurrency-override",
        "management--queues--concurrency-reset"
    ],
    "API_SCHEDULES.md": [
        "management--schedules--list", "management--schedules--create",
        "management--schedules--retrieve", "management--schedules--update",
        "management--schedules--delete", "management--schedules--deactivate",
        "management--schedules--activate", "management--schedules--timezones"
    ],
    "API_ENV_VARS.md": [
        "management--envvars--list", "management--envvars--create",
        "management--envvars--retrieve", "management--envvars--update",
        "management--envvars--delete", "management--envvars--import"
    ],
    "API_DEPLOYMENTS.md": [
        "management--deployments--retrieve", "management--deployments--get-latest",
        "management--deployments--promote"
    ],
    "API_WAITPOINTS.md": [
        "management--waitpoints--create", "management--waitpoints--list",
        "management--waitpoints--retrieve", "management--waitpoints--complete",
        "management--waitpoints--complete-callback"
    ],
    "API_QUERY.md": ["management--query--execute"],

    # ── Guides & Patterns ──
    "API_KEYS.md": ["apikeys"],
    "LIMITS.md": ["limits"],
    "TROUBLESHOOTING.md": [
        "troubleshooting", "how-to-reduce-your-spend",
        "troubleshooting-debugging-in-vscode", "upgrading-packages",
        "troubleshooting-alerts", "troubleshooting-uptime-status",
        "troubleshooting-github-issues"
    ],
    "MIGRATION_V3_TO_V4.md": ["migrating-from-v3", "migration-mergent"],

    # ── Additional Files ──
    "GETTING_STARTED.md": [
        "introduction", "quick-start", "manual-setup", "how-it-works",
        "video-walkthrough"
    ],
    "BUILDING_WITH_AI.md": [
        "building-with-ai", "mcp-introduction", "mcp-tools",
        "mcp-agent-rules", "skills"
    ],
    "DASHBOARD.md": [
        "bulk-actions", "run-tests", "replaying", "troubleshooting-alerts"
    ],
    "GUIDES_FRAMEWORKS.md": [
        "guides--introduction", "guides--frameworks--nextjs",
        "guides--frameworks--nextjs-webhooks", "guides--frameworks--nodejs",
        "guides--frameworks--remix", "guides--frameworks--remix-webhooks",
        "guides--frameworks--bun", "guides--frameworks--prisma",
        "guides--frameworks--drizzle", "guides--frameworks--sequin",
        "guides--frameworks--supabase-guides-overview",
        "guides--frameworks--supabase-edge-functions-basic",
        "guides--frameworks--supabase-edge-functions-database-webhooks",
        "guides--frameworks--supabase-authentication",
        "guides--frameworks--webhooks-guides-overview"
    ],
    "GUIDES_AI_AGENTS.md": [
        "guides--ai-agents--overview", "guides--ai-agents--claude-code-trigger",
        "guides--ai-agents--generate-translate-copy",
        "guides--ai-agents--respond-and-check-content",
        "guides--ai-agents--route-question",
        "guides--ai-agents--translate-and-refine",
        "guides--ai-agents--verify-news-article"
    ],
    "GUIDES_EXAMPLES.md": [
        "guides--examples--dall-e3-generate-image",
        "guides--examples--deepgram-transcribe-audio",
        "guides--examples--fal-ai-image-to-cartoon",
        "guides--examples--fal-ai-realtime",
        "guides--examples--ffmpeg-video-processing",
        "guides--examples--firecrawl-url-crawl",
        "guides--examples--hookdeck-webhook",
        "guides--examples--libreoffice-pdf-conversion",
        "guides--examples--lightpanda",
        "guides--examples--open-ai-with-retrying",
        "guides--examples--pdf-to-image",
        "guides--examples--puppeteer",
        "guides--examples--react-email",
        "guides--examples--react-pdf",
        "guides--examples--replicate-image-generation",
        "guides--examples--resend-email-sequence",
        "guides--examples--satori",
        "guides--examples--scrape-hacker-news",
        "guides--examples--sentry-error-tracking",
        "guides--examples--sharp-image-processing",
        "guides--examples--stripe-webhook",
        "guides--examples--supabase-database-operations",
        "guides--examples--supabase-storage-upload",
        "guides--examples--vercel-ai-sdk",
        "guides--examples--vercel-sync-env-vars"
    ],
    "GUIDES_EXAMPLE_PROJECTS.md": [
        "guides--example-projects--anchor-browser-web-scraper",
        "guides--example-projects--batch-llm-evaluator",
        "guides--example-projects--claude-changelog-generator",
        "guides--example-projects--claude-github-wiki",
        "guides--example-projects--claude-thinking-chatbot",
        "guides--example-projects--cursor-background-agent",
        "guides--example-projects--human-in-the-loop-workflow",
        "guides--example-projects--mastra-agents-with-memory",
        "guides--example-projects--meme-generator-human-in-the-loop",
        "guides--example-projects--openai-agent-sdk-guardrails",
        "guides--example-projects--openai-agents-sdk-typescript-playground",
        "guides--example-projects--product-image-generator",
        "guides--example-projects--realtime-csv-importer",
        "guides--example-projects--realtime-fal-ai",
        "guides--example-projects--smart-spreadsheet",
        "guides--example-projects--turborepo-monorepo-prisma",
        "guides--example-projects--vercel-ai-sdk-deep-research",
        "guides--example-projects--vercel-ai-sdk-image-generator"
    ],
    "GUIDES_PYTHON.md": [
        "guides--python--python-crawl4ai",
        "guides--python--python-doc-to-markdown",
        "guides--python--python-image-processing",
        "guides--python--python-pdf-form-extractor"
    ],
    "GUIDES_USE_CASES.md": [
        "guides--use-cases--overview",
        "guides--use-cases--data-processing-etl",
        "guides--use-cases--marketing",
        "guides--use-cases--media-generation",
        "guides--use-cases--media-processing"
    ],
    "GUIDES_COMMUNITY.md": [
        "guides--community--dotenvx", "guides--community--fatima",
        "guides--community--rate-limiter", "guides--community--sveltekit"
    ],
    "OPEN_SOURCE.md": [
        "open-source-contributing", "open-source-self-hosting", "github-repo",
        "changelog", "roadmap", "community", "help-email", "help-slack",
        "request-feature"
    ],
}

# Cross-reference keywords -> target file
CROSS_REFS = {
    "queue": "QUEUES_CONCURRENCY.md",
    "concurrency": "QUEUES_CONCURRENCY.md",
    "retry": "ERRORS_RETRIES.md",
    "error": "ERRORS_RETRIES.md",
    "idempotency": "IDEMPOTENCY.md",
    "machine": "MACHINES.md",
    "trigger.config": "CONFIG.md",
    "build extension": "BUILD_EXTENSIONS.md",
    "realtime": "REALTIME.md",
    "stream": "STREAMS.md",
    "react hook": "REACT_HOOKS.md",
    "metadata": "METADATA_TAGS.md",
    "tag": "METADATA_TAGS.md",
    "wait": "WAITS_TOKENS.md",
    "schedule": "SCHEDULING.md",
    "version": "VERSIONING.md",
    "deploy": "DEPLOYMENT.md",
    "cli": "CLI.md",
    "self-host": "SELF_HOSTING.md",
    "github action": "GITHUB_ACTIONS.md",
}


def page_to_url(page_name: str) -> str:
    """Convert page filename to source URL."""
    path = page_name.replace("--", "/")
    return f"https://trigger.dev/docs/{path}"


def read_page(page_name: str) -> str:
    """Read a source page file."""
    path = PAGES / f"{page_name}.txt"
    if not path.exists():
        return f"<!-- CONTENT NOT AVAILABLE: {page_name} was not found in llms-full.txt -->\n"
    return path.read_text()


def extract_title(content: str) -> str:
    """Extract the page title from the first # heading."""
    match = re.match(r'^# (.+)$', content, re.MULTILINE)
    return match.group(1) if match else "Untitled"


def build_sources_block(pages: list) -> str:
    """Build the > Sources: block."""
    lines = ["> Sources:"]
    seen = set()
    for p in pages:
        url = page_to_url(p)
        if url not in seen:
            lines.append(f"> - {url}")
            seen.add(url)
    return "\n".join(lines)


def strip_source_header(content: str) -> str:
    """Remove the # Title and Source: URL lines from page content."""
    lines = content.split("\n")
    start = 0
    # Skip the title line
    if lines and lines[0].startswith("# "):
        start = 1
    # Skip the Source: line
    if start < len(lines) and lines[start].startswith("Source: "):
        start += 1
    # Skip blank lines after header
    while start < len(lines) and lines[start].strip() == "":
        start += 1
    return "\n".join(lines[start:])


def build_output_file(filename: str, pages: list) -> str:
    """Build the complete output file content."""
    parts = []

    # Sources block
    parts.append(build_sources_block(pages))
    parts.append("")

    # File title from filename
    title = filename.replace(".md", "").replace("_", " ").title()
    # Special case titles
    title_map = {
        "TASKS.md": "Tasks",
        "TRIGGERING.md": "Triggering",
        "RUNS.md": "Runs",
        "QUEUES_CONCURRENCY.md": "Concurrency & Queues",
        "WAITS_TOKENS.md": "Waits & Waitpoint Tokens",
        "ERRORS_RETRIES.md": "Errors & Retrying",
        "SCHEDULING.md": "Scheduling (Cron)",
        "REALTIME.md": "Realtime",
        "STREAMS.md": "Streams",
        "REACT_HOOKS.md": "React Hooks",
        "METADATA_TAGS.md": "Metadata, Tags & Priority",
        "IDEMPOTENCY.md": "Idempotency",
        "MACHINES.md": "Machines",
        "MAX_DURATION_HEARTBEATS.md": "Max Duration & Heartbeats",
        "VERSIONING.md": "Versioning",
        "CONFIG.md": "Configuration (trigger.config.ts)",
        "BUILD_EXTENSIONS.md": "Build Extensions",
        "LOGGING_TRACING.md": "Logging, Tracing & Metrics",
        "DEPLOYMENT.md": "Deployment",
        "CLI.md": "CLI Reference",
        "GITHUB_ACTIONS.md": "CI / GitHub Actions",
        "SELF_HOSTING.md": "Self-Hosting",
        "API_OVERVIEW.md": "Management API Overview",
        "API_TASKS.md": "Tasks API",
        "API_RUNS.md": "Runs API",
        "API_BATCHES.md": "Batches API",
        "API_QUEUES.md": "Queues API",
        "API_SCHEDULES.md": "Schedules API",
        "API_ENV_VARS.md": "Environment Variables API",
        "API_DEPLOYMENTS.md": "Deployments API",
        "API_WAITPOINTS.md": "Waitpoints API",
        "API_QUERY.md": "Query API",
        "API_KEYS.md": "API Keys",
        "LIMITS.md": "Limits & Quotas",
        "TROUBLESHOOTING.md": "Troubleshooting",
        "MIGRATION_V3_TO_V4.md": "Migrating from v3 to v4",
        "GETTING_STARTED.md": "Getting Started",
        "BUILDING_WITH_AI.md": "Building with AI",
        "DASHBOARD.md": "Dashboard",
        "GUIDES_FRAMEWORKS.md": "Framework Guides",
        "GUIDES_AI_AGENTS.md": "AI Agent Guides",
        "GUIDES_EXAMPLES.md": "Code Examples",
        "GUIDES_EXAMPLE_PROJECTS.md": "Example Projects",
        "GUIDES_PYTHON.md": "Python Guides",
        "GUIDES_USE_CASES.md": "Use Cases",
        "GUIDES_COMMUNITY.md": "Community Guides",
        "OPEN_SOURCE.md": "Open Source & Community",
    }
    title = title_map.get(filename, title)
    parts.append(f"# {title}")
    parts.append("")

    # Add each page's content as a section
    seen_pages = set()
    for page_name in pages:
        if page_name in seen_pages:
            continue
        seen_pages.add(page_name)

        content = read_page(page_name)
        page_title = extract_title(content)
        body = strip_source_header(content)

        # Add as H2 section
        parts.append(f"## {page_title}")
        parts.append("")
        parts.append(body.rstrip())
        parts.append("")
        parts.append("---")
        parts.append("")

    return "\n".join(parts)


def build_readme() -> str:
    """Build the README.md index file."""
    parts = []
    parts.append("# Trigger.dev Documentation Reference")
    parts.append("")
    parts.append(f"Structured reference extracted from the official Trigger.dev documentation.")
    parts.append("")
    parts.append("- **Source index:** https://trigger.dev/docs/llms.txt")
    parts.append("- **Source content:** https://trigger.dev/docs/llms-full.txt")
    parts.append("- **Extraction date:** 2026-03-29")
    parts.append("- **Total pages processed:** 242")
    parts.append("")

    categories = {
        "Core Reference": [
            ("TASKS.md", "Task definitions, schema tasks, scheduled tasks, context, and run usage"),
            ("TRIGGERING.md", "All trigger methods, batch trigger, delay, TTL, idempotency at trigger time"),
            ("RUNS.md", "Run lifecycle, statuses, and the run object"),
            ("QUEUES_CONCURRENCY.md", "Concurrency configuration, queue definitions, concurrency keys"),
            ("WAITS_TOKENS.md", "wait.for, wait.until, wait.forToken, waitpoint token lifecycle"),
            ("ERRORS_RETRIES.md", "Error handling, retrying, catchError, onFailure, OOM recovery"),
            ("SCHEDULING.md", "Cron-based scheduled tasks and the schedules API"),
            ("REALTIME.md", "Realtime overview, architecture, run object, auth, backend subscriptions"),
            ("STREAMS.md", "Output streams, input streams, Streams v2, streams.define, streams.pipe"),
            ("REACT_HOOKS.md", "React hooks for realtime updates, streaming, triggering from frontend"),
            ("METADATA_TAGS.md", "Run metadata, tags, and priority"),
            ("IDEMPOTENCY.md", "Idempotency keys, TTL, and deduplication"),
            ("MACHINES.md", "Machine presets, vCPU/memory/disk, OOM handling, ResourceMonitor"),
            ("MAX_DURATION_HEARTBEATS.md", "Max duration configuration and heartbeats"),
            ("VERSIONING.md", "Versioning, version locking, atomic deploys"),
        ],
        "Configuration & Build": [
            ("CONFIG.md", "trigger.config.ts — all configuration options"),
            ("BUILD_EXTENSIONS.md", "All built-in and custom build extensions"),
            ("LOGGING_TRACING.md", "Logging, tracing, metrics, OpenTelemetry, dashboards, TRQL"),
        ],
        "Deployment & Operations": [
            ("DEPLOYMENT.md", "Deployment overview, environment variables, preview branches, integrations"),
            ("CLI.md", "CLI commands reference — dev, deploy, login, init, promote, and more"),
            ("GITHUB_ACTIONS.md", "CI/CD with GitHub Actions"),
            ("SELF_HOSTING.md", "Self-hosting with Docker, Kubernetes, and environment variables"),
        ],
        "API Reference": [
            ("API_OVERVIEW.md", "Management API authentication, errors, pagination, advanced usage"),
            ("API_TASKS.md", "Tasks API — trigger, batch trigger"),
            ("API_RUNS.md", "Runs API — list, retrieve, replay, cancel, reschedule, metadata, tags"),
            ("API_BATCHES.md", "Batches API — create, retrieve, results, stream items"),
            ("API_QUEUES.md", "Queues API — list, retrieve, pause/resume, concurrency override"),
            ("API_SCHEDULES.md", "Schedules API — CRUD, activate/deactivate, timezones"),
            ("API_ENV_VARS.md", "Environment Variables API — CRUD and import"),
            ("API_DEPLOYMENTS.md", "Deployments API — retrieve, get latest, promote"),
            ("API_WAITPOINTS.md", "Waitpoints API — create, list, retrieve, complete, HTTP callback"),
            ("API_QUERY.md", "Query API — execute TRQL queries"),
        ],
        "Guides & Patterns": [
            ("API_KEYS.md", "API key authentication setup"),
            ("LIMITS.md", "All limits and quotas"),
            ("TROUBLESHOOTING.md", "Common problems, reducing spend, debugging, upgrading"),
            ("MIGRATION_V3_TO_V4.md", "Migrating from v3 — breaking changes and import paths"),
        ],
        "Getting Started & AI": [
            ("GETTING_STARTED.md", "Introduction, quick start, manual setup, how it works"),
            ("BUILDING_WITH_AI.md", "AI tools, MCP server, agent rules, skills"),
            ("DASHBOARD.md", "Dashboard features — bulk actions, run tests, replaying, alerts"),
        ],
        "Framework & Integration Guides": [
            ("GUIDES_FRAMEWORKS.md", "Next.js, Remix, Node.js, Bun, Prisma, Drizzle, Supabase, Sequin"),
            ("GUIDES_AI_AGENTS.md", "AI agent patterns — Claude, OpenAI, translation, verification"),
            ("GUIDES_EXAMPLES.md", "Code examples — DALL-E, Deepgram, Fal.ai, FFmpeg, Puppeteer, and more"),
            ("GUIDES_EXAMPLE_PROJECTS.md", "Full example projects — chatbots, image generators, deep research"),
            ("GUIDES_PYTHON.md", "Python guides — Crawl4AI, MarkItDown, image processing, PDF extraction"),
            ("GUIDES_USE_CASES.md", "Use cases — data processing, marketing, media generation/processing"),
            ("GUIDES_COMMUNITY.md", "Community packages — dotenvx, Fatima, rate limiter, SvelteKit"),
        ],
        "Open Source": [
            ("OPEN_SOURCE.md", "Contributing, self-hosting (legacy), GitHub, changelog, roadmap, community"),
        ],
    }

    for category, files in categories.items():
        parts.append(f"## {category}")
        parts.append("")
        parts.append("| File | Description |")
        parts.append("|---|---|")
        for fname, desc in files:
            parts.append(f"| [{fname}](./{fname}) | {desc} |")
        parts.append("")

    return "\n".join(parts)


def verify_coverage():
    """Check that all source pages are covered by at least one output file."""
    all_pages = set()
    for pages in FILE_MAP.values():
        all_pages.update(pages)

    existing_pages = {p.stem for p in PAGES.glob("*.txt")}
    uncovered = existing_pages - all_pages
    if uncovered:
        print(f"WARNING: {len(uncovered)} pages not covered by any output file:")
        for p in sorted(uncovered):
            print(f"  - {p}")
    else:
        print("All pages covered!")
    return uncovered


def main():
    # Verify coverage first
    uncovered = verify_coverage()

    # Build all output files
    for filename, pages in FILE_MAP.items():
        output_path = BASE / filename
        content = build_output_file(filename, pages)
        output_path.write_text(content)
        print(f"Wrote {filename} ({len(pages)} source pages)")

    # Build README
    readme_path = BASE / "README.md"
    readme_content = build_readme()
    readme_path.write_text(readme_content)
    print(f"Wrote README.md")

    # Summary
    print(f"\nTotal output files: {len(FILE_MAP) + 1}")
    print(f"Source pages directory: {PAGES}")


if __name__ == "__main__":
    main()
