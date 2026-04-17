# API Error Handling

> **Source:** https://docs.shovels.ai/docs/knowledge-base/api/errors/error-handling
> **Fetched:** 2026-04-16

Quick guide to handling Shovels API errors. See `14-api-basics/01-introduction.md` for the full error-code table from the API introduction page.

## Error codes and interpretations

| Code | Meaning | What to do |
|------|---------|-----------|
| 200 | OK | Verify `items` array — an empty array is not an error, just no matches |
| 400 | Bad request — malformed request format | Review request syntax |
| 401 | Unauthorized — API credentials invalid/missing | Validate API key and `X-API-Key` header |
| 402 | Payment required — credit limit exceeded | See `14-api-basics/04-credit-limits.md` |
| 403 | Forbidden — insufficient permissions | Contact sales to upgrade access |
| 404 | Not found — resource doesn't exist | May also indicate conflicting parameters (see troubleshooting) |
| 422 | Unprocessable entity — required parameter missing/invalid | Typically an unresolved `geo_id`; see `02-error-422.md` |
| 429 | Too many requests — rate limited | Exponential backoff |
| 500 | Internal server error | Retry; contact `support@shovels.ai` if persistent |

## Recommended handling

**422 (most common).** A 422 error typically means you're missing a required parameter — usually a `geo_id`. Resolve by calling the Address Search endpoint first, then supplying the returned `geo_id` to subsequent permit requests. See `02-error-422.md`.

**200 with empty results.** This is normal operation, not an error. An empty `items` array with HTTP 200 means the query was formatted properly but matched no records.

**Other codes.** Review request syntax for 400, verify authentication for 401, and contact `support@shovels.ai` for recurring 500s.

## Further reading

- `14-api-basics/01-introduction.md` — full intro-level error-code table and header details.
- `02-error-422.md` — dedicated 422 resolution guide.
- `03-troubleshooting.md` — 5-step diagnostic and 404-cause analysis.
