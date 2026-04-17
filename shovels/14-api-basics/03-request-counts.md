# How Do API Credits Work? (Request Counts)

> **Source:** https://docs.shovels.ai/docs/knowledge-base/api/basics/request-counts
> **Fetched:** 2026-04-16

The Shovels API uses a **record-based credit system**: each record returned by an API call counts against your credits.

## Core rule

> Each record returned by an API call counts against your credits.

Concretely:

- A search returning 100 permits consumes **100 credits**.
- A detail call returning 3 contractors consumes **3 credits**.
- A single permit lookup consumes **1 credit**.

This rule applies uniformly across search endpoints and detail endpoints on paid plans.

## Free trial exception

Free trial accounts use a **request-based** system instead:

- Each API call = 1 request regardless of records returned.
- 250 total requests per trial account.

## Monitoring consumption

Three ways to track usage:

1. **API endpoint:** `GET /v2/usage` — returns current credit usage for the rolling 30-day period.
2. **Response headers:** every response includes `X-Credits-Request`, `X-Credits-Limit`, and `X-Credits-Remaining`.
3. **Dashboard:** the usage panel at `app.shovels.ai` under account settings.

## Optimization guidance

- Refine searches with filters before pulling records.
- Prefer search endpoints when you need the full detail payload — search responses already include full detail, so a follow-up detail call is typically unnecessary.
- Cache locally to avoid duplicate fetches.
