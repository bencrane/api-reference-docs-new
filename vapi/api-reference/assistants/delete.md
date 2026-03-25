# Delete Assistant API Reference

## Endpoint

**Method:** `DELETE`

**URL:** `https://api.vapi.ai/assistant/{id}`

## Description

Removes an assistant configuration from the Vapi system. This operation permanently deletes the specified assistant resource.

## Parameters

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | The unique identifier of the assistant to delete |

### Header Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from Dashboard" |

## Response

**Status Code:** `200 OK`

**Content Type:** `application/json`

### Response Schema

The endpoint returns the deleted Assistant object with all its configuration details. The response schema references the complete `Assistant` component, which includes:

- Basic assistant metadata (id, name, created timestamp)
- Voice and transcriber configurations
- Language model settings
- Phone number and messaging parameters
- Webhook endpoints
- Custom voice and memory options
- Fallback transcriber plans

## Notes

- This is a destructive operation and cannot be undone
- The API key must be valid and have appropriate permissions
- The assistant ID must exist in the system for successful deletion
- A successful response confirms the assistant has been removed

---

**Reference Documentation:** https://docs.vapi.ai/api-reference/assistants/delete
