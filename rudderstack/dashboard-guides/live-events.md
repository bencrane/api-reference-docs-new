# Live Events

Use the Live Events feature to view your source and destination events in real-time.

* * *

  * __5 minute read

  * 


RudderStack’s **Live Events** feature gives you a real-time view of the events flowing from your sources to the connected destinations. You can use this feature for better observability into your events and debug errors in case of any event failures at the destination level.

You can use this utility to view the following three types of events:

Live events type| Description  
---|---  
Source live events| View source events collected by RudderStack in real-time.  
Destination live events| View events sent to the destination in real-time.  
Transformation live events| View transformed events in real-time.  
  
## Required permissions

[Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have full access to live events for sources, destinations, and transformations.

[Members](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) must have the following [permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#pii-permissions>) in their workspace policy to view the live events:

PII permission| Description  
---|---  
Source Live Events| View live events for a source  
Destination Live Events| View live events for a destination  
Transformation Live Events| View live events flowing through a transformation  
  
To view live events ingested by Reverse ETL sources, they must have the following permissions:

PII permission| Description  
---|---  
Table Live Events| View live events from a Reverse ETL source created via a warehouse table  
Audience Live Events| View live events from a Reverse ETL source created via an audience  
SQL Model Live Events| View live events from a Reverse ETL source created via a SQL model  
  
## Source live events

This feature provides you with the real-time visibility into the source events collected by RudderStack — it is helpful when you want to verify if your source is correctly configured.

### View source live events

  1. Go to the source for which you want to view the live events.
  2. Click the **Live events** button.

[![Live Events](/docs/images/rs-cloud/source-live-events.webp)](</docs/images/rs-cloud/source-live-events.webp>)

  3. Once you send the event data from the source to RudderStack, you will see the following details in this view:

     * **Name** of the event
     * **Type** of the event collected from the source
     * **Date** and **Time** of the collected event
     * The **Payload** panel containing the event payload
     * The **Tracking Plan Validation** panel on the bottom right, just below the **Payload** panel.

[![Valid event](/docs/images/data-governance/tracking-plans/valid-event.webp)](</docs/images/data-governance/tracking-plans/valid-event.webp>)

Note that:

  * It can take a couple of seconds before your events start showing up in this view.
  * You can view live events sent up to the past 15 minutes.


> ![announcement](/docs/images/announcement.svg)
> 
> RudderStack supports [real-time tracking plan validation](<https://www.rudderstack.com/docs/data-governance/tracking-plans/observability/#real-time-tracking-plan-validation>) at the source level — this means RudderStack validates the events against the [tracking plan rules](<https://www.rudderstack.com/docs/data-governance/tracking-plans/create-tracking-plans/>) as they are being sent from the source.
> 
> **This feature is currently behind a feature flag.** Contact [RudderStack Support](<mailto:support@rudderstack.com>) to enable it for your workspace.

## Destination live events

The **destination live events** view gives you real-time visibility into your destination’s responses.

> ![info](/docs/images/info.svg)
> 
> When routing events to a destination, there can be instances when the events do not show up in the destination — in such cases, the error message included in this view is helpful for debugging.

### View destination live events

> ![warning](/docs/images/warning.svg)
> 
> You can view live events for [cloud mode destinations](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>) only .

  1. Go to the destination for which you want to view the live events.

  2. Click the **Live events** button.

  3. Once you send the events from your source to the destination, you will see the following details in this view:

     * **Name** of the event
     * **Type** of the event
     * **Date** and **Time** of the event
     * **Error message** of the event in case of event failure — it gives specific details related to an error including the error response and the date and time of the attempt made to send the event.
     * The **Payload** panel containing the event payload sent to the destination.

[![Payload to the destination](/docs/images/rs-cloud/destination-live-events-details.webp)](</docs/images/rs-cloud/destination-live-events-details.webp>)

Note that:

  * Live events are shown for all destinations. However, the event payload is not shown for some destination types like the [object storage platforms](<https://www.rudderstack.com/docs/destinations/streaming-destinations/#object-storage>) and [data warehouses](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).
  * It can take a couple of seconds before your events start showing up in this view.
  * You can view live events sent up to the past 15 minutes.
  * You can use this view to filter events by source if your destination is connected to multiple sources.


### Use case

Suppose that you send some events to [Facebook Custom Audience](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/facebook-custom-audience/>) but they are not delivered. On checking the **Live Events** tab for the **Facebook Custom Audience** destination, you see the following error:

[![Custom Audience destination error](/docs/images/rs-cloud/custom-audience-error.webp)](</docs/images/rs-cloud/custom-audience-error.webp>)

Clicking on **See full error** option displays the following error response:

[![Custom Audience full destination error](/docs/images/rs-cloud/custom-audience-full-error.webp)](</docs/images/rs-cloud/custom-audience-full-error.webp>)

[Facebok Custom Audience](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/facebook-custom-audience/>) supports only `record` type of events. As seen above, an `identify` event is sent instead and hence you see the error.

RudderStack tries sending this event several times before marking it as aborted.

## Transformations live events

You can also view the live events in case a [transformation](<https://www.rudderstack.com/docs/transformations/overview/>) is connected to a destination. RudderStack lets you view the events before and after a transformation is applied:

[![Transformation live events](/docs/images/rs-cloud/transformation-live-events.webp)](</docs/images/rs-cloud/transformation-live-events.webp>)

RudderStack also notifies you about any dropped events or errors during the transformation along with the details:

[![Transformation live events error message](/docs/images/rs-cloud/transformation-live-events-errors.webp)](</docs/images/rs-cloud/transformation-live-events-errors.webp>)

Note that:

  * It can take a couple of seconds before your events start showing up in this view.
  * You can view live events sent up to the past 15 minutes.


## FAQ

#### Why are the events sent to the destination failing?

Routing events to a destination can fail for various reasons. Often, it is due to the incorrect configuration of a destination in the RudderStack dashboard. Some other possible reasons are:

  * Incorrect/bad event payload structure
  * Rate-limiting by the destination
  * Network error
  * Destination downtime


The Destination Live Events feature gives you better visibility into how your events are sent to the destination. If there are any delivery failures, the utility also gives you insights into the reasons for the failure.

#### Are live events supported for device mode destinations?

RudderStack does not support the live events functionality for device mode destinations, that is, destinations configured to receive events in [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).

You can view live events for [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>) destinations only.