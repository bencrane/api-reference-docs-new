# Monetate

Send your event data from RudderStack to Monetate.

* * *

  * __3 minute read

  * 


[Monetate](<https://monetate.com/>) is a personalization platform that allows you to create unique customer experiences. Its state-of-the-art features allow you to increase customer engagement, boost conversion rates, and improve overall sales.

RudderStack allows you to send your event data from your client-side or server-side components to Monetate. This guide will help you set up, configure, and use Monetate for your project.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/monetate>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Cloud, Warehouse, React Native , Unity, AMP , Flutter, Cordova, Shopify
  * Refer to it as **Monetate** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the platform supports sending events to Monetate, perform the steps below:

  * From your [RudderStack dashboard](<https://app.rudderlabs.com/>), add the source and select **Monetate** from the list of destinations.
  * Name your destination, and click **Next**. You should be able to see the following screen:


[![](/docs/images/image%20%286%29.webp)](</docs/images/image%20%286%29.webp>)Connection Settings for Monetate

  * The connection settings are described in more details below:
    * **Monetate Channel** \- Enter the name of the Monetate channel you would like to send your events to.
    * **Retailer Short Name** \- Your Monetate account’s retailer short name goes here.
  * After filling in these values, click **Next** to complete the setup. Monetate should now be added and enabled as a destination in RudderStack.


## Track

> ![warning](/docs/images/warning.svg)
> 
> This destination does not strictly adhere to the [RudderStack Ecommerce Event Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).

For each `track` call you make, we send the data to Monetate using Monetate’s Engine API.

The table below summarizes the various Monetate events and properties sent by RudderStack:

> ![info](/docs/images/info.svg)
> 
> The Monetate event is sent only if the corresponding RudderStack key is present.

RudderStack Key| Monetate Event| Monetate Event Properties  
---|---|---  
`context.ip`| `monetate:context:IpAddress`| `ipAddress` : `context.ip`  
`"properties.page"` OR `"context.page"`| `monetate:context:PageView`| `url`: `page.url`, `path`: `page.path`, `categories`: [`page.category`], `breadcrumbs`: [`page.breadcrumbs`]  
`context.referrer.url`| `monetate:context:Referrer`| `referrer`: `context.referrer.url`  
`context.screen`| `monetate:context:ScreenSize`| `height`: `context.screen.height`, `width`: `context.screen.width`  
`context.userAgent`| `monetate:context:UserAgent`| `userAgent` : `context.userAgent`  
  
> ![success](/docs/images/tick.svg)
> 
> RudderStack also sends `monetateId` along with the events if you send `monetateId` in the event’s properties.

RudderStack sends an additional event to Monetate for the following ecommerce events :

RudderStack Event| Monetate Event  
---|---  
`Product Viewed`| `monetate:context:ProductDetailView`  
`Product List Viewed`| `monetate:context:ProductThumbnailView`  
`Product Added`| `monetate:context:Cart`  
`Cart Viewed`| `monetate:context:Cart`  
`Order Completed`| `monetate:context:Purchase`  
  
The code snippet below shows a sample `track` call :
    
    
    rudderanalytics.track("Form Submitted", {
      plan: "trial",
      country: "UK",
    })
    

## Screen

For each `screen` call, RudderStack sends the following events to Monetate:

RudderStack Key| Monetate Event| Monetate Event Properties  
---|---|---  
`context.screen`| `monetate:context:ScreenSize`| `height`: `context.screen.height`, `width`: `context.screen.width`  
  
> ![info](/docs/images/info.svg)
> 
> Note that RudderStack sends the Monetate event only if the corresponding RudderStack key is present.

The code snippet below shows a sample `screen` call :
    
    
    [[RudderClient sharedInstance] screen:@"Main"
                properties:@{@"prop_key" : @"prop_value"}];
    

## Page

For each `page` call, RudderStack sends the following events to Monetate:

RudderStack Key| Monetate Event| Monetate Event Properties  
---|---|---  
`"properties.page"` OR `"context.page"`| `monetate:context:PageView`| `url`: `page.url`, `path`: `page.path`, `categories`: [`page.category`], `breadcrumbs`: [`page.breadcrumbs`]  
`context.referrer.url`| `monetate:context:Referrer`| `referrer`: `context.referrer.url`  
  
> ![info](/docs/images/info.svg)
> 
> Note that RudderStack sends the Monetate event only if the corresponding RudderStack key is present.

The code snippet below shows a sample `page` call :
    
    
    rudderanalytics.page("HomePage", {
      path: "/homepage",
      url: "https://example.com/homepage",
    })