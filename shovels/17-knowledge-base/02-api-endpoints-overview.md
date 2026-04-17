# API Endpoints Overview (KB)

> **Source:** https://docs.shovels.ai/docs/knowledge-base/api/basics/api-endpoints
> **Fetched:** 2026-04-16

Quick overview of Shovels API endpoints. For complete details, see the API Reference documentation and the local `02-permits/` through `12-usage/` section files.

## Main categories and paths

The API organizes resources into five primary groups:

1. **Permits** — `/v2/permits/*` — building permit information.
2. **Contractors** — `/v2/contractors/*` — contractor details, employees, metrics.
3. **Addresses** — `/v2/addresses/*` — geographic ID resolution and address metrics.
4. **Lists** — `/v2/lists/*` — reference values (e.g., tags, zip codes).
5. **Meta** — `/v2/meta/*` — system metadata and data release date.

Additional resource families not listed on this particular KB page but present in the API Reference:

- `/v2/cities/*`, `/v2/counties/*`, `/v2/jurisdictions/*`, `/v2/states/*`, `/v2/zipcodes/*` — geographic search and metrics.
- `/v2/usage` — credit usage.

## Endpoint types

Two distinct query patterns:

- **Search endpoints** — retrieve multiple records filtered by specified criteria. Support cursor pagination; `size` up to 100.
- **Detail endpoints** — fetch individual records identified by ID. Max 50 IDs per call.

> Search responses include full detail payloads — you usually don't need a separate detail call.

## Related

- Local: `02-permits/01-search-permits.md`, `03-contractors/02-search-contractors.md`, etc.
- `../14-api-basics/05-permits-per-call.md` — per-call limits.
- `../14-api-basics/06-pagination.md` — pagination semantics.
