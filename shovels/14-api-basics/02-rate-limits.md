# Rate Limits

> **Source:** https://docs.shovels.ai/docs/knowledge-base/api/basics/rate-limits
> **Fetched:** 2026-04-16

The Shovels API enforces rate limits to maintain system stability and ensure fair access across users. Exceeding a limit returns **HTTP 429 Too Many Requests**.

## Rate limits vs. credit limits

Two distinct concepts:

- **Rate limits** — technical throttle on request frequency. Controls how quickly you can call the API.
- **Credit limits** — billing-related cap on how many records your plan permits. See `04-credit-limits.md`.

## Recommended approaches

- Distribute requests over time rather than clustering them.
- Implement exponential backoff when you receive a 429 response.
- Request larger result sets using the `size` parameter (up to 100) to minimize call frequency.
- Cache fetched results locally to avoid redundant queries.

## Published numeric limit

No fixed numeric rate limit is published. Limits are individually enforced and may vary by account. If you experience unexpected throttling, contact `support@shovels.ai`.

## Historical reference

Per release v2.0.4 (2025-03-14): "New API rate limits: 1M requests/month (~33K requests/day)." That figure may have changed since — treat it as historical context, not a current contract.
