# List Provider Resources API Reference

## Endpoint

**Method:** GET
**URL:** `https://api.vapi.ai/provider/{provider}/{resourceName}`

## Description

Retrieves a paginated list of resources from a specified provider. This endpoint allows you to query provider-managed resources with filtering, sorting, and pagination options.

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `provider` | string | Yes | The provider identifier (e.g., `cartesia`, `11labs`) |
| `resourceName` | string | Yes | The resource type (e.g., `pronunciation-dictionary`) |

## Query Parameters

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `id` | string | No | Filter by resource ID | — |
| `resourceId` | string | No | Filter by provider-specific resource ID | — |
| `page` | number | No | Page number for pagination | 1 |
| `sortOrder` | string | No | Sort order (`ASC` or `DESC`) | DESC |
| `limit` | number | No | Maximum items to return | 100 |
| `createdAtGt` | datetime | No | Items created after this timestamp | — |
| `createdAtLt` | datetime | No | Items created before this timestamp | — |
| `createdAtGe` | datetime | No | Items created at or after this timestamp | — |
| `createdAtLe` | datetime | No | Items created at or before this timestamp | — |
| `updatedAtGt` | datetime | No | Items updated after this timestamp | — |
| `updatedAtLt` | datetime | No | Items updated before this timestamp | — |
| `updatedAtGe` | datetime | No | Items updated at or after this timestamp | — |
| `updatedAtLe` | datetime | No | Items updated at or before this timestamp | — |

## Headers

| Header | Type | Required | Description |
|--------|------|----------|-------------|
| `Authorization` | string | Yes | API key from Dashboard (bearer token format) |

## Response Schema

**Status Code:** 200 (Success)

```json
{
  "results": [
    {
      "id": "string",
      "orgId": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "updatedAt": "2024-01-01T00:00:00Z",
      "provider": "cartesia",
      "resourceName": "pronunciation-dictionary",
      "resourceId": "string",
      "resource": {}
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

### Response Fields

**results array:**
- `id`: Unique resource identifier
- `orgId`: Organization ID for resource ownership
- `createdAt`: ISO 8601 creation timestamp
- `updatedAt`: ISO 8601 modification timestamp
- `provider`: Managing provider name
- `resourceName`: Resource type designation
- `resourceId`: Provider-specific identifier
- `resource`: Full resource data from provider API

**metadata object:**
- `itemsPerPage`: Items per page
- `totalItems`: Total available items
- `currentPage`: Current page number
- `itemsBeyondRetention`: Data retention indicator
- `createdAtLe/Ge`: Creation date range boundaries

## Example Request

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")

response = client.provider_resources.provider_resource_controller_get_provider_resources_paginated(
    provider="cartesia",
    resource_name="pronunciation-dictionary",
)
```
