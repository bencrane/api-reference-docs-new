# Delete Phone Number API Reference

## Endpoint

**DELETE** `https://api.vapi.ai/phone-number/{id}`

## Description

Removes a phone number from your Vapi account. The deletion process returns the complete phone number object that was deleted.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the phone number to delete |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from Dashboard" |

## Response

### 200 Success Response

Returns the deleted phone number object. The response structure varies based on the phone number provider.

#### Response Schema

The response is a discriminated union supporting multiple provider types:

- **byo-phone-number** - Bring Your Own phone number
- **twilio** - Twilio-managed number
- **vonage** - Vonage-managed number
- **vapi** - Vapi-managed number
- **telnyx** - Telnyx-managed number

#### Common Fields (All Providers)

```json
{
  "id": "string",
  "provider": "string (discriminator)",
  "orgId": "string",
  "createdAt": "ISO 8601 datetime",
  "updatedAt": "ISO 8601 datetime",
  "status": "active | activating | blocked",
  "name": "string (optional)",
  "number": "string",
  "assistantId": "string (optional)",
  "squadId": "string (optional)",
  "workflowId": "string (optional)",
  "server": "Server object (optional)",
  "fallbackDestination": "Transfer destination (optional)",
  "hooks": "array of hook objects (optional)"
}
```

#### Provider-Specific Fields

**Twilio:**
- `twilioAccountSid` (required)
- `twilioAuthToken` (optional)
- `twilioApiKey` (optional)
- `twilioApiSecret` (optional)
- `smsEnabled` (boolean, default: true)

**Vonage/Telnyx:**
- `credentialId` (required)

**BYO Phone Number:**
- `credentialId` (required)
- `numberE164CheckEnabled` (boolean, default: true)

**Vapi:**
- `numberDesiredAreaCode` (optional)
- `sipUri` (optional)
- `authentication` (SIP authentication object, optional)

## Example Request

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN_HERE",
)

client.phone_numbers.delete(
    id="id",
)
```

## Example Response

```json
{
  "id": "phone_12345678",
  "provider": "vapi",
  "orgId": "org_abc123",
  "createdAt": "2024-01-15T10:30:00Z",
  "updatedAt": "2024-01-20T15:45:00Z",
  "status": "active",
  "number": "+14155551234",
  "name": "Sales Line",
  "assistantId": "assistant_xyz789",
  "sipUri": "sip:sales@sip.vapi.ai"
}
```

## Authentication

This endpoint requires bearer token authentication. Include your API key in the `Authorization` header as `Bearer YOUR_API_KEY`.
