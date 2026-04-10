# Cal.com API -- Operations Guide & Known Gaps

> Use-case-driven cookbook + documented limitations and ambiguities.

---

## Table of Contents

1. [Key API Operations by Use Case](#1-key-api-operations-by-use-case)
2. [Gaps & Limitations](#2-gaps--limitations)
3. [Deprecations](#3-deprecations)
4. [Doc Contradictions & Ambiguities](#4-doc-contradictions--ambiguities)

---

## 1. Key API Operations by Use Case

### 1.1 Booking a Meeting on Behalf of Someone

**Flow: Check availability → Reserve slot → Create booking**

```
Step 1: Get available slots
GET /v2/slots?eventTypeId=123&start=2024-08-13&end=2024-08-14&timeZone=America/New_York
Header: cal-api-version: 2024-09-04

Step 2 (optional): Reserve a slot to prevent double-booking
POST /v2/slots/reservations
Header: cal-api-version: 2024-09-04
Body: { "eventTypeId": 123, "slotStart": "2024-08-13T14:00:00Z", "reservationDuration": 10 }
→ Returns reservationUid

Step 3: Create the booking
POST /v2/bookings
Header: cal-api-version: 2026-02-25
Body: {
  "start": "2024-08-13T14:00:00Z",
  "eventTypeId": 123,
  "attendee": {
    "name": "Client Name",
    "email": "client@example.com",
    "timeZone": "America/New_York"
  },
  "metadata": { "source": "ai-agent", "externalId": "deal-456" }
}
```

**Key details:**
- `POST /v2/bookings` is PUBLIC -- no auth required. Auth is optional (enables `allowConflicts` and `allowBookingOutOfBounds` for hosts).
- Start time MUST be in UTC. Convert from local time before sending.
- For team event types, use `teamSlug` + `eventTypeSlug` instead of (or in addition to) `eventTypeId`.
- For multi-duration event types, pass `lengthInMinutes` to select desired duration.
- For instant meetings, add `"instant": true` -- bypasses scheduling, immediately rings available team members.
- For recurring event types, the API automatically creates all recurrence bookings.
- Slot reservations default to 5 minutes. Authenticated requests can set custom `reservationDuration`.

**Booking with custom fields:**
If the event type has custom booking fields, include them in `bookingFieldsResponses`:
```json
{
  "bookingFieldsResponses": {
    "company": "Acme Corp",
    "phone": "+15551234567"
  }
}
```
To discover required fields, fetch the event type first -- `bookingFields` array shows all custom questions with `required` flags.

**Booking with email verification:**
If the event type has `requiresBookerEmailVerification: true`, the booker must verify their email. Include `emailVerificationCode` in the booking request.

### 1.2 Checking Availability for a User or Team

**By event type ID (simplest):**
```
GET /v2/slots?eventTypeId=123&start=2024-08-13&end=2024-08-20&timeZone=America/New_York
```

**By username + slug:**
```
GET /v2/slots?username=outbound-solutions&eventTypeSlug=25min&start=2024-08-13&end=2024-08-20
```

**By team slug:**
```
GET /v2/slots?teamSlug=sales-team&eventTypeSlug=demo&start=2024-08-13&end=2024-08-20
```

**For multiple users (dynamic event type):**
```
GET /v2/slots?usernames=alice,bob&username=bob&organizationSlug=my-org&start=2024-08-13&end=2024-08-20
```

**With org context:**
```
GET /v2/slots?organizationSlug=my-org&username=bob&eventTypeSlug=intro&start=2024-08-13&end=2024-08-20
```

**Notes:**
- Response organizes slots by date. Each slot has `start` (and optionally `end` with `format=range`).
- For seated event types, slots include `attendeesCount` and `bookingUid`.
- For managed event types (templates), you CANNOT query slots by the parent event type ID. You must find the child event type IDs first and query each individually.
- Use `bookingUidToReschedule` to show the original time slot as available when rescheduling.

### 1.3 Managing Event Types (CRUD)

**Create personal event type:**
```
POST /v2/event-types
Header: cal-api-version: 2024-06-14
Body: {
  "title": "30 Minute Meeting",
  "slug": "30min",
  "lengthInMinutes": 30,
  "locations": [{ "type": "integration", "integration": "google-meet" }]
}
```

**Create team event type:**
```
POST /v2/teams/{teamId}/event-types
Header: cal-api-version: 2024-06-14
Body: {
  "title": "Team Demo",
  "slug": "demo",
  "lengthInMinutes": 45,
  "schedulingType": "roundRobin",
  "hosts": [
    { "userId": 123, "mandatory": false, "priority": "high" },
    { "userId": 456, "mandatory": true, "priority": "medium" }
  ],
  "locations": [{ "type": "integration", "integration": "google-meet" }]
}
```

**Update event type:**
```
PATCH /v2/event-types/{eventTypeId}
```
All fields optional. WARNING: `bookingFields` is a FULL REPLACEMENT. Fetch current fields first, modify, then send the complete array. Sending only one field removes all others.

**List event types:**
```
GET /v2/event-types?username=outbound-solutions
```
Hidden event types only returned when authenticated as the owner.

### 1.4 Managing Webhooks

**Create a user-level webhook:**
```
POST /v2/webhooks
Body: {
  "subscriberUrl": "https://your-server.com/calcom-webhook",
  "triggers": ["BOOKING_CREATED", "BOOKING_CANCELLED", "BOOKING_RESCHEDULED"],
  "active": true,
  "secret": "hmac-signing-secret"
}
```

**Create an event-type-level webhook:**
```
POST /v2/event-types/{eventTypeId}/webhooks
```
Same body schema.

**Create an org-level webhook:**
```
POST /v2/organizations/{orgId}/webhooks
Header: cal-api-version: 2024-08-13
```
Same body schema. Requires org admin/owner role.

### 1.5 Managing Teams and Memberships

**Create a team:**
```
POST /v2/teams
Body: {
  "name": "Sales Team",
  "slug": "sales",
  "timeZone": "America/New_York",
  "autoAcceptCreator": true
}
```
IMPORTANT: Platform customers should NOT set `autoAcceptCreator: false` or the creator can't create team event types.

**Add a member:**
```
POST /v2/teams/{teamId}/memberships
Body: {
  "userId": 789,
  "role": "MEMBER",
  "accepted": true
}
```

**Create invite link:**
```
POST /v2/teams/{teamId}/invite
→ Returns { token, inviteLink }
```

**List members with email filter:**
```
GET /v2/teams/{teamId}/memberships?emails=alice@example.com,bob@example.com
```

### 1.6 Accessing Recordings and Transcripts

**Get recordings:**
```
GET /v2/bookings/{bookingUid}/recordings
→ Returns array of recording objects with downloadLink (S3 URL)
```
Access: booking organizer, team admin, or org admin/owner.

**Get transcripts:**
```
GET /v2/bookings/{bookingUid}/transcripts
→ Returns array of download URLs (valid for 1 hour only)
```
Transcripts are only generated when someone clicks "Transcribe" during a Cal Video meeting.

**Get video sessions:**
```
GET /v2/bookings/{bookingUid}/conferencing-sessions
→ Returns session details with participants, join times, duration
```
Cal Video only.

### 1.7 Managing Schedules and OOO

**Create a schedule:**
```
POST /v2/schedules
Header: cal-api-version: 2024-06-11
Body: {
  "name": "Extended Hours",
  "timeZone": "America/New_York",
  "isDefault": false,
  "availability": [
    { "days": ["Monday", "Tuesday", "Wednesday"], "startTime": "08:00", "endTime": "20:00" },
    { "days": ["Thursday", "Friday"], "startTime": "09:00", "endTime": "17:00" }
  ],
  "overrides": [
    { "date": "2024-12-25", "startTime": "00:00", "endTime": "00:00" }
  ]
}
```

**Assign schedule to event type:**
```
PATCH /v2/event-types/{eventTypeId}
Body: { "scheduleId": 254 }
```

**Create OOO:**
```
POST /v2/me/ooo
Body: {
  "start": "2024-12-20T00:00:00.000Z",
  "end": "2024-12-31T23:59:59.999Z",
  "notes": "Holiday break",
  "reason": "vacation",
  "toUserId": 456
}
```

### 1.8 Reschedule / Cancel / Confirm Flows

**Reschedule (as host or attendee):**
```
POST /v2/bookings/{bookingUid}/reschedule
Body: {
  "start": "2024-08-14T15:00:00Z",
  "rescheduledBy": "host@example.com",
  "reschedulingReason": "Conflict with another meeting"
}
```
If `rescheduledBy` matches the event type owner email, reschedule is auto-confirmed. Otherwise, owner must confirm.

**Request reschedule (sends email to attendee):**
```
POST /v2/bookings/{bookingUid}/request-reschedule
Body: { "rescheduleReason": "Need to find a different time" }
```
This cancels the current booking and sends the attendee an email with a reschedule link.

**Cancel:**
```
POST /v2/bookings/{bookingUid}/cancel
Body: { "cancellationReason": "No longer needed" }
```
For recurring bookings, pass the recurring booking UID to cancel all. Use `cancelSubsequentBookings: true` to cancel this and all future recurrences.

**Confirm/Decline (event types requiring confirmation):**
```
POST /v2/bookings/{bookingUid}/confirm    (no body needed)
POST /v2/bookings/{bookingUid}/decline    (optional: { "reason": "..." })
```

### 1.9 Routing Form Workflows

**Get routing forms for a team:**
```
GET /v2/organizations/{orgId}/teams/{teamId}/routing-forms
```

**Submit a response and get routed slots:**
```
POST /v2/organizations/{orgId}/teams/{teamId}/routing-forms/{formId}/responses
Body: {
  "responses": { "field1": "value1", "field2": "value2" },
  "start": "2024-08-13",
  "end": "2024-08-20"
}
```

**Calculate slots without saving (user-level):**
```
POST /v2/routing-forms/{formId}/calculate-slots?start=2024-08-13&end=2024-08-20
```

---

## 2. Gaps & Limitations

### 2.0 Booking & Webhook Payloads Have No Org/Team Context (Critical)

The booking object -- and therefore all webhook payloads -- contains **no org or team identifiers**. Validated against the live API: a booking includes `eventTypeId`, `eventType: { id, slug }`, `hosts[].id/email/username`, and `attendees[]`. But there is no `organizationId`, `teamId`, or org membership info anywhere on the booking or its nested objects.

**What's always present on a booking:**
- `eventTypeId` + `eventType.slug` -- identifies which event type
- `hosts[].id`, `hosts[].email`, `hosts[].username` -- identifies the host user
- `attendees[].email`, `attendees[].name` -- identifies the attendee

**What's never present:**
- `organizationId` / `orgId` -- not on the booking, not on the host, not on the event type stub
- `teamId` -- not on the booking, not derivable from any nested field
- Whether this was a personal, team, or org-level event type

**Why this matters:** If you're receiving webhooks for multiple orgs/teams (or building a multi-tenant system), there's no way to route the event to the right context from the payload alone.

**Workarounds (in order of reliability):**

1. **Build a local `eventTypeId → teamId → orgId` lookup table.** On startup, pull all event types via org endpoints, cache the mapping, and refresh periodically. This is the most reliable approach.
2. **Fetch the event type on each webhook.** `GET /v2/event-types/{id}` returns `ownerId` for personal event types, and team event types include `teamId` and `team: { id, slug, ... }`. Adds latency per webhook.
3. **Use org-level webhook registration.** If you register via `POST /v2/organizations/{orgId}/webhooks`, you know the webhook came from that org. But the payload still doesn't tell you which team within the org.
4. **Inject context via `metadata`.** When creating bookings programmatically, stuff `orgId`/`teamId` into the `metadata` field. Only works for bookings you create -- not ones from the Cal.com UI or public booking page.
5. **Reverse-lookup the host.** Use `hosts[].email` or `hosts[].id` against your own user database to infer org/team. Fragile if users belong to multiple teams.

**This is the single biggest gap for building webhook-driven automation.** A service-engine-x wrapper should maintain the eventTypeId mapping table and enrich incoming webhook payloads with org/team context before forwarding to downstream handlers.

### 2.1 Cannot Act as a Different Organizer

An API key is tied to one user. You CANNOT create a booking where someone else is the organizer using your API key. To manage bookings for other users:
- Use org-level endpoints (requires Organizations plan)
- Use team event types where the API key owner is a team member
- Use OAuth to get tokens for each user

**Implication for automation:** If you need to book meetings on behalf of multiple team members, you need either:
1. An org admin API key + org-level endpoints
2. Separate API keys per user
3. OAuth tokens per user

### 2.2 Cannot Scope API Calls to a Specific Team with User-Level Key

User-level endpoints (`/v2/bookings`, `/v2/event-types`) return the authenticated user's resources, not a team's. To get team-scoped data:
- Use `/v2/teams/{teamId}/bookings` (Teams plan)
- Use `/v2/organizations/{orgId}/teams/{teamId}/bookings` (Org plan)
- Filter by `teamId` or `teamsIds` query params on `/v2/bookings`

### 2.3 Routing Forms Are Read-Only via API (No CRUD)

The API allows:
- Listing routing forms (`GET`)
- Submitting responses and getting slots
- Reading/updating responses

But you CANNOT:
- Create routing forms via API
- Update routing form configuration via API
- Delete routing forms via API

Routing forms must be created/configured through the Cal.com web UI.

### 2.4 Managed Event Types Require Extra Steps for Slots

Managed event types (`schedulingType: "managed"`) are templates. You cannot query slots for the parent. You must:
1. Get the team event types to find child event type IDs
2. Query slots for each child individually

There's no API to list all children of a managed event type directly. You have to filter by `parentEventTypeId` on the team event types list response.

### 2.5 Booking Location Update Doesn't Sync to Calendar

`PATCH /v2/bookings/{uid}/location` updates the location in Cal.com's database, but the corresponding calendar event (Google Calendar, Outlook, etc.) is NOT updated. The old location persists in the calendar. This is a documented known limitation.

### 2.6 Calendar Meeting Details Only Support Google

`GET /v2/calendars/{calendar}/event/{eventUid}` and `PATCH /v2/calendars/{calendar}/events/{eventUid}` only support `calendar=google`. Office365 and Apple are not supported for direct meeting detail access.

### 2.7 Conferencing App Installation Limitations

Via the API, you can only install:
- Google Meet (`google-meet`)
- Microsoft Teams (`office365-video` / `msteams`)
- Zoom (`zoom`)
- Cal Video (`cal-video`) -- installed by default

All other conferencing integrations (Riverside, Around, etc.) require installation through the Cal.com web app.

### 2.8 Rate Limit Constraints for Automation

- **120 requests/minute** is the default. For high-volume automation (e.g., checking availability for many users), this is constraining.
- Can be increased to ~200 without charges; up to 800 with support request (may incur charges).
- `POST /v2/bookings/{uid}/guests` has a separate 5 req/min limit.
- No webhook delivery rate limits are documented, but webhook delivery failures/retries are not documented either.

### 2.9 No Bulk Operations

There are no bulk/batch endpoints for:
- Creating multiple bookings at once
- Updating multiple event types
- Creating multiple webhooks
- Managing multiple team memberships

Each operation requires a separate API call.

### 2.10 Webhook Payload Inconsistencies

- `MEETING_STARTED` and `MEETING_ENDED` use a flat payload structure, unlike all other webhook events that use `{ triggerEvent, createdAt, payload: { ... } }`.
- The webhook docs don't provide canonical payload examples for every trigger type. The payloads are inferred from the booking object shape.

### 2.11 Email Change Requires Verification

Updating a user's email via `PATCH /v2/me` triggers a verification flow. The primary email stays unchanged until verification completes. This means you can't programmatically change a user's email in one step unless:
- The new email is already a verified secondary email, or
- The user is platform-managed

### 2.12 Limited Workflow Configuration via API

Workflows (automated email/SMS/WhatsApp/AI phone call) are only available at the org-team level. There's no user-level workflow API. You also cannot:
- List available workflow templates
- Preview a workflow before activation
- Test-fire a workflow

### 2.13 No Direct API for Org User Creation Without Org Admin

To add users to an organization, you need:
- Org admin/owner API key
- `POST /v2/organizations/{orgId}/users`

There's no self-registration API for org users.

### 2.14 Booking Reassignment Limited to Round Robin

`POST /v2/bookings/{uid}/reassign` and `/reassign/{userId}` only work for round-robin event types. You cannot reassign bookings for collective or personal event types.

### 2.15 Transcript Download Links Expire

Transcript download links from `GET /v2/bookings/{uid}/transcripts` are valid for **1 hour only**. After expiration, you must make a new API request for fresh links. There's no permanent transcript storage URL.

---

## 3. Deprecations

### API v1 Shutdown: April 8, 2026

API v1 is deprecated and will be permanently shut down on **April 8, 2026**. All integrations must migrate to v2.

Key v1 → v2 changes:
- Auth: query param → `Authorization` header + `cal-api-version` header
- `responses` → `attendee` (booking creation)
- `length` → `lengthInMinutes` (event types)
- `eventTriggers` → `triggers` (webhooks)
- Location types simplified (no `integrations:` prefix in v2)
- Response envelope: `{ booking: ... }` → `{ status, data: ... }`

### Platform Endpoints (Deprecated)

All `/v2/oauth-clients/...` endpoints are deprecated:
- Managed user CRUD
- OAuth client CRUD
- Platform webhooks
- Token force-refresh

Enterprise support continues for existing customers; no new Platform plan signups.

### Deprecated Fields

- `meetingUrl` on booking create request: use `location` object instead
- `loggedInUsersTz` on busy-times endpoint: use `timeZone` instead

---

## 4. Doc Contradictions & Ambiguities

### 4.1 API Version Header Values

Different endpoint groups document different `cal-api-version` values:
- Most booking endpoints show `2024-08-13` as default, but some show `2026-02-25`
- The AI agents guide says `2024-08-13`
- The migration guide says `2024-08-13`
- Some booking endpoints (like location update, add guests, add attendees) specifically require `2024-08-13` (not `2026-02-25`)

**Recommendation:** Use `2024-08-13` as the safe default for bookings. Use `2026-02-25` if you need newer features like `allowBookingOutOfBounds`.

### 4.2 Webhook Trigger Enum vs. Examples

The formal enum lists 21 triggers, but cURL examples show `BOOKING_CONFIRMED`, `BOOKING_COMPLETED`, `BOOKING_NO_SHOW`, and `BOOKING_REOPENED` which are NOT in the enum. These may be undocumented, reserved for future use, or example errors. Use only the 21 documented triggers.

### 4.3 Credits Endpoint Response

The docs show `GET /v2/credits/available` and `POST /v2/credits/charge` as returning empty objects `{}`, but the AI agents guide documents structured responses with `hasCredits`, `balance.monthlyRemaining`, `balance.additional`, `charged`, `remainingBalance`. The live response likely matches the AI agents guide -- the endpoint reference docs appear incomplete.

### 4.4 Org Team Event Type Schema vs. User Event Type Schema

The org-level team event type create endpoint (`POST /v2/organizations/{orgId}/teams/{teamId}/event-types`) uses some different field names than the user/team-level endpoints:
- `recurrence`: uses `{ interval, count, freq }` vs. `{ interval, occurrences, frequency }`
- `calVideoSettings`: uses `{ recordingsEnabled, transcriptionSettings: { mode } }` vs. individual boolean flags
- Additional fields like `aiPhoneCallConfig`, `isInstantEvent`, `instantMeetingExpiryTimeOffsetInSeconds`, `autoTranslateDescriptionEnabled`

This may reflect different API versions or inconsistent documentation. Test with the live API when using org-level endpoints.

### 4.5 `bookingFieldsResponses` Shape in Webhook vs. API

The booking object from the live API includes system fields in `bookingFieldsResponses` (like `email`, `name`, `guests`, `location`, `displayEmail`, `displayGuests`), not just custom fields. Webhook handlers should be prepared for both custom and system fields in this object.

### 4.6 Auth Token Types Per Endpoint

Some endpoints document all three auth methods (API key, managed user token, OAuth token), while others only mention API key (`cal_` prefix). The distinction matters:
- User-level webhooks: API key only
- Event-type webhooks: all three
- Notifications: API key only
- Most other endpoints: all three

### 4.7 Where We'd Need a Wrapper Endpoint

Based on the gaps above, a service-engine-x wrapper would be useful for:

1. **Webhook payload enrichment with org/team context** (CRITICAL) -- maintain a synced `eventTypeId → teamId → orgId` lookup table; enrich every incoming webhook payload with org/team identifiers before forwarding to downstream handlers. Without this, webhook-driven automation cannot route events to the right tenant/context. See [Gap 2.0](#20-booking--webhook-payloads-have-no-orgteam-context-critical).
2. **Bulk availability check** -- query slots for multiple event types/users in one call
3. **Booking on behalf of a specific organizer** -- abstract away org-level API complexity
4. **Routing form CRUD** -- expose create/update/delete since the API only supports read
5. **Managed event type slot aggregation** -- find all children and aggregate their slots
6. **Persistent transcript storage** -- download and store transcripts before links expire
7. **Unified webhook payload normalization** -- flatten the `MEETING_STARTED`/`MEETING_ENDED` inconsistency
8. **Calendar-synced location updates** -- update both Cal.com and the external calendar event
9. **Credit management with balance tracking** -- wrap the sparse credit endpoints with proper balance responses
