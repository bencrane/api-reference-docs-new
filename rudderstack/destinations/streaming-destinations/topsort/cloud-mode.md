# Topsort Cloud Mode Integration Beta

Send events to Topsort using RudderStack cloud mode.

* * *

  * __2 minute read

  * 


After you have successfully instrumented Topsort as a destination in RudderStack, follow this guide to correctly send your events to Topsort in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/develop/src/v0/destinations/topsort>).

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to capture user events along with the associated properties and send them to Topsort.

A sample `track` call is shown:
    
    
    rudderanalytics.track("Product Added", {
      product_id: "9578257311",
      sku: "8472-998-0112",
      name: "Sample Product"
    })
    

### Default event mappings

By default, RudderStack maps the following [ecommerce events](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>) to the corresponding Topsort events:

RudderStack event| Topsort event  
---|---  
`Order Completed`| `purchases`  
`Product Clicked`  
`Product Added`| `clicks`  
`Product Viewed`  
`Product List Viewed`| `impressions`  
  
Note that you can change these mappings in the RudderStack dashboard using the [Event mapping settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/topsort/setup-guide/#event-mapping-settings>).

### Purchases event mappings

RudderStack maps the following `track` event properties to the corresponding Topsort `purchases` event properties:

RudderStack property| Data type| Topsort property  
---|---|---  
`messageId`  
Required  
Automatically added by RudderStack in the final event payload.| String| `id`  
`timestamp`  
`originalTimestamp`  
Required  
Automatically added by RudderStack in the final event payload.| Datetime| `occuredAt`  
`anonymousId`  
Required| String| `opaqueUserId`  
`products`  
Required| Object| `Items`  
  
#### `Items` object mappings

RudderStack property| Data type| Topsort property  
---|---|---  
`products.$.product_id`  
Required| String| `productId`  
`products.$.price`  
Required| Number| `unitPrice`  
`products.$.quantity`| Integer| `quantity`  
`products.$.vendorId`| String| `vendorId`  
  
### Impressions event mappings

RudderStack maps the following `track` event properties to the corresponding Topsort `impressions` event properties:

RudderStack property| Data type| Topsort property  
---|---|---  
`messageId`  
Required  
Automatically added by RudderStack in the final event payload.| String| `id`  
`timestamp`  
`originalTimestamp`  
Required  
Automatically added by RudderStack in the final event payload.| Datetime| `occuredAt`  
`anonymousId`  
Required| String| `opaqueUserId`  
`properties.resolvedBidId`| String| `resolvedBidId`  
`properties.entity`| Object| `entity`  
`properties.additionalAttribution`| Object| `additionalAttribution`  
`properties.placement`| Object| `placement`  
  
#### `placement` object mappings

RudderStack property| Data type| Topsort property  
---|---|---  
`context.page.path`  
Required| String| `path`  
`properties.position`| Integer| `position`  
`properties.product_id`| String| `productId`  
`properties.query`| String| `searchQuery`  
`properties.pageNumber`| Integer| `page`  
`properties.pageSize`| Integer| `pageSize`  
[`properties.category_id`]| Array| `categoryIds`  
  
### Clicks event mappings

RudderStack maps the following `track` event properties to the corresponding Topsort `clicks` event properties:

RudderStack property| Data type| Topsort property  
---|---|---  
`messageId`  
Required  
Automatically added by RudderStack in the final event payload.| String| `id`  
`timestamp`  
`originalTimestamp`  
Required  
Automatically added by RudderStack in the final event payload.| Datetime| `occuredAt`  
`anonymousId`  
Required| String| `opaqueUserId`  
`properties.resolvedBidId`| String| `resolvedBidId`  
`properties.entity`| Object| `entity`  
`properties.additionalAttribution`| Object| `additionalAttribution`  
`properties.placement`| Object| `placement`  
  
#### `placement` object mappings

RudderStack property| Data type| Topsort property  
---|---|---  
`context.page.path`  
Required| String| `path`  
`properties.position`| Integer| `position`  
`properties.product_id`| String| `productId`  
`properties.query`| String| `searchQuery`  
`properties.pageNumber`| Integer| `page`  
`properties.pageSize`| Integer| `pageSize`  
[`properties.category_id`]| Array| `categoryIds`