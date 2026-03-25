# Delete Provider Resource API Reference

## Endpoint

**Method:** DELETE
**URL:** `https://api.vapi.ai/provider/{provider}/{resourceName}/{id}`

## Description

Removes a provider resource from the system. This operation deletes the specified resource managed by the given provider.

## Parameters

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `provider` | string | Yes | The service provider (e.g., `cartesia`, `11labs`) |
| `resourceName` | string | Yes | The resource type (e.g., `pronunciation-dictionary`) |
| `id` | string (UUID) | Yes | Unique identifier of the resource to delete |

### Header Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `Authorization` | string | Yes | API key from your dashboard |

## Response Schema

**Success (200):**
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

**Not Found (404):**
Returns error indicating the provider resource doesn't exist.

## SDK Example

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")

client.provider_resources.provider_resource_controller_delete_provider_resource(
    provider="cartesia",
    resource_name="pronunciation-dictionary",
    id="id",
)
```
