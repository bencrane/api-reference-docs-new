# Keen

Send your event data from RudderStack to Keen.

* * *

  * __4 minute read

  * 


[Keen](<https://keen.io/>) is a customer analytics platform that allows you to collect, analyze and get invaluable marketing insights from your customer event data.

RudderStack supports S2S (Server to Server) cloud mode and Web Native SDK for integration with Keen. You can thus send event data attached to Keen collections using RudderStack APIs.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/keen>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Keen** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Keen native SDK from the`https://cdn.jsdelivr.net/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Keen SDK successfully.

## Get started

Once you have confirmed that the platform supports sending events to Keen, perform the steps below:

  * From your [RudderStack dashboard](<https://app.rudderlabs.com/>), add the source. From the list of destinations, select **Keen**.
  * Give a name to the destination and click **Next**. You should then see the following screen:


[![](/docs/images/image%20%2824%29.webp)](</docs/images/image%20%2824%29.webp>)Connection Settings for Keen in RudderStack

  * Please enter the **Project ID** and **Write Key**.
  * You can enable the **Use native SDK to send events** setting to send events via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) through Keen’s native JavaScript SDK.


### Configuring Add-ons

If enabled, RudderStack attaches the following Keen add-ons to the events, which helps in their data enrichment before routing them to Keen:

Add-on| Description  
---|---  
**Geo IP Add On**|  The enriched output will be available under the `ip_geo_info` key.  
**User Agent Add On**|  The enriched output will be available under the `parsed_user_agent` key.  
**URL Parsing Add On**|  The enriched output will be available under the `parsed_page_url` key.  
**Referrer Parsing Add On**|  The enriched output will be available under the `referrer_info` key.  
  
> ![info](/docs/images/info.svg)
> 
> Note: We only pass the IP, page and referrer add-ons to Keen if the event contains a valid `ip`, `page`, `URL` and `referrer` property.

[![](/docs/images/image%20%2838%29.webp)](</docs/images/image%20%2838%29.webp>)Keen add-ons settings in RudderStack

  * Once you have finalized all settings, click **Next** to complete the configuration. Keen will now be added as a destination in RudderStack.


## Identify

Calling `rudderanalytics.identify()` has no effect on Keen whatsoever, when called from the server-side SDKs. However, when called from client-side SDKs, RudderStack calls the Keen `extendEvents`with a user object `userId`and traits passed in from the `identify` call.

Calling `extendEvents` adds the user object to all subsequent`recordEvent` calls to Keen. Hence, to view the `identify` data , you will have to make a subsequent `page` and `track` call from RudderStack.

A sample `identify` call is as shown in the following code snippet:
    
    
    rudderanalytics.identify("my-userID", {
      name: "Tintin",
      city: "Brussels",
      country: "Belgium",
      email: "tintin@herge.com",
    });
    

This will pass the below user to every subsequent event data:
    
    
    user: {
      userId: "my-userID",
      traits: {
        name: "Tintin",
        city: "Brussels",
        country: "Belgium",
        email: "tintin@herge.com"
      }
    }
    

## Page

Calling `rudderanalytics.page()` will pass the `page` properties to the Keen collection `Viewed <category> <name> page`. To learn more about the `page`call, please refer to our [RudderStack Events Specification](<https://www.rudderstack.com/docs/event-spec/standard-events/>) documentation.

A sample `page` call is as shown in the snippet below:
    
    
    // "home" is the name of the page.
    rudderanalytics.page("home", {
      path: "path",
      url: "url",
      title: "title",
      search: "search",
      referrer: "referrer"
    });
    

This will send the following properties to the Keen `Viewed Home Page` collection:

  * `path`
  * `url`
  * `title`
  * `search`
  * `referrer`
  * `userId`
  * `user traits` (If coming from the client SDKs)


## Track

Calling `rudderanalytics.track()` will pass the event properties to Keen on the collection `event-name`. To learn more about the `track`call, please refer to our [RudderStack Events Specification](<https://www.rudderstack.com/docs/event-spec/standard-events/>) documentation.

An example `track` call is as shown:
    
    
    rudderanalytics.track("Track me", {
      category: "category",
      label: "label",
      value: "value",
    });
    

The above call will send the following properties to Keen’s `Track me` collection:

  * `category`
  * `label`
  * `value`
  * `userId`
  * `user traits` (If coming from the client SDKs)


## Screen

The `screen` call records the screen views of the user in your App.

If you have turned on the screen views in your App implementation from the [iOS (Obj-C)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/>) or [Android (Java)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/>) SDK it will be registered in your dashboard. RudderStack forwards the `properties` you’ve passed along with the `screen` call as is.

Here is a sample `screen` call in using RudderStack iOS (Obj-C) SDK:
    
    
    [[RudderClient sharedInstance] screen:@"Main"
                properties:@{@"prop_key" : @"prop_value"}];
    

## FAQ

#### Where do I get the Project ID and Write Key for configuring Keen on RudderStack?

You will find the **Project ID** and **Write Key** by navigating to **Projects** \- (select your project) - **Access** \- **Project Details**.