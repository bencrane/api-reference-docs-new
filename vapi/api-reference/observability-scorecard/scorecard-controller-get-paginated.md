# List Scorecards API Reference

## Endpoint

**GET** `https://api.vapi.ai/observability/scorecard`

## Description

Retrieve a paginated list of scorecards configured for your organization.

## Parameters

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | No | Filter by scorecard ID |
| `page` | number | No | "This is the page number to return. Defaults to 1." |
| `sortOrder` | string | No | "This is the sort order for pagination. Defaults to 'DESC'." (ASC or DESC) |
| `limit` | number | No | "This is the maximum number of items to return. Defaults to 100." |
| `createdAtGt` | string (date-time) | No | Return items where creation date exceeds specified value |
| `createdAtLt` | string (date-time) | No | Return items where creation date is less than specified value |
| `createdAtGe` | string (date-time) | No | Return items where creation date is greater than or equal to specified value |
| `createdAtLe` | string (date-time) | No | Return items where creation date is less than or equal to specified value |
| `updatedAtGt` | string (date-time) | No | Return items where update date exceeds specified value |
| `updatedAtLt` | string (date-time) | No | Return items where update date is less than specified value |
| `updatedAtGe` | string (date-time) | No | Return items where update date is greater than or equal to specified value |
| `updatedAtLe` | string (date-time) | No | Return items where update date is less than or equal to specified value |

### Header Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from [Dashboard](dashboard.vapi.ai)." |

## Response Schema

### 200 Success Response

```json
{
  "results": [
    {
      "id": "string",
      "orgId": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "updatedAt": "2024-01-01T00:00:00Z",
      "name": "string",
      "description": "string",
      "metrics": [
        {
          "structuredOutputId": "string",
          "conditions": []
        }
      ],
      "assistantIds": ["string"]
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

## Python SDK Example

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")

response = client.observability_scorecard.scorecard_controller_get_paginated()
```
