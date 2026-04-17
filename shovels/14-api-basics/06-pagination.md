# Pagination

> **Source:** https://docs.shovels.ai/docs/shovels-api-introduction (pagination section) — no dedicated KB page exists
> **Fetched:** 2026-04-16

## Cursor-only since 2025-08-01

As of **2025-08-01**, offset-based pagination (the `page` parameter) has been **removed** from the Shovels API. Cursor-based pagination is the only supported model.

History:

- **v2.0.6 (2025-05-06)** — cursor-based pagination added for all endpoints; `page` parameter deprecated.
- **v2.0.7 (2025-06-10)** — deprecation notice repeated; `page` supported for 3 more months.
- **v2.0.8 (2025-07-02)** — final reminder that `page`-based pagination is discontinued August 1, 2025.
- **v2.0.9 (2025-07-15)** — token-based pagination fully live; page-parameter removal scheduled for August 1, 2025.

## How cursor pagination works

Each paginated response envelope contains:

- `items` — the list of records for this page.
- `size` — number of records returned in this page (governed by the `size` query parameter, default 50, max 100).
- `next_cursor` — opaque token to pass into the next request. When `null`, there are no more pages.

### Example flow

```
# page 1
GET /v2/permits/search?geo_id=abc&size=100
→ { "items": [...], "size": 100, "next_cursor": "eyJ..." }

# page 2
GET /v2/permits/search?geo_id=abc&size=100&cursor=eyJ...
→ { "items": [...], "size": 100, "next_cursor": "eyJ..." }

# last page
→ { "items": [...], "size": 42, "next_cursor": null }
```

## Ordering

Per release v2.0.6: response ordering is chronological, descending (newest first).

## Related

- `05-permits-per-call.md` — per-call ceilings and cursor usage examples.
- `01-introduction.md` — overall pagination model overview.
