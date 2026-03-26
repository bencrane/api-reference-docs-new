# Event Stream Quickstart

Get event data flowing from your website or app in less than 15 minutes.

* * *

  * __10 minute read

  * 


RudderStack’s Event Stream pipelines help you collect behavioral events and automatically send them to other tools in your stack.

For simple use cases, you can get data flowing in less than 15 minutes by following these three steps:

  1. **Install a RudderStack SDK** in your website or app.
  2. **Instrument API calls** to identify users and capture user actions (like page views and button clicks).
  3. **Connect destination integrations** to stream events to business tools and your warehouse automatically.

[![RudderStack Event Stream Quickstart - 3 steps to collecting and integrating events](/docs/images/get-started/event-stream-quick-start-3-steps.png)](</docs/images/get-started/event-stream-quick-start-3-steps.png>)

Data teams often need to collaborate with front-end and back-end engineers to get RudderStack SDKs installed and event API calls instrumented.

Step 1 and Step 2 of this guide include helpful information for data engineers and software engineers who are collaborating on initial installation and instrumentation.

> ![success](/docs/images/tick.svg)
> 
> You can use the Event Playground app if you want to test events flowing through RudderStack **without** any instrumentation.

## Step 1: Install the JavaScript SDK

In most cases, installing one of RudderStack’s SDKs in a dev environment takes a front-end or back-end developer less than 10 minutes.

Starting with the JavaScript SDK is recommended for the following reasons:

  * The JavaScript SDK captures rich, client-side context in the payloads that help data engineers understand the full event schema.
  * Front-end updates are often faster to implement and deploy than back-end updates.


You can also see our Quickstart guides for [mobile](<https://www.rudderstack.com/docs/data-pipelines/event-stream/quickstart/mobile-quickstart/>) and [server-side](<https://www.rudderstack.com/docs/data-pipelines/event-stream/quickstart/server-side-quickstart/>) SDKs.

### How data engineers can get the JavaScript SDK code

  1. Sign in to your RudderStack account and click **\+ Add source** in the default **Connections** view.

[![Add source](/docs/images/get-started/quickstart/add-source.webp)](</docs/images/get-started/quickstart/add-source.webp>)

  2. Select **JavaScript**.

[![JavaScript source](/docs/images/get-started/quickstart/js-sdk.webp)](</docs/images/get-started/quickstart/js-sdk.webp>)

  3. Copy the installation snippet under the **Setup** tab (this snippet contains the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) and [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard. ](</docs/resources/glossary/#data-plane-url>), which ensure events are sent to the correct source).

[![JavaScript SDK snippet](/docs/images/get-started/quickstart/js-sdk-snippet.webp)](</docs/images/get-started/quickstart/js-sdk-snippet.webp>)

  4. Send the snippet to your front-end development team.


### How front-end engineers can install the JavaScript SDK

Your data engineer should have provided you a code snippet per the above steps. To install, paste the code into your website’s `<head>` section.

The snippet you received already contains the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) and [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) needed to route the event to the correct RudderStack source.

> ![info](/docs/images/info.svg)
> 
> The implicit `page` call at the end of the snippet (in case of the previous JavaScript SDK versions) is removed in [JavaScript SDK v3](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>). You will have to instrument it separately.

## Step 2: Verify data flow

Once you have installed the JavaScript SDK, you can use RudderStack’s **Event Playground app** (embedded in step 3 below) to send test events to your account and verify the data flow **without** any instrumentation.

Follow these steps to use the **Event Playground app** to send test events to your account:

  1. Sign in to the [RudderStack dashboard](<https://app.rudderstack.com/>). Note the [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) at the top of the default **Connections** page.

[![Data plane URL](/docs/images/general/data-plane-url.webp)](</docs/images/general/data-plane-url.webp>)

  2. Set up a [source](<https://www.rudderstack.com/docs/dashboard-guides/sources/#add-a-source>) and note its [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination. ](</docs/resources/glossary/#write-key>).

[![JavaScript SDK source write key](/docs/images/get-started/quickstart/js-write-key.webp)](</docs/images/get-started/quickstart/js-write-key.webp>)

  3. Click **Use My Account** in the **Event Playground app** below and specify the write key and data plane URL obtained in the above steps.


  4. Click **Save**.
  5. Select the required **API Method** from the dropdown. You can also edit the relevant fields or traits/properties.
  6. Click **Send to my account** to send the event.
  7. Go to the [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/#view-source-live-events>) viewer of your source (set up in Step 2) to verify that the event is successfully received.


See Step 4: Check live events for more information on the **Live Events** feature.  
  


## Step 3: Instrument API calls

The RudderStack JavaScript SDK follows a [standard event spec](<https://www.rudderstack.com/docs/event-spec/standard-events/>). It helps you plan your event data and supports various API calls for tracking your website events - these include `identify`, `track`, `screen`, `group`, `alias`, and `reset` calls.

The best place to start instrumentation is with `page` calls, which help you track pages your unique users visit.

### Instrumenting `page` calls

[`page`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#page>) events help you in analyzing customer journeys in your warehouse or data lake. You can also forward them directly to downstream tools like Google Analytics or Amplitude for real-time marketing and product analytics.

A sample `page` call is shown below:
    
    
    rudderanalytics.page();
    

For other frameworks and single page apps, run the `page` call whenever the URL changes. Here’s an example of how to do this in Next.js:
    
    
    'use client'
    
    import { useEffect } from 'react'
    import { usePathname } from 'next/navigation'
    
    export const RudderAnalytics = () => {
      const pathname = usePathname()
    
      useEffect(() => {
         window.rudderanalytics.page()
      }, [pathname])
    
    }
    

If you’re running a Jamstack setup, see the [Jamstack setup guides](<https://www.rudderstack.com/docs/user-guides/how-to-guides/rudderstack-jamstack-integration/>) for framework-specific instructions.

### Instrumenting additional API calls

Apart from `page` calls, `track` and `identify` are the most commonly used API calls.

  * `track` events represent user actions, like button clicks.
  * `identify` calls let you identify users, assign them traits (like name and email), and associate the user to their actions.


> ![info](/docs/images/info.svg)
> 
> To see an example of instrumentation in the context of a full HTML page, see the full HTML page example where the SDK is installed and `track` and `identify` calls are instrumented.

#### **Track events**

To implement [`track`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#track>) calls, you need to listen for the desired user action, then fire a `track` call when it happens. You can describe these events by adding [propertiesProperties are additional contextual information you can add to a `track` call to further describe the action a user takes.](</docs/resources/glossary/#properties>) to the payload.

Here is an example of basic, inline front-end code that fires a `track` call named `click` when a user clicks on an element. The properties are `target_url` and `link_text`.
    
    
    <a
      href="/foo"
      onclick="window.rudderanalytics.track('click', {
      target_url: '/foo',
      link_text: 'Bar'
      })
      ">
    Bar
    </a>
    

#### **Identify events**

[`identify`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#identify>) calls are typically fired when a user performs an identifying action like making a purchase or submitting a form. `identify` calls also associate a known user with their actions (even if previously anonymous). You can describe users with attributes by adding [traitsTraits are attributes that describe a user. They can be added to an identify call in the `traits` object. Some examples of traits include age, gender, or some specific details - for example, a user’s product plan (free, basic, premium).](</docs/resources/glossary/#traits>) to the payload.

Here is an example of basic, inline front-end code that fires an `identify` call on form submit. The `traits` are `company`, `name`, and `email`.
    
    
    <form>
      <input type="text" name="name" id="name" placeholder="name" />
      <input type="text" name="company" id="company" placeholder="company" />
      <input type="text" name="email" id="email" placeholder="email" />
      <input
        type="submit"
        onclick="
        window.rudderanalytics.identify(
        document.getElementById('email').value, 
        { company: document.getElementById('company').value, 
        name: document.getElementById('name').value,
        email: document.getElementById('email').value 
        }); return false;" />
    </form>
    

## Step 4: Check live events

Once software engineers have installed the SDK and instrumented events, the data team can verify the event flow into RudderStack. Then, they can connect destination integrations to forward events to the tools in their stack automatically.

To see the live events, go to your JavaScript source from the **Connections** view and click the **Live Events** button in the top right of your screen.

> ![info](/docs/images/info.svg)
> 
> There will be a delay before you see events in the **Live Events** view. RudderStack does not store any data; it temporarily opens a gateway between the control plane and data plane to show you the live events. The delays usually last only a few seconds but on the [RudderStack Cloud Free](<https://rudderstack.com/pricing/>) plan, they can last up to one minute.

[![Live Events](/docs/images/rs-cloud/source-live-events.webp)](</docs/images/rs-cloud/source-live-events.webp>)

After a few seconds, you will see events populating the feed.

> ![warning](/docs/images/warning.svg)
> 
> If you do not see events in the **Live Events** view, then there is likely a problem with your instrumentation.

## Step 5: Connect destination integrations

> ![success](/docs/images/tick.svg)
> 
> RudderStack supports 200+ integrations including data warehouses and data lakes, marketing platforms, CRMs, analytics tools, streaming platforms, and more. You can see the full list of supported destination integrations [here](<https://www.rudderstack.com/docs/destinations/overview/>).

To add a destination in RudderStack:

  1. Click **\+ Add destination** in the default **Connections** view.

[![Add destination](/docs/images/get-started/quickstart/add-destination.webp)](</docs/images/get-started/quickstart/add-destination.webp>)

  2. From the list, select a destination where you want to route your event data. Here are some popular destinations to help you get started:

Category| Destination  
---|---  
Analytics| [Amplitude](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amplitude/>), [Mixpanel](<https://www.rudderstack.com/docs/destinations/streaming-destinations/mixpanel/>), [GA4](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-analytics-4/>)  
CRM| [HubSpot](<https://www.rudderstack.com/docs/destinations/streaming-destinations/hubspot/>), [Salesforce](<https://www.rudderstack.com/docs/destinations/streaming-destinations/salesforce/>)  
Marketing| [Braze](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/>), [Mailchimp](<https://www.rudderstack.com/docs/destinations/streaming-destinations/mailchimp/>)  
Object storage| [Amazon S3](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amazon-s3/>), [Redis](<https://www.rudderstack.com/docs/destinations/streaming-destinations/redis/>)  
Streaming platforms| [Apache Kafka](<https://www.rudderstack.com/docs/destinations/streaming-destinations/kafka/>), [Amazon Kinesis](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amazon-kinesis/>)  
Warehouses| [Snowflake](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/>), [BigQuery](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/bigquery/>), [Redshift](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/redshift/>)  
Data lakes & lakehouses| [Databricks](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/delta-lake/>), [Google Cloud Storage](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/gcs-datalake/>)  
  
  3. Set up the destination by configuring the connection settings. For details, see the [destination-specific documentation](<https://www.rudderstack.com/docs/destinations/overview/>).


## Next steps

This section contains some optional but helpful steps that leverage RudderStack’s most popular features for transforming events and debugging problems.

### Add event transformations

One of RudderStack’s most-used features is [Event Transformations](<https://www.rudderstack.com/docs/transformations/overview/>), which you can use to operate on the payloads flowing through RudderStack. You can use it for:

  * Sampling or filtering events.
  * Removing sensitive user PII from your events.
  * Enriching events using static logic, an external API, and more.


To use a transformation:

  1. In the left sidebar, go to **Collect** > **Transformations**. Then, click **Create Transformation**.

[![Create transformation](/docs/images/get-started/quickstart/create-transformation.webp)](</docs/images/get-started/quickstart/create-transformation.webp>)

  2. Select a [transformation template](<https://www.rudderstack.com/docs/transformations/templates/>) from the list depending on your use case. To create a transformation from scratch, click **Custom transformation**.


> ![success](/docs/images/tick.svg)
> 
> Transformation templates contain prepopulated, ready-to-use transformation logic, which you can apply to your events before sending them to the destination. You can also modify the code as per your needs.

[![Choose a template](/docs/images/features/transformation-templates-2.webp)](</docs/images/features/transformation-templates-2.webp>)

  3. Verify if your transformation works as expected by clicking the **Run Test** button.

[![Testing a transformation](/docs/images/features/run-test-transformations.webp)](</docs/images/features/run-test-transformations.webp>)

  4. Click **Save** to save your transformation.
  5. Go to the **Connections** tab of your transformation and connect it to the destination you set up above. See [Connect transformation to destination](<https://www.rudderstack.com/docs/transformations/manage/#connect-transformation-to-destination>) for more information.


> ![info](/docs/images/info.svg)
> 
> When you add a transformation and connect it to a destination, RudderStack does the following:
> 
>   1. Tracks events at the source.
>   2. Applies the transformation logic to your events.
>   3. Converts the events in a format the destination expects - RudderStack does this internally and requires no user intervention.
>   4. Sends the transformed events to your destination.
> 


### Debugging

RudderStack gives you complete observability into your events and the ability to debug errors that might occur in case of event failures. It provides the [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/>) feature, where you can:

  * Verify your instrumentation.
  * Get a real-time view of the events flowing from your sources to the connected destinations.
  * Identify and debug any errors at the source, destination, or transformation level and narrow down the root cause of the issue.


#### **Source Live Events viewer**

This is helpful to verify if RudderStack is receiving the source events at all. The payload you see in this viewer is the raw event payload collected from your website.

[![Live Events](/docs/images/rs-cloud/source-live-events.webp)](</docs/images/rs-cloud/source-live-events.webp>)[![Source live events details](/docs/images/rs-cloud/source-live-events-details.webp)](</docs/images/rs-cloud/source-live-events-details.webp>)

#### **Transformation Live Events viewer**

This viewer will give you a before and after snapshot of the event going into your user transformation and what it looks like afterward. It also notifies you about any dropped events or errors during the transformation, along with the details.

[![Transformation live events](/docs/images/rs-cloud/transformation-live-events.webp)](</docs/images/rs-cloud/transformation-live-events.webp>)[![Transformation live events error message](/docs/images/rs-cloud/transformation-live-events-errors.webp)](</docs/images/rs-cloud/transformation-live-events-errors.webp>)

#### **Destination Live Events viewer**

This viewer shows you what the payload looks like when RudderStack sends it to the destination. You can also see the detailed error message if the destination returns an error.

[![Payload to the destination](/docs/images/rs-cloud/destination-live-events-details.webp)](</docs/images/rs-cloud/destination-live-events-details.webp>)

See the [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/>) documentation for more details.

## Full HTML page example

Here’s an example of the RudderStack JavaScript SDK installed on an HTML page with `track` and `identify` calls instrumented inline.

> ![info](/docs/images/info.svg)
> 
> See [these instructions](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/installation/#using-cdn>) to get the JavaScript SDK installation snippet.
    
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <script type="text/javascript">
      // Replace the <script> tag with your JavaScript SDK snippet.
      </script>
      <title>RudderStack Example</title>
    </head>
    
    <body>
        <form>
            <input type="text" name="name" id="name" placeholder="name" />
            <input type="text" name="company" id="company" placeholder="company" />
            <input type="text" name="email" id="email" placeholder="email" />
            <input
              type="submit"
              onclick="
              window.rudderanalytics.identify(
              document.getElementById('email').value, 
              { 
                company: document.getElementById('company').value, 
                name: document.getElementById('name').value,
                email: document.getElementById('email').value 
              }); return false;" />
        </form>
        <a
            href="/foo"
            onclick="window.rudderanalytics.track('click', {
            target_url: '/foo',
            link_text: 'Bar'
            })
            ">
            Bar
        </a>
    </body>