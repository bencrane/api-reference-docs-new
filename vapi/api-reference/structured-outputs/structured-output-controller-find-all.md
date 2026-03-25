# List Structured Outputs API Reference

## Endpoint

**GET** `https://api.vapi.ai/structured-output`

## Description

This endpoint retrieves a paginated list of structured outputs. It allows filtering by various criteria including ID, name, and timestamp ranges, with support for sorting and pagination.

## Authentication

**Required Header:**
- `Authorization` (string): API Key from [Dashboard](dashboard.vapi.ai)

## Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | No | Filter results where ID matches the specified value |
| `name` | string | No | Filter results where name matches the specified value |
| `page` | number | No | Page number for pagination (defaults to 1) |
| `sortOrder` | string | No | Sort order: `ASC` or `DESC` (defaults to `DESC`) |
| `limit` | number | No | Maximum items to return (defaults to 100) |
| `createdAtGt` | date-time | No | Items created after this timestamp |
| `createdAtLt` | date-time | No | Items created before this timestamp |
| `createdAtGe` | date-time | No | Items created on or after this timestamp |
| `createdAtLe` | date-time | No | Items created on or before this timestamp |
| `updatedAtGt` | date-time | No | Items updated after this timestamp |
| `updatedAtLt` | date-time | No | Items updated before this timestamp |
| `updatedAtGe` | date-time | No | Items updated on or after this timestamp |
| `updatedAtLe` | date-time | No | Items updated on or before this timestamp |

## Response Schema

**Status Code: 200**

```json
{
  "results": [
    {
      "type": "ai",
      "regex": null,
      "model": {
        "provider": "openai",
        "model": "gpt-4o",
        "temperature": 0.7,
        "maxTokens": 1000
      },
      "compliancePlan": {
        "forceStoreOnHipaaEnabled": false
      },
      "id": "structured-output-id",
      "orgId": "org-id",
      "createdAt": "2024-01-15T10:30:00Z",
      "updatedAt": "2024-01-15T10:30:00Z",
      "name": "Customer Information",
      "description": "Extracts customer details from conversation",
      "assistantIds": ["assistant-1", "assistant-2"],
      "workflowIds": ["workflow-1"],
      "schema": {
        "type": "object",
        "properties": {
          "customerName": {
            "type": "string",
            "description": "Full name of the customer"
          },
          "email": {
            "type": "string",
            "format": "email"
          }
        },
        "required": ["customerName", "email"]
      }
    }
  ],
  "metadata": {
    "itemsPerPage": 100,
    "totalItems": 250,
    "currentPage": 1,
    "itemsBeyondRetention": false,
    "createdAtLe": "2024-12-31T23:59:59Z",
    "createdAtGe": "2024-01-01T00:00:00Z"
  }
}
```

## Python SDK Example

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")

response = client.structured_outputs.structured_output_controller_find_all()
```

## Key Response Fields

- **results**: Array of structured output objects matching the query
- **metadata.totalItems**: Complete count of available items
- **metadata.currentPage**: Current page number in pagination
- **metadata.itemsPerPage**: Items returned per page
