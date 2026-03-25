# List Phone Numbers - API Reference

## Endpoint

**GET** `https://api.vapi.ai/phone-number`

Lists all phone numbers associated with your organization.

---

## Description

Retrieves a paginated list of phone numbers configured in your Vapi account. Results can be filtered by creation and update timestamps.

---

## Parameters

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `limit` | number | No | Maximum items to return. Defaults to 100. |
| `createdAtGt` | string (date-time) | No | Items created after this timestamp. |
| `createdAtLt` | string (date-time) | No | Items created before this timestamp. |
| `createdAtGe` | string (date-time) | No | Items created on or after this timestamp. |
| `createdAtLe` | string (date-time) | No | Items created on or before this timestamp. |
| `updatedAtGt` | string (date-time) | No | Items updated after this timestamp. |
| `updatedAtLt` | string (date-time) | No | Items updated before this timestamp. |
| `updatedAtGe` | string (date-time) | No | Items updated on or after this timestamp. |
| `updatedAtLe` | string (date-time) | No | Items updated on or before this timestamp. |

### Header Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `Authorization` | string | Yes | API Key retrieved from your Dashboard. |

---

## Response

**Status:** 200 OK

**Content-Type:** `application/json`

Returns an array of phone number objects. Each object varies by provider type:

### Response Schema

The response is an array where each item represents a phone number. Items are discriminated by the `provider` field and include one of these variants:

- **byo-phone-number**
- **twilio**
- **vonage**
- **vapi**
- **telnyx**

### Common Fields (All Variants)

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique phone number identifier. |
| `orgId` | string | Organization ID this number belongs to. |
| `createdAt` | string (date-time) | ISO 8601 creation timestamp. |
| `updatedAt` | string (date-time) | ISO 8601 last update timestamp. |
| `status` | string | Status: `active`, `activating`, or `blocked`. |
| `provider` | string | Provider type (discriminator). |
| `name` | string | Display name for reference. |
| `number` | string | Phone number digits. |
| `assistantId` | string | Assigned assistant ID for inbound calls. |
| `squadId` | string | Assigned squad ID for inbound calls. |
| `workflowId` | string | Assigned workflow ID for inbound calls. |
| `fallbackDestination` | object | Transfer destination if assistant unavailable. |
| `hooks` | array | Hooks for `call.ringing` and `call.ending` events. |
| `server` | object | Webhook server configuration. |

### Provider-Specific Fields

**Vapi Provider:**
- `numberDesiredAreaCode`: Requested area code.
- `sipUri`: SIP URI for incoming INVITE requests.
- `authentication`: SIP authentication credentials.

**Twilio Provider:**
- `twilioAccountSid`: Twilio Account SID.
- `twilioAuthToken`: Twilio Auth Token.
- `twilioApiKey`: Twilio API Key.
- `twilioApiSecret`: Twilio API Secret.
- `smsEnabled`: Whether messaging webhook is configured.

**BYO Phone Number & SIP:**
- `credentialId`: SIP trunk or carrier credential ID.
- `numberE164CheckEnabled`: E164 validation toggle.

**Vonage & Telnyx Providers:**
- `credentialId`: Provider credential identifier.

---

## Example Request

```bash
curl -X GET "https://api.vapi.ai/phone-number?limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

With timestamp filtering:

```bash
curl -X GET "https://api.vapi.ai/phone-number?limit=5&createdAtGe=2024-01-01T00:00:00Z" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

---

## Example Response

```json
[
  {
    "provider": "vapi",
    "id": "phone-123abc",
    "orgId": "org-456def",
    "createdAt": "2024-01-15T10:30:00Z",
    "updatedAt": "2024-01-15T10:30:00Z",
    "status": "active",
    "number": "+14155551234",
    "name": "Customer Service Line",
    "assistantId": "asst-789ghi",
    "sipUri": "sip:phone-123abc@sip.vapi.ai"
  },
  {
    "provider": "twilio",
    "id": "phone-456def",
    "orgId": "org-456def",
    "createdAt": "2024-01-10T14:22:00Z",
    "updatedAt": "2024-01-14T09:15:00Z",
    "status": "active",
    "number": "+14155559876",
    "twilioAccountSid": "AC1234567890abcdef",
    "squadId": "squad-101jkl",
    "name": "Sales Team"
  }
]
```

---

## SDK Example (Python)

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")

# List all phone numbers
phone_numbers = client.phone_numbers.list()

# List with limit
phone_numbers = client.phone_numbers.list(limit=5)

# List with date filtering
phone_numbers = client.phone_numbers.list(
    limit=10,
    createdAtGe="2024-01-01T00:00:00Z"
)
```

---

## Notes

- If neither `assistantId`, `squadId`, nor `workflowId` is set, Vapi sends an `assistant-request` to your configured server URL.
- The `fallbackDestination` specifies where calls transfer if the primary assistant is unavailable.
- Hooks allow custom actions on `call.ringing` and `call.ending` events.
- Refer to [Dashboard](https://dashboard.vapi.ai) to retrieve your API key.
