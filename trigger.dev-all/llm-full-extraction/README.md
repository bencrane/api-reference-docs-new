# Trigger.dev Documentation Reference

Structured reference extracted from the official Trigger.dev documentation.

- **Source index:** https://trigger.dev/docs/llms.txt
- **Source content:** https://trigger.dev/docs/llms-full.txt
- **Extraction date:** 2026-03-29
- **Total pages processed:** 242

## Core Reference

| File | Description |
|---|---|
| [TASKS.md](./TASKS.md) | Task definitions, schema tasks, scheduled tasks, context, and run usage |
| [TRIGGERING.md](./TRIGGERING.md) | All trigger methods, batch trigger, delay, TTL, idempotency at trigger time |
| [RUNS.md](./RUNS.md) | Run lifecycle, statuses, and the run object |
| [QUEUES_CONCURRENCY.md](./QUEUES_CONCURRENCY.md) | Concurrency configuration, queue definitions, concurrency keys |
| [WAITS_TOKENS.md](./WAITS_TOKENS.md) | wait.for, wait.until, wait.forToken, waitpoint token lifecycle |
| [ERRORS_RETRIES.md](./ERRORS_RETRIES.md) | Error handling, retrying, catchError, onFailure, OOM recovery |
| [SCHEDULING.md](./SCHEDULING.md) | Cron-based scheduled tasks and the schedules API |
| [REALTIME.md](./REALTIME.md) | Realtime overview, architecture, run object, auth, backend subscriptions |
| [STREAMS.md](./STREAMS.md) | Output streams, input streams, Streams v2, streams.define, streams.pipe |
| [REACT_HOOKS.md](./REACT_HOOKS.md) | React hooks for realtime updates, streaming, triggering from frontend |
| [METADATA_TAGS.md](./METADATA_TAGS.md) | Run metadata, tags, and priority |
| [IDEMPOTENCY.md](./IDEMPOTENCY.md) | Idempotency keys, TTL, and deduplication |
| [MACHINES.md](./MACHINES.md) | Machine presets, vCPU/memory/disk, OOM handling, ResourceMonitor |
| [MAX_DURATION_HEARTBEATS.md](./MAX_DURATION_HEARTBEATS.md) | Max duration configuration and heartbeats |
| [VERSIONING.md](./VERSIONING.md) | Versioning, version locking, atomic deploys |

## Configuration & Build

| File | Description |
|---|---|
| [CONFIG.md](./CONFIG.md) | trigger.config.ts — all configuration options |
| [BUILD_EXTENSIONS.md](./BUILD_EXTENSIONS.md) | All built-in and custom build extensions |
| [LOGGING_TRACING.md](./LOGGING_TRACING.md) | Logging, tracing, metrics, OpenTelemetry, dashboards, TRQL |

## Deployment & Operations

| File | Description |
|---|---|
| [DEPLOYMENT.md](./DEPLOYMENT.md) | Deployment overview, environment variables, preview branches, integrations |
| [CLI.md](./CLI.md) | CLI commands reference — dev, deploy, login, init, promote, and more |
| [GITHUB_ACTIONS.md](./GITHUB_ACTIONS.md) | CI/CD with GitHub Actions |
| [SELF_HOSTING.md](./SELF_HOSTING.md) | Self-hosting with Docker, Kubernetes, and environment variables |

## API Reference

| File | Description |
|---|---|
| [API_OVERVIEW.md](./API_OVERVIEW.md) | Management API authentication, errors, pagination, advanced usage |
| [API_TASKS.md](./API_TASKS.md) | Tasks API — trigger, batch trigger |
| [API_RUNS.md](./API_RUNS.md) | Runs API — list, retrieve, replay, cancel, reschedule, metadata, tags |
| [API_BATCHES.md](./API_BATCHES.md) | Batches API — create, retrieve, results, stream items |
| [API_QUEUES.md](./API_QUEUES.md) | Queues API — list, retrieve, pause/resume, concurrency override |
| [API_SCHEDULES.md](./API_SCHEDULES.md) | Schedules API — CRUD, activate/deactivate, timezones |
| [API_ENV_VARS.md](./API_ENV_VARS.md) | Environment Variables API — CRUD and import |
| [API_DEPLOYMENTS.md](./API_DEPLOYMENTS.md) | Deployments API — retrieve, get latest, promote |
| [API_WAITPOINTS.md](./API_WAITPOINTS.md) | Waitpoints API — create, list, retrieve, complete, HTTP callback |
| [API_QUERY.md](./API_QUERY.md) | Query API — execute TRQL queries |

## Guides & Patterns

| File | Description |
|---|---|
| [API_KEYS.md](./API_KEYS.md) | API key authentication setup |
| [LIMITS.md](./LIMITS.md) | All limits and quotas |
| [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) | Common problems, reducing spend, debugging, upgrading |
| [MIGRATION_V3_TO_V4.md](./MIGRATION_V3_TO_V4.md) | Migrating from v3 — breaking changes and import paths |

## Getting Started & AI

| File | Description |
|---|---|
| [GETTING_STARTED.md](./GETTING_STARTED.md) | Introduction, quick start, manual setup, how it works |
| [BUILDING_WITH_AI.md](./BUILDING_WITH_AI.md) | AI tools, MCP server, agent rules, skills |
| [DASHBOARD.md](./DASHBOARD.md) | Dashboard features — bulk actions, run tests, replaying, alerts |

## Framework & Integration Guides

| File | Description |
|---|---|
| [GUIDES_FRAMEWORKS.md](./GUIDES_FRAMEWORKS.md) | Next.js, Remix, Node.js, Bun, Prisma, Drizzle, Supabase, Sequin |
| [GUIDES_AI_AGENTS.md](./GUIDES_AI_AGENTS.md) | AI agent patterns — Claude, OpenAI, translation, verification |
| [GUIDES_EXAMPLES.md](./GUIDES_EXAMPLES.md) | Code examples — DALL-E, Deepgram, Fal.ai, FFmpeg, Puppeteer, and more |
| [GUIDES_EXAMPLE_PROJECTS.md](./GUIDES_EXAMPLE_PROJECTS.md) | Full example projects — chatbots, image generators, deep research |
| [GUIDES_PYTHON.md](./GUIDES_PYTHON.md) | Python guides — Crawl4AI, MarkItDown, image processing, PDF extraction |
| [GUIDES_USE_CASES.md](./GUIDES_USE_CASES.md) | Use cases — data processing, marketing, media generation/processing |
| [GUIDES_COMMUNITY.md](./GUIDES_COMMUNITY.md) | Community packages — dotenvx, Fatima, rate limiter, SvelteKit |

## Open Source

| File | Description |
|---|---|
| [OPEN_SOURCE.md](./OPEN_SOURCE.md) | Contributing, self-hosting (legacy), GitHub, changelog, roadmap, community |
