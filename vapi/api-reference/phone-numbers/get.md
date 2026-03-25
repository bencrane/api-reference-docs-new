# Get Phone Number API Reference

## Endpoint

**GET** `https://api.vapi.ai/phone-number/{id}`

Retrieves details for a specific phone number using its unique identifier.

## Description

This endpoint fetches comprehensive information about a phone number managed within the Vapi system. The response varies based on the provider type and includes configuration details, status, and associated settings.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The unique identifier for the phone number |

### Headers

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from [Dashboard](dashboard.vapi.ai)." |

## Response Schema

The response is discriminated by the `provider` field and returns one of six variants:

### Common Fields (All Variants)

- `id` (string): Unique phone number identifier
- `orgId` (string): Organization ID owning the phone number
- `createdAt` (string, date-time): ISO 8601 creation timestamp
- `updatedAt` (string, date-time): ISO 8601 last update timestamp
- `status` (enum): `active`, `activating`, or `blocked`
- `name` (string): User-defined name for reference
- `assistantId` (string): Assistant handling inbound calls
- `squadId` (string): Squad handling inbound calls
- `workflowId` (string): Workflow handling inbound calls
- `server` (Server): Webhook destination configuration
- `fallbackDestination` (TransferDestination): Transfer target if assistant unavailable
- `hooks` (array): Event-triggered actions for `call.ringing` and `call.ending`

### Provider Variants

**byo-phone-number**: Bring-Your-Own phone number with SIP trunk integration
- `credentialId` (string, required): SIP trunk/carrier credential
- `number` (string): Phone number digits
- `numberE164CheckEnabled` (boolean, default: true): Validate E164 format

**twilio**: Twilio-managed number
- `number` (string, required): Phone number digits
- `twilioAccountSid` (string, required): Account identifier
- `twilioAuthToken` (string): Authentication token
- `twilioApiKey` (string): API key
- `twilioApiSecret` (string): API secret
- `smsEnabled` (boolean, default: true): Configure messaging webhook

**vonage**: Vonage-managed number
- `number` (string, required): Phone number digits
- `credentialId` (string, required): Vonage credential identifier

**vapi**: Vapi-managed number
- `number` (string): Phone number digits
- `numberDesiredAreaCode` (string): Area code for new purchases
- `sipUri` (string): SIP URI for direct invitations
- `authentication` (SipAuthentication): Optional SIP authentication

**telnyx**: Telnyx-managed number
- `number` (string, required): Phone number digits
- `credentialId` (string, required): Telnyx credential identifier

## Example Request

```bash
curl -X GET "https://api.vapi.ai/phone-number/abc123" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

## Example Response (Vapi Provider)

```json
{
  "provider": "vapi",
  "id": "abc123",
  "orgId": "org456",
  "createdAt": "2024-01-15T10:30:00Z",
  "updatedAt": "2024-01-20T14:22:00Z",
  "status": "active",
  "number": "+14155551234",
  "name": "Main Support Line",
  "assistantId": "asst789",
  "server": {
    "url": "https://your-domain.com/webhooks",
    "timeoutSeconds": 20
  },
  "sipUri": "sip:support@vapi.ai",
  "authentication": {
    "username": "user123",
    "password": "secure_password"
  }
}
```

## SDK Usage

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")
response = client.phone_numbers.get(id="abc123")
```
