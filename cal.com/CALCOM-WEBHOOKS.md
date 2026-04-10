# Cal.com Webhooks -- Complete Reference

> All webhook trigger events, payload shapes, verification, and configuration details.

---

## Table of Contents

1. [Webhook Registration Levels](#1-webhook-registration-levels)
2. [All Trigger Events](#2-all-trigger-events)
3. [Payload Structure](#3-payload-structure)
4. [HMAC Verification](#4-hmac-verification)
5. [Custom Payload Templates](#5-custom-payload-templates)
6. [Webhook Versioning](#6-webhook-versioning)
7. [Webhook CRUD Operations](#7-webhook-crud-operations)

---

## 1. Webhook Registration Levels

Webhooks can be registered at three levels, controlling the scope of events they receive:

| Level | Endpoint | Fires For | Response Contains |
|---|---|---|---|
| **User-level** | `POST /v2/webhooks` | All bookings where authenticated user is involved | `userId` |
| **Event-type-level** | `POST /v2/event-types/{eventTypeId}/webhooks` | Only bookings for that specific event type | `eventTypeId` |
| **Org-level** | `POST /v2/organizations/{orgId}/webhooks` | All events across the entire organization | `platformOwnerId` |

Additionally, there are:
- **Team event-type-level:** `POST /v2/teams/{teamId}/event-types/{eventTypeId}/webhooks`
- **Org team event-type-level:** `POST /v2/organizations/{orgId}/teams/{teamId}/event-types/{eventTypeId}/webhooks`
- **Deprecated platform-level:** `POST /v2/oauth-clients/{clientId}/webhooks` (contains `oAuthClientId`)

**Auth requirements:**
- User-level webhooks: API key only (`cal_` prefix)
- Event-type-level webhooks: API key, managed user access token, or OAuth access token
- Org-level webhooks: API key with org admin/owner role (or PBAC permission `webhook.create`)

---

## 2. All Trigger Events

### Complete Trigger List (21 events)

| Trigger | Description | Requires Existing Booking |
|---|---|---|
| **Booking Lifecycle** |||
| `BOOKING_CREATED` | New booking created | No (creates one) |
| `BOOKING_REQUESTED` | Booking requires manual confirmation (pending state) | No (creates one) |
| `BOOKING_RESCHEDULED` | Existing booking rescheduled to new time | Yes |
| `BOOKING_CANCELLED` | Booking cancelled by host or attendee | Yes |
| `BOOKING_REJECTED` | Pending booking rejected by host | Yes |
| `BOOKING_NO_SHOW_UPDATED` | No-show status updated (mark-absent) | Yes |
| **Payment** |||
| `BOOKING_PAYMENT_INITIATED` | Payment process started for a booking | Yes |
| `BOOKING_PAID` | Payment completed for a booking | Yes |
| **Meeting Events** |||
| `MEETING_STARTED` | Cal Video meeting started | Yes |
| `MEETING_ENDED` | Cal Video meeting ended | Yes |
| `INSTANT_MEETING` | Instant meeting created (bypasses scheduling) | No (creates one) |
| **Recording & Transcription** |||
| `RECORDING_READY` | Cal Video recording is ready for download | Yes |
| `RECORDING_TRANSCRIPTION_GENERATED` | Cal Video transcription generated | Yes |
| **Routing Forms** |||
| `FORM_SUBMITTED` | Routing form submitted (with event created) | No |
| `FORM_SUBMITTED_NO_EVENT` | Routing form submitted (no event created) | No |
| `ROUTING_FORM_FALLBACK_HIT` | Routing form hit fallback route | No |
| **Out-of-Office** |||
| `OOO_CREATED` | Out-of-office entry created | No |
| **No-Show Detection** |||
| `AFTER_HOSTS_CAL_VIDEO_NO_SHOW` | Host didn't join Cal Video meeting | Yes |
| `AFTER_GUESTS_CAL_VIDEO_NO_SHOW` | Guest didn't join Cal Video meeting | Yes |
| **System** |||
| `DELEGATION_CREDENTIAL_ERROR` | Error with delegation credentials | No |
| `WRONG_ASSIGNMENT_REPORT` | Wrong assignment reported on a booking | Yes |

### Trigger Categorization

**Events that create bookings:**
- `BOOKING_CREATED`, `BOOKING_REQUESTED`, `INSTANT_MEETING`

**Events that modify existing bookings:**
- `BOOKING_RESCHEDULED`, `BOOKING_CANCELLED`, `BOOKING_REJECTED`, `BOOKING_NO_SHOW_UPDATED`

**Events independent of bookings:**
- `FORM_SUBMITTED`, `FORM_SUBMITTED_NO_EVENT`, `ROUTING_FORM_FALLBACK_HIT`, `OOO_CREATED`, `DELEGATION_CREDENTIAL_ERROR`

**Cal Video-only events (require Cal Video as location):**
- `MEETING_STARTED`, `MEETING_ENDED`, `RECORDING_READY`, `RECORDING_TRANSCRIPTION_GENERATED`, `AFTER_HOSTS_CAL_VIDEO_NO_SHOW`, `AFTER_GUESTS_CAL_VIDEO_NO_SHOW`

### Discrepancy Note

The API docs' cURL examples show trigger values `BOOKING_CONFIRMED`, `BOOKING_COMPLETED`, `BOOKING_NO_SHOW`, and `BOOKING_REOPENED` in example arrays, but these are NOT in the formal enum. They may be undocumented, deprecated, or example errors. Use only the 21 triggers listed above.

---

## 3. Payload Structure

### Standard Booking Payload (most triggers)

Triggers like `BOOKING_CREATED`, `BOOKING_REQUESTED`, `BOOKING_RESCHEDULED`, `BOOKING_CANCELLED`, `BOOKING_REJECTED`, `BOOKING_NO_SHOW_UPDATED`, `BOOKING_PAYMENT_INITIATED`, `BOOKING_PAID`, and `INSTANT_MEETING` all send a booking payload.

Based on the live API booking object shape (validated against actual responses):

```json
{
  "triggerEvent": "BOOKING_CREATED",
  "createdAt": "2026-04-10T01:20:38.024Z",
  "payload": {
    "id": 18140519,
    "uid": "uEMA1kr2TCZv5X3CbDrwDJ",
    "title": "Quick Call between Benjamin Crane and Magic Johnson",
    "description": "",
    "status": "accepted",
    "start": "2026-04-10T13:25:00.000Z",
    "end": "2026-04-10T13:50:00.000Z",
    "duration": 25,
    "eventTypeId": 3863864,
    "eventType": {
      "id": 3863864,
      "slug": "25min"
    },
    "location": "https://meet.google.com/mwe-jxnm-bem",
    "meetingUrl": "https://meet.google.com/mwe-jxnm-bem",
    "hosts": [
      {
        "id": 1905657,
        "name": "Benjamin Crane",
        "email": "benjamin.crane@revenueengineer.com",
        "displayEmail": "benjamin.crane@revenueengineer.com",
        "username": "outbound-solutions",
        "timeZone": "America/New_York"
      }
    ],
    "attendees": [
      {
        "name": "Magic Johnson",
        "email": "magic@showtime.com",
        "displayEmail": "magic@showtime.com",
        "timeZone": "America/New_York",
        "language": "en",
        "absent": false
      }
    ],
    "guests": [],
    "bookingFieldsResponses": {
      "email": "magic@showtime.com",
      "name": "Magic Johnson",
      "guests": [],
      "location": {
        "value": "integrations:google:meet",
        "optionValue": ""
      }
    },
    "metadata": {},
    "absentHost": false,
    "createdAt": "2026-04-10T01:20:38.024Z",
    "updatedAt": "2026-04-10T01:20:40.754Z",
    "cancellationReason": "",
    "cancelledByEmail": "",
    "rescheduledByEmail": null,
    "rescheduledFromUid": null,
    "rescheduledToUid": null,
    "rating": null,
    "icsUid": "uEMA1kr2TCZv5X3CbDrwDJ@Cal.com"
  }
}
```

### Cancellation Payload Additions

When `triggerEvent` is `BOOKING_CANCELLED`:
- `payload.cancellationReason` -- the reason string
- `payload.cancelledByEmail` -- email of the person who cancelled

### Reschedule Payload Additions

When `triggerEvent` is `BOOKING_RESCHEDULED`:
- `payload.rescheduledFromUid` -- UID of the original booking
- `payload.rescheduledByEmail` -- email of person who rescheduled
- `payload.reschedulingReason` -- reason for rescheduling

### MEETING_STARTED / MEETING_ENDED Payload

These have a **flat structure** (not nested under `payload`):

```json
{
  "triggerEvent": "MEETING_STARTED",
  "createdAt": "2024-01-15T10:00:00Z",
  "bookingId": 123,
  "roomName": "daily-video-room-123",
  "startTime": 1678901234,
  "participants": [
    {
      "userId": "user123",
      "userName": "John Doe",
      "joinTime": 1678901234
    }
  ]
}
```

This is a structural difference from all other webhook events -- `MEETING_STARTED` and `MEETING_ENDED` use a flat format rather than the standard `{ triggerEvent, createdAt, payload: { ... } }` envelope.

### RECORDING_READY Payload

```json
{
  "triggerEvent": "RECORDING_READY",
  "createdAt": "2024-01-15T11:00:00Z",
  "payload": {
    "bookingId": 123,
    "recordings": [
      {
        "id": "1234567890",
        "roomName": "daily-video-room-123",
        "startTs": 1678901234,
        "status": "completed",
        "duration": 3600,
        "shareToken": "share-token-123",
        "maxParticipants": 10,
        "downloadLink": "https://cal-video-recordings.s3.us-east-2.amazonaws.com/..."
      }
    ]
  }
}
```

### FORM_SUBMITTED Payload

```json
{
  "triggerEvent": "FORM_SUBMITTED",
  "createdAt": "2024-01-15T10:00:00Z",
  "payload": {
    "formId": "routing-form-uuid",
    "responses": { ... },
    "eventTypeId": 123,
    "booking": { ... }
  }
}
```

### OOO_CREATED Payload

```json
{
  "triggerEvent": "OOO_CREATED",
  "createdAt": "2024-01-15T10:00:00Z",
  "payload": {
    "userId": 2,
    "id": 2,
    "uuid": "e84be5a3-4696-49e3-acc7-b2f3999c3b94",
    "start": "2023-05-01T00:00:00.000Z",
    "end": "2023-05-10T23:59:59.999Z",
    "toUserId": 2,
    "notes": "Vacation in Hawaii",
    "reason": "vacation"
  }
}
```

---

## 4. HMAC Verification

Webhooks support HMAC signing for payload verification:

1. **Set the secret** when creating/updating the webhook:
   ```json
   { "secret": "your-hmac-secret" }
   ```

2. **Verify incoming payloads** by computing an HMAC signature over the raw request body and comparing it to the signature header sent by Cal.com.

The docs reference `cal.com/docs/core-features/webhooks` for the specific header name and algorithm. Based on Cal.com's standard implementation:
- The signature is sent in the `X-Cal-Signature-256` header
- Algorithm: HMAC-SHA256
- Compute `HMAC-SHA256(secret, raw_body)` and compare to the header value

---

## 5. Custom Payload Templates

The `payloadTemplate` field uses **Mustache-style double-brace syntax** for variable interpolation.

### Available Template Variables

| Variable | Description |
|---|---|
| `{{type}}` | The trigger event type |
| `{{title}}` | Booking/event title |
| `{{organizer.name}}` | Organizer's name |
| `{{organizer.email}}` | Organizer's email |
| `{{attendees.0.name}}` | First attendee's name |
| `{{attendees.0.email}}` | First attendee's email |
| `{{startTime}}` | Booking start time |
| `{{endTime}}` | Booking end time |
| `{{location}}` | Meeting location/URL |

### Example Template

```json
{
  "payloadTemplate": "{\"content\":\"A new event has been scheduled\",\"type\":\"{{type}}\",\"name\":\"{{title}}\",\"organizer\":\"{{organizer.name}}\",\"booker\":\"{{attendees.0.name}}\"}"
}
```

When `payloadTemplate` is set, the webhook sends only the rendered template instead of the full payload. This is useful for integrating with services like Slack or Discord that expect a specific format.

If `payloadTemplate` is null/omitted, the full default payload is sent.

---

## 6. Webhook Versioning

Currently one version available: `"2021-10-20"`.

Set via the `version` field when creating/updating a webhook. This controls the payload shape. The current version is the default if not specified.

---

## 7. Webhook CRUD Operations

### Create

```
POST /v2/webhooks                                              (user-level)
POST /v2/event-types/{eventTypeId}/webhooks                    (event-type-level)
POST /v2/teams/{teamId}/event-types/{eventTypeId}/webhooks     (team event-type-level)
POST /v2/organizations/{orgId}/webhooks                        (org-level)
```

**Request body:**

| Field | Type | Required | Description |
|---|---|---|---|
| `subscriberUrl` | string | **required** | URL to receive webhook payloads |
| `triggers` | string[] | **required** | Array of trigger event names |
| `active` | boolean | **required** | Whether webhook is active |
| `secret` | string | optional | HMAC signing secret |
| `payloadTemplate` | string | optional | Custom payload template |
| `version` | enum | optional | `"2021-10-20"` |

**Response:**

```json
{
  "status": "success",
  "data": {
    "id": 123,
    "subscriberUrl": "https://...",
    "triggers": ["BOOKING_CREATED"],
    "active": true,
    "secret": "...",
    "payloadTemplate": "...",
    "userId": 456,
    "eventTypeId": null
  }
}
```

The response contains `userId` (user-level), `eventTypeId` (event-type-level), `platformOwnerId` (org-level), or `oAuthClientId` (deprecated platform-level) depending on the registration level.

### Read

```
GET /v2/webhooks                                               (list all user webhooks)
GET /v2/webhooks/{webhookId}                                   (get specific)
GET /v2/event-types/{eventTypeId}/webhooks                     (list event-type webhooks)
GET /v2/event-types/{eventTypeId}/webhooks/{webhookId}         (get specific)
```

List endpoints support `take` (default 250) and `skip` (default 0) pagination.

### Update

```
PATCH /v2/webhooks/{webhookId}
PATCH /v2/event-types/{eventTypeId}/webhooks/{webhookId}
```

All fields optional. Same schema as create.

### Delete

```
DELETE /v2/webhooks/{webhookId}                                (single user webhook)
DELETE /v2/event-types/{eventTypeId}/webhooks/{webhookId}      (single event-type webhook)
DELETE /v2/event-types/{eventTypeId}/webhooks                  (ALL event-type webhooks)
```

Note: Event-type-level has a "delete all" endpoint; user-level does not.

---

## Workflow-Based Automation vs. Webhooks

For org-team event types, Cal.com also supports **Workflows** -- server-side automation that can send emails, SMS, WhatsApp messages, or trigger AI phone calls based on booking events. Workflows are configured via the org-team endpoints and do not require an external webhook receiver.

| Feature | Webhooks | Workflows |
|---|---|---|
| Where logic runs | Your server | Cal.com server |
| Trigger types | 21 event types | 12 event-type triggers + 2 routing-form triggers |
| Actions | HTTP POST to your URL | Email, SMS, WhatsApp, AI phone call |
| Custom logic | Full control | Templates only |
| Scope | User, event-type, or org | Team event types or routing forms |
| Availability | All plans | Org-team level only |
