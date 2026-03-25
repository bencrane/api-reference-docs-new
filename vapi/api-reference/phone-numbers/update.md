# Update Phone Number API Reference

## Endpoint

**PATCH** `https://api.vapi.ai/phone-number/{id}`

Updates an existing phone number configuration with new settings and parameters.

## Parameters

### Path Parameters
- **id** (required, string): The unique identifier of the phone number to update

### Header Parameters
- **Authorization** (required, string): API key obtained from the Dashboard at dashboard.vapi.ai

### Request Body
The request accepts one of five provider-specific schemas, distinguished by the `provider` field:

#### Common Fields (All Providers)
- `name` (string): Reference label for the phone number
- `assistantId` (string): Assistant to handle incoming calls
- `squadId` (string): Squad to handle incoming calls
- `workflowId` (string): Workflow to handle incoming calls
- `server` (Server object): Webhook destination configuration
- `fallbackDestination` (Transfer object): Destination if primary routing fails
- `hooks` (array): Event-triggered actions for incoming calls

#### Provider-Specific Fields

**byo-phone-number:**
- `number` (string): Customer phone number
- `credentialId` (string): SIP trunk credential reference
- `numberE164CheckEnabled` (boolean, default: true): Enable E.164 validation

**twilio:**
- `number` (string): Twilio phone number digits
- `twilioAccountSid` (string): Twilio Account identifier
- `twilioAuthToken` (string): Twilio authentication token
- `twilioApiKey` (string): Twilio API key
- `twilioApiSecret` (string): Twilio API secret
- `smsEnabled` (boolean, default: true): Configure messaging webhook

**vonage:**
- `number` (string): Vonage phone number digits
- `credentialId` (string): Vonage credential reference

**vapi:**
- `sipUri` (string): SIP URI for incoming invitations
- `authentication` (SipAuthentication): Optional digest authentication
- `numberDesiredAreaCode` (string): Preferred area code

**telnyx:**
- `number` (string): Telnyx phone number digits
- `credentialId` (string): Telnyx credential reference

## Response

**Status: 200 OK**

Returns the updated phone number object matching the provider type, including:

- `id` (string): Unique identifier
- `orgId` (string): Organization ownership
- `provider` (string): Provider type
- `status` (enum): Current state—active, activating, or blocked
- `createdAt` (datetime): Creation timestamp
- `updatedAt` (datetime): Last modification timestamp
- All provided configuration fields

Provider-specific response fields mirror the request fields plus computed values like `sipUri` for Vapi numbers.

## Example Request

```json
{
  "provider": "vapi",
  "name": "Customer Support Line",
  "assistantId": "a-12345abc",
  "server": {
    "url": "https://example.com/webhook",
    "timeoutSeconds": 20
  },
  "sipUri": "sip:support@vapi.ai",
  "authentication": {
    "username": "user123",
    "password": "secure_pass"
  }
}
```

## Example Response

```json
{
  "id": "pn-abc123xyz",
  "orgId": "org-789def",
  "provider": "vapi",
  "status": "active",
  "name": "Customer Support Line",
  "assistantId": "a-12345abc",
  "sipUri": "sip:support@vapi.ai",
  "server": {
    "url": "https://example.com/webhook",
    "timeoutSeconds": 20
  },
  "createdAt": "2024-01-15T10:30:00Z",
  "updatedAt": "2024-01-20T14:45:00Z"
}
```

## Notes

- At least one of `assistantId`, `squadId`, or `workflowId` must be configured
- If none are set, inbound calls trigger an `assistant-request` webhook
- Transfer destinations support phone numbers or SIP URIs with customizable routing behavior
- Hook system enables call-ringing and call-ending event handlers
