# Bloomreach Cloud Mode Integration Beta

Send events to Bloomreach using RudderStack cloud mode.

* * *

  * __3 minute read

  * 


After you have successfully instrumented Bloomreach as a destination in RudderStack, follow this guide to correctly send your events to Bloomreach in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>). RudderStack uses Bloomreach’s [batch commands API](<https://documentation.bloomreach.com/engagement/reference/batch-commands-2>) which supports up to 50 commands/calls in a batch.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/main/src/cdk/v2/destinations/bloomreach>).

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create or update customer properties in Bloomreach.

A sample `identify` call is shown:
    
    
    rudderanalytics.identify("27340af5c8819", {
      name: "Alex Keener",
      email: "alex@example.com",
      logins: 2
    })
    

### Supported mappings

RudderStack maps the following properties to the corresponding Bloomreach properties:

RudderStack property| Bloomreach property  
---|---  
`userId`  
Required, if anonymousId is absent.| Hard ID (mentioned in the RudderStack dashboard setting)  
`anonymousId`  
Required, if userId is absent.| Soft ID (mentioned in the RudderStack dashboard setting)  
`traits`| `properties`  
`timestamp`  
`originalTimestamp`| `update_timestamp`  
  
## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to capture user events along with the associated properties.

A sample `track` call is shown:
    
    
    rudderanalytics.track("Product Reviewed", {
      review_id: "86ac1cd43",
      product_id: "9578257311",
      rating: 3.0,
      review_body: "OK for the price. It works but the material feels flimsy."
    })
    

### Supported mappings

RudderStack maps the following properties to the corresponding Bloomreach properties:

RudderStack property| Bloomreach property  
---|---  
`userId`  
Required, if anonymousId is absent.| Hard ID (mentioned in the RudderStack dashboard setting)  
`anonymousId`  
Required, if userId is absent.| Soft ID (mentioned in the RudderStack dashboard setting)  
`event`  
Required| `event_type`  
`properties`| `properties`  
`timestamp`  
`originalTimestamp`| `timestamp`  
  
## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record your website’s page views with any additional relevant information about the viewed page.

A sample `page` call is shown:
    
    
    rudderanalytics.page("Home")
    

### Supported mappings

RudderStack maps the following properties to the corresponding Bloomreach properties:

RudderStack property| Bloomreach property  
---|---  
`userId`  
Required, if anonymousId is absent.| Hard ID (mentioned in the RudderStack dashboard setting)  
`anonymousId`  
Required, if userId is absent.| Soft ID (mentioned in the RudderStack dashboard setting)  
`Viewed {{ category }} {{ name }} Page`  
Required| `event_type`  
`properties`| `properties`  
`timestamp`  
`originalTimestamp`| `timestamp`  
  
## Screen

You can use the [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to record whenever a user views their mobile screen and capture any properties about the viewed screen.

A sample `screen` call is shown:
    
    
    [
      [RSClient sharedInstance] screen: @ "Main"
      properties: @ {
        @ "title": "Home | RudderStack",
          @ "url": @ "http://www.rudderstack.com"
      }
    ];
    

### Supported mappings

RudderStack maps the following properties to the corresponding Bloomreach properties:

RudderStack property| Bloomreach property  
---|---  
`userId`  
Required, if anonymousId is absent.| Hard ID (mentioned in the RudderStack dashboard setting)  
`anonymousId`  
Required, if userId is absent.| Soft ID (mentioned in the RudderStack dashboard setting)  
`Viewed {{ category }} {{ name }} Screen`  
Required| `event_type`  
`properties`| `properties`  
`timestamp`  
`originalTimestamp`| `timestamp`  
  
## Send multiple hard and soft IDs

Bloomreach supports multiple hard and soft IDs which you can use for customer identification and profile merging.

If you want to send multiple hard and soft IDs, apart from setting one in the RudderStack dashboard, you can send them in the `integrations` object as shown:
    
    
    {
      All: true,
      BLOOMREACH: {
        hardID: {"test_key": "value"}
        softID: {google_analytics: "test_id1", "other_id": "test_id2"}
      },
    };