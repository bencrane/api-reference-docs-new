# Lemnisk Web Device Mode Integration

Send events to Lemnisk using the RudderStack web device mode.

* * *

  * __2 minute read

  * 


RudderStack lets you send your event data to Lemnisk via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) using the native web SDK.

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to to identify a user and associate them to their actions. It also lets you record any traits about them like their name, email, etc.

When you send an `identify` event via Rudderstack, Lemnisk’s [`identify`](<https://lemnisk.gitbook.io/lemnisk-platform-documentation/events/identify>) event is triggered. Lemnisk needs a unique user ID to associate an event with a user. By default, it uses a cookie to identify the user. Optionally, you can also pass a unique user ID in the first parameter of the `identify` call.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("hashed_user_id", {
      name: "Alex Keener",
      email: "alex@example.com",
    })
    

### Property mappings

The following table lists the mappings between the RudderStack and Lemnisk properties:

RudderStack property| Lemnisk property| Data type  
---|---|---  
`userId`  
`anonymousId`  
Required| `userId`| String  
`traits`| `customerProperties`| Object  
  
## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you record the user actions along with any properties associated with them. When you send a `track` call, RudderStack triggers Lemnisk’s [`track`](<https://lemnisk.gitbook.io/lemnisk-platform-documentation/events/track>) event.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Product Reviewed", {
      review_id: "12345",
      product_id: "123",
      rating: 3.0,
      review_body: "Average product, expected much more."
    })
    

### Property mappings

The following table lists the mappings between the RudderStack and Lemnisk properties:

RudderStack property| Lemnisk property| Data type  
---|---|---  
`event`  
Required| `event`| String  
`properties`| `properties`| Object  
  
## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record when a user views a page of your website, along with any optional properties about the page. When you send a `page` call via Rudderstack, Lemnisk’s [`page`](<https://lemnisk.gitbook.io/lemnisk-platform-documentation/events/page>) event is triggered.

A sample `page` call is shown below:
    
    
    rudderanalytics.page("Home")
    

### Property mappings

The following table lists the mappings between the RudderStack and Lemnisk properties:

RudderStack property| Lemnisk property| Data type  
---|---|---  
`name`| `name`| String  
`context.page`  
`properties`| `properties`| Object