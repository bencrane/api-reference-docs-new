# FAQ

## Duplicate Payload Handling

Sendoso does not handle duplicate payloads. Any order that is sent to Sendoso will be processed immediately.

## API Request Throttling

The platform implements rate limiting at 10 requests per second. Organizations needing higher throughput should reach out to developers@sendoso.com.

## History Tracking

Sendoso does not publish history via the API. However, all API-initiated updates and sends appear in the platform and Send Tracker tab.

## Dynamic Content Support

Yes, dynamic text is supported for notes. This enables flexible, template-based messaging.

## Sandbox vs. Production

The sandbox mirrors production workflows but differs in touch IDs and package status progression, which halts at processing stage in sandbox environments.

## API-Platform Integration

API modifications immediately sync with the Sendoso application, and all API-sent items display on the Send Tracker section.

## Notification Email Changes

Notifications route to the person initiating the send; this setting cannot be modified.

## Deployment Schedule

The system operates on zero-downtime deployment. Technical issues should be reported to developers@sendoso.com with environment details, API request specifics, error responses, and timestamps.
