# Permits Per Call (Per-Call Limits)

> **Source:** https://docs.shovels.ai/docs/knowledge-base/api/basics/permits-per-call
> **Fetched:** 2026-04-16

Per-call limits that apply to search and detail endpoints.

## Maximum records per call

- **Search endpoints:** up to **100 records per page** (default `size=50`, max `size=100`).
- **Detail endpoints:** up to **50 IDs per call**.

## Search endpoint usage

Use the `size` parameter to control how many records are returned (default 50, max 100):

```
GET /v2/permits/search?geo_id=94103&size=100
```

## Pagination for larger result sets

When you need more than 100 records, use cursor-based pagination:

1. Make an initial request.
2. Extract `next_cursor` from the response.
3. Pass the cursor in the next request:
   ```
   GET /v2/permits/search?geo_id=CA&size=100&cursor=CURSOR_VALUE
   ```
4. Repeat until `next_cursor` is `null`.

## Detail endpoint usage

Request up to 50 specific permit IDs in a single call:

```
GET /v2/permits?id=permit_123,permit_456,permit_789
```

The same 50-ID ceiling applies to the contractor detail endpoint.

## Cost implications

> Your API credits are based on records returned — a call returning 100 permits uses 100 credits, while a call returning 1 permit uses 1 credit.

## Recommended practices

- Maximize efficiency by setting `size=100` on search queries.
- Batch detail lookups to respect the 50-ID ceiling.
- Implement pagination logic for complete dataset retrieval.
- Cache results locally to prevent duplicate requests.
