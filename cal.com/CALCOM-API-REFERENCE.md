# Cal.com API v2 -- Canonical Reference

> Produced from a complete read of 290 Cal.com API reference docs + live API validation.
> Intended audience: downstream agents building database tables, webhook handlers, booking flows, or calendar management.

---

## Table of Contents

1. [Authentication & API Structure](#1-authentication--api-structure)
2. [Core Entities & Relationships](#2-core-entities--relationships)
3. [Complete Endpoint Catalog](#3-complete-endpoint-catalog)
4. [Key Schemas](#4-key-schemas)

---

## 1. Authentication & API Structure

### Base URL

```
https://api.cal.com/v2
```

All requests must use HTTPS. Plain HTTP fails.

### Authentication Methods

| Method | Header | Token Format | Use Case |
|--------|--------|--------------|----------|
| **API Key** | `Authorization: Bearer <key>` | Prefixed `cal_` (test) or `cal_live_` (production) | Primary method for server-to-server integrations |
| **OAuth 2.0** | `Authorization: Bearer <access_token>` | JWT (expires in 30 min) | Third-party apps acting on behalf of a user |
| **Platform (DEPRECATED)** | `x-cal-client-id` + `x-cal-secret-key` | OAuth client credentials | Legacy managed-user platform customers only |

### Required Headers

Every request MUST include:

```
Authorization: Bearer cal_live_xxxxxxxxxxxx
cal-api-version: <version>
Content-Type: application/json  (for POST/PATCH/PUT)
```

**The `cal-api-version` header is critical.** Without it, requests return 404 or fall back to v1 behavior. Different endpoint groups use different versions:

| Endpoint Group | `cal-api-version` Value |
|---|---|
| Bookings (core, org, team) | `2024-08-13` or `2026-02-25` |
| Event Types | `2024-06-14` |
| Schedules | `2024-06-11` |
| Slots | `2024-09-04` |
| Private Links | `2024-09-04` |
| Webhooks | *(not required)* |
| Me / Profile | *(not required)* |
| Out-of-Office | *(not required)* |
| Credits | *(not required)* |
| Calendars / Conferencing | *(not required)* |
| Organizations (most) | `2024-08-13` |

### Rate Limits

- **API Key authentication:** 120 requests/minute (default). Can be increased to ~200; up to 800 with support request (may involve charges).
- **No authentication:** 120 requests/minute.
- **Retry strategy:** Implement exponential backoff. On 429 responses, wait `2^i * 1000` ms.
- **Guest endpoint rate limit:** `POST /v2/bookings/{uid}/guests` is rate-limited to 5 requests/minute.

### Response Envelope

All v2 responses use a standard envelope:

```json
{
  "status": "success",
  "data": { ... }
}
```

Error responses:

```json
{
  "status": "error",
  "error": {
    "code": "NOT_FOUND",
    "message": "Event type not found"
  }
}
```

List endpoints include pagination:

```json
{
  "status": "success",
  "data": [ ... ],
  "pagination": {
    "totalItems": 123,
    "remainingItems": 103,
    "returnedItems": 10,
    "itemsPerPage": 10,
    "currentPage": 2,
    "totalPages": 13,
    "hasNextPage": true,
    "hasPreviousPage": false
  }
}
```

Most list endpoints use `take` (default 250, max 250) and `skip` (default 0) query params.

### Scoping: User vs. Team vs. Organization

Cal.com has a three-level hierarchy that determines which endpoints you use:

```
Organization (orgId)
  └── Team (teamId)
       └── User (userId)
```

**How scoping works:**

| Level | Path Prefix | Who Can Access | What They See |
|---|---|---|---|
| User | `/v2/bookings`, `/v2/event-types`, `/v2/schedules` | The authenticated user | Only their own resources |
| Team | `/v2/teams/{teamId}/...` | Team members (API key owner must be member) | Team-scoped resources |
| Org > Team | `/v2/organizations/{orgId}/teams/{teamId}/...` | Org admins, team admins | Team resources within the org |
| Org > User | `/v2/organizations/{orgId}/users/{userId}/...` | Org admins | User resources within the org |
| Org | `/v2/organizations/{orgId}/...` | Org admins/owners | All resources across the org |

**Key rules:**
- Org `admin` or `owner` can access ANY team endpoint regardless of team membership.
- Org `member` must have separate team membership; their team role is checked.
- You CANNOT act as a different user with a single API key. The API key is tied to one user. To manage other users' resources, use org-level endpoints.
- Team-level endpoints (non-org path) work for Teams plan customers.
- Org-level endpoints work for Organizations plan customers.

### OAuth Scopes

Scopes follow a hierarchy: `ORG_*` scopes automatically grant corresponding `TEAM_*` scopes.

**User scopes:** `EVENT_TYPE_READ`, `EVENT_TYPE_WRITE`, `BOOKING_READ`, `BOOKING_WRITE`, `SCHEDULE_READ`, `SCHEDULE_WRITE`, `APPS_READ`, `APPS_WRITE`, `PROFILE_READ`, `PROFILE_WRITE`

**Team scopes:** `TEAM_EVENT_TYPE_READ/WRITE`, `TEAM_BOOKING_READ/WRITE`, `TEAM_SCHEDULE_READ/WRITE`, `TEAM_PROFILE_READ/WRITE`, `TEAM_MEMBERSHIP_READ/WRITE`

**Org scopes:** `ORG_EVENT_TYPE_READ/WRITE`, `ORG_BOOKING_READ/WRITE`, `ORG_SCHEDULE_READ/WRITE`, `ORG_PROFILE_READ/WRITE`, `ORG_MEMBERSHIP_READ/WRITE`

**Public endpoints (no auth required):** `POST /v2/bookings` (create), `POST /v2/bookings/:uid/cancel`, `POST /v2/bookings/:uid/reschedule`, `GET /v2/slots` (availability).

### PBAC (Permission-Based Access Control)

Optional, per-organization. When enabled, custom roles with granular permissions (e.g., `eventType.create`, `booking.update`) can bypass role-level checks. Each org/team endpoint doc specifies the minimum role AND the PBAC permission required. There are 60+ permission values.

---

## 2. Core Entities & Relationships

### Entity Relationship Map

```
Organization
  ├── Users (org memberships: owner/admin/member)
  │     ├── Schedules (availability windows)
  │     ├── Event Types (personal)
  │     ├── Bookings (as host)
  │     ├── Out-of-Office entries
  │     └── Webhooks (user-level)
  │
  ├── Teams (org team memberships: owner/admin/member)
  │     ├── Event Types (team: collective/roundRobin/managed)
  │     │     ├── Webhooks (event-type-level)
  │     │     └── Private Links
  │     ├── Bookings (team bookings)
  │     ├── Schedules (read-only aggregate of member schedules)
  │     ├── Routing Forms
  │     │     └── Responses
  │     ├── Workflows (event-type or routing-form triggered)
  │     └── Verified Resources (emails, phones)
  │
  ├── Attributes (org-level, assignable to users for routing)
  ├── Roles & Permissions (PBAC)
  ├── Webhooks (org-level)
  ├── Delegation Credentials
  └── Managed Organizations (sub-orgs, platform only)
```

### Event Types

An event type is a bookable meeting template. Key fields:

| Field | Type | Description |
|---|---|---|
| `id` | number | Unique identifier |
| `title` | string | Display name |
| `slug` | string | URL-safe identifier |
| `lengthInMinutes` | number | Default duration |
| `lengthInMinutesOptions` | number[] | Multi-duration options |
| `schedulingType` | enum | `collective` (all hosts must be free), `roundRobin` (one host assigned), `managed` (template that creates child event types per member) -- team event types only |
| `scheduleId` | number | Which schedule governs availability |
| `locations` | object[] | Where the meeting happens (address, link, integration, phone, cal-video, etc.) |
| `bookingFields` | object[] | Custom form fields beyond name/email |
| `recurrence` | object | Makes it a recurring event type |
| `seats` | object | Multiple attendees per time slot |
| `confirmationPolicy` | object | Requires manual confirmation |
| `hidden` | boolean | Not publicly visible |

**Personal vs. Team Event Types:**
- Personal: created via `POST /v2/event-types`, owned by one user
- Team: created via `POST /v2/teams/{teamId}/event-types` (or org path), requires `schedulingType` and `hosts`
- Managed: a team event type template (`schedulingType: "managed"`) that auto-creates child event types for each team member. You cannot fetch slots for the parent; use child event type IDs.

**Location types:** `address`, `link`, `integration` (Google Meet = `google-meet`, Zoom = `zoom`, MS Teams = `office365-video`), `phone`, `attendeePhone`, `organizerPhone`, `calVideo`, `conferencing`, `unknown`

### Bookings

A booking is a scheduled meeting instance. Full lifecycle:

```
created ──► accepted (auto or manual confirm)
         ──► requested (needs confirmation) ──► accepted / rejected

accepted ──► rescheduled (creates new booking, links via rescheduledFromUid/rescheduledToUid)
accepted ──► cancelled (with cancellationReason)
accepted ──► mark-absent (no-show tracking)
accepted ──► reassign (round-robin only, to specific or auto-selected host)
```

**Status values for filtering:** `upcoming`, `recurring`, `past`, `cancelled`, `unconfirmed`

**Key booking fields:**

| Field | Type | Description |
|---|---|---|
| `id` | number | Numeric ID |
| `uid` | string | Unique string identifier (used in all path params) |
| `title` | string | Auto-generated meeting title |
| `status` | string | Current status (`accepted`, `cancelled`, etc.) |
| `start` / `end` | ISO 8601 | Meeting time window in UTC |
| `duration` | number | Minutes |
| `eventTypeId` | number | Which event type this booking is for |
| `eventType` | object | `{ id, slug }` |
| `hosts` | object[] | `{ id, name, email, displayEmail, username, timeZone }` |
| `attendees` | object[] | `{ name, email, displayEmail, timeZone, absent, language, phoneNumber }` |
| `guests` | string[] | Additional guest email addresses |
| `location` / `meetingUrl` | string | Where the meeting happens |
| `bookingFieldsResponses` | object | Custom field answers (slug:value pairs) |
| `metadata` | object | Arbitrary key-value data (max 50 keys, key max 40 chars, values max 500 chars) |
| `cancellationReason` | string | Why it was cancelled |
| `rescheduledFromUid` / `rescheduledToUid` | string | Links rescheduled bookings |
| `icsUid` | string | Calendar ICS UID |
| `rating` | number | Post-meeting rating |

**Creating a booking (public, no auth required):**

Two identification methods:
1. By `eventTypeId` (numeric)
2. By `eventTypeSlug` + `username` (personal) or `eventTypeSlug` + `teamSlug` (team), optionally with `organizationSlug`

Required fields: `start` (UTC ISO 8601), `attendee` (`name`, `email`, `timeZone`). Optional: `guests`, `location`, `metadata`, `bookingFieldsResponses`, `lengthInMinutes` (for multi-duration), `instant` (true for instant meetings).

**Seated bookings:** Event types with `seats` config allow multiple attendees per time slot. Each attendee gets a `seatUid`. Cancel by `seatUid` to remove one attendee; cancel by `bookingUid` + auth to cancel all seats.

### Schedules

A schedule defines when a user is available for bookings.

| Field | Type | Description |
|---|---|---|
| `id` | number | Schedule ID |
| `ownerId` | number | User who owns it |
| `name` | string | Display name |
| `timeZone` | string | Timezone for availability |
| `isDefault` | boolean | Used when event type has no specific schedule |
| `availability` | object[] | `{ days: string[], startTime: "HH:MM", endTime: "HH:MM" }` |
| `overrides` | object[] | `{ date: "YYYY-MM-DD", startTime: "HH:MM", endTime: "HH:MM" }` |

Each user should have exactly one default schedule. If a managed user is created with `timeZone`, a Mon-Fri 9AM-5PM default schedule is auto-created. Without `timeZone`, you must manually create a default schedule before the user can be booked.

### Slots

Slots represent available time windows for booking. They are computed from schedules, event type configuration, and existing bookings.

**Getting slots:** `GET /v2/slots` with required `start` and `end` params. Returns a map of dates to arrays of slot objects:

```json
{
  "2050-09-05": [
    { "start": "2050-09-05T09:00:00.000+02:00" },
    { "start": "2050-09-05T10:00:00.000+02:00" }
  ]
}
```

With `format=range`, each slot includes both `start` and `end`. For seated event types, slots include `attendeesCount` and `bookingUid`.

**Reserving slots:** `POST /v2/slots/reservations` temporarily holds a slot (default 5 minutes, configurable when authenticated). Returns a `reservationUid` for managing the reservation.

### Teams

| Field | Type | Description |
|---|---|---|
| `id` | number | Team ID |
| `name` | string | Team name |
| `slug` | string | URL-safe identifier |
| `isOrganization` | boolean | Whether this "team" is actually an org |
| `parentId` | number | Parent org ID |
| `timeZone` | string | Default timezone (creates default schedule) |
| `metadata` | object | Arbitrary data |
| `isPrivate` | boolean | Visibility |
| `hideBookATeamMember` | boolean | UI control |

**Memberships:** Each team membership has `userId`, `teamId`, `role` (MEMBER/ADMIN/OWNER), `accepted` (boolean), `disableImpersonation`. The `user` object on membership includes `avatarUrl`, `username`, `name`, `email`, `bio`, `metadata`.

### Webhooks

Three levels of webhook registration:
1. **User-level:** `POST /v2/webhooks` -- fires for all the user's bookings
2. **Event-type-level:** `POST /v2/event-types/{eventTypeId}/webhooks` -- fires only for that event type
3. **Org-level:** `POST /v2/organizations/{orgId}/webhooks` -- fires for all org events

See [CALCOM-WEBHOOKS.md](./CALCOM-WEBHOOKS.md) for complete webhook documentation.

### Routing Forms

Routing forms collect responses and route to the appropriate event type. Available at org-team level. Key operations:
- `GET /v2/organizations/{orgId}/teams/{teamId}/routing-forms` -- list forms
- `POST /v2/organizations/{orgId}/teams/{teamId}/routing-forms/{formId}/responses` -- submit response and get routed slots
- `GET /v2/organizations/{orgId}/teams/{teamId}/routing-forms/{formId}/responses` -- list responses
- `PATCH .../{responseId}` -- update a response

Also available at user level: `POST /v2/routing-forms/{routingFormId}/calculate-slots` -- calculate slots based on form response without saving.

### Workflows

Automated actions triggered by booking events. Only available at org-team level.

**Two types:**
1. **Event-type workflows:** 12 trigger types (`beforeEvent`, `afterEvent`, `newEvent`, `eventCancelled`, `rescheduleEvent`, etc.) with 8 action types (`email_host`, `email_attendee`, `email_address`, `sms_attendee`, `sms_number`, `whatsapp_attendee`, `whatsapp_number`, `cal_ai_phone_call`)
2. **Routing-form workflows:** 2 trigger types (`formSubmitted`, `formSubmittedNoEvent`) with 4 action types (email and SMS only)

### Calendars & Conferencing

**Connected calendars:** Supports Google, Office365, Apple (CalDAV), and ICS feeds. `GET /v2/calendars` returns all connected calendars with their `credentialId` and `externalId`.

**Destination calendar:** The calendar where new booking events are written. Set via `PUT /v2/destination-calendars`.

**Selected calendars:** Which calendars are checked for busy times. Managed via `POST/DELETE /v2/selected-calendars`.

**Conferencing:** Google Meet, Zoom, MS Teams, Cal Video (built-in). Cal Video is installed by default. Others require OAuth connection. Set default via `POST /v2/conferencing/{app}/default`.

### Out-of-Office

OOO entries block availability for a date range. Fields: `start`, `end`, `notes`, `toUserId` (covering user), `reason` (unspecified/vacation/travel/sick/public_holiday).

Available at user level (`/v2/me/ooo`), team-user level (`/v2/teams/{teamId}/users/{userId}/ooo`), and org-user level (`/v2/organizations/{orgId}/users/{userId}/ooo`).

### Credits

Cal.com has a credit system for AI agent interactions, SMS, and phone calls.

- `GET /v2/credits/available` -- check balance
- `POST /v2/credits/charge` -- charge credits (uses `externalRef` for idempotency)

Credit types: `SMS`, `CAL_AI_PHONE_CALL`, `AI_AGENT`.

---

## 3. Complete Endpoint Catalog

### User-Level Endpoints

| Method | Path | Description | Auth Required |
|---|---|---|---|
| **Profile** ||||
| GET | `/v2/me` | Get my profile | Yes |
| PATCH | `/v2/me` | Update my profile | Yes |
| **Bookings** ||||
| GET | `/v2/bookings` | List all bookings | Yes |
| GET | `/v2/bookings/{uid}` | Get a booking | Optional |
| POST | `/v2/bookings` | Create a booking | No |
| POST | `/v2/bookings/{uid}/cancel` | Cancel a booking | Optional |
| POST | `/v2/bookings/{uid}/confirm` | Confirm a booking | Yes (owner) |
| POST | `/v2/bookings/{uid}/decline` | Decline a booking | Yes (owner) |
| POST | `/v2/bookings/{uid}/reschedule` | Reschedule a booking | Optional |
| POST | `/v2/bookings/{uid}/request-reschedule` | Request reschedule (sends email) | Yes |
| POST | `/v2/bookings/{uid}/mark-absent` | Mark no-show | Yes (owner) |
| POST | `/v2/bookings/{uid}/reassign/{userId}` | Reassign to specific host | Yes (owner) |
| POST | `/v2/bookings/{uid}/reassign` | Reassign to auto-selected host | Yes (owner) |
| GET | `/v2/bookings/by-seat/{seatUid}` | Get booking by seat UID | Optional |
| GET | `/v2/bookings/{uid}/calendar-links` | Get add-to-calendar links | Yes |
| GET | `/v2/bookings/{uid}/recordings` | Get Cal Video recordings | Yes |
| GET | `/v2/bookings/{uid}/references` | Get booking references (calendar/video) | Yes |
| GET | `/v2/bookings/{uid}/transcripts` | Get transcript download links (1hr TTL) | Yes |
| GET | `/v2/bookings/{uid}/conferencing-sessions` | Get video meeting sessions | Yes |
| PATCH | `/v2/bookings/{uid}/location` | Update booking location | Yes |
| POST | `/v2/bookings/{uid}/guests` | Add guests (max 10/req, 30/booking, 5 req/min) | Yes |
| POST | `/v2/bookings/{uid}/attendees` | Add attendee | Yes |
| GET | `/v2/bookings/{uid}/attendees` | List attendees | Yes |
| GET | `/v2/bookings/{uid}/attendees/{id}` | Get attendee | Yes |
| **Event Types** ||||
| POST | `/v2/event-types` | Create event type | Yes |
| GET | `/v2/event-types` | List event types | Optional |
| GET | `/v2/event-types/{id}` | Get event type | Yes |
| PATCH | `/v2/event-types/{id}` | Update event type | Yes |
| DELETE | `/v2/event-types/{id}` | Delete event type | Yes |
| **Event Type Private Links** ||||
| POST | `/v2/event-types/{id}/private-links` | Create private link | Yes |
| GET | `/v2/event-types/{id}/private-links` | List private links | Yes |
| PATCH | `/v2/event-types/{id}/private-links/{linkId}` | Update private link | Yes |
| DELETE | `/v2/event-types/{id}/private-links/{linkId}` | Delete private link | Yes |
| **Event Type Webhooks** ||||
| POST | `/v2/event-types/{id}/webhooks` | Create webhook | Yes |
| GET | `/v2/event-types/{id}/webhooks` | List webhooks | Yes |
| GET | `/v2/event-types/{id}/webhooks/{webhookId}` | Get webhook | Yes |
| PATCH | `/v2/event-types/{id}/webhooks/{webhookId}` | Update webhook | Yes |
| DELETE | `/v2/event-types/{id}/webhooks/{webhookId}` | Delete webhook | Yes |
| DELETE | `/v2/event-types/{id}/webhooks` | Delete all webhooks | Yes |
| **User Webhooks** ||||
| POST | `/v2/webhooks` | Create user webhook | Yes |
| GET | `/v2/webhooks` | List user webhooks | Yes |
| GET | `/v2/webhooks/{id}` | Get user webhook | Yes |
| PATCH | `/v2/webhooks/{id}` | Update user webhook | Yes |
| DELETE | `/v2/webhooks/{id}` | Delete user webhook | Yes |
| **Schedules** ||||
| POST | `/v2/schedules` | Create schedule | Yes |
| GET | `/v2/schedules` | List schedules | Yes |
| GET | `/v2/schedules/{id}` | Get schedule | Yes |
| GET | `/v2/schedules/default` | Get default schedule | Yes |
| PATCH | `/v2/schedules/{id}` | Update schedule | Yes |
| DELETE | `/v2/schedules/{id}` | Delete schedule | Yes |
| **Slots** ||||
| GET | `/v2/slots` | Get available slots | Yes |
| POST | `/v2/slots/reservations` | Reserve a slot | Optional |
| GET | `/v2/slots/reservations/{uid}` | Get reservation | Yes |
| PATCH | `/v2/slots/reservations/{uid}` | Update reservation | Yes |
| DELETE | `/v2/slots/reservations/{uid}` | Delete reservation | Yes |
| **Out-of-Office** ||||
| POST | `/v2/me/ooo` | Create OOO entry | Yes |
| GET | `/v2/me/ooo` | List OOO entries | Yes |
| PATCH | `/v2/me/ooo/{id}` | Update OOO entry | Yes |
| DELETE | `/v2/me/ooo/{id}` | Delete OOO entry | Yes |
| **Calendars** ||||
| GET | `/v2/calendars` | Get all connected calendars | Yes |
| GET | `/v2/calendars/{calendar}/check` | Check calendar connection | Yes |
| POST | `/v2/calendars/{calendar}/disconnect` | Disconnect calendar | Yes |
| GET | `/v2/calendars/{calendar}/connect` | Get OAuth connect URL | Yes |
| GET | `/v2/calendars/{calendar}/save` | Save OAuth credentials (callback) | Yes |
| POST | `/v2/calendars/{calendar}/credentials` | Save Apple calendar credentials | Yes |
| GET | `/v2/calendars/busy-times` | Get busy times | Yes |
| GET | `/v2/calendars/ics-feed/check` | Check ICS feed | Yes |
| POST | `/v2/calendars/ics-feed/save` | Save ICS feed | Yes |
| GET | `/v2/calendars/{calendar}/event/{uid}` | Get meeting details (Google only) | Yes |
| PATCH | `/v2/calendars/{calendar}/events/{uid}` | Update meeting details (Google only) | Yes |
| PUT | `/v2/destination-calendars` | Update destination calendar | Yes |
| POST | `/v2/selected-calendars` | Add selected calendar | Yes |
| DELETE | `/v2/selected-calendars` | Remove selected calendar | Yes |
| **Conferencing** ||||
| GET | `/v2/conferencing` | List conferencing apps | Yes |
| GET | `/v2/conferencing/default` | Get default conferencing app | Yes |
| POST | `/v2/conferencing/{app}/default` | Set default conferencing app | Yes |
| POST | `/v2/conferencing/{app}/connect` | Connect conferencing app | Yes |
| DELETE | `/v2/conferencing/{app}/disconnect` | Disconnect conferencing app | Yes |
| GET | `/v2/conferencing/{app}/oauth/auth-url` | Get OAuth auth URL | Yes |
| GET | `/v2/conferencing/{app}/oauth/callback` | OAuth callback | Yes |
| **Credits** ||||
| GET | `/v2/credits/available` | Check credit balance | Yes |
| POST | `/v2/credits/charge` | Charge credits | Yes |
| **Notifications** ||||
| POST | `/v2/notifications/subscriptions/app-push` | Register push notification | Yes (API key only) |
| DELETE | `/v2/notifications/subscriptions/app-push` | Remove push notification | Yes (API key only) |
| **Routing Forms** ||||
| POST | `/v2/routing-forms/{formId}/calculate-slots` | Calculate slots from form response | Yes |
| **Stripe** ||||
| GET | `/v2/stripe/check` | Check Stripe connection | Yes |
| GET | `/v2/stripe/connect` | Get Stripe connect URL | Yes |
| GET | `/v2/stripe/save` | Save Stripe credentials (callback) | Yes |
| **Auth** ||||
| POST | `/v2/api-keys/refresh` | Refresh API key | Yes |
| POST | `/v2/auth/oauth2/token` | Exchange code or refresh token | No |
| GET | `/v2/auth/oauth2/clients/{clientId}` | Get OAuth client info | Yes |
| **Verified Resources** ||||
| GET | `/v2/verified-resources/emails` | List verified emails | Yes |
| GET | `/v2/verified-resources/emails/{id}` | Get verified email | Yes |
| POST | `/v2/verified-resources/emails/verification-code/request` | Request email verification | Yes |
| POST | `/v2/verified-resources/emails/verification-code/verify` | Verify email | Yes |
| GET | `/v2/verified-resources/phones` | List verified phones | Yes |
| GET | `/v2/verified-resources/phones/{id}` | Get verified phone | Yes |
| POST | `/v2/verified-resources/phones/verification-code/request` | Request phone verification | Yes |
| POST | `/v2/verified-resources/phones/verification-code/verify` | Verify phone | Yes |

### Team-Level Endpoints (`/v2/teams/{teamId}/...`)

| Method | Path | Description |
|---|---|---|
| **Teams CRUD** |||
| POST | `/v2/teams` | Create team |
| GET | `/v2/teams` | List teams |
| GET | `/v2/teams/{teamId}` | Get team |
| PATCH | `/v2/teams/{teamId}` | Update team |
| DELETE | `/v2/teams/{teamId}` | Delete team |
| **Team Bookings** |||
| GET | `/v2/teams/{teamId}/bookings` | List team bookings |
| **Team Event Types** |||
| POST | `/v2/teams/{teamId}/event-types` | Create team event type |
| GET | `/v2/teams/{teamId}/event-types` | List team event types |
| GET | `/v2/teams/{teamId}/event-types/{id}` | Get team event type |
| PATCH | `/v2/teams/{teamId}/event-types/{id}` | Update team event type |
| DELETE | `/v2/teams/{teamId}/event-types/{id}` | Delete team event type |
| POST | `/v2/teams/{teamId}/event-types/{id}/create-phone-call` | Create AI phone call |
| **Team Event Type Webhooks** |||
| POST | `/v2/teams/{teamId}/event-types/{id}/webhooks` | Create webhook |
| GET | `/v2/teams/{teamId}/event-types/{id}/webhooks` | List webhooks |
| GET | `/v2/teams/{teamId}/event-types/{id}/webhooks/{wid}` | Get webhook |
| PATCH | `/v2/teams/{teamId}/event-types/{id}/webhooks/{wid}` | Update webhook |
| DELETE | `/v2/teams/{teamId}/event-types/{id}/webhooks/{wid}` | Delete webhook |
| DELETE | `/v2/teams/{teamId}/event-types/{id}/webhooks` | Delete all webhooks |
| **Team Memberships** |||
| POST | `/v2/teams/{teamId}/memberships` | Create membership |
| GET | `/v2/teams/{teamId}/memberships` | List memberships |
| GET | `/v2/teams/{teamId}/memberships/{id}` | Get membership |
| PATCH | `/v2/teams/{teamId}/memberships/{id}` | Update membership |
| DELETE | `/v2/teams/{teamId}/memberships/{id}` | Delete membership |
| **Team Invite** |||
| POST | `/v2/teams/{teamId}/invite` | Create invite link |
| **Team Schedules** |||
| GET | `/v2/teams/{teamId}/schedules` | List all member schedules |
| **Team Users OOO** |||
| POST | `/v2/teams/{teamId}/users/{userId}/ooo` | Create OOO for member |
| GET | `/v2/teams/{teamId}/users/{userId}/ooo` | List OOO for member |
| PATCH | `/v2/teams/{teamId}/users/{userId}/ooo/{id}` | Update OOO |
| DELETE | `/v2/teams/{teamId}/users/{userId}/ooo/{id}` | Delete OOO |
| **Team Verified Resources** |||
| GET | `/v2/teams/{teamId}/verified-resources/emails` | List verified emails |
| GET | `/v2/teams/{teamId}/verified-resources/emails/{id}` | Get verified email |
| POST | `/v2/teams/{teamId}/verified-resources/emails/verification-code/request` | Request verification |
| POST | `/v2/teams/{teamId}/verified-resources/emails/verification-code/verify` | Verify email |
| GET | `/v2/teams/{teamId}/verified-resources/phones` | List verified phones |
| GET | `/v2/teams/{teamId}/verified-resources/phones/{id}` | Get verified phone |
| POST | `/v2/teams/{teamId}/verified-resources/phones/verification-code/request` | Request verification |
| POST | `/v2/teams/{teamId}/verified-resources/phones/verification-code/verify` | Verify phone |

### Organization-Level Endpoints (`/v2/organizations/{orgId}/...`)

> 120+ endpoints. Key groups:

| Group | Path Pattern | Description |
|---|---|---|
| Attributes | `/{orgId}/attributes/...` | CRUD + assign/unassign to users, option management |
| Bookings | `/{orgId}/bookings` | Org-wide booking list, block attendee, report booking |
| Delegation Credentials | `/{orgId}/delegation-credentials` | Save/update delegation creds |
| Managed Orgs | `/{orgId}/organizations` | CRUD sub-organizations (platform only) |
| Memberships | `/{orgId}/memberships/...` | CRUD org memberships |
| Roles | `/{orgId}/roles/...` | CRUD roles + permission management |
| Routing Forms | `/{orgId}/teams/{teamId}/routing-forms/...` | Forms + responses |
| Schedules | `/{orgId}/schedules` | Read-only org-wide schedule view |
| Webhooks | `/{orgId}/webhooks/...` | CRUD org webhooks |
| Users | `/{orgId}/users/...` | CRUD org users |
| User Bookings | `/{orgId}/users/{userId}/bookings` | User bookings within org |
| User OOO | `/{orgId}/users/{userId}/ooo/...` | CRUD user OOO |
| User Schedules | `/{orgId}/users/{userId}/schedules/...` | Full CRUD user schedules |
| Teams | `/{orgId}/teams/...` | CRUD teams, memberships, invites |
| Team Bookings | `/{orgId}/teams/{teamId}/bookings` | Team bookings, references |
| Team Conferencing | `/{orgId}/teams/{teamId}/conferencing/...` | Team conferencing management |
| Team Event Types | `/{orgId}/teams/{teamId}/event-types/...` | Full CRUD + phone calls |
| Team Event Type Private Links | `/{orgId}/teams/{teamId}/event-types/{id}/private-links/...` | CRUD |
| Team Memberships | `/{orgId}/teams/{teamId}/memberships/...` | CRUD |
| Team Roles | `/{orgId}/teams/{teamId}/roles/...` | CRUD + permissions |
| Team Routing Forms | `/{orgId}/teams/{teamId}/routing-forms/...` | Forms + responses |
| Team Schedules | `/{orgId}/teams/{teamId}/schedules` | Read-only team schedules |
| Team Stripe | `/{orgId}/teams/{teamId}/stripe/...` | Stripe connection |
| Team User Schedules | `/{orgId}/teams/{teamId}/users/{userId}/schedules` | Member schedules |
| Team Workflows | `/{orgId}/teams/{teamId}/workflows/...` | Event-type + routing-form workflows |
| Team Verified Resources | `/{orgId}/teams/{teamId}/verified-resources/...` | Emails + phones |

### Deprecated Endpoints

| Group | Path Pattern | Notes |
|---|---|---|
| Platform Managed Users | `/v2/oauth-clients/{clientId}/users/...` | CRUD managed users, force-refresh tokens |
| Platform OAuth Clients | `/v2/oauth-clients/...` | CRUD OAuth clients |
| Platform Webhooks | `/v2/oauth-clients/{clientId}/webhooks/...` | CRUD platform webhooks |
| Platform Token Refresh | `/v2/oauth/{clientId}/refresh` | Refresh managed user tokens |

All deprecated endpoints will be removed in the future. Enterprise support continues for existing customers.

---

## 4. Key Schemas

### Booking Create Request

```json
{
  "start": "2024-08-13T09:00:00Z",
  "attendee": {
    "name": "Jane Smith",
    "email": "jane@example.com",
    "timeZone": "America/New_York",
    "phoneNumber": "+19876543210",
    "language": "en"
  },
  "eventTypeId": 123,
  "guests": ["guest1@example.com"],
  "location": { "type": "integration", "integration": "google-meet" },
  "bookingFieldsResponses": { "company": "Acme Corp" },
  "metadata": { "source": "ai-agent" },
  "lengthInMinutes": 30,
  "instant": true
}
```

Alternative identification (instead of `eventTypeId`):
```json
{
  "eventTypeSlug": "30min",
  "username": "outbound-solutions",
  "organizationSlug": "my-org"
}
```

### Schedule Create Request

```json
{
  "name": "Business Hours",
  "timeZone": "America/New_York",
  "isDefault": true,
  "availability": [
    { "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "startTime": "09:00", "endTime": "17:00" }
  ],
  "overrides": [
    { "date": "2024-12-25", "startTime": "00:00", "endTime": "00:00" }
  ]
}
```

### Team Event Type Create Request

```json
{
  "title": "Team Consultation",
  "slug": "team-consultation",
  "lengthInMinutes": 30,
  "schedulingType": "roundRobin",
  "hosts": [
    { "userId": 123, "mandatory": false, "priority": "high" },
    { "userId": 456, "mandatory": true, "priority": "medium" }
  ],
  "locations": [{ "type": "integration", "integration": "google-meet" }]
}
```

### Webhook Create Request

```json
{
  "subscriberUrl": "https://your-server.com/webhook",
  "triggers": ["BOOKING_CREATED", "BOOKING_CANCELLED", "BOOKING_RESCHEDULED"],
  "active": true,
  "secret": "your-hmac-secret",
  "payloadTemplate": "{\"type\":\"{{type}}\",\"title\":\"{{title}}\"}",
  "version": "2021-10-20"
}
```

### Metadata Constraints (All Entities)

- Maximum 50 keys
- Key maximum length: 40 characters
- String value maximum length: 500 characters
- Values can be: strings, numbers, or booleans
