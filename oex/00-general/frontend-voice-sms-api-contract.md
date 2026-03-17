# Frontend Voice & SMS API Contract

> Source of truth for the browser-based communications SDK.
> Auto-generated from source code by Directive 25.
> **Do not edit manually** — regenerate from source when endpoints change.

Last generated: 2026-03-17

---

## Summary

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | /api/voice/token | `voice.write` | Mint voice access token |
| POST | /api/voice/sessions/{call_sid}/disposition | `voice.write` | Set business disposition |
| POST | /api/voice/sessions/{call_sid}/action | `voice.write` | Modify a live call |
| GET | /api/voice/sessions | `voice.read` | List voice sessions |
| GET | /api/voice/sessions/{call_sid} | `voice.read` | Get single voice session |
| POST | /api/outbound-calls | `voice.write` | Initiate outbound call |
| GET | /api/outbound-calls/{call_sid} | `voice.read` | Get call status |
| POST | /api/sms | `sms.write` | Send SMS/MMS |
| GET | /api/sms/{message_sid} | `sms.read` | Get message status |
| GET | /api/sms | `sms.read` | List messages |

---

## Auth Model

- All endpoints require authentication via API token or JWT session.
- Auth is passed via `Authorization: Bearer <token>` header.
- The permission string listed for each endpoint is the RBAC permission checked. If the authenticated user's role does not include the required permission, the request returns `403`.
- `org_id` is always derived from the auth token, never from the request body.
- `company_id` is derived from auth context when available (set on the user record).
- Request bodies use `model_config = {"extra": "forbid"}` — unknown fields are rejected with a `422` validation error.

---

## Voice

### GET /api/voice/token

Mint a short-lived voice access token for the Twilio JS SDK.

**Auth**

Permission: `voice.write` via `require_permission("voice.write")`

**Query parameters**

None.

**Request body**

None.

**Response body**

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| `token` | string | no | JWT access token for Twilio Voice SDK |
| `identity` | string | no | User identity embedded in the token (user_id) |
| `ttl_seconds` | integer | no | Token time-to-live in seconds |

**Error responses**

| Status | Condition | Body |
|--------|-----------|------|
| 400 | Twilio account_sid or auth_token missing | `{"detail": "Twilio credentials not configured for this organization"}` |
| 400 | API Key credentials missing | `{"detail": "Twilio API Key credentials (api_key_sid, api_key_secret) not configured for this organization"}` |
| 400 | TwiML App SID missing | `{"detail": "TwiML Application SID (twiml_app_sid) not configured for this organization"}` |
| 404 | Organization not found | `{"detail": "Organization not found"}` |

---

### POST /api/voice/sessions/{call_sid}/disposition

Set the business disposition for a voice session.

**Auth**

Permission: `voice.write` via `require_permission("voice.write")`

**Path parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| `call_sid` | string | Twilio Call SID |

**Request body**

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `disposition` | string | yes | — | Must be one of: `busy`, `callback_scheduled`, `disqualified`, `do_not_call`, `follow_up_needed`, `gatekeeper`, `left_voicemail`, `meeting_booked`, `no_answer`, `not_interested`, `other`, `qualified`, `wrong_number` | Call outcome |
| `notes` | string \| null | no | null | — | Optional free-text notes about the call outcome |

If `notes` is provided, it is stored in the session's `last_callback_payload` under the key `disposition_notes`.

**Response body**

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| `call_sid` | string | no | Twilio Call SID |
| `business_disposition` | string | no | The disposition that was set |
| `updated_at` | string | no | ISO 8601 timestamp of the update |

**Error responses**

| Status | Condition | Body |
|--------|-----------|------|
| 400 | Invalid disposition value | `{"detail": "Invalid disposition '<value>'. Must be one of: busy, callback_scheduled, disqualified, do_not_call, follow_up_needed, gatekeeper, left_voicemail, meeting_booked, no_answer, not_interested, other, qualified, wrong_number"}` |
| 404 | Voice session not found | `{"detail": "Voice session not found"}` |

---

### POST /api/voice/sessions/{call_sid}/action

Modify a live call (hangup, redirect, hold, unhold).

**Auth**

Permission: `voice.write` via `require_permission("voice.write")`

**Path parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| `call_sid` | string | Twilio Call SID |

**Request body**

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `action` | string | yes | — | Must be one of: `hangup`, `hold`, `redirect`, `unhold` | The action to perform on the live call |
| `twiml` | string \| null | no | null | — | TwiML to redirect to (for `redirect` action) |
| `url` | string \| null | no | null | — | URL returning TwiML (for `redirect` action) |

**Action-specific validation:**
- `redirect` requires either `url` or `twiml` to be provided. If neither is set, returns `400`.
- `hangup` sets the call status to `completed`.
- `hold` redirects the call to hold music TwiML.
- `unhold` redirects the call back to the org's Twilio webhook URL.

**Response body**

This endpoint does not use a typed response model. It returns one of two shapes:

*Case 1: Session re-fetched successfully* — returns the raw `voice_sessions` row. See `VoiceSessionResponse` fields for the approximate shape.

*Case 2: Session re-fetch returns empty* — returns:

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| `call_sid` | string | no | The call SID acted upon |
| `action` | string | no | The action that was performed |

**Error responses**

| Status | Condition | Body |
|--------|-----------|------|
| 400 | Invalid action value | `{"detail": "Invalid action '<value>'. Must be one of: hangup, hold, redirect, unhold"}` |
| 400 | redirect without url or twiml | `{"detail": "redirect requires url or twiml"}` |
| 400 | Twilio credentials missing | `{"detail": "Twilio credentials not configured for this organization"}` |
| 404 | Organization not found | `{"detail": "Organization not found"}` |
| 404 | Voice session not found | `{"detail": "Voice session not found"}` |
| 502 | Twilio API error | `{"detail": "Twilio API error: <error message>"}` |

---

### GET /api/voice/sessions

List voice sessions for the organization.

**Auth**

Permission: `voice.read` via `require_permission("voice.read")`

**Query parameters**

| Parameter | Type | Required | Default | Constraints | Description |
|-----------|------|----------|---------|-------------|-------------|
| `company_id` | string | no | null | — | Filter by company |
| `company_campaign_id` | string | no | null | — | Filter by campaign |
| `direction` | string | no | null | — | Filter by call direction (e.g. `inbound`, `outbound`) |
| `status` | string | no | null | — | Filter by call status (query param `status`, aliased from `status_filter` internally) |
| `disposition` | string | no | null | — | Filter by business disposition |
| `limit` | integer | no | 50 | max 200 | Page size |
| `offset` | integer | no | 0 | — | Pagination offset |

**Response body**

Array of `VoiceSessionResponse`:

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| `id` | string | no | Voice session UUID |
| `call_sid` | string | no | Twilio Call SID |
| `direction` | string | no | `inbound` or `outbound` |
| `from_number` | string | no | Caller phone number |
| `to_number` | string | no | Called phone number |
| `status` | string | no | Call status |
| `agent_identity` | string \| null | yes | Identity of the agent on the call |
| `duration_seconds` | integer \| null | yes | Call duration in seconds |
| `business_disposition` | string \| null | yes | Disposition set by agent |
| `amd_result` | string \| null | yes | Answering Machine Detection result |
| `recording_sid` | string \| null | yes | Twilio Recording SID |
| `recording_url` | string \| null | yes | URL to the recording |
| `recording_duration_seconds` | integer \| null | yes | Recording duration in seconds |
| `company_id` | string \| null | yes | Associated company |
| `company_campaign_id` | string \| null | yes | Associated campaign |
| `company_campaign_lead_id` | string \| null | yes | Associated campaign lead |
| `started_at` | string \| null | yes | ISO 8601 timestamp |
| `answered_at` | string \| null | yes | ISO 8601 timestamp |
| `ended_at` | string \| null | yes | ISO 8601 timestamp |
| `created_at` | string | no | ISO 8601 timestamp |
| `updated_at` | string | no | ISO 8601 timestamp |

**Error responses**

No endpoint-specific errors beyond shared errors.

---

### GET /api/voice/sessions/{call_sid}

Get a single voice session by call SID.

**Auth**

Permission: `voice.read` via `require_permission("voice.read")`

**Path parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| `call_sid` | string | Twilio Call SID |

**Response body**

Single `VoiceSessionResponse` (see field listing under [GET /api/voice/sessions](#get-apivoicesessions)).

**Error responses**

| Status | Condition | Body |
|--------|-----------|------|
| 404 | Voice session not found | `{"detail": "Voice session not found"}` |

---

## Outbound Calls

### POST /api/outbound-calls

Initiate an outbound call.

**Auth**

Permission: `voice.write` via `require_permission("voice.write")`

**Request body**

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `to` | string | yes | — | E.164 format | Phone number to call |
| `from_number` | string | yes | — | E.164 format | Caller ID (must be owned by org) |
| `greeting_text` | string \| null | no | null | — | Text spoken when call connects (before AMD). If omitted, a brief pause is used. |
| `voicemail_text` | string \| null | no | null | Mutually exclusive with `voicemail_audio_url` | Text-to-speech voicemail message if machine answers |
| `voicemail_audio_url` | string \| null | no | null | Mutually exclusive with `voicemail_text` | Pre-recorded audio URL for voicemail drop |
| `human_message_text` | string \| null | no | null | — | Text spoken if a human answers. Required for system-initiated calls with no rep. |
| `record` | boolean | no | false | — | Whether to record the call |
| `timeout` | integer | no | 30 | min 5, max 120 (`ge=5, le=120`) | Ring timeout in seconds |
| `company_campaign_id` | string \| null | no | null | — | Associated campaign ID |
| `company_campaign_lead_id` | string \| null | no | null | — | Associated campaign lead ID |

**Validation rules:**
- `voicemail_text` and `voicemail_audio_url` are mutually exclusive. Providing both returns `400`.

**Response body**

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| `call_sid` | string | no | Twilio Call SID |
| `status` | string | no | Initial call status |
| `direction` | string | no | Call direction |
| `from_number` | string | no | Caller ID used |
| `to` | string | no | Destination number |
| `voice_session_id` | string \| null | yes | UUID of the created voice session |

**Error responses**

| Status | Condition | Body |
|--------|-----------|------|
| 400 | Both voicemail_text and voicemail_audio_url provided | `{"detail": "Cannot provide both voicemail_text and voicemail_audio_url"}` |
| 400 | Twilio credentials missing | `{"detail": "Twilio credentials not configured for this organization"}` |
| 404 | Organization not found | `{"detail": "Organization not found"}` |
| 502 | Twilio API error | `{"detail": "Twilio API error: <error message>"}` |

---

### GET /api/outbound-calls/{call_sid}

Get call status from voice_sessions.

> **Note:** This endpoint has no typed response model — it returns the raw `voice_sessions` database row. The `VoiceSessionResponse` fields are the closest approximation.

**Auth**

Permission: `voice.read` via `require_permission("voice.read")`

**Path parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| `call_sid` | string | Twilio Call SID |

**Response body**

Raw `voice_sessions` row. See `VoiceSessionResponse` fields under [GET /api/voice/sessions](#get-apivoicesessions) for approximate shape. Additional database columns not in the typed model may also be present.

**Error responses**

| Status | Condition | Body |
|--------|-----------|------|
| 404 | Call not found | `{"detail": "Call not found"}` |

---

## SMS

### POST /api/sms

Send an SMS/MMS message.

**Auth**

Permission: `sms.write` via `require_permission("sms.write")`

**Request body**

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `to` | string | yes | — | E.164 format | Phone number to send to |
| `body` | string \| null | no | null | Up to 1600 chars | Text content of the message |
| `from_number` | string \| null | no | null | E.164 format; mutually exclusive with `messaging_service_sid` | Sender number. If omitted, uses Messaging Service. |
| `messaging_service_sid` | string \| null | no | null | Mutually exclusive with `from_number` | Messaging Service SID for sender pool routing |
| `media_url` | string[] \| null | no | null | Max 10 URLs | URLs of media to attach (MMS) |
| `company_campaign_id` | string \| null | no | null | — | Associated campaign ID |
| `company_campaign_lead_id` | string \| null | no | null | — | Associated campaign lead ID |

**Validation rules (4 rules):**

1. **Body or media required** — at least one of `body` or `media_url` must be provided. If neither is set, returns `400`.
2. **Max 10 media URLs** — if `media_url` has more than 10 items, returns `400`.
3. **from_number / messaging_service_sid mutually exclusive** — providing both returns `400`.
4. **Fallback to org-level Messaging Service** — if neither `from_number` nor `messaging_service_sid` is provided, the system falls back to the org's configured `messaging_service_sid` from `provider_configs.twilio.messaging_service_sid`. If that is also not configured, returns `400`.

**Response body**

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| `message_sid` | string | no | Twilio Message SID |
| `status` | string | no | Initial message status |
| `direction` | string | no | Message direction |
| `from_number` | string | no | Sender number used |
| `to` | string | no | Destination number |

**Error responses**

| Status | Condition | Body |
|--------|-----------|------|
| 400 | No body or media_url | `{"detail": "Must provide at least one of body or media_url"}` |
| 400 | More than 10 media URLs | `{"detail": "Maximum 10 media URLs allowed"}` |
| 400 | Both from_number and messaging_service_sid | `{"detail": "Cannot provide both from_number and messaging_service_sid"}` |
| 400 | No sender and no default Messaging Service | `{"detail": "No sender specified and no default Messaging Service configured."}` |
| 400 | Twilio credentials missing | `{"detail": "Twilio credentials not configured for this organization"}` |
| 404 | Organization not found | `{"detail": "Organization not found"}` |
| 502 | Twilio API error | `{"detail": "Twilio API error: <error message>"}` |

---

### GET /api/sms/{message_sid}

Get message status from sms_messages.

**Auth**

Permission: `sms.read` via `require_permission("sms.read")`

**Path parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| `message_sid` | string | Twilio Message SID |

**Response body**

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| `id` | string | no | SMS message UUID |
| `message_sid` | string | no | Twilio Message SID |
| `direction` | string | no | `inbound` or `outbound` |
| `from_number` | string | no | Sender phone number |
| `to_number` | string | no | Recipient phone number |
| `body` | string \| null | yes | Message text |
| `status` | string | no | Message delivery status |
| `error_code` | integer \| null | yes | Twilio error code if failed |
| `error_message` | string \| null | yes | Twilio error message if failed |
| `num_segments` | integer \| null | yes | Number of SMS segments |
| `num_media` | integer \| null | yes | Number of media attachments |
| `media_urls` | string[] \| null | yes | URLs of attached media |
| `date_sent` | string \| null | yes | ISO 8601 timestamp when sent |
| `created_at` | string | no | ISO 8601 timestamp |
| `updated_at` | string | no | ISO 8601 timestamp |

**Error responses**

| Status | Condition | Body |
|--------|-----------|------|
| 404 | Message not found | `{"detail": "Message not found"}` |

---

### GET /api/sms

List messages for the org with pagination.

**Auth**

Permission: `sms.read` via `require_permission("sms.read")`

**Query parameters**

| Parameter | Type | Required | Default | Constraints | Description |
|-----------|------|----------|---------|-------------|-------------|
| `direction` | string | no | null | — | Filter by direction (`inbound`, `outbound`) |
| `status` | string | no | null | — | Filter by message status (query param `status`, aliased from `sms_status` internally) |
| `limit` | integer | no | 50 | min 1, max 200 (`ge=1, le=200`) | Page size |
| `offset` | integer | no | 0 | min 0 (`ge=0`) | Pagination offset |

**Response body**

Array of `SmsMessageResponse` (see field listing under [GET /api/sms/{message_sid}](#get-apismsmessage_sid)).

**Error responses**

No endpoint-specific errors beyond shared errors.

---

## Shared Error Responses

These errors can be returned by any endpoint:

| Status | Condition | Body |
|--------|-----------|------|
| 401 | Missing authorization header | `{"detail": "Missing authorization header"}` |
| 401 | Invalid or expired token | `{"detail": "Invalid or expired token"}` |
| 403 | Insufficient permissions | `{"detail": "Permission required: <permission_key>"}` |
| 404 | Organization not found (credential resolution) | `{"detail": "Organization not found"}` |
| 400 | Twilio credentials not configured (credential resolution) | `{"detail": "Twilio credentials not configured for this organization"}` |
| 422 | Request body validation failure (missing required fields, unknown fields, type errors) | Pydantic validation error |

---

## TypeScript Type Definitions

```typescript
// --- Voice ---

interface VoiceTokenResponse {
  token: string;
  identity: string;
  ttl_seconds: number;
}

interface VoiceSessionResponse {
  id: string;
  call_sid: string;
  direction: string;
  from_number: string;
  to_number: string;
  status: string;
  agent_identity: string | null;
  duration_seconds: number | null;
  business_disposition: string | null;
  amd_result: string | null;
  recording_sid: string | null;
  recording_url: string | null;
  recording_duration_seconds: number | null;
  company_id: string | null;
  company_campaign_id: string | null;
  company_campaign_lead_id: string | null;
  started_at: string | null;
  answered_at: string | null;
  ended_at: string | null;
  created_at: string;
  updated_at: string;
}

interface DispositionRequest {
  disposition: string;
  notes?: string | null;
}

interface DispositionResponse {
  call_sid: string;
  business_disposition: string;
  updated_at: string;
}

interface CallActionRequest {
  action: string;
  twiml?: string | null;
  url?: string | null;
}

// --- Outbound Calls ---

interface OutboundCallRequest {
  to: string;
  from_number: string;
  greeting_text?: string | null;
  voicemail_text?: string | null;
  voicemail_audio_url?: string | null;
  human_message_text?: string | null;
  record?: boolean;
  timeout?: number;
  company_campaign_id?: string | null;
  company_campaign_lead_id?: string | null;
}

interface OutboundCallResponse {
  call_sid: string;
  status: string;
  direction: string;
  from_number: string;
  to: string;
  voice_session_id: string | null;
}

// --- SMS ---

interface SendSmsRequest {
  to: string;
  body?: string | null;
  from_number?: string | null;
  messaging_service_sid?: string | null;
  media_url?: string[] | null;
  company_campaign_id?: string | null;
  company_campaign_lead_id?: string | null;
}

interface SendSmsResponse {
  message_sid: string;
  status: string;
  direction: string;
  from_number: string;
  to: string;
}

interface SmsMessageResponse {
  id: string;
  message_sid: string;
  direction: string;
  from_number: string;
  to_number: string;
  body: string | null;
  status: string;
  error_code: number | null;
  error_message: string | null;
  num_segments: number | null;
  num_media: number | null;
  media_urls: string[] | null;
  date_sent: string | null;
  created_at: string;
  updated_at: string;
}
```
