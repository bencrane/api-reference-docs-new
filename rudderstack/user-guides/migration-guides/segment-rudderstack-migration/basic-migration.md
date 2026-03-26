# Phase 1: Basic SDK, Event, and Property migration

Update your SDK, event, and property implementations while migrating from Segment to RudderStack.

* * *

  * __6 minute read

  * 


RudderStack provides a wide range of SDKs for different platforms, including JavaScript, iOS, Android, and server-side languages like Node.js, Python, and Ruby.

This guide covers the process of updating your SDK, events, and properties implementation for web, mobile, and server while migrating from Segment to RudderStack.

## JavaScript SDK

  1. Install the RudderStack JavaScript SDK by including the [JavaScript SDK installation snippet](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/installation/#using-cdn>) in the `<head>` section of your website.


> ![info](/docs/images/info.svg)
> 
> Make sure to replace the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) and [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) with their actual values from the RudderStack dashboard.

  2. Update your `page`, `track`, and `identify` calls to use the RudderStack SDK. RudderStack and Segment calls are nearly identical. Here are a few examples:


    
    
    // Segment
    analytics.identify("user_id", {
      name: "John Doe",
      email: "john@example.com",
      plan: "Premium"
    });
    
    // RudderStack 
    rudderanalytics.identify("user_id", {
      name: "John Doe",
      email: "john@example.com",
      plan: "Premium"
    });
    
    
    
    // Segment
    analytics.page();
    
    // RudderStack 
    rudderanalytics.page();
    
    
    
    // Segment
    
    analytics.track("Order Completed", {
      order_id: "12345",
      revenue: 99.95,
      shipping_method: "FedEx"
    });
    
    // RudderStack 
    
    rudderanalytics.track("Order Completed", {
      order_id: "12345",
      revenue: 99.95,
      shipping_method: "FedEx"
    });
    

  3. After implementing your calls, verify that the data flows correctly by checking the **Live Events** tab in your [RudderStack dashboard](<https://app.rudderstack.com/>). You should see events appearing in real time as users interact with your website.


## iOS (Obj-C)/Android (Java) SDK

The native iOS (Obj-C) or Android (Java) SDK implementations can be migrated similarly and the calls will be very similar to Segment as well.

> ![info](/docs/images/info.svg)
> 
> Your [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) changes per source but your [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) stays the same.

**Example for iOS**

  1. Install the [RudderStack iOS (Obj-C) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/>) as follows:


    
    
    RSConfigBuilder *builder = [[RSConfigBuilder alloc] init];
    [builder withDataPlaneUrl:"DATA_PLANE_URL"];
    [RSClient getInstance:"WRITE_KEY" config:[builder build]];
    
    
    
    RSConfigBuilder *builder = [[RSConfigBuilder alloc] init];
    [builder withDataPlaneUrl:"DATA_PLANE_URL"];
    [RSClient getInstance:"WRITE_KEY" config:[builder build]];
    

> ![info](/docs/images/info.svg)
> 
> Replace the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) and [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) with their actual values from the RudderStack dashboard.

  2. Implement `identify` and `track` calls in your app as below:


    
    
    RSClient.sharedInstance()?.identify("user_id", traits: [
        "key_1": "value_1",
        "key_2": "value_2",
        "email": "alex@example.com"
    ])
    
    
    
    RSClient.sharedInstance()?.track("user_id", properties: [
        "key_1": "value_1",
        "key_2": "value_2"
    ])
    

  3. Verify the data flow by checking the **Live Events** tab in your [RudderStack dashboard](<https://app.rudderstack.com/>).


> ![success](/docs/images/tick.svg)
> 
> See the RudderStack [Android (Java) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/>) and [iOS (Obj-C) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/>) documentation for detailed implementation and examples.

## Server-side SDKs

RudderStack supports eight different [server-side SDKs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/#server>) that can be implemented similarly to Segment.

**Example for Node.js**

  1. Install the [RudderStack Node.js SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-node-sdk/>) using npm:


    
    
    npm install @rudderstack/rudder-sdk-node
    

  2. Import and initialize the SDK in your Node.js app:


    
    
    const RudderAnalytics = require('@rudderstack/rudder-sdk-node');
    
    const client = new RudderAnalytics(WRITE_KEY, {
      dataPlaneUrl: YOUR_DATA_PLANE_URL,
    
      // More initialization options
    });
    

> ![info](/docs/images/info.svg)
> 
> Replace the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) and [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) with their actual values from the RudderStack dashboard.

  3. Implement `identify` and `track` calls in your server-side code:


    
    
    client.identify({
      userId: "1hKOmRA4GRlm",
      traits: {
        name: "Alex Keener",
        email: "alex@example.com",
        plan: "Free",
        friends: 21,
      },
    })
    
    
    
    client.track({
      userId: "1hKOmRA4GRlm",
      event: "Item Viewed",
      properties: {
        revenue: 19.95,
        shippingMethod: "Premium",
      },
    })
    

  4. Verify the data flow by checking the **Live Events** tab in your [RudderStack dashboard](<https://app.rudderstack.com/>).


## Historical data imports

If you have a significant amount of historical data in your Segment warehouse **and** you are moving warehouses, you should migrate your historical Segment data into your new warehouse (Snowflake, BigQuery, Databricks, etc.) using your preferred ETL tool.

Once data is in your new data warehouse, you can combine SQL tables for a unified historical view of your customer data.

> ![info](/docs/images/info.svg)
> 
> If you are **not** changing data warehouses, you don’t need to set up pipelines.

## Migrate user traits and event properties

When migrating from Segment to RudderStack, follow these steps to ensure that all your custom user traits and event properties are properly mapped and migrated:

  1. Identify the key user traits and event properties that you want to migrate from Segment to RudderStack. The easiest way to do this is to set up [Segment as a source](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/segment/>) in a [RudderStack Tracking Plan](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>).

  2. Create new events in the [RudderStack Data Catalog](<https://www.rudderstack.com/docs/data-governance/data-catalog/events/>):


[![Add new event](/docs/images/data-governance/data-catalog-add-event.webp)](</docs/images/data-governance/data-catalog-add-event.webp>)

  3. Update your RudderStack SDK implementation to use the mapped trait and property names, ensuring your data is correctly structured and labeled in RudderStack.
  4. If you have any downstream destinations or data, consumers that rely on the Segment trait and property names, update their configurations to use the new RudderStack names.
  5. Verify that your user traits and event properties are correctly captured and forwarded by RudderStack by inspecting your live events stream and destination data.


By carefully mapping and migrating your user traits and event properties, you can maintain data consistency and ensure that your downstream systems continue to function as expected.

## Handle custom events and mappings

If your Segment implementation includes custom events or mappings, you can set up Segment as a RudderStack source to import your existing mappings into a RudderStack tracking plan and manage them in the RudderStack data catalog. Otherwise, you must recreate your schema in RudderStack to ensure a seamless migration by following these steps:

  1. Identify any custom events or mappings in your Segment implementation like custom page or screen events, e-commerce events, or user attribute mappings.
  2. For each custom event, create an equivalent event in RudderStack using the `track` method and the appropriate event name and properties. For example:


    
    
    // Segment
    
    analytics.track("Custom Event Name", {
      property1: "value1",
      property2: "value2"
    });
    
    // RudderStack 
    
    rudderanalytics.track("Custom Event Name", {
      property1: "value1",
      property2: "value2"
    });
    

  3. If you have any custom mappings or transformations in Segment like user attribute synchronization or event property renaming, implement them in RudderStack using the JavaScript SDK’s `identify` and `track` methods or by leveraging RudderStack’s server-side transformations.
  4. Test your custom events and mappings thoroughly to ensure that they are being correctly captured and processed by RudderStack.
  5. Update any downstream systems or integrations that rely on the custom events or mappings to use the new RudderStack event names and property structures.


By handling custom events and mappings during the migration process, you can ensure that your data remains consistent and actionable across your entire stack.

## Next steps

[Phase 2: Advanced migration techniques](<https://www.rudderstack.com/docs/user-guides/migration-guides/segment-rudderstack-migration/advanced-migration/>)