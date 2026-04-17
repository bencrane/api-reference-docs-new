# Shovels.ai - Contractors - Get Contractors by ID

## Endpoint

```
GET /v2/contractors
```

```bash
curl --request GET \
  --url https://api.shovels.ai/v2/contractors \
  --header 'X-API-Key: <api-key>'
```

## Authorization

| Name | Type | Location | Required |
|------|------|----------|----------|
| X-API-Key | string | header | Yes |

## Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | string[] | Yes | Filter by the contractor ID. Max array length: 50 |
| cursor | string \| null | No | Cursor for pagination |

## Response (200)

Schema for paginated contractors details response.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| items | ContractorsRead[] | Yes | The list of items returned in the response following given criteria. |
| size | integer | Yes | The number of items returned in the response. |
| next_cursor | string \| null | Yes | The cursor for retrieving the next page of results. |

### Notes

- Returns contractors by their IDs.
- Multiple `id` query parameters can be provided in the same API call.
- Results are paginated using cursor-based pagination.
- **Max 50 IDs per call.** See `../14-api-basics/05-permits-per-call.md`.

> **[UPDATED 2026-04-16 — Release v2.1.7]** Contractor IDs were fully regenerated on 2026-04-02. Cached IDs from before that date must be remapped via the contractor-ID changelog (81.8% coverage) or relooked-up by business name / address / license number. See `../17-knowledge-base/05-contractor-id-changes.md` and `../13-release-notes/01-release-notes.md` v2.1.7. Under v2.1.5 (2026-02-01) a separate regeneration also affected 5M Oregon, Douglas County, and Omaha IDs.

> **[UPDATED 2026-04-16]** Cursor-only pagination since 2025-08-01. See `../14-api-basics/06-pagination.md`.

> **[UPDATED 2026-04-16]** Unresolved IDs return 404; see `../15-errors/03-troubleshooting.md` for 404 remediation. Missing required params (e.g., unresolved `geo_id` on related endpoints) return 422; see `../15-errors/02-error-422.md`.