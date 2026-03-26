# Engage Web Device Mode Integration

Send events to Engage using RudderStack web device mode.

* * *

  * __2 minute read

  * 


RudderStack lets you send your event data to Engage via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) using the native web SDK.

Find the open source JavaScript SDK code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/Engage>).

## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call lets you identify a visiting user and associate them to their actions. It also lets you record the traits about them like their name, email address, etc.

RudderStack sends the attributes to Engage as is, using their `identify()` API.

A sample `identify` call is as shown:
    
    
    rudderanalytics.identify("1hKOmRA4el9Z", {
        "email": "alex@example.com"
    })
    

The following table lists the RudderStack event properties and their mappings with the Engage properties/attributes:

RudderStack property| Engage property| Data type  
---|---|---  
`externalId.engageId`, `userId`  
(Required)| `id`| String  
`context.traits`  
(Optional)| `payload`| Object  
  
## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you capture user events along with the properties associated with them.

RudderStack sends the event properties to Engage as is, using their `track()` API.

A sample `track` call is as shown:
    
    
    rudderanalytics.track(
      "Product Added", {
        product_id: "12345",
        product_name: "Pink flowers",
        product_url: "http://www.yourdomain.com/products/pink-flowers",
      })
    

The following table lists the RudderStack event properties and their mappings with the Engage properties/attributes:

RudderStack property| Engage property| Data type  
---|---|---  
`externalId.engageId`, `userId`  
(Required)| `id`| String  
`event`  
(Required)| `event`| String  
`propertes`  
(Optional)| `properties`| Object  
  
## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record your website’s page views with any additional relevant information about the viewed page.

RudderStack sends the page-related information to Engage as is, using their `track()` API.

A sample `page` call is as shown:
    
    
    rudderanalytics.page(
      "Cart",
      "Cart Viewed", {
        title: "new blank page",
        url: "/pages/new"
      }
    );
    

The following table lists the RudderStack event properties and their mappings with the Engage properties/attributes:

RudderStack property| Engage property| Data type  
---|---|---  
`externalId.engageId`, `userId`  
(Required)| `id`| String  
`Visited {Category} {Name} Page`  
(Optional)| `event`| String  
`propertes`  
(Optional)| `properties`| Object