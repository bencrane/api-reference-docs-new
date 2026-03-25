# Create Phone Number API Reference

## Endpoint

**POST** `https://api.vapi.ai/phone-number`

## Description

Creates a new phone number that can receive inbound calls and be connected to an assistant, squad, or workflow.

## Authentication

**Header Parameter:**
- `Authorization` (required): Your API Key from the Dashboard

## Request Body

The request uses a discriminator pattern based on the `provider` field. Five provider types are supported:

### Provider: `byo-phone-number`

Bring your own phone number via a SIP trunk or carrier.

**Required fields:**
- `provider`: "byo-phone-number"
- `credentialId`: SIP trunk/carrier credential ID
- `number`: Phone number digits

**Optional fields:**
- `name`: Reference name for the number
- `assistantId`: Assistant for incoming calls
- `squadId`: Squad for incoming calls
- `workflowId`: Workflow for incoming calls
- `numberE164CheckEnabled`: Toggle E164 validation (default: true)
- `fallbackDestination`: Transfer destination if assistant request fails
- `hooks`: Array of call event hooks
- `server`: Webhook configuration

### Provider: `twilio`

Import and manage a Twilio phone number.

**Required fields:**
- `provider`: "twilio"
- `number`: Phone number digits
- `twilioAccountSid`: Twilio Account SID

**Optional fields:**
- `twilioAuthToken`: Twilio Auth Token
- `twilioApiKey`: Twilio API Key
- `twilioApiSecret`: Twilio API Secret
- `smsEnabled`: Configure messaging webhook (default: true)
- `name`, `assistantId`, `squadId`, `workflowId`, `fallbackDestination`, `hooks`, `server`

### Provider: `vonage`

Manage a Vonage-owned phone number.

**Required fields:**
- `provider`: "vonage"
- `number`: Phone number digits
- `credentialId`: Vonage credential ID

**Optional fields:**
- `name`, `assistantId`, `squadId`, `workflowId`, `fallbackDestination`, `hooks`, `server`

### Provider: `vapi`

Purchase or manage a number from Vapi's inventory.

**Required fields:**
- `provider`: "vapi"

**Optional fields:**
- `numberDesiredAreaCode`: Requested area code
- `sipUri`: SIP URI for the number
- `authentication`: SIP authentication credentials
- `name`, `assistantId`, `squadId`, `workflowId`, `fallbackDestination`, `hooks`, `server`

### Provider: `telnyx`

Manage a Telnyx-owned phone number.

**Required fields:**
- `provider`: "telnyx"
- `number`: Phone number digits
- `credentialId`: Telnyx credential ID

**Optional fields:**
- `name`, `assistantId`, `squadId`, `workflowId`, `fallbackDestination`, `hooks`, `server`

## Response (201 Created)

Returns the created phone number object with all configuration details and metadata:

**Common response fields:**
- `id`: Unique phone number identifier
- `orgId`: Organization ID
- `provider`: Provider type
- `number`: Phone number digits
- `status`: "active", "activating", or "blocked"
- `createdAt`: ISO 8601 creation timestamp
- `updatedAt`: ISO 8601 last update timestamp
- `name`: Reference name
- `assistantId`, `squadId`, `workflowId`: Assigned handler
- `server`: Webhook configuration
- `fallbackDestination`: Fallback transfer details
- `hooks`: Configured event hooks

Provider-specific fields are included as applicable (e.g., `twilioAccountSid`, `credentialId`, `sipUri`).

## Key Concepts

**Assistant Assignment:** "If neither `assistantId`, `squadId` nor `workflowId` is set, `assistant-request` will be sent" to your server URL.

**Fallback Destination:** Used when assistant assignment fails; the call transfers here or hangs up with an error.

**Hooks:** Trigger custom actions on events like incoming calls or call termination based on filters.

**Transfer Plans:** Detailed configuration for call transfers, including warm/blind transfer modes, messages, and timeouts.
