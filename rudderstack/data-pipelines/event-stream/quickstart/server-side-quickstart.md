# Event Stream Server-side Quickstart

Get event data flowing from your server-side app in less than 15 minutes.

* * *

  * __8 minute read

  * 


This quickstart guide walks through code examples using the [Node.js SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-node-sdk/>). It will help you get started with our server-side SDKs.

For simple use cases, you can get data flowing in less than 15 minutes by following these three steps:

  1. **Install a RudderStack SDK** in your back-end/server-side app.
  2. **Instrument API calls** to identify users and capture user actions (like page views and button clicks).
  3. **Connect destination integrations** to stream events to business tools and your warehouse automatically.


> ![info](/docs/images/info.svg)
> 
> [Sign up](<https://app.rudderstack.com/signup>) for a free RudderStack Cloud account before you get started.

## Step 1: Installing the Node.js SDK

In most cases, installing one of RudderStack’s [server-side](<https://www.rudderstack.com/docs/sources/event-streams/sdks/#server>) SDKs in a dev environment takes a back-end developer less than 10 minutes.

### How data engineers can get the Node.js SDK code

  1. Sign in to your RudderStack account and click **\+ Add source** in the default **Connections** view.

[![Add source](/docs/images/get-started/quickstart/add-source.webp)](</docs/images/get-started/quickstart/add-source.webp>)

  2. Select **Node**.

[![Add Node source](/docs/images/get-started/quickstart/add-node-source.webp)](</docs/images/get-started/quickstart/add-node-source.webp>)

  3. Copy the installation snippet under the **Setup** tab (this snippet contains the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) and [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard. ](</docs/resources/glossary/#data-plane-url>), which ensure events are sent to the correct source).

[![Node.js SDK snippet](/docs/images/get-started/quickstart/node-snippet.webp)](</docs/images/get-started/quickstart/node-snippet.webp>)

  4. Send the snippet to your back-end development team.


### How back-end engineers can install the Node.js SDK

Install the Node.js SDK in your back-end app using npm by running the following command:
    
    
    npm install @rudderstack/rudder-sdk-node
    

#### **Initialize the SDK**

Your data engineer should have provided you the Node.js SDK snippet. Follow these steps to initialize the SDK:

The snippet you recieved should already contain the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) and [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) values, which are needed in order to route the event to the correct source in RudderStack.

For reference, here’s what the Node.js SDK installation snippet looks like:
    
    
    const RudderAnalytics = require('@rudderstack/rudder-sdk-node');
    
    const client = new RudderAnalytics(WRITE_KEY, {
      dataPlaneUrl: DATA_PLANE_URL
    });
    

For more information, see the full [Node.js SDK documentation](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-node-sdk/>).

> ![info](/docs/images/info.svg)
> 
> Import the initialization snippet in `app.js` or any other file in your project, depending on your requirement.

> ![success](/docs/images/tick.svg)
> 
> See this [sample Node app](<https://github.com/rudderlabs/rudder-sdk-node/blob/develop/examples/sample-app/app.js>) for more information on initializing the SDK.

## Step 2: Instrument API calls

All RudderStack server-side SDKs follow a [standard event spec](<https://www.rudderstack.com/docs/event-spec/standard-events/>). It helps you plan your event data and supports various API calls for tracking events in your app - these include `identify`, `track`, `screen`, `group`, `alias`, and `reset` calls.

Most users start by implementing `track` and `identify` calls.

You can use **`track` calls** to record user activities like clicking a button, creating a post, or making a purchase. You can describe `track` events with [propertiesProperties are additional contextual information you can add to a `track` call to further describe the action a user takes. ](</docs/resources/glossary/#properties>).

Here is an example of a `track` call named `Item Viewed`. The properties are `price` and `item_id`:
    
    
    client.track({
      userId: "1hKOmRA4GRlm",
      event: "Item Viewed",
      properties: {
        price: 19.95,
        item_id: "1234abcd",
      },
    })
    

**[`identify`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-node-sdk/#identify>) calls** are typically fired when a user performs an identifying action like creating an account or making a purchase. `identify` calls also associate a known user with their actions (even if previously anonymous). You can describe users with attributes by adding [traitsTraits are attributes that describe a user. They can be added to an identify call in the `traits` object. Some examples of traits include age, gender, or some specific details - for example, a user’s product plan (free, basic, premium).](</docs/resources/glossary/#traits>) to the payload.

Here is an example of an `identify` call. The `traits` are `name`, `email`, `plan`, and `friends`.
    
    
    client.identify({
      userId: "1hKOmRA4GRlm",
      traits: {
        name: "Alex Keener",
        email: "alex@example.com",
        plan: "Free",
        friends: 21,
      },
    })
    

> ![warning](/docs/images/warning.svg)
> 
> **RudderStack does not store or persist user state in any of the server-side SDKs.**
> 
> Unlike the client-side SDKs that automatically store state information for individual users, the server-side SDKs don’t persist state. Hence, you must specify either `userId` or `anonymousId` every time you make any API calls using a server-side SDK to associate events with individual users.

See the [RudderStack Node.js SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-node-sdk/#sending-events>) documentation for more information on the other supported API calls.

## Step 3: Verify data flow and connect destination integrations

Once software engineers have installed the SDK and instrumented events, the data team can verify the event flow into RudderStack. Then, they can connect destination integrations to forward events to the tools in their stack automatically.

### 1\. Verify data flow for your Node source

Before connecting destinations, verify that events are flowing into RudderStack by checking the **Live Events** viewer in your Node source.

To see live events, go to your Node source from the **Connections** view and click the **Live Events** button in the top right of your screen.

> ![info](/docs/images/info.svg)
> 
> There will be a delay before you see events in the **Live Events** view. RudderStack doesn’t store any data; it temporarily opens a gateway between the control plane and data plane to show you the live events. The delays usually last only a few seconds but on the [RudderStack Cloud Free](<https://rudderstack.com/pricing/>) plan, they can last up to one minute.

[![Live Events](/docs/images/get-started/quickstart/source-live-events-node.webp)](</docs/images/get-started/quickstart/source-live-events-node.webp>)

After a few seconds, you will see events populating the feed.

> ![warning](/docs/images/warning.svg)
> 
> If you do not see events in the **Live Events** view, then there is likely a problem with your instrumentation.

### 2\. Connect destination integrations

> ![success](/docs/images/tick.svg)
> 
> RudderStack supports 200+ integrations including data warehouses and data lakes, marketing platforms, CRMs, analytics tools, streaming platforms, and more. You can see the full list of supported destination integrations [here](<https://www.rudderstack.com/docs/destinations/overview/>).

To add a destination in RudderStack:

  1. Click **\+ Add destination** in the default **Connections** view.

[![Add destination](/docs/images/get-started/quickstart/add-destination-node.webp)](</docs/images/get-started/quickstart/add-destination-node.webp>)

  2. From the list, select your preferred destination where you want to route the event data. Here are some popular destinations to help you get started:

Category| Destination  
---|---  
Analytics| [Amplitude](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amplitude/>), [Mixpanel](<https://www.rudderstack.com/docs/destinations/streaming-destinations/mixpanel/>), [GA4](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-analytics-4/>)  
CRM| [HubSpot](<https://www.rudderstack.com/docs/destinations/streaming-destinations/hubspot/>), [Salesforce](<https://www.rudderstack.com/docs/destinations/streaming-destinations/salesforce/>)  
Marketing| [Braze](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/>), [Mailchimp](<https://www.rudderstack.com/docs/destinations/streaming-destinations/mailchimp/>)  
Object storage| [Amazon S3](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amazon-s3/>), [Redis](<https://www.rudderstack.com/docs/destinations/streaming-destinations/redis/>)  
Streaming platforms| [Apache Kafka](<https://www.rudderstack.com/docs/destinations/streaming-destinations/kafka/>), [Amazon Kinesis](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amazon-kinesis/>)  
Warehouses| [Snowflake](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/>), [BigQuery](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/bigquery/>), [Redshift](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/redshift/>)  
Data lakes & lakehouses| [Databricks](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/delta-lake/>), [Google Cloud Storage](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/gcs-datalake/>)  
  
  3. Set up the destination by configuring the connection settings. For details, see the destination-specific documentation.


## Next steps

This section contains some optional, but helpful steps that leverage RudderStack’s most popular features for transforming events and debugging problems.

### Add event transformations

One of RudderStack’s most-loved features is [Event Transformations](<https://www.rudderstack.com/docs/transformations/overview/>), which you can use to operate on the payloads flowing through RudderStack. You can use it for:

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

[![Live Events](/docs/images/get-started/quickstart/source-live-events-node.webp)](</docs/images/get-started/quickstart/source-live-events-node.webp>)[![Source live events details](/docs/images/rs-cloud/source-live-events-details.webp)](</docs/images/rs-cloud/source-live-events-details.webp>)

#### **Transformation Live Events viewer**

This viewer will give you a before and after snapshot of the event going into your user transformation and what it looks like afterward. It also notifies you about any dropped events or errors during the transformation, along with the details.

[![Transformation live events](/docs/images/rs-cloud/transformation-live-events.webp)](</docs/images/rs-cloud/transformation-live-events.webp>)[![Transformation live events error message](/docs/images/rs-cloud/transformation-live-events-errors.webp)](</docs/images/rs-cloud/transformation-live-events-errors.webp>)

#### **Destination Live Events viewer**

This viewer shows you what the payload looks like when RudderStack sends it to the destination. You can also see the detailed error message if the destination returns an error.

[![Payload to the destination](/docs/images/rs-cloud/destination-live-events-details.webp)](</docs/images/rs-cloud/destination-live-events-details.webp>)

See the [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/>) documentation for more details.

## Support

For any questions on using RudderStack, you can:

  * Start a conversation in our [Community Slack](<https://rudderstack.com/join-rudderstack-slack-community>).
  * Drop an email to [RudderStack support](<mailto:support@rudderstack.com>).