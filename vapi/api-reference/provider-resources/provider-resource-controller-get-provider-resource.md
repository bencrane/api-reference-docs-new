# Get Provider Resource API Reference

## Endpoint

**Method:** GET
**URL:** `https://api.vapi.ai/provider/{provider}/{resourceName}/{id}`

## Description

Retrieves a specific provider resource by its identifier. This endpoint allows you to fetch resource data managed by external providers such as ElevenLabs or Cartesia.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `provider` | string | Yes | "The provider (e.g., 11labs)" - Enum: `cartesia`, `11labs` |
| `resourceName` | string | Yes | "The resource name (e.g., pronunciation-dictionary)" - Enum: `pronunciation-dictionary` |
| `id` | string (UUID) | Yes | Unique identifier for the resource |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from [Dashboard](dashboard.vapi.ai)." |

## Response Schema

### Success Response (200)

```json
{
  "id": "string",
  "orgId": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "updatedAt": "2024-01-01T00:00:00Z",
  "provider": "cartesia|11labs",
  "resourceName": "pronunciation-dictionary",
  "resourceId": "string",
  "resource": {}
}
```

### Error Response (404)

Returns a 404 status when the provider resource cannot be found.

## Example Request

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")

client.provider_resources.provider_resource_controller_get_provider_resource(
    provider="cartesia",
    resource_name="pronunciation-dictionary",
    id="id",
)
```
