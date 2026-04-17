# Introducing the Shovels API

> **Source:** https://docs.shovels.ai/docs/shovels-api-introduction
> **Fetched:** 2026-04-16

Comprehensive guide to the Shovels REST API: authentication, pagination, error handling, and getting started.

## Base URL and authentication

- Base URL: `https://api.shovels.ai/v2`
- All requests require SSL.
- Authentication uses a header-based API key:

```
X-API-Key: YOUR_API_KEY_HERE
```

## Primary resources

The API exposes two primary objects — **Permits** (official construction documents) and **Contractors** (skilled building-trade professionals) — plus supporting resources: **Lists**, **Addresses**, and **Meta** endpoints.

## Pagination model

The API supports two pagination approaches:

**Cursor-based (recommended).** Uses opaque token cursors for consistent performance on large datasets. Responses include `items`, `size`, and `next_cursor` fields. When `next_cursor` is `null`, no additional results exist.

**Offset-based (deprecated).** Traditional page-number pagination using `page` and `size` parameters. Being removed in future releases.

> **[UPDATED 2026-04-16]** Offset-based (`page` parameter) pagination was **removed 2025-08-01**. Only cursor-based pagination is supported today. Source: release notes v2.0.8 (2025-07-02) and v2.0.9 (2025-07-15).

## Usage-tracking headers

Every response includes the following credit-related headers:

- `X-Credits-Request` — credits consumed by the current request
- `X-Credits-Limit` — total credit limit on your plan
- `X-Credits-Remaining` — credits available

Credits operate on a rolling 30-day window.

## Error response codes

| Code | Meaning |
|------|---------|
| 200 | OK — successful request |
| 400 | Bad request — invalid input |
| 401 | Unauthorized — authentication failure |
| 402 | Payment required — credit limit exceeded |
| 403 | Forbidden — insufficient permissions |
| 404 | Not found — resource doesn't exist |
| 422 | Unprocessable entity — data validation failed (most commonly an unresolved `geo_id`) |
| 429 | Too many requests — rate limited |
| 500 | Internal server error |

See `15-errors/01-error-handling.md` for the complete error-handling guide and `15-errors/02-error-422.md` for the canonical 422 resolution pattern.

## Example: check usage

```bash
curl -X GET "https://api.shovels.ai/v2/usage" \
  -H "X-API-Key: YOUR_API_KEY_HERE"
```

## Free trial

New users receive 250 free requests — no time limit, no credit card required. In the free trial tier, each API call counts as one request regardless of records returned; paid plans move to the record-based credit model.
