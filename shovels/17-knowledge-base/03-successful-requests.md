# Verifying a Successful Request

> **Source:** https://docs.shovels.ai/docs/knowledge-base/api/basics/successful-requests
> **Fetched:** 2026-04-16

How to determine if your Shovels API request succeeded.

## Success indicator

A successful request returns **HTTP 200 OK** with the requested data in the response body.

## Response structure

Successful paginated responses contain:

- `items` — array of records for the page.
- `next_cursor` — cursor for the next page (null when exhausted).
- `size` — number of records in this page.
- A total count field (available via `include_count=true` on the 7 endpoints that support it — see release v2.1.6).

## Status-code reference

| Code | Meaning |
|------|---------|
| 200 | Success (including empty results) |
| 400 | Bad request — review parameters |
| 401 | Unauthorized — validate API key |
| 422 | Unprocessable — required parameter missing |
| 429 | Rate limit exceeded |
| 500 | Server error — retry the request |

## Empty results clarification

A 200 response with an empty `items` array is **not an error**. It indicates that the address/geo_id is known but no permits match your criteria. Causes:

- The address has no permits in Shovels.
- Date filters exclude all matches.
- The `geo_id` is valid in format but not yet mapped.

## Verification steps

1. Confirm the API key is included in the headers.
2. Validate required parameters (typically `geo_id`).
3. Ensure dates use `YYYY-MM-DD` format.
4. Examine error messages in the response body.
