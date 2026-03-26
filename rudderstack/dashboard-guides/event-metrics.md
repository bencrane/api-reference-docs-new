# Event Metrics

Get detailed metrics on event ingestion, delivery, and transformation.

* * *

  * __9 minute read

  * 


RudderStack gives you observability into events at various stages of the pipeline, specifically at:

  * Event ingestion (Source)
  * Transformation, and
  * Event delivery (Destination)


This guide walks you through the different event metrics in detail.

> ![info](/docs/images/info.svg)
> 
> The event metrics covered in this guide may not reflect real-time events due to reporting latency.

## Source events

Click the **Events** tab in your source page to view detailed metrics for the ingested events along with their details.

[![View blocked event metrics for the source](/docs/images/data-governance/event-blocking/blocked-event-metrics-source.webp)](</docs/images/data-governance/event-blocking/blocked-event-metrics-source.webp>)

### Events ingested

This section gives you observability into the following metrics:

  * Number of events ingested and [blocked](<https://www.rudderstack.com/docs/data-governance/event-blocking/>) by the source.

  * Number of [bot events](<https://www.rudderstack.com/docs/data-governance/bot-management/>) ingested and blocked by the source.

  * If you have a [Tracking Plan](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>) connected to the source, then you will also see the below details:

    * Number of events validated by the Tracking Plan.
    * Number of events containing [Tracking Plan violations](<https://www.rudderstack.com/docs/data-governance/tracking-plans/violation-management/#violation-types>).
    * Number of events dropped as a result of these violations.

[![Events Ingested view](/docs/images/dashboard-guides/event-metrics/events-ingested-view.webp)](</docs/images/dashboard-guides/event-metrics/events-ingested-view.webp>)

##### **Filtering window**

You can filter the above metrics for the past 2 hours, 1 day, 7 days, and 30 days.

> ![info](/docs/images/info.svg)
> 
> The 2 hours filtering option is available only in RudderStack’s [Starter](<https://www.rudderstack.com/pricing/>), [Growth](<https://www.rudderstack.com/pricing/>) and [Enterprise](<https://www.rudderstack.com/enterprise-quote/>) plans.

[![Event filtering window options](/docs/images/dashboard-guides/event-metrics/event-filtering-window.webp)](</docs/images/dashboard-guides/event-metrics/event-filtering-window.webp>)

Note that the default filtering option varies with the RudderStack plan:

RudderStack plan| Default filtering window  
---|---  
[Starter](<https://www.rudderstack.com/pricing/>), [Growth](<https://www.rudderstack.com/pricing/>) and [Enterprise](<https://www.rudderstack.com/enterprise-quote/>)| 2 hours  
Free| 1 day  
  
##### **Event flow graph**

RudderStack also provides an event flow graph that highlights the event ingestion and processing trends over the selected time period.

[![Event flow details](/docs/images/dashboard-guides/event-metrics/source-events-flow.webp)](</docs/images/dashboard-guides/event-metrics/source-events-flow.webp>)

### Event details

This section gives you details on the ingested events and violations arising due to non-compliance with the connected Tracking Plan.

You can search for specific event names or sort all events by type, name, count, and last occurred.

[![Event details section](/docs/images/dashboard-guides/event-metrics/source-event-details.webp)](</docs/images/dashboard-guides/event-metrics/source-event-details.webp>)

#### Event metrics

You will see the following details under the **Events** tab:

Column name| Description  
---|---  
Event type| Type of event, for example, `identify`, `track`, etc.  
Event name| Name of the event in case the type is `track`.  
Count| Number of events received in the selected time period.  
Last seen| Time since the event last occurred.  
  
#### Violation details

You will see the following details under the **Violations** tab:

Column name| Description  
---|---  
Event name| Name of the event in case the type is `track`.  
Event type| Type of event, for example, `identify`, `track`, etc.  
Events validated| Number of events validated against the connected Tracking Plan.  
Events with violations| Number of events containing any [Tracking Plan violations](<https://www.rudderstack.com/docs/data-governance/tracking-plans/violation-management/#violation-types>).  
Events dropped| Number of events dropped as a result of violations.  
Last seen| Time since the event that caused the violation last occurred.  
  
Click on a row to see the detailed violation details, including the [violation type](<https://www.rudderstack.com/docs/data-governance/tracking-plans/violation-management/#violation-types>) and a sample payload.

> ![warning](/docs/images/warning.svg)
> 
> **Required permissions**
> 
> [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have full access to view the Tracking Plan violation details.
> 
> [Members](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) must have the [**Tracking Plan Violation Samples**](<https://www.rudderstack.com/docs/access-management/policies-overview/#pii-permissions>) PII permission to see the violation details.

[![Source violation details](/docs/images/dashboard-guides/event-metrics/source-violation-details.webp)](</docs/images/dashboard-guides/event-metrics/source-violation-details.webp>)

#### Blocked events

You will see the following details under the **Blocked** tab:

Column name| Description  
---|---  
Event name| Name of the blocked event.  
Block count| Number of times the event was blocked.  
Last blocked| Time since the event was last blocked by RudderStack.  
  
## Destination events

Click the **Events** tab in your destination page to view detailed metrics for the events sent to the destination along with their details.

[![Events tab for destinations in RudderStack dashboard](/docs/images/dashboard-guides/event-metrics/destination-events.webp)](</docs/images/dashboard-guides/event-metrics/destination-events.webp>)

##### **Filtering window**

You can filter the event metrics by source and time period - past 2 hours, 1 day, 7 days, or 30 days.

> ![info](/docs/images/info.svg)
> 
> The 2 hours filtering option is available only in RudderStack’s [Starter](<https://www.rudderstack.com/pricing/>), [Growth](<https://www.rudderstack.com/pricing/>) and [Enterprise](<https://www.rudderstack.com/enterprise-quote/>) plans.

[![Event filtering window options](/docs/images/dashboard-guides/event-metrics/destination-events-filtering-window.webp)](</docs/images/dashboard-guides/event-metrics/destination-events-filtering-window.webp>)

Note that the default filtering option varies with the RudderStack plan:

RudderStack plan| Default filtering window  
---|---  
[Starter](<https://www.rudderstack.com/pricing/>), [Growth](<https://www.rudderstack.com/pricing/>) and [Enterprise](<https://www.rudderstack.com/enterprise-quote/>)| 

  * Cloud destinations: 2 hours
  * Warehouse destinations: 1 day

  
Free| 

  * Cloud destinations: 1 day
  * Warehouse destinations: 1 day

  
  
### Event delivery

This section covers observability metrics for cloud and warehouse destinations.

#### Cloud destinations

You will see the below metrics for cloud destinations in the **Events delivery** section:

  * Total events delivered to the destination.
  * Number of events that failed to deliver and the failure rate.
  * P95 latency, that is, the maximum latency experienced by 95% of the events to reach the destination (only visible to [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>)).


##### **Event delivery trend**

RudderStack also provides a detailed events trend in the **Delivery** tab that highlights how it delivered the events to the cloud destination over the selected time period.

Note that the graph only shows events sent in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>) \- it does not include the metrics from [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) and [hybrid mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#hybrid-mode>) connections.

[![Event trends for destination](/docs/images/dashboard-guides/event-metrics/destination-events-trend.webp)](</docs/images/dashboard-guides/event-metrics/destination-events-trend.webp>)

##### **P95 latency**

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * The P95 latency metric is available only in RudderStack’s [Enterprise](<https://www.rudderstack.com/enterprise-quote/>) plan
>   * It is only applicable for cloud destinations connected to [Event Stream sources](<https://www.rudderstack.com/docs/sources/event-streams/>)
> 

> 
> See [P95 latency alerts](<https://www.rudderstack.com/docs/data-governance/alerts/#p95-latency-alerts>) to configure alerts for this metric.

Switch to the **Latency** tab to view the P95 latency trends for the cloud destination over the specified time period.

[![Latency trends for destination](/docs/images/dashboard-guides/event-metrics/destination-latency-trend.webp)](</docs/images/dashboard-guides/event-metrics/destination-latency-trend.webp>)

**Factors affecting event delivery latency**

The event delivery latency can be impacted by one or more of the following factors:

Factor| Notes  
---|---  
Connection to multiple sources| If a destination is connected to two sources wherein one source has a significantly higher event volume than the other, then the high volume of one source can impact the delivery latency of the events coming from the other source.  
Destination response time| RudderStack’s delivery speed is dependent on the destination API’s performance. Destination rate limits and downtime can impact delivery latency.  
Transformation connection, time, and complexity| 

  * A destination connected to multiple sources and a transformation can have a higher delivery latency compared to a destination connected to the same sources without a transformation.
  * A complex and/or long-running transformation can cause delays in event processing, which can increase latency.

  
Handling volume spikes and cluster scaling| RudderStack dynamically scales its clusters up or down to handle sudden spikes or any variations in event volume. During this process, it may temporarily pause event processing to balance the load across nodes, ensuring the events are processed in the correct order. While this safeguards data integrity, it may create a temporary event backlog and impact the delivery latency.  
  
[Contact](<mailto:support@rudderstack.com>) the RudderStack team to learn more about provisioning for spikes.  
  
#### Warehouse destinations

You will see the below metrics for warehouse destinations in the **Event delivery** section:

  * Total events delivered to the destination.
  * Number of events that failed to deliver and the failure rate.
  * Maximum sync duration for the specified time period. See Sync duration for more information on this metric.


##### **Event delivery trend**

RudderStack also provides a detailed events trend in the **Delivery** tab that highlights how it delivered the events to the warehouse destination over the selected time period.

Note that the graph only shows events sent in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>) \- it does not include the metrics from [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) and [hybrid mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#hybrid-mode>) connections.

[![Warehouse destination events trend](/docs/images/dashboard-guides/event-metrics/warehouse-destination-events-trend.webp)](</docs/images/dashboard-guides/event-metrics/warehouse-destination-events-trend.webp>)

##### **Sync duration**

Switch to the **Sync duration** tab to see the trends for **maximum sync duration** , that is, the longest sync duration for all the data syncs within each specified time bucket. Note that the frequency of these syncs is configurable via the [Sync Frequency](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/bigquery/#connection-settings>) connection setting for the warehouse destination.

[![Sync duration trends for warehouse destination](/docs/images/dashboard-guides/event-metrics/warehouse-destination-sync-duration.webp)](</docs/images/dashboard-guides/event-metrics/warehouse-destination-sync-duration.webp>)

### Event details (Event Stream)

> ![info](/docs/images/info.svg)
> 
> These metrics are shown only for cloud destinations connected to [Event Stream sources](<https://www.rudderstack.com/docs/sources/event-streams/>).

This section details all the events sent to the cloud destination within the specified time period.

Column name| Description  
---|---  
Event name| Name of the event in case the type is `track`.  
Event type| Type of event, for example, `identify`, `track`, etc.  
Successful deliveries| Number of events delivered to the destination successfully.  
Last successful delivery| Time since the last event was delivered to the destination successfully.  
Failures| Number of events that failed to reach the destination.  
Last failure| Time since the last event failed to reach the destination.  
[![Event details section for cloud destinations](/docs/images/dashboard-guides/event-metrics/event-details.webp)](</docs/images/dashboard-guides/event-metrics/event-details.webp>)

#### View failed event details

Click a row to see the event failure details along with the sample error and payload.

[![Event failure details for cloud destinations](/docs/images/dashboard-guides/event-metrics/event-details-failure.webp)](</docs/images/dashboard-guides/event-metrics/event-details-failure.webp>)

> ![warning](/docs/images/warning.svg)
> 
> **Required permissions**
> 
> [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have full access to view the delivery failure details.
> 
> [Members](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) must have the [**Destination Failure Samples**](<https://www.rudderstack.com/docs/access-management/policies-overview/#pii-permissions>) PII permission to see the delivery failure details. Otherwise, they will see the following message:
> 
> ![PII permissions message](/docs/images/dashboard-guides/event-metrics/pii-permissions.webp)

### Delivery failures (Warehouse and RETL)

These metrics give you visibility into the errors that caused delivery failure for:

  * [Warehouse destinations](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>)
  * Cloud destinations connected to [Reverse ETL sources](<https://www.rudderstack.com/docs/sources/reverse-etl/>)

Column name| Description  
---|---  
Error category| Error that caused the delivery failures.  
Count| Number of events that failed because of the error.  
Last seen| Time since the event that caused this error last occurred.  
[![Delivery failure details](/docs/images/dashboard-guides/event-metrics/delivery-failures.webp)](</docs/images/dashboard-guides/event-metrics/delivery-failures.webp>)

#### View delivery failure details

Click a row to see the delivery failure details along with the sample error and payload.

[![Delivery failures error details](/docs/images/dashboard-guides/event-metrics/destination-delivery-error.webp)](</docs/images/dashboard-guides/event-metrics/destination-delivery-error.webp>)

> ![warning](/docs/images/warning.svg)
> 
> **Required permissions**
> 
> [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have full access to view the delivery failure details.
> 
> [Members](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) must have the [**Destination Failure Samples**](<https://www.rudderstack.com/docs/access-management/policies-overview/#pii-permissions>) PII permission to see the delivery failure details. Otherwise, they will see the following message:
> 
> ![PII permissions message](/docs/images/dashboard-guides/event-metrics/pii-permissions.webp)

## Transformation events

Click the **Events** tab in your transformation page to view detailed metrics for the events processed by the transformation. You will see the following details:

  * Total events ingested for transformation.
  * Number of events dropped intentionally by the transformation (because of the transformation’s logic). For example, if your transformation [allowlists](<https://www.rudderstack.com/docs/transformations/templates/#allowlist>) only `track` events with the name `Product Purchased`, any event that does not meet this criteria is dropped.
  * Number of events dropped due to transformation errors.
  * Number of events successfully transformed and forwarded for further processing.


##### **Filtering window**

You can filter the above metrics by source, destination, and time period (past 2 hours, 1 day, 7 days, or 30 days).

> ![info](/docs/images/info.svg)
> 
> The 2 hours filtering option is available only in RudderStack’s [Starter](<https://www.rudderstack.com/pricing/>), [Growth](<https://www.rudderstack.com/pricing/>) and [Enterprise](<https://www.rudderstack.com/enterprise-quote/>) plans.

[![Events tab for transformations in RudderStack dashboard](/docs/images/dashboard-guides/event-metrics/transformation-events.webp)](</docs/images/dashboard-guides/event-metrics/transformation-events.webp>)

Note that the default filtering option varies with the RudderStack plan:

RudderStack plan| Default filtering window  
---|---  
[Starter](<https://www.rudderstack.com/pricing/>), [Growth](<https://www.rudderstack.com/pricing/>) and [Enterprise](<https://www.rudderstack.com/enterprise-quote/>)| 2 hours  
Free| 1 day  
  
### Event flow

RudderStack also provides a detailed event flow graph that highlights how it transformed the events over the selected time period.

[![Event trends for transformation](/docs/images/dashboard-guides/event-metrics/transformation-events-trend.webp)](</docs/images/dashboard-guides/event-metrics/transformation-events-trend.webp>)

### Transformation errors

This section gives you visibility into the transformation errors. You will see the following details:

Column name| Description  
---|---  
Event type| Type of event, for example, `identify`, `track`, etc.  
Event name| Name of the event in case the type is `track`.  
Source| Source from where the event was ingested.  
Destination| Destination where the transformed event was to be forwarded.  
Event count| Number of events dropped due to tranformation error.  
Last seen| Time since the event that caused the transformation error last occurred.  
Status code| HTTP status code of the tranformation error.  
[![Transformation errors](/docs/images/dashboard-guides/event-metrics/transformation-errors.webp)](</docs/images/dashboard-guides/event-metrics/transformation-errors.webp>)

#### View transformation error details

> ![warning](/docs/images/warning.svg)
> 
> **Required permissions**
> 
> [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have full access to view the transformation error details.
> 
> [Members](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) must have the [**Transformation Failure Samples**](<https://www.rudderstack.com/docs/access-management/policies-overview/#pii-permissions>) PII permission to see the transformation error details. Otherwise, they will **not** see the **Details** option next to the errors, as shown:
> 
> ![Transformation error details](/docs/images/dashboard-guides/event-metrics/transformation-error-details-2.webp)

Click **Details** to see the error description and the payload that caused the error:

[![Transformation error details](/docs/images/dashboard-guides/event-metrics/transformation-error-details.webp)](</docs/images/dashboard-guides/event-metrics/transformation-error-details.webp>)