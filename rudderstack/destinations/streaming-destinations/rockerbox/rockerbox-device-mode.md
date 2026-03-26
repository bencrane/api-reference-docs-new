# Rockerbox Web Device Mode Integration

Send events to Rockerbox using RudderStack web device mode.

* * *

  * __2 minute read

  * 


RudderStack lets you send your event data to Rockerbox via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) using the native web SDK.

Find the open source JavaScript SDK code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/Rockerbox>).

## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call lets you identify a visiting user and associate them to their actions. It also lets you record the traits about them like their name, email address, etc.

A sample `identify` call is as shown:
    
    
    rudderanalytics.identify("1hKOmRA4el9Z", {
        "email": "alex@example.com"
    })
    

The following table lists the **optional** properties and their mappings between RudderStack and Rockerbox:

RudderStack property| Rockerbox property  
---|---  
`userId`| `external_id`  
`traits.email`/`context.traits.email`| `email`  
`traits.phone`/`context.traits.phone`| `phone_number`  
  
> ![info](/docs/images/info.svg)
> 
> The `userId` is the ID for a logged-in user. It is a first-party identifier that persists across sessions. A unique user ID is essential in a conversion pixel for capturing the new or returning user’s data. You can include as many user identifiers but only the first-party identifier should be passed to Rockerbox as `external_id`.

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you capture user events along with the properties associated with them.

> ![info](/docs/images/info.svg)
> 
> RudderStack supports the `track` call in both the cloud and device modes for Rockerbox integration. Refer to the [Hybrid mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/rockerbox/setting-up-rockerbox/#hybrid-mode>) for more information.

A sample `track` call is as shown:
    
    
    rudderanalytics.track(
      "Product Added", {
        product_id: "00000",
        product_name: "Pink bolognas",
        product_url: "http://www.yourdomain.com/products/pink-bolognas",
      })
    

## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record your website’s page views with any additional relevant information about the viewed page.

The `page` call sends a `RB.track("view")` event to Rockerbox by default, along with any additional properties.

A sample `page` call is as shown:
    
    
    rudderanalytics.page(
      "Cart",
      "Cart Viewed", {
        title: "new blank page",
        url: "/pages/new"
      }
    );