# Smartly Cloud Mode Integration Beta

Send events to Smartly using RudderStack cloud mode.

* * *

  * __less than a minute

  * 


After you have successfully instrumented Smartly as a destination in RudderStack, follow this guide to correctly send your events to Smartly in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/main/src/cdk/v2/destinations/smartly>).

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) to record user actions along with any associated properties.

A sample `track` call is as shown:
    
    
    rudderanalytics.track(
      "Purchase", {
        adUnitId: "123456789",
        platform: "snapchat",
        adInteractionTime: 1640999520,
        installTime: 1640999825,
        timestamp: 1641000678,
        conversions: 1,
        value: 15,
        currency: "EUR",
      }
    );
    

### Supported mappings

RudderStack maps the following `track` fields to the corresponding Smartly properties:

RudderStack property| Destination property| Data type  
---|---|---  
`event`  
Required| `event_name`| String  
`properties.adUnitId`  
Required| `ad_unit_id`| Number  
`properties.platform`  
Required| `platform`| String  
`properties.adInteractionTime`  
Required| `ad_interaction_time`| UNIX (time in seconds)  
`properties.conversions`  
`properties.products.length`  
`1`| `conversions`| Number  
`properties.value`  
`properties.total`  
`properties.revenue`  
`properties.price*properties.quantity`| `value`| Number  
`properties.installTime`| `install_time`| UNIX (time in seconds)  
`originalTimestamp`  
`timestamp`| `event_time`| UNIX (time in seconds)  
`properties.currency`| `value_currency`| Number