# Rockerbox Cloud Mode Integration

Send events to Rockerbox using RudderStack cloud mode.

* * *

  * __less than a minute

  * 


RudderStack lets you send your event data to Rockerbox via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/rockerbox>).

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you capture user events along with the properties associated with them.

> ![info](/docs/images/info.svg)
> 
> RudderStack supports the `track` call in both the cloud and device modes for the Rockerbox destination. Refer to the [Hybrid mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/rockerbox/setting-up-rockerbox/#hybrid-mode>) for more information.

A sample `track` call is shown below:
    
    
    rudderanalytics.track(
      "Order Completed", {
        revenue: 30,
        currency: "USD",
        user_actual_id: 12345 
      })
    

> ![info](/docs/images/info.svg)
> 
> RudderStack sends all properties of the `track` event to Rockerbox.

The following table lists the **required** properties and their mappings between RudderStack and Rockerbox:

RudderStack property| Rockerbox property  
---|---  
`context.traits.email`/`properties.email`| `email`  
`userId`| `customer_id`  
`event`| `action`  
`timestamp`| `timestamp`  
  
The following table lists the **optional** properties which are pre-defined in Rockerbox and their mappings with RudderStack:

RudderStack property| Rockerbox property  
---|---  
`properties.revenue`| `revenue`  
`properties.order_id`/`orderId`| `orderId`  
`properties.in_store`| `in_store`  
`properties.salesforce`| `salesforce`  
`context.traits.phone`| `phone`  
`properties.products.$.item_list_name`| `item_list_name`  
`properties.products.$.location_id`| `location_id`  
`properties.products.$.promotion_id`| `promotion_id`  
`properties.products.$.promotion_name`| `promotion_name`  
`properties.countryCode`| `country_code`  
`properties.listingId`| `listing_id`