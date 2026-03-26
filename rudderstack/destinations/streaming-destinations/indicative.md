# Indicative

Send your event data from RudderStack to Indicative.

* * *

  * __3 minute read

  * 


[Indicative](<https://indicative.com>) is a popular customer analytics platform designed especially for product managers, marketers, and data analysts. It connects directly to your data warehouse, allowing you to have an easy access to your data. As a result, you can also avoid any errors that arise due to data duplication during the collection stage or any form of data mismatch.

RudderStack supports Indicative as a destination to which you can send your event data seamlessly.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/indicative>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Indicative** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the platform supports sending events to Indicative, perform the steps below:

  * From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. From the list of destinations, select **Indicative**.
  * Assign a name to your destination and click **Next**. You should then see the following screen:


[![](/docs/images/indicative.webp)](</docs/images/indicative.webp>)Indicative Connection Settings in RudderStack

### Connection settings

This section lists the settings to be configured to set up Indicative as a destination in RudderStack.

  * **Indicative API Key** : Enter the Indicative **API Key**. It can be found under **Project Settings** in your Indicative account.


## Identify

When an `identify` call is made, RudderStack leverages Indicative’s [Identify Users](<https://support.indicative.com/hc/en-us/articles/360004147512-REST-API-Guide#IdentifyUsers1>) API and sends the data accordingly.

> ![warning](/docs/images/warning.svg)
> 
> A user is identified by `userId`. If the field is not passed in the call, the event is not sent.

A sample `identify` call is as shown:
    
    
    rudderanalytics.identify("hashed_user_id", {
      name: "Name Surname",
      email: "sample@example.com",
    });
    

> ![info](/docs/images/info.svg)
> 
> RudderStack passes the user traits passed along with the `identify` call to Indicative as `properties`.

## Page

When the `page` method is called, RudderStack sends a track event to Indicative with the `userId` and `eventName` parameters.

A sample `page` call is as shown in the snippet below:
    
    
    rudderanalytics.page({
      path: "path",
      url: "url",
      title: "title",
      search: "search",
      referrer: "referrer",
    });
    

## Screen

The `screen` call is the mobile equivalent of the `page`. When called, it sends a `track` event to Indicative with a `userId` and `eventName` .

A sample `screen` call is as shown:
    
    
    [[RSClient sharedInstance] screen:@"Main"];
    

## Track

When the `track` call is made, RudderStack calls Indicative’s [Track Events](<https://support.indicative.com/hc/en-us/articles/360004147512-REST-API-Guide#TrackEvents>) API to send the events. The event properties are sent as data fields in the request, while the name of the event is sent as a custom event.

A sample `track` call is as shown in the snippet below:
    
    
    rudderanalytics.track("Product Reviewed", {
      review_id: "12345",
      product_id: "123",
      rating: 3.0,
      review_body: "Average product, expected much more.",
    });
    

## Alias

When the `alias` call is made, RudderStack calls Indicative’s [Alias Users](<https://support.indicative.com/hc/en-us/articles/360004147512-REST-API-Guide#AliasUsers2>) API and sends the data accordingly.

A sample `alias` call is shown below:
    
    
    rudderanalytics.alias("12345");
    

> ![success](/docs/images/tick.svg)
> 
> The RudderStack SDK automatically passes the user’s `anonymousId` as `previousId` in the payload.

## FAQ

#### Where can I get the Indicative API key?

You can get the Indicative API key under the **Project Settings** section in your Indicative account.