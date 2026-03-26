# Kissmetrics

Send your event data from RudderStack to Kissmetrics.

* * *

  * __5 minute read

  * 


[Kissmetrics](<https://www.kissmetrics.io/>) is a product analytics platform to help you increase conversion, as well as drive customer engagement and retention.

RudderStack supports sending your events from cloud mode S2S (Server to Server) and Web Native SDKs by calling our APIs.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/kissmetrics>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Kiss Metrics** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
AMP| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Java)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cloud| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cordova| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Swift)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
React Native| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Shopify| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Unity| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Warehouse| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Kissmetrics native SDK from the`https://kissmetrics.com` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Kissmetrics SDK successfully.

## Get started

Once you have confirmed that Kissmetrics supports the source type, perform the steps below:

  * From your [RudderStack dashboard](<https://app.rudderlabs.com/>), add the source and select **Kissmetrics** as a destination.
  * Give a name to your destination, and then click **Next**. You should see the following screen:

[![](/docs/images/image%20%2824%29%20%281%29%20%281%29.webp)](</docs/images/image%20%2824%29%20%281%29%20%281%29.webp>)

  * Please enter the **API Key** in the **Connection Settings**. You may also enable the **Use native SDK to send events** setting to send events via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>), through Kissmetrics’ native JavaScript SDK.


### Prefix Properties

Enabling this setting will add the event name to all properties of the event. This works for `page` **and** `track` properties.

> ![info](/docs/images/info.svg)
> 
> You will need to enable this setting while building reports in Kissmetrics.

  * Once you have finalized the settings, click **Next** to complete the configuration and add Kissmetrics as a destination in RudderStack.


## Identify

Calling `rudderanalytics.identify()` pushes an `identify` call with the `userId` and `set` with the `user-traits` to the Kissmetrics queue object while using the the Native SDK. For more information on the `identify` call, please refer to our [RudderStack Events Specification](<https://www.rudderstack.com/docs/event-spec/standard-events/>) documentation.

For sending data through the API’s cloud mode, we call the `http://trk.kissmetrics.com/s` end-point for registering users and their traits.

A sample `identify` call is as shown:
    
    
    // a sample identify
    rudderanalytics.identify("my-userID", {
      name: "Tintin",
      city: "Brussels",
      country: "Belgium",
      email: "tintin@herge.com"
    });
    

will pass the following to the `_kmq kissmetrics` object.
    
    
    ['identify', 'my-userID']
    ['set',
      {
        name: "Tintin",
        city: "Brussels",
        country: "Belgium",
        email: "tintin@herge.com"
      }
    ]
    

> ![info](/docs/images/info.svg)
> 
> Nested objects are flattened as `a.b.c` for input data `{a:{b:c}}` before sending the data to Kissmetrics, as it is unable to parse nested objects.

## Page

Calling `rudderanalytics.page()` will record the page properties for event `Viewed <category> <name> page`. For more information on the `page` call, please refer to our [RudderStack Events Specification](<https://www.rudderstack.com/docs/event-spec/standard-events/>) documentation.

A sample page event is as shown:
    
    
    // "home" is the name of the page.
    rudderanalytics.page("home", {
      path: "path",
      url: "url",
      title: "title",
      search: "search",
      referrer: "referrer"
    });
    

The above snippet will pass the following to the `_kmq kissmetrics` object:
    
    
    ['record', 'Viewed home page',  {
      path: "path",
      url: "url",
      title: "title",
      search: "search",
      referrer: "referrer"
    }]
    

> ![info](/docs/images/info.svg)
> 
> Automatically-tracked Kissmetrics events such as **Visited a site** , etc. will function as and when integrated with RudderStack. Stay tuned!

## Track

Calling `rudderanalytics.track()` pushes a record with the event name and the associated properties __when using the native SDK integration. For more information on the `track` call, please refer to our [RudderStack Events Specification](<https://www.rudderstack.com/docs/event-spec/standard-events/>) documentation.

For sending data through the API’s cloud mode, we call the <http://trk.kissmetrics.com/e> end-point for registering the event and its associated properties.

A sample `track` call is as shown:
    
    
    rudderanalytics.track("Track me", {
      category: "category",
      label: "label",
      value: "value",
    });
    

will pass the following to the `_kmq kissmetrics` object.
    
    
    ['record', "Track me", {
      category: "category",
      label: "label",
      value: "value"
    }]
    

An event sent to RudderStack with a property called `revenue` , is passed on to Kissmetrics as `Billing amount` as well as `revenue`.

> ![info](/docs/images/info.svg)
> 
> In order to send ecommerce events that have a product array as one of their `track` properties, RudderStack sends each product property to the `/s` endpoint from cloud mode, or pushes it as `['set', {id:, sku: ...}]` from the native SDK.

## Alias

Calling `rudderanalytics.alias()` passes an `alias`call with `userId` and `previousId` to the Kissmetrics queue, when used as a Native SDK integration.

While passing data using cloud mode, we call the <http://trk.kissmetrics.com/a> endpoint to alias user identities.

The following code snippet shows a sample `alias` call in RudderStack:
    
    
    // assuming the previous set userId was "my-userID"
    rudderanalytics.alias("my-new-userID");
    

will pass the following to the `_kmq kissmetrics` object.
    
    
    ['alias', "my-new-userID", "userId"]
    

## Screen

The `screen` call records the screen views of the user in your App. If you have turned on the screen views in your App implementation from the [iOS (Obj-C)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/>) or [Android (Java)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/>) SDK it will register in your dashboard. RudderStack forwards the `properties` you’ve passed along with the `screen` call as is.

Here is a sample `screen` call in using RudderStack iOS (Obj-C) SDK:
    
    
    [[RudderClient sharedInstance] screen:@"Main"
                properties:@{@"prop_key" : @"prop_value"}];
    

## FAQ

#### Where do I get the API Key for Kissmetrics?

You can obtain the Kissmetrics API Key by logging into your Kissmetrics account, and navigating to the **Product Settings**. Please refer to the following screenshot for more details:

[![](/docs/images/image%20%2813%29%20%282%29.webp)](</docs/images/image%20%2813%29%20%282%29.webp>)Kissmetrics API Key