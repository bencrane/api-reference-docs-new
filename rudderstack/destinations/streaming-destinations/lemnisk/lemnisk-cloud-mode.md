# Lemnisk Cloud Mode Integration

Send events to Lemnisk using the RudderStack cloud mode.

* * *

  * __2 minute read

  * 


RudderStack lets you send your event data to Lemnisk via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/lemnisk>).

RudderStack supports sending data to the following Lemnisk platforms:

  * DIAPI
  * Pixel Listener


## DIAPI

When you choose to send events to Lemnisk via the server-side cloud mode, RudderStack uses Lemnisk’s [HTTP API](<https://lemnisk.gitbook.io/lemnisk-platform-documentation/sources/http-api>) to send your website or app data.

### Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you record the user actions along with any properties associated with them.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Product Reviewed", {
      review_id: "12345",
      product_id: "123",
      rating: 3.0,
      review_body: "Average product, expected much more."
    })
    

#### Property mappings

The following table lists the mappings between the RudderStack and Lemnisk properties:

RudderStack property| Lemnisk property| Data type  
---|---|---  
`userId`  
`anonymousId`  
Required| `userId`| String  
`properties`| `properties`| Object  
`event`| `eventname`| String  
`config.srcid`| `srcId`| String  
`config.diapiWriteKey`| `writekey`| String  
  
## Pixel Listener

When you choose to send events to Lemnisk via the web cloud mode, RudderStack uses Lemnisk’s [JavaScript SDK](<https://lemnisk.gitbook.io/lemnisk-platform-documentation/sources/javascript-sdk>) to send data from your website.

### Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to identify a user and associate them to their actions. It also lets you record any traits about them like their name, email, etc.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("hashed_user_id", {
      name: "Alex Keener",
      email: "alex@example.com",
    })
    

#### Property mappings

The following table lists the mappings between the RudderStack and Lemnisk properties:

RudderStack property| Lemnisk property| Data type  
---|---|---  
`userId`  
`anonymousId`  
Required| `userId`  
`id`| String  
`context`  
Required| `context`| Object  
`traits`  
Required| `customerProperties`| Object  
`messageId`  
Required| `messageId`| String  
  
### Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you record the user actions along with any properties associated with them.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Product Reviewed", {
      review_id: "12345",
      product_id: "123",
      rating: 3.0,
      review_body: "Average product, expected much more."
    })
    

#### Property mappings

The following table lists the mappings between the RudderStack and Lemnisk properties:

RudderStack property| Lemnisk property| Data type  
---|---|---  
`userId`  
`anonymousId`  
Required| `userId`  
`id`| String  
`event`  
Required| `event`| String  
`properties`| `properties`| Object  
`timestamp`  
Required| `originalTimestamp`| String  
`messageId`  
Required| `messageId`| String  
`context`  
Required| `context`| Object  
`properties`| `properties`| Object  
  
### Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record when a user views a page of your website, along with any optional properties about the page.

A sample `page` call is shown below:
    
    
    rudderanalytics.page("Home")
    

#### Property mappings

The following table lists the mappings between the RudderStack and Lemnisk properties:

RudderStack property| Lemnisk property| Data type  
---|---|---  
`userId`  
`anonymousId`  
Required| `userId`  
`id`| String  
`name`  
Required| `name`| String  
`timestamp`  
Required| `originalTimestamp`| String  
`messageId`  
Required| `messageId`| String  
`context`  
Required| `context`| Object  
`properties`| `properties`| Object