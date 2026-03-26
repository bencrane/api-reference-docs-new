# Event StreamMobile Quickstart

Get event data flowing from your mobile app in less than 15 minutes.

* * *

  * __8 minute read

  * 


This quickstart guide will help you get started with using [RudderStack mobile SDKs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/#mobile>) to stream events from your mobile app to other tools in your stack.

Note that all the examples and code snippets in this guide are for the iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. .

## Overview

For simple use cases, you can get data flowing from your mobile app to other tools in your stack in less than 15 minutes by following these steps:

  1. **Install a RudderStack SDK** in your mobile app.
  2. **Instrument API calls** to identify users and capture user actions (like page views and button clicks).
  3. **Connect destination integrations** to stream events to business tools and your warehouse automatically.


> ![tip](/docs/images/tip.svg)
> 
> **Tip:** [Sign up](<https://app.rudderstack.com/signup>) for a free RudderStack Cloud account before you get started.

## Step 1: Install the iOS (Obj-C) SDK

In most cases, installing one of RudderStack’s [mobile SDKs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/#mobile>) takes a developer less than 10 minutes.

### How data engineers can get the iOS (Obj-C) SDK code

  1. Sign in to your RudderStack account and click **\+ Add source** in the default **Connections** view.

[![Add source](/docs/images/get-started/quickstart/add-source.webp)](</docs/images/get-started/quickstart/add-source.webp>)

  2. Select **iOS (Obj-C)** from the list of sources.
  3. Copy the installation snippet under the **Setup** tab (this snippet contains the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) and [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard. ](</docs/resources/glossary/#data-plane-url>), which ensure events are sent to the correct source).

[![iOS SDK snippet](/docs/images/get-started/quickstart/ios-snippet.webp)](</docs/images/get-started/quickstart/ios-snippet.webp>)

  4. Send the snippet to your mobile development team.


### How mobile developers can install the iOS (Obj-C) SDK

> ![info](/docs/images/info.svg)
> 
> Before installing the iOS (Obj-C) SDK, make sure to first initialize the `Podfile` within your app by running `pod init`.
> 
> If you are using Swift Package Manager (SPM) to install the iOS (Obj-C) SDK, see these [instructions](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/#swift-package-manager>).

  1. Install the iOS (Obj-C) SDK using [Cocoapods](<https://cocoapods.org/pods/Rudder>) by adding the iOS (Obj-C) SDK to your application’s `Podfile`:


    
    
    pod 'Rudder'
    

  2. Run the following command to install the SDK and the required dependencies:


    
    
    pod install
    

> ![warning](/docs/images/warning.svg)
> 
> Include the following code in all `.m` and `.h` files where you want to reference or use the RudderStack SDK classes.
>     
>     
>     #import <Rudder/Rudder.h>
>     

#### **Initialize the SDK**

Your data engineer should have provided you the iOS (Obj-C) SDK snippet. Follow these steps to initialize the SDK:

  1. Open your app’s `AppDelegate.m` file - the entry point of the app.
  2. Place the initialization snippet under the `didFinishLaunchingWithOptions` method.


> ![info](/docs/images/info.svg)
> 
> You can choose to place the snippet under any method in any other file based on your requirement.

A sample initialization snippet is shown below:
    
    
    RSConfigBuilder *builder = [[RSConfigBuilder alloc] init];
    [builder withDataPlaneUrl:DATA_PLANE_URL];
    [RSClient getInstance:WRITE_KEY config:[builder build]];
    
    
    
    let builder: RSConfigBuilder = RSConfigBuilder()
        .withDataPlaneUrl(DATA_PLANE_URL)
    RSClient.getInstance(WRITE_KEY, config: builder.build())
    

For more information, see the full [iOS (Obj-C) SDK documentation](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/>).

> ![success](/docs/images/tick.svg)
> 
> See this [sample iOS app](<https://github.com/rudderlabs/rudder-sdk-ios/blob/develop/Examples/RudderSampleAppObjC/RudderSampleAppObjC/_AppDelegate.m>) for more information on initializing the SDK.

## Step 2: Instrument API calls

All RudderStack mobile SDKs follow a [standard event spec](<https://www.rudderstack.com/docs/event-spec/standard-events/>). It helps you plan your event data and supports various API calls for tracking your mobile app events - these include `identify`, `track`, `screen`, `group`, `alias`, and `reset` calls.

In addition, the mobile SDKs track the following [application lifecycle events](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/>) automatically:

  * [`Application Installed`](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/#application-installed>)
  * [`Application Updated`](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/#application-updated>)
  * [`Application Opened`](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/#application-opened>)
  * [`Application Backgrounded`](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/#application-backgrounded>)


Most users start by implementing `track` and `identify` calls.

You can use **`track` calls** to record user activities like adding a product to a cart or wishlist, tapping a button on the app, selecting an option, etc. You can describe the `track` events with [propertiesProperties are additional contextual information you can add to a `track` call to further describe the action a user takes. ](</docs/resources/glossary/#properties>).

Here is an example of a `track` call named `Product Added`. The properties are `price` and `quantity`:
    
    
    [[RSClient sharedInstance] track:@"Product Added" properties:@{
        @"price" : @"23.99",
        @"quantity" : @"2"
    }];
    

**`identify` calls** are typically fired when a user performs an identifying action like creating an account or making a purchase. `identify` calls also associate a known user with their actions (even if previously anonymous). You can describe users with attributes by adding [traitsTraits are attributes that describe a user. They can be added to an identify call in the `traits` object. Some examples of traits include age, gender, or some specific details - for example, a user’s product plan (free, basic, premium).](</docs/resources/glossary/#traits>) to the payload.

Here is an example of an `identify` call. The `traits` are `firstName`, `lastName`, `email`, and `country`:
    
    
    [[RSClient sharedInstance] identify:@"user_id"
    traits:@{@"firstName": @"Alex",
            @"lastName": @"Keener",
            @"email": @"alex@example.com",
            @"country" : @"US",
    }
    ];
    

See the [RudderStack iOS (Obj-C) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/>) documentation for more information on the other supported API calls.

## Step 3: Verify data flow and connect destination integrations

Once software engineers have installed the SDK and instrumented events, the data team can verify the event flow into RudderStack. Then, they can connect destination integrations to forward events to the tools in their stack automatically.

### 1\. Verify data flow for your iOS (Obj-C) source

Before connecting destinations, verify that events are flowing into RudderStack by checking the **Live Events** viewer in your iOS (Obj-C) source.

To see live events, go to your iOS (Obj-C) source from the **Connections** view and click the **Live Events** button in the top right of your screen.

> ![info](/docs/images/info.svg)
> 
> There will be a delay before you see events in the **Live Events** view. RudderStack doesn’t store any data; it temporarily opens a gateway between the control plane and data plane to show you the live events. The delays usually last only a few seconds but on the [RudderStack Cloud Free](<https://rudderstack.com/pricing/>) plan, they can last up to one minute.

[![Live Events](/docs/images/get-started/quickstart/source-live-events-ios.webp)](</docs/images/get-started/quickstart/source-live-events-ios.webp>)

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

[![Add destination](/docs/images/get-started/quickstart/add-destination.webp)](</docs/images/get-started/quickstart/add-destination.webp>)

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

[![Live Events](/docs/images/get-started/quickstart/source-live-events-ios.webp)](</docs/images/get-started/quickstart/source-live-events-ios.webp>)[![Source live events details](/docs/images/rs-cloud/source-live-events-details.webp)](</docs/images/rs-cloud/source-live-events-details.webp>)

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