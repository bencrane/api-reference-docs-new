# Credit Limits

> **Source:** https://docs.shovels.ai/docs/knowledge-base/api/basics/credit-limits
> **Fetched:** 2026-04-16

Credit limits are billing-tier caps on how many records you can retrieve via the API.

## Free trial

- **250 requests** — no time limit, no credit card required.
- Counted as **requests, not records**: each API call is 1 request regardless of how many records come back.

## Paid plans

- Custom credit allocations based on usage needs.
- Per-tier limits are not published on the docs site; prospects must create an account at `app.shovels.ai` or contact sales for current options.

## How credits are counted on paid plans

- Each record returned consumes one credit (see `03-request-counts.md`).
- Search endpoints return up to 100 records per page (default 50).
- Detail endpoints accept up to 50 IDs per call.
- Search responses include full detail data, eliminating the need for a separate detail call.

## Exceeding the limit

When you exhaust your credit allocation, the API returns **HTTP 402 Payment Required**.

## Usage tracking

- **Profile Settings:** at `app.shovels.ai`.
- **API:** `GET /v2/usage` endpoint.
- **Response headers:** `X-Credits-Request`, `X-Credits-Limit`, `X-Credits-Remaining` on every response.
- Credits operate on a **30-day rolling window** — resets are based on consumption timing, not calendar dates.

## Getting higher limits

- Email `sales@shovels.ai`
- Phone `1-800-511-7457`
- Trial users who need additional requests should contact sales as well.

## Related

- Documentation index: https://docs.shovels.ai/llms.txt
