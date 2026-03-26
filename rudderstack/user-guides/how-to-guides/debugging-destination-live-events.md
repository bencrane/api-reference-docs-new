# Debug Destination Live Events

Debug and test event failures.

* * *

  * __2 minute read

  * 


When routing events to a destination via RudderStack, there may be times when the events do not show up in your destination. This guide walks you through the steps to debug your destination live events using RudderStack’s [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/>) feature.

> ![warning](/docs/images/warning.svg)
> 
> To view and debug your destination live events, your destination must be configured to send events via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

## Why are events sent to the destination failing?

Routing events to a destination via RudderStack can fail for various reasons. Some of the common ones include:

  * Incorrect destination configuration.
  * Bad event structure, that is, event is not in a destination-specific format.
  * Rate limiting enforced by the destination.
  * Destination downtime.


You can use RudderStack’s **Live Events** feature to view the events sent to your destination in real-time, and debug any delivery failure.

## Viewing destination live events

To view the events sent to your destination in real-time, follow these steps:

  1. [Set up your destination](<https://www.rudderstack.com/docs/dashboard-guides/destinations/#adding-a-destination>) in RudderStack.
  2. Click the **LIve Events** button to view the events sent from your source:

[![Destination Live Events button](/docs/images/user-guides/destination-live-events.webp)](</docs/images/user-guides/destination-live-events.webp>)

The resulting window highlights the following information:

  * **Name** of the event.
  * **Error message** of the event in case of any event failure. Upon clicking **See full error** , you get the specific details like the error response and the time of the first attempt made to send the event.

[![Destination Live Events error details](/docs/images/user-guides/destination-live-events-error-new.webp)](</docs/images/user-guides/destination-live-events-error-new.webp>)

  * Clicking the event also lets you view the **payload** sent to the destination.

[![Destination Live Events window](/docs/images/user-guides/destination-live-events-details.webp)](</docs/images/user-guides/destination-live-events-details.webp>)

> ![warning](/docs/images/warning.svg)
> 
> Live events are shown for all RudderStack destinations. However, the **event payload** is not shown for some object storage destinations like [Amazon S3](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amazon-s3/>), [Google Cloud Storage](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-cloud-storage/>), and [Microsoft Azure Blob Storage](<https://www.rudderstack.com/docs/destinations/streaming-destinations/microsoft-azure-blob-storage/>). These also include the [supported warehouse destinations](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>) like [Amazon Redshift](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/redshift/>), [Google BigQuery](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/bigquery/>), [Snowflake](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/>), etc.

## Use case

Suppose that you send some events to the [Facebook Custom Audience](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/facebook-custom-audience/>) destination but they are not delivered.

Upon checking the **Live Events** tab for the **Facebook Custom Audience** destination, you observe the following error:

[![Custom Audience destination error](/docs/images/rs-cloud/custom-audience-error.webp)](</docs/images/rs-cloud/custom-audience-error.webp>)

On clicking the **See full error** option, you can see the following error response:

[![Custom Audience full destination error](/docs/images/rs-cloud/custom-audience-full-error.webp)](</docs/images/rs-cloud/custom-audience-full-error.webp>)

From the error response, it is clear that an [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) event was sent to the destination. According to the [Facebook Custom Audience documentation](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/facebook-custom-audience/>), only [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) events are supported. As a result, when RudderStack tries sending the `identify` event, the destination gives an error. RudderStack retries sending this event several times before marking it as aborted.

This way, you can use the **Live Events** feature to better understand the responses received from the destination in case of any delivery failures and resolve them faster.