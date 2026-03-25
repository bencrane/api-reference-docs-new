# Delete Call API Reference

## Endpoint

**DELETE** `https://api.vapi.ai/call/{id}`

## Description

Removes a call record from the system. Supports both individual and bulk deletion operations.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The unique identifier for the call to delete |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | API key from your Vapi Dashboard |
| `Content-Type` | string | Yes | `application/json` |

## Request Body

### DeleteCallDTO Schema

```json
{
  "ids": ["string", "string"]
}
```

**Properties:**

| Property | Type | Description |
|----------|------|-------------|
| `ids` | array[string] | Collection of call IDs for bulk deletion. When provided, the path parameter ID is ignored. Bulk operations execute asynchronously with webhook updates sent to your organization's configured server URL. Processing may take several hours. |

## Response

### Success Response (200 OK)

Returns a Call object with the following structure:

```json
{
  "id": "string",
  "type": "inboundPhoneCall|outboundPhoneCall|webCall|vapi.websocketCall",
  "status": "scheduled|queued|ringing|in-progress|forwarding|ended|not-found|deletion-failed",
  "endedReason": "string",
  "costs": {
    "transport": 0,
    "stt": 0,
    "llm": 0,
    "tts": 0,
    "vapi": 0,
    "total": 0
  },
  "messages": [],
  "destination": {
    "type": "number|sip",
    "number": "string"
  }
}
```

## Key Details

- **Single Deletion**: Specify the call ID in the URL path
- **Bulk Deletion**: Include an `ids` array in the request body; the path ID parameter will be disregarded
- **Asynchronous Processing**: Bulk deletions are processed asynchronously with webhook notifications
- **Timeline**: Bulk operations may require up to several hours for completion
- **Webhooks**: Deletion status updates are sent to the organization's configured server URL in settings

## Example Request

### Single Call Deletion
```bash
curl -X DELETE https://api.vapi.ai/call/call_12345 \
  -H "Authorization: your_api_key" \
  -H "Content-Type: application/json"
```

### Bulk Deletion
```bash
curl -X DELETE https://api.vapi.ai/call/call_12345 \
  -H "Authorization: your_api_key" \
  -H "Content-Type: application/json" \
  -d '{
    "ids": ["call_12345", "call_67890", "call_11111"]
  }'
```

## Reference
[Vapi API Documentation](https://docs.vapi.ai/api-reference/calls/delete)
