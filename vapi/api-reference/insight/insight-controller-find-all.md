# Get Insights API Reference

## Endpoint
- **Method:** GET
- **URL:** `https://api.vapi.ai/reporting/insight`
- **Operation ID:** insight-controller-find-all

## Description
Retrieves a paginated collection of insights with filtering and sorting capabilities.

## Authentication
- **Required Header:** Authorization (Bearer token from Dashboard)

## Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | string | No | Filter by insight ID |
| page | number | No | Page number for pagination (defaults to 1) |
| sortOrder | string | No | Sort direction: ASC or DESC (defaults to DESC) |
| limit | number | No | Max items per page (defaults to 100) |
| createdAtGt | date-time | No | Items created after this timestamp |
| createdAtLt | date-time | No | Items created before this timestamp |
| createdAtGe | date-time | No | Items created on or after this timestamp |
| createdAtLe | date-time | No | Items created on or before this timestamp |
| updatedAtGt | date-time | No | Items updated after this timestamp |
| updatedAtLt | date-time | No | Items updated before this timestamp |
| updatedAtGe | date-time | No | Items updated on or after this timestamp |
| updatedAtLe | date-time | No | Items updated on or before this timestamp |

## Response Schema

**InsightPaginatedResponse:**
```json
{
  "results": [
    {
      "id": "string",
      "name": "string",
      "type": "bar|line|pie|text",
      "orgId": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "updatedAt": "2024-01-01T00:00:00Z"
    }
  ],
  "metadata": {
    "itemsPerPage": 100,
    "totalItems": 0,
    "currentPage": 1,
    "itemsBeyondRetention": false,
    "createdAtLe": "2024-01-01T00:00:00Z",
    "createdAtGe": "2024-01-01T00:00:00Z"
  }
}
```

## SDK Example

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")
response = client.insight.insight_controller_find_all()
```
