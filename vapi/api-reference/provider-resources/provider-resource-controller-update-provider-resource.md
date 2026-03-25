# Update Provider Resource API Reference

## Endpoint

**Method:** PATCH
**URL:** `https://api.vapi.ai/provider/{provider}/{resourceName}/{id}`

## Description

Updates an existing provider resource with new data.

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `provider` | string | Yes | The service provider (e.g., `cartesia`, `11labs`) |
| `resourceName` | string | Yes | The resource category (e.g., `pronunciation-dictionary`) |
| `id` | UUID | Yes | The unique identifier of the resource to update |

## Headers

| Header | Type | Required | Description |
|--------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from [Dashboard](dashboard.vapi.ai)" |

## Response Schema

**Status 200 - Success:**

```json
{
  "id": "string",
  "orgId": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "updatedAt": "2024-01-01T00:00:00Z",
  "provider": "cartesia | 11labs",
  "resourceName": "pronunciation-dictionary",
  "resourceId": "string",
  "resource": {}
}
```

**Status 404 - Not Found:**
Provider resource not found error response.

## Python SDK Example

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")

response = client.provider_resources.provider_resource_controller_update_provider_resource(
    provider="cartesia",
    resource_name="pronunciation-dictionary",
    id="id",
)
```
