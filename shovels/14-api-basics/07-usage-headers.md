# Usage Headers

> **Source:** https://docs.shovels.ai/docs/shovels-api-introduction (usage-tracking section); https://docs.shovels.ai/docs/knowledge-base/api/basics/request-counts
> **Fetched:** 2026-04-16

No dedicated docs page covers usage headers alone — the information lives in the API introduction and the request-counts KB page. This file archives what both pages say.

## Per-response credit headers

Every Shovels API response includes three headers:

| Header | Meaning |
|--------|---------|
| `X-Credits-Request` | Credits consumed by the **current** request |
| `X-Credits-Limit` | Total credit limit on your plan |
| `X-Credits-Remaining` | Credits you have left in the rolling 30-day window |

Credits operate on a **30-day rolling window**. Resets depend on consumption timing, not the calendar.

## Alternate usage-tracking paths

- `GET /v2/usage` — returns your current credit usage for the rolling 30-day period as a JSON response.
- `app.shovels.ai` — dashboard view under Profile Settings (includes daily breakdown, `is_over_limit` flag, and `available_at` projection per release v2.1.6).

## Relationship to error codes

- `X-Credits-Remaining = 0` → next call returns **402 Payment Required**.
- See `15-errors/01-error-handling.md` for the 402 handler.
