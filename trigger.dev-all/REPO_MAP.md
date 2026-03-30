# REPO_MAP.md — trigger.dev-all

> Definitive guide to this repo's contents. Last updated: 2026-03-29.

This repo aggregates Trigger.dev documentation, reference material, and source code into one place. It contains four top-level content folders, each serving a different purpose and audience.

---

## Overview

| Folder | Files | What it is | Trust level |
|--------|-------|------------|-------------|
| `canonical-reference/` | 12 | Reconciled canonical SDK reference (synthesized, corrected, verified) | High — verified against official docs, unverified items marked |
| `llm-full-extraction/` | 51 | Complete official docs extracted and organized by topic | High — direct from trigger.dev/docs |
| `api-site-docs/` | 80+ | Raw official docs in original site structure | Authoritative — original source format |
| `github/` | 3,500+ | GitHub repo extract: source code, examples, self-hosting templates | Authoritative — production codebase |

---

## Root Files

| File | Description |
|------|-------------|
| `REPO_MAP.md` | This file |
| `.git` | Git worktree pointer |

No other files exist at the repo root. The `.context/` directory is gitignored workspace metadata.

---

## How the Folders Relate

```
Official Trigger.dev docs site (trigger.dev/docs)
    |
    ├── api-site-docs/         Raw docs in original site structure (markdown + OpenAPI)
    ├── llm-full-extraction/   Full docs site extracted and organized by topic
    ├── github/                Repo source code, examples, templates
    |
    └──→ canonical-reference/   Canonical reference — synthesized from all of the above,
                               corrected, organized for engineers building with Trigger.dev
```

- **`api-site-docs/`** and **`llm-full-extraction/`** are **source material** — direct from Trigger.dev, minimally processed. They reflect the official docs as-is.
- **`github/`** is **supplementary** — working code examples, self-hosting templates, and the full monorepo source for resolving ambiguity or checking implementation details.
- **`canonical-reference/`** is the **derived reference** — opinionated, organized for engineers, with production patterns and decision trees that don't exist in the raw docs. It was produced by merging two independent research agents' outputs with verified corrections applied.

---

## Where Do I Look?

| If you need... | Look in... |
|----------------|------------|
| The canonical reference before building a Trigger.dev task | `canonical-reference/` |
| Official docs content organized by topic (source of truth) | `llm-full-extraction/` |
| Raw API endpoint documentation in original site format | `api-site-docs/` |
| REST Management API endpoint details | `api-site-docs/management/` or `llm-full-extraction/API_*.md` |
| Working code examples (30 projects) | `github/examples/` |
| Self-hosting Docker templates | `github/docker-self-hosted-templates/` |
| The actual Trigger.dev source code | `github/main/` |
| Production patterns (fan-out, rate limiting, human-in-the-loop) | `canonical-reference/TRIGGER_DEV_PATTERNS.md` |
| "Should I use X or Y?" decision guidance | `canonical-reference/TRIGGER_DEV_DECISION_TREE.md` |
| To verify a fact in canonical-reference | Cross-check against `llm-full-extraction/` |

---

## Per-Folder File Listings

### canonical-reference/

Reconciled canonical reference for Trigger.dev SDK v4.4.3. Produced by merging two independent research agents with verified corrections applied. Items that couldn't be confirmed are marked `<!-- UNVERIFIED -->`.

| File | Covers |
|------|--------|
| `README.md` | Index, reconciliation methodology, list of verified corrections applied |
| `TRIGGER_DEV_MASTER.md` | Architecture, SDK surface area, authentication, configuration, limits, quotas, troubleshooting, glossary |
| `TRIGGER_DEV_TASKS.md` | `task()`, `schemaTask()`, scheduled tasks, lifecycle hooks, triggering methods, subtask patterns, metadata API, machine types |
| `TRIGGER_DEV_QUEUES_CONCURRENCY.md` | Queue definitions, concurrency limits, concurrency keys, per-tenant isolation, queue management API, checkpointing, priority |
| `TRIGGER_DEV_WAITS_TOKENS.md` | `wait.for()`, `wait.until()`, waitpoint tokens, HTTP callbacks, token lifecycle, idempotency, input streams |
| `TRIGGER_DEV_ERRORS_RETRIES.md` | Retry configuration, `catchError` hook, `retry.onThrow()`, `retry.fetch()`, `AbortTaskRunError`, `onFailure`, OOM retry |
| `TRIGGER_DEV_REALTIME.md` | Public access tokens, React hooks (`useRealtimeRun`, `useRealtimeRunWithStreams`, `useRealtimeStream`), backend subscriptions, run status lifecycle |
| `TRIGGER_DEV_STREAMS.md` | `streams.define()`, `streams.input()`, `streams.pipe()`, Zod schemas, frontend hooks, Vercel AI SDK integration |
| `TRIGGER_DEV_DEPLOYMENT.md` | CLI commands (dev, deploy, login, init, promote), `trigger.config.ts`, build extensions, CI/CD, GitHub App, self-hosting |
| `TRIGGER_DEV_MANAGEMENT_API.md` | REST API endpoint inventory with confidence ratings, authentication matrix, ID prefixes, pagination, error handling |
| `TRIGGER_DEV_PATTERNS.md` | Fan-out/fan-in, sequential pipelines, per-tenant rate limiting, idempotent retries, human-in-the-loop, webhook callbacks, scheduled sync, realtime progress, error recovery, M2M triggers |
| `TRIGGER_DEV_DECISION_TREE.md` | Decision trees: task vs inline, trigger vs triggerAndWait, custom queues, wait types, batch strategies, schedules |

---

### llm-full-extraction/

Complete Trigger.dev documentation extracted from `trigger.dev/docs/llms-full.txt` (242 pages processed), organized into topic-scoped markdown files. Also contains `pages/` (raw per-page `.txt` files) and `raw/` (original source files including `llms-full.txt` and `llms.txt`).

**Core Reference**

| File | Covers |
|------|--------|
| `TASKS.md` | Task definitions, schema tasks, scheduled tasks, context, run usage |
| `TRIGGERING.md` | All trigger methods, batch trigger, delay, TTL, idempotency |
| `RUNS.md` | Run lifecycle, statuses, run object |
| `QUEUES_CONCURRENCY.md` | Concurrency config, queue definitions, concurrency keys |
| `WAITS_TOKENS.md` | Duration/date waits, waitpoint tokens, token lifecycle |
| `ERRORS_RETRIES.md` | Error handling, retrying, catchError, onFailure, OOM recovery |
| `SCHEDULING.md` | Cron scheduling, schedules API |
| `REALTIME.md` | Realtime architecture, run subscriptions, auth, backend subscriptions |
| `STREAMS.md` | Output streams, input streams, Streams v2, streams.define, streams.pipe |
| `REACT_HOOKS.md` | React hooks for realtime, streaming, triggering from frontend |
| `METADATA_TAGS.md` | Run metadata, tags, priority |
| `IDEMPOTENCY.md` | Idempotency keys, TTL, deduplication |
| `MACHINES.md` | Machine presets, vCPU/memory/disk, OOM handling |
| `MAX_DURATION_HEARTBEATS.md` | Max duration config and heartbeats |
| `VERSIONING.md` | Versioning, version locking, atomic deploys |

**Configuration & Build**

| File | Covers |
|------|--------|
| `CONFIG.md` | `trigger.config.ts` — all configuration options |
| `BUILD_EXTENSIONS.md` | All built-in and custom build extensions |
| `LOGGING_TRACING.md` | Logging, tracing, metrics, OpenTelemetry, dashboards, TRQL |

**Deployment & Operations**

| File | Covers |
|------|--------|
| `DEPLOYMENT.md` | Deployment overview, env vars, preview branches, integrations |
| `CLI.md` | CLI commands reference |
| `GITHUB_ACTIONS.md` | CI/CD with GitHub Actions |
| `SELF_HOSTING.md` | Self-hosting with Docker, Kubernetes, env vars |

**API Reference**

| File | Covers |
|------|--------|
| `API_OVERVIEW.md` | Management API auth, errors, pagination, advanced usage |
| `API_TASKS.md` | Tasks API — trigger, batch trigger |
| `API_RUNS.md` | Runs API — list, retrieve, replay, cancel, reschedule |
| `API_BATCHES.md` | Batches API — create, retrieve, results, stream items |
| `API_QUEUES.md` | Queues API — list, retrieve, pause/resume, concurrency override |
| `API_SCHEDULES.md` | Schedules API — CRUD, activate/deactivate, timezones |
| `API_ENV_VARS.md` | Environment Variables API — CRUD and import |
| `API_DEPLOYMENTS.md` | Deployments API — retrieve, get latest, promote |
| `API_WAITPOINTS.md` | Waitpoints API — create, list, retrieve, complete |
| `API_QUERY.md` | Query API — execute TRQL queries |
| `API_KEYS.md` | API key authentication setup |

**Guides & Frameworks**

| File | Covers |
|------|--------|
| `GUIDES_FRAMEWORKS.md` | Next.js, Remix, Node.js, Bun, Prisma, Drizzle, Supabase, Sequin |
| `GUIDES_AI_AGENTS.md` | AI agent patterns — Claude, OpenAI, translation, verification |
| `GUIDES_EXAMPLES.md` | Code examples — DALL-E, Deepgram, Fal.ai, FFmpeg, Puppeteer, more |
| `GUIDES_EXAMPLE_PROJECTS.md` | Full example projects — chatbots, image gen, deep research |
| `GUIDES_PYTHON.md` | Python guides — Crawl4AI, MarkItDown, image processing, PDF |
| `GUIDES_USE_CASES.md` | Use cases — data processing, marketing, media |
| `GUIDES_COMMUNITY.md` | Community packages — dotenvx, Fatima, rate limiter, SvelteKit |

**Getting Started, Migration & Support**

| File | Covers |
|------|--------|
| `GETTING_STARTED.md` | Introduction, quick start, manual setup, how it works |
| `BUILDING_WITH_AI.md` | AI tools, MCP server, agent rules, skills |
| `DASHBOARD.md` | Dashboard features — bulk actions, run tests, replaying, alerts |
| `LIMITS.md` | All limits and quotas |
| `TROUBLESHOOTING.md` | Common problems, reducing spend, debugging |
| `MIGRATION_V3_TO_V4.md` | Migrating from v3 — breaking changes and import paths |
| `OPEN_SOURCE.md` | Contributing, self-hosting (legacy), GitHub, roadmap |
| `README.md` | Index of all files with descriptions |

**Tooling**

| File | Covers |
|------|--------|
| `build_reference.py` | Python script used to generate/extract the documentation |

**Subdirectories**

| Directory | Contents |
|-----------|----------|
| `pages/` | 200+ raw `.txt` files — one per docs page, named by URL path (e.g., `guides--frameworks--nextjs.txt`) |
| `raw/` | Original source files: `llms-full.txt` (full concatenated docs) and `llms.txt` (index) |

---

### api-site-docs/

Official Trigger.dev documentation in original site structure. Markdown files with frontmatter, plus the OpenAPI spec (`v3-openapi.yaml`). Organized hierarchically by topic.

**Root-level files** (65+ markdown files covering core SDK topics):

| File | Covers |
|------|--------|
| `introduction.md` | Welcome and overview |
| `quick-start.md` | Getting started in 3 minutes |
| `how-it-works.md` | Architecture and concepts |
| `writing-tasks-introduction.md` | Introduction to writing tasks |
| `triggering.md` | All triggering methods and patterns |
| `queue-concurrency.md` | Queue and concurrency setup |
| `runs.md` | Run management and lifecycle |
| `idempotency.md` | Idempotency configuration |
| `wait.md` / `wait-for.md` / `wait-until.md` / `wait-for-token.md` | Wait methods |
| `errors-retrying.md` | Error handling and retry config |
| `logging.md` | Logging setup and usage |
| `machines.md` | Machine presets and resource specs |
| `tags.md` / `context.md` / `skills.md` | Tags, context object, Trigger.dev skills |
| `limits.md` | Rate limits, concurrency, payload sizes |
| `troubleshooting.md` | Common issues and solutions |
| `migrating-from-v3.md` | V3 to V4 migration guide |
| `how-to-reduce-your-spend.md` | Cost optimization |
| `_llms.txt` | Flat concatenation of all docs for LLM indexing |
| `v3-openapi.yaml` | OpenAPI 3.0 specification (160 KB) |
| CLI docs (`cli-*.md`) | 14 files covering each CLI command |
| MCP docs (`mcp-*.md`) | MCP server, tools, agent rules |
| GitHub/deploy docs | GitHub integration, Actions, Vercel integration |

**Subdirectories:**

| Directory | Files | Covers |
|-----------|-------|--------|
| `config/` | `config-file.md` + `extensions/` (14 files) | `trigger.config.ts` options and all build extensions |
| `deployment/` | 3 files | Deployment overview, atomic deploys, preview branches |
| `tasks/` | 4 files | Task overview, scheduled tasks, schemaTask, streams |
| `runs/` | 4 files | Heartbeats, max duration, metadata, priority |
| `realtime/` | 6 files + `backend/` (3) + `react-hooks/` (6) | Realtime overview, auth, backend subscriptions, React hooks |
| `observability/` | 2 files | Dashboards, TRQL query |
| `self-hosting/` | 4 files + `env/` (2) | Docker, Kubernetes, env vars for webapp/supervisor |
| `management/` | 4 root files + 9 subdirs | REST API: batches, deployments, envvars, query, queues, runs, schedules, tasks, waitpoints |
| `guides/` | `introduction.md` + 7 subdirs | AI agents, community, example projects, code examples, frameworks, Python, use cases |

---

### github/

Content pulled from the Trigger.dev GitHub repo. Three subdirectories:

#### github/docker-self-hosted-templates/

Docker Compose templates and scripts for self-hosting Trigger.dev.

| File | Purpose |
|------|---------|
| `README.md` | Setup instructions |
| `docker-compose.yml` | Main Docker Compose config |
| `docker-compose.webapp.yml` | Webapp service config |
| `docker-compose.worker.yml` | Worker service config |
| `start.sh` | Start all services |
| `stop.sh` | Stop all services |
| `update.sh` | Update to latest version |
| `tunnel.sh` | Set up tunnel for external access |
| `lib.sh` | Shared shell utilities |

#### github/examples/

30 example projects demonstrating Trigger.dev patterns. Each has a `README.md` with setup instructions. Also includes a root `README.md` and `LICENSE`.

| Project | Category | Demonstrates |
|---------|----------|-------------|
| `trigger-nextjs-hello-world` | Framework | Minimal Next.js + Trigger.dev starter |
| `nextjs-server-actions` | Framework | Next.js Server Actions integration |
| `nextjs-webhooks` | Framework | Next.js webhooks with Trigger.dev |
| `remix-webhooks` | Framework | Remix webhook integration |
| `supabase-edge-functions` | Integration | Supabase Edge Functions |
| `monorepos` | Framework | Turborepo monorepo setup |
| `building-effective-agents` | AI | Building effective AI agents |
| `claude-agent-github-wiki` | AI | Claude-powered GitHub wiki generator |
| `claude-agent-sdk-trigger` | AI | Claude Agent SDK with Trigger.dev |
| `claude-thinking-chatbot` | AI | Claude with extended thinking |
| `vercel-ai-sdk-deep-research-agent` | AI | Deep research agent with Vercel AI SDK |
| `vercel-ai-sdk-image-generator` | AI | Image generation with Vercel AI SDK |
| `batch-llm-evaluator` | AI | Batch evaluation with LLMs |
| `openai-agents-sdk-with-trigger-playground` | AI | OpenAI Agent SDK integration |
| `openai-agent-sdk-guardrails-examples` | AI | OpenAI agents with Guardrails |
| `mastra-agents` | AI | Mastra agent framework |
| `meme-generator-human-in-the-loop` | Pattern | Human-in-the-loop workflow |
| `article-summary-workflow` | Pattern | Article summarization |
| `changelog-generator` | Pattern | Changelog from commits |
| `smart-spreadsheet` | Pattern | Smart spreadsheet operations |
| `product-image-generator` | Media | Product image generation |
| `realtime-csv-importer` | Realtime | Real-time CSV importing |
| `realtime-fal-ai-image-generation` | Realtime | Real-time Fal.ai image gen |
| `anchor-browser-web-scraper` | Tools | Web scraping with Anchor browser |
| `cursor-cli-demo` | Tools | Cursor CLI integration |
| `python-crawl4ai` | Python | Web crawling with Crawl4AI |
| `python-doc-to-markdown-converter` | Python | Document to Markdown conversion |
| `python-image-processing` | Python | Image processing workflows |
| `python-pdf-form-extractor` | Python | PDF form extraction |

#### github/main/

Full Trigger.dev monorepo (pnpm + Turborepo). This is a large codebase (~3,500+ files). Key structure:

**Root documentation:**

| File | Purpose |
|------|---------|
| `README.md` | Project overview |
| `CONTRIBUTING.md` | Contribution guidelines (vouch requirement) |
| `AGENTS.md` | Guidance for coding agents |
| `CLAUDE.md` | Claude Code guidance |
| `RELEASE.md` | Release process |
| `DOCKER_INSTALLATION.md` | Docker setup |
| `CHANGESETS.md` | Changeset documentation |
| `LICENSE` | Apache 2.0 |

**Applications (`apps/`):**

| Directory | What it is |
|-----------|------------|
| `webapp/` | Main Remix app (API, dashboard, orchestration engine) |
| `supervisor/` | Task execution container manager |
| `coordinator/` | Coordination service |
| `docker-provider/` | Docker-based task provider |
| `kubernetes-provider/` | Kubernetes task provider |

**Public packages (`packages/`):**

| Package | npm name | Purpose |
|---------|----------|---------|
| `trigger-sdk/` | `@trigger.dev/sdk` | Main SDK |
| `cli-v3/` | `trigger.dev` | CLI tool |
| `core/` | `@trigger.dev/core` | Shared types and utilities |
| `build/` | `@trigger.dev/build` | Build extensions |
| `react-hooks/` | — | React hooks for realtime |
| `redis-worker/` | `@trigger.dev/redis-worker` | Redis background jobs |
| `rsc/` | — | React Server Components |
| `python/` | — | Python SDK |
| `schema-to-json/` | — | Schema utilities |

**Internal packages (`internal-packages/`):**

| Package | Purpose |
|---------|---------|
| `database/` | Prisma 6.14.0 schema and client |
| `run-engine/` | Run Engine 2.0 (core lifecycle management) |
| `run-queue/` | Run queue management |
| `schedule-engine/` | Durable cron scheduling |
| `redis/` | Redis utilities |
| `clickhouse/` | ClickHouse analytics client |
| `cache/` | Caching utilities |
| `emails/` | Email templates |
| `llm-model-catalog/` | LLM model catalog |
| `otlp-importer/` | OpenTelemetry importer |
| `replication/` | Data replication |
| `testcontainers/` | Test helpers (Redis/PostgreSQL) |
| `tracing/` | Distributed tracing |
| `tsql/` | SQL utilities |
| `zod-worker/` | Zod validation workers |
| `sdk-compat-tests/` | SDK compatibility tests |

**Other directories:** `docs/` (Mintlify site), `references/` (22 reference/test projects), `tests/` (E2E tests), `docker/` (Docker build files), `hosting/` (deploy configs), `rules/` (SDK docs distributed via installer), `ai/` (AI reference docs), `.changeset/` (pending changesets), `.github/` (CI/CD workflows).

---

## Gaps and Observations

1. **Significant overlap between `llm-full-extraction/` and `api-site-docs/`** — Both contain the same official documentation, just in different formats. `api-site-docs/` preserves the original site structure; `llm-full-extraction/` reorganizes by topic. The `pages/` subdirectory in `llm-full-extraction/` contains `.txt` versions of the same content in `api-site-docs/`. This overlap is intentional (different consumption formats) but worth noting.

2. **`llm-full-extraction/pages/` vs `api-site-docs/`** — The `pages/` directory contains `.txt` files named by URL path that map 1:1 to the `.md` files in `api-site-docs/`. These are effectively the same content in plain text format.

3. **`build_reference.py` in llm-full-extraction** — A tooling script lives alongside reference content. Could be moved to a `scripts/` folder or repo root.

4. **No top-level README.md** — The repo root has no `README.md`. This `REPO_MAP.md` now serves that purpose, but a `README.md` is conventional.

5. **`github/main/` is enormous** — At ~3,500 files it dwarfs everything else in the repo. For pure reference purposes, a curated subset (SDK package, key docs, examples) might suffice. The full monorepo includes CI/CD, Docker configs, E2E tests, and internal tooling that isn't directly useful for understanding the SDK.
