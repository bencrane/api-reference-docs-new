# Event Blocking Beta

Prevent unwanted events from entering RudderStack to maintain clean data capture and control costs.

Available Plans

  * growth
  * enterprise


* * *

  *  __6 minute read

  * 


> ![announcement](/docs/images/announcement.svg)
> 
> This feature is in **Closed Beta** as part of RudderStack’s [Early Access Program](<https://www.rudderstack.com/docs/get-started/alpha-and-beta-features/beta-features/closed-beta/>), where we work with early users and customers to test new features and get feedback before making them generally available.
> 
> [Contact the Product team](<mailto:product@rudderstack.com>) if you have any questions.

This guide walks you through RudderStack’s event blocking feature and explains how to prevent unwanted events from entering your data pipelines.

## Overview

RudderStack’s **Event Blocking** feature lets you prevent specific events from being ingested by RudderStack. When you block an event, it’s completely dropped before entering your data pipelines, which helps maintain clean data capture and reduces unnecessary costs.

> ![success](/docs/images/tick.svg)
> 
> Blocked events are not counted toward your billable event volume, which can help reduce costs.

## When to use event blocking

Event blocking is designed for specific scenarios where you need to prevent events from entering RudderStack entirely:

  * **Mobile lifecycle events** : Mobile SDKs automatically track lifecycle events, but not all of them are useful for every use case. You can block specific lifecycle events that don’t provide value for your analysis.
  * **Bug-related event overflow** : When a bug in your application causes events to fire multiple times or creates an overflow of unwanted events, you can temporarily block those events while you deploy a fix.
  * **Deprecated or incorrectly instrumented events** : When event definitions change or events become deprecated, but the development cycle for removing them through code takes time, event blocking provides an immediate solution to maintain clean data capture.


> ![warning](/docs/images/warning.svg)
> 
> Event blocking results in permanent data loss. Blocked events cannot be [replayed](<https://www.rudderstack.com/docs/user-guides/administrators-guide/event-replay/>) or recovered.
> 
> See the Limitations section for more details.

Event blocking is **not the right solution** for the following scenarios:

  * **Destination-specific event filtering** : You can use the [`integrations` object](<https://www.rudderstack.com/docs/user-guides/how-to-guides/how-to-filter-selective-destinations/>) or [Transformations](<https://www.rudderstack.com/docs/transformations/>) to filter events from going to specific destinations.
  * **Property-level filtering** : Use [Tracking Plans](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>) to handle malformed event properties or validate event schemas.
  * **Complex filtering logic** : Event blocking only supports blocking by event name. For more complex filtering requirements, use [Transformations](<https://www.rudderstack.com/docs/transformations/>).


## Enable event blocking

> ![info](/docs/images/info.svg)
> 
> Only **Admins** have access to enable the event blocking feature.

To enable or disable the event blocking feature for your workspace:

  1. Go to **Govern** > **Event Blocking**.
  2. Locate the **Block events** toggle on the top right corner of the page.
  3. Turn it on or off to enable or disable the feature.

[![Enable event blocking in the Event Blocking page](/docs/images/data-governance/event-blocking/enable-event-blocking.webp)](</docs/images/data-governance/event-blocking/enable-event-blocking.webp>)

## Configure event blocking

RudderStack provides a very simple dashboard interface to manage event blocking.

### Block an event

You can block events in the RudderStack dashboard in any of the following ways:

#### 1\. Via the Event Blocking page

  1. Go to **Govern** > **Event Blocking**.
  2. Click **Add Event**.

[![Add event button in the Event Blocking page](/docs/images/data-governance/event-blocking/event-blocking.webp)](</docs/images/data-governance/event-blocking/event-blocking.webp>)

  3. Select the events from the list (populated based on the events present in your Data Catalog).
  4. Click **Add events**.

[![Block an event in the Event Blocking page](/docs/images/data-governance/event-blocking/configure-events.webp)](</docs/images/data-governance/event-blocking/configure-events.webp>)

You can also block a new event in this page:

  1. Click **Add Event** > **Block a new event**.

[![Block a new event in the Event Blocking page](/docs/images/data-governance/event-blocking/block-new-event-1.webp)](</docs/images/data-governance/event-blocking/block-new-event-1.webp>)

  2. Enter the event name, description, and category.
  3. Click **Create event**.
  4. Confirm your action in the subsequent dialog by clicking **Yes, block event**.


> ![info](/docs/images/info.svg)
> 
> The new event will also be added to the Data Catalog.

[![Block a new event in the Event Blocking page](/docs/images/data-governance/event-blocking/block-new-event-2.webp)](</docs/images/data-governance/event-blocking/block-new-event-2.webp>)

#### 2\. Via the Data Catalog

  1. Go to **Govern** > **Data Catalog** > **Events**.
  2. From the list of events, click on the event you want to block.
  3. In the **Event details** view, locate the **Block event** toggle and turn it on.
  4. Confirm your action in the subsequent dialog by clicking **Yes, block event**.

[![Block an event in the Data Catalog](/docs/images/data-governance/event-blocking/event-blocking-catalog.webp)](</docs/images/data-governance/event-blocking/event-blocking-catalog.webp>)

Once you enable event blocking for an event, RudderStack will stop ingesting events with that name across all your sources.

### Unblock an event

To unblock an event that you blocked previously:

  1. Go to **Govern** > **Event Blocking**.
  2. Find the specific blocked event.
  3. Click the meatballs (**…**) menu next to the event and select **Remove event from block list**.
  4. Confirm your action in the dialog by clicking **Remove**.

[![Unblock an event in the Event Blocking page](/docs/images/data-governance/event-blocking/unblock-event.webp)](</docs/images/data-governance/event-blocking/unblock-event.webp>)

You can also unblock an event in the **Event details** view in the Data Catalog:

  1. Go to **Govern** > **Data Catalog** > **Events**.
  2. Find the event you want to unblock and click on it to open the **Event details** view.
  3. Locate the **Block event** toggle and turn it off.
  4. Confirm your action in the subsequent dialog by clicking **Yes, unblock event**.


Once unblocked, the event will start flowing through your data pipelines again.

## Observability

This section explains how to view blocked events in your Data Catalog and see the overall blocked event metrics for a particular source.

### View source-level blocked event metrics

  1. Go to **Collect** > **Sources** and select your source.
  2. Navigate to the **Events** tab.
  3. See the **Blocked events** metric to see the number of blocked events for that specific source.


> ![info](/docs/images/info.svg)
> 
> The blocked events count shown in this view represents events blocked for that specific source only, not the total blocked events across all sources.

See the **Event Details** section for more granular details like:

  * **Event name** : The name of the event
  * **Block count** : Number of times the event was blocked
  * **Last blocked** : When the event was last blocked by RudderStack

[![View blocked event metrics for the source](/docs/images/data-governance/event-blocking/blocked-event-metrics-source.webp)](</docs/images/data-governance/event-blocking/blocked-event-metrics-source.webp>)

### View blocked event details in Data Catalog

  1. Go to **Govern** > **Event Blocking**.
  2. Find the specific blocked event.
  3. Click the meatballs (**…**) menu next to the event and select **View event in Data Catalog**.

[![View blocked event in Data Catalog](/docs/images/data-governance/event-blocking/blocked-event-metrics-catalog-1.webp)](</docs/images/data-governance/event-blocking/blocked-event-metrics-catalog-1.webp>)

  4. You will see the following information in the **Event details** view:


  * **Last seen** : When the event was last blocked by RudderStack
  * **30 days volume** : Number of events blocked in the last 30 days

[![View blocked event details in Data Catalog](/docs/images/data-governance/event-blocking/blocked-event-metrics-catalog-2.webp)](</docs/images/data-governance/event-blocking/blocked-event-metrics-catalog-2.webp>)

## Considerations

Keep the following points in mind when before using the event blocking feature:

### Event blocking and Tracking Plans

Event blocking has specific interactions with Tracking Plans:

  * **Events defined in Tracking Plans cannot be blocked** : You cannot block an event that is already defined in a Tracking Plan. Remove it from the Tracking Plan first if you need to block it.
  * **Blocked events cannot be added to Tracking Plans** : You cannot add a blocked event to any Tracking Plan.


### Data loss implications

Event blocking results in permanent data loss. Before blocking an event:

  * Confirm that the event has no current or future analytical value.
  * Consider whether downstream teams or systems depend on this event data.
  * Evaluate if alternative solutions (like Transformations or Tracking Plans) would be more appropriate.


### Impact on metrics and reporting

Blocking events will affect:

  * Historical trend analysis if you compare pre-blocking and post-blocking periods.
  * Downstream analytics and reporting that depend on the blocked events.
  * Event volume metrics and billing calculations.


### Testing and validation

Before blocking events in production:

  * Test the impact in a development environment if possible.
  * Communicate with stakeholders who might be affected by the data change.
  * Have a plan for unblocking events, if needed.


## Limitations

The event blocking feature has the following limitations currently:

  * **Event type restriction** : You can block only `track` events — support for `page`, `screen`, `identify`, `group`, and `alias` events is not available.
  * **Global blocking only** : Events are blocked across all sources. You cannot block events from specific sources or a subset of sources.
  * **Event name only** : Blocking is based solely on the event name. You cannot block events based on properties, user attributes, or other complex logic.
  * **No automated configuration** : You must configure event blocking manually through the Data Catalog interface.
  * **Plan limitations** : Available only for Growth (Maximum of 2 blocked events are configurable) and Enterprise (unlimited blocked events) plans.
  * **Permanent data loss** : Blocked events cannot be recovered, replayed, or analyzed later.