# Update Call API Reference

## Endpoint

**PATCH** `https://api.vapi.ai/call/{id}`

## Description

Updates an existing call with new information. This endpoint allows you to modify call details after creation, such as renaming the call for reference purposes.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The unique identifier of the call to update |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | API Key from your Dashboard (dashboard.vapi.ai) |
| `Content-Type` | string | Yes | Must be `application/json` |

## Request Body

The request body follows the `UpdateCallDTO` schema:

```json
{
  "name": "string"
}
```

### UpdateCallDTO Schema

| Property | Type | Description |
|----------|------|-------------|
| `name` | string | A descriptive name for the call, used for your own reference purposes |

## Response

**Status Code:** `200 OK`

The response returns the complete updated `Call` object with all its properties, including:

- Call metadata (id, type, status)
- Timing information (createdAt, startedAt, endedAt)
- Participant details (customer, phoneNumber)
- Assistant configuration
- Call transcript and messages
- Cost breakdown and analysis
- Recording and artifact information

## Example Request

```bash
curl -X PATCH https://api.vapi.ai/call/call_12345 \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Customer Service Call - John Doe"
  }'
```

## Example Response

```json
{
  "id": "call_12345",
  "name": "Customer Service Call - John Doe",
  "type": "outboundPhoneCall",
  "status": "ended",
  "startedAt": 1699564800000,
  "endedAt": 1699564950000,
  "createdAt": 1699564750000,
  "phoneNumber": {
    "number": "+14155551234"
  },
  "customer": {
    "number": "+14155555678"
  },
  "endedReason": "customer-ended-call",
  "artifact": {
    "transcript": "Customer: Hello..."
  },
  "costBreakdown": {
    "total": 0.25,
    "transport": 0.10,
    "stt": 0.05,
    "llm": 0.08,
    "tts": 0.02
  }
}
```

## Notes

- Only the `name` property can be modified through this endpoint
- The name is for internal reference and does not affect call functionality
- All other call properties are read-only after the call is created
