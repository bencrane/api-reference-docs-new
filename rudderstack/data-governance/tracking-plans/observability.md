# Tracking Plan Observability

Get complete visibility into the events passing through your tracking plans and any tracking plan violations.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __4 minute read

  * 


This guide walks you through the different tracking plan observability metrics that give you visibility into the events passing through your tracking plans.

## Overview

RudderStack gives you complete visibility into the events passing through a tracking plan and details on the tracking plan violations, that is, events that do not comply with the tracking plan rules.

To see these metrics, click the **Events** tab of the source connected to your tracking plan.

[![Tracking plan observability](/docs/images/data-governance/tracking-plans-observability.webp)](</docs/images/data-governance/tracking-plans-observability.webp>)

### Events ingested

This section shows the tracking plan currently linked to your source and the following details:

Metric| Description  
---|---  
Total events| Captures all events that pass through the source.  
Events validated| Number of events validated by the tracking plan.  
Events with violations| Number of events that do not comply with the tracking plan rules.  
Events dropped| Number of events dropped due to tracking plan violations.  
  
You can see these metrics for all tracking plans connected to that source and filter them by version and time period (past one day, seven days, or 30 days).

[![Events ingested section](/docs/images/data-governance/tracking-plans-observability-1.webp)](</docs/images/data-governance/tracking-plans-observability-1.webp>)

### Event flow

This section gives a graphical overview of all the events ingested per day over the specified period and the number of events with violations.

[![Event flow section](/docs/images/data-governance/tracking-plans-observability-2.webp)](</docs/images/data-governance/tracking-plans-observability-2.webp>)

### Event details

Click the **Events** tab to see the following event-related metrics:

Metric| Description  
---|---  
Event name| Name of the event.  
Count| Number of events validated by the tracking plan according to filter set in Events ingested.  
Last seen| Number of days since the last violation occurred.  
[![Events tab](/docs/images/data-governance/tracking-plans-observability-3.webp)](</docs/images/data-governance/tracking-plans-observability-3.webp>)

### Violation details

Click the **Violations** tab to see the following metrics:

Metric| Description  
---|---  
Event name| Name of the event.  
Event type| Type of event (`identify`, `track`, `group`, `page`, or `screen`).  
  
**Note** : Tracking plans **do not** validate `alias` events. If you send any `alias` events, they are shown in this view and returned as is, without any validation.  
Events validated| Number of events validated by the tracking plan according to filtering period.  
Events with violations| Number of events that did not comply with the tracking plan rules.  
Events dropped| Number of events that were not allowed to flow through.  
Last occurred| Date and time of the last observed violation.  
[![Violations tab](/docs/images/data-governance/tracking-plans-observability-4.webp)](</docs/images/data-governance/tracking-plans-observability-4.webp>)

You can also click on an event to view the [violation type](<https://www.rudderstack.com/docs/data-governance/tracking-plans/violation-management/>) and individual metrics.

[![Tracking plan observability for individual event](/docs/images/data-governance/tracking-plans-observability-5.webp)](</docs/images/data-governance/tracking-plans-observability-5.webp>)

Click the **View** option for more details, like the violation description and sample payload that caused the violation.

[![Violation description](/docs/images/data-governance/tracking-plans-observability-6.webp)](</docs/images/data-governance/tracking-plans-observability-6.webp>)

## Real-time tracking plan validation

> ![announcement](/docs/images/announcement.svg)
> 
> Real-time tracking plan validation is feature-flagged. Contact [RudderStack Support](<mailto:support@rudderstack.com>) to enable it for your workspace.

RudderStack supports real-time tracking plan validation at the source level — this means that RudderStack validates the events against the tracking plan rules as they are being sent from the source.

To see this feature in action:

  1. Create a tracking plan.
  2. Connect a source to the tracking plan.
  3. Send events from the source.
  4. Go to the source’s **Live Events** tab — see [Source live events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/#source-live-events>) for more information.

[![Source live events](/docs/images/rs-cloud/source-live-events.webp)](</docs/images/rs-cloud/source-live-events.webp>)

  5. See the **Tracking Plan Validation** panel on the bottom right, just below the **Payload** panel.

[![Real-time tracking plan validation panel](/docs/images/data-governance/tracking-plans/real-time-validation-panel.webp)](</docs/images/data-governance/tracking-plans/real-time-validation-panel.webp>)

### How validation works

RudderStack always validates each incoming event against a specific tracking plan version.

> ![success](/docs/images/tick.svg)
> 
> Validating against an explicit tracking plan version prevents false validation errors when multiple app versions send events instrumented against different tracking plan versions.

The following sections describe how validation works in different scenarios.

#### When using RudderTyper

When you use [RudderTyper](<https://www.rudderstack.com/docs/dev-tools/ruddertyper/>) to generate type-safe SDK code:

  * RudderTyper includes the tracking plan version in the event payload. This makes validation deterministic across multiple app versions because each event carries the exact schema version it was generated from.
  * You can see the tracking plan version used for validation in the **Tracking Plan Validation** panel of the **Live Events** viewer.


#### When using dashboard-based sources (non-RudderTyper)

For sources connected to a tracking plan in the RudderStack dashboard:

  * Events do not include the tracking plan version in the payload.
  * RudderStack automatically looks up the tracking plan version linked to the source in the backend and uses that version for validation.


**Example scenario**

  * App version 1.0 uses tracking plan version 90
  * App version 1.1 uses tracking plan version 92
  * Events from both versions are validated against their respective tracking plan versions (90 and 92)
  * This ensures each event is validated against the rules it was designed to follow


### Validation status messages

Status| Message| Description  
---|---|---  
Valid| This event will pass validation| The event adheres to all the tracking plan rules and will be forwarded for processing.  
Invalid| This event will not pass validation| The event has [validation errors](<https://www.rudderstack.com/docs/data-governance/tracking-plans/violation-management/#violation-types>) but will be processed because your [tracking plan settings](<https://www.rudderstack.com/docs/data-governance/tracking-plans/create-tracking-plans/#configure-tracking-plan-settings>) are configured to allow such events.  
Dropped| This event will not pass validation and will be dropped| The event has [validation errors](<https://www.rudderstack.com/docs/data-governance/tracking-plans/violation-management/#violation-types>) and your [tracking plan settings](<https://www.rudderstack.com/docs/data-governance/tracking-plans/create-tracking-plans/#configure-tracking-plan-settings>) are configured to drop such events.  
API Error| Failed to validate events with tracking plan| The validation process failed due to network/server issues and the validation status is unknown.  
  
Some screenshots depicting the above statuses are shown:

![Valid event](/docs/images/data-governance/tracking-plans/valid.webp)

![Invalid event](/docs/images/data-governance/tracking-plans/invalid.webp)

![Dropped event](/docs/images/data-governance/tracking-plans/dropped.webp)

![API error](/docs/images/data-governance/tracking-plans/api-error.webp)

## FAQ

#### Which events are supported by the tracking plans?

The tracking plans support [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>), [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>), [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>), [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>), and [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) events.

Note that the [`alias`](<https://www.rudderstack.com/docs/event-spec/standard-events/alias/>) call is not supported.