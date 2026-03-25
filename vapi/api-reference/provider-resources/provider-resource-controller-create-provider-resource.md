# Create Provider Resource API Reference

## Endpoint

**Method:** POST
**URL:** `https://api.vapi.ai/provider/{provider}/{resourceName}`

## Description

This endpoint enables the creation of a new provider resource.

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `provider` | string | Yes | The service provider (options: `cartesia`, `11labs`) |
| `resourceName` | string | Yes | The resource type (options: `pronunciation-dictionary`) |

## Headers

| Header | Type | Required | Description |
|--------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from Dashboard" |

## Response Schema

The successful response returns a `ProviderResource` object with the following properties:

| Property | Type | Description |
|----------|------|-------------|
| `id` | string | Unique identifier for the provider resource |
| `orgId` | string | Organization identifier owning this resource |
| `createdAt` | ISO 8601 datetime | Resource creation timestamp |
| `updatedAt` | ISO 8601 datetime | Resource last modification timestamp |
| `provider` | string | Managing service provider |
| `resourceName` | string | Resource type/name |
| `resourceId` | string | Provider-specific resource identifier |
| `resource` | object | Complete resource data from the provider API |

## Status Codes

- **201:** Successfully created provider resource

## SDK Example

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")

client.provider_resources.provider_resource_controller_create_provider_resource(
    provider="cartesia",
    resource_name="pronunciation-dictionary",
)
```
