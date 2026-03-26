# FullStory Cloud Mode Integration Beta

Send events to FullStory using RudderStack cloud mode.

* * *

  * __2 minute read

  * 


This guide will help you send events to FullStory in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>) using their [Server API](<https://developer.fullstory.com/server/getting-started/>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/main/src/cdk/v2/destinations/fullstory>).

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create a user in FullStory.

RudderStack uses the [Create User](<https://developer.fullstory.com/server/users/create-user/>) endpoint to send user details to FullStory.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      displayName: "Alex",
      email: "alex@example.com",
      country: "US",
    });
    

### Supported mappings

The following table details the mapping between RudderStack and FullStory properties:

RudderStack property| FullStory property  
---|---  
`userId`| `uid`  
`context.traits.email`| `email`  
`context.traits.name`| `display_name`  
`traits`  
`context.traits`| `properties`  
  
## Track

Use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to create object-specific events with the associated details.

RudderStack uses the [Create Events](<https://developer.fullstory.com/server/events/create-events/>) endpoint to send the event details to FullStory.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Order Completed", {
      orderId: "1234567",
      price: "567",
      currency: "USD",
    });
    

### Supported mappings

In addition to the event properties mapped to the FullStory’s `properties`, the following table details the mapping between RudderStack and FullStory properties for the following three objects:

  * `user`
  * `session`
  * `context`


#### **user**

RudderStack property| FullStory property  
---|---  
`userId`| `uid`  
  
#### **session**

RudderStack property| FullStory property  
---|---  
`properties.sessionId`| `id`  
`properties.useMostRecent`| `useMostRecent`  
  
#### **context**

RudderStack property| FullStory property  
---|---  
`context.page.url`| `context.browser.url`  
`context.userAgent`| `context.browser.user_agent`  
`context.page.initial_referrer`| `context.browser.initial_referrer`  
`context.app.name`| `context.mobile.app_name`  
`context.app.version`| `context.mobile.app_version`  
`context.device.manufacturer`| `context.device.manufacturer`  
`context.device.model`| `context.device.model`  
`context.ip`| `context.location.ip_address`  
`properties.latitude`| `context.location.latitude`  
`properties.longitude`| `context.location.longitude`  
`properties.city`| `context.location.city`  
`properties.region`| `context.location.region`  
`properties.country`| `context.location.country`