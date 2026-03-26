# X Pixel Web Device Mode Integration Beta

Send events to X Pixel using RudderStack web device mode.

* * *

  * __2 minute read

  * 


After you have successfully instrumented X Pixel as a destination in RudderStack, follow this guide to correctly send your events to X Pixel in [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to record user actions along with any associated properties.

A sample `track` call is as shown:
    
    
    rudderanalytics.track(
      "Purchase", {
        conversionId: 'transactionId',
        value: 35.0,
        currency: 'GBP'
      })
    

### Supported mappings

The following table lists the mappings between RudderStack and X Pixel properties:

RudderStack property| X Pixel property| Data Type| Description  
---|---|---|---  
`properties.value`  
`properties.price`  
`properties.revenue`| `value`| Integer or Float| Total value of the conversion event. For example, $ value of the transaction in case of a purchase, LTV value of a lead, etc.  
`properties.currency`| `currency`| String| ISO 4217 currency code. For example, `USD`, `JPY`, `EUR`, `GBP`, etc.  
`properties.conversionId`  
`conversion_id`| `conversion_id`| String| Unique identifier for the event that can be used for deduplication purposes.  
`properties.searchString`  
`search_string`| `search_string`| String| Text that users search for on your website.  
`properties.description`| `description`| String| String description for additional information.  
`properties.twclid`| `twclid`| String| X click ID that you can include with any request. X Pixel automatically passes `twclid` from the URL or first-party cookie. You can use this parameter optionally to force attribution to a certain ad click.  
`properties.status`| `status`| String| Status of user sign up or subscription. Allowed values are `started` or `completed`.  
`properties.contents`| `contents`| Array of objects| Array of JSON objects representing products or content.  
  
See below table for sub-parameters that you can include in the array.  
  
The following table lists the mappings between `properties.contents` (from `properties.products` object) fields and X Pixel fields:

`properties.contents` field| X Pixel field| Data type| Description  
---|---|---|---  
`type`| `content_type`| String| Category of the purchased product. See [Google product taxonomy)](<https://www.google.com/basepages/producttype/taxonomy.en-US.txt>) for the detailed list.  
`id`| `content_id`| String| Pass the SKU value for the product catalog users.  
  
For all other users, pass the Global Trade Item Number (GTIN) value (if available). Otherwise, pass the SKU value.  
`name`| `content_name`| String| Name of the product or service.  
`price`| `content_price`| Integer or Float| Price of the product or service.  
`quantity`| `num_items`| Integer| Number of products purchased.  
`groupId`| `content_group_id`| String| ID associated with a group of product variants.  
  
## Page

You can use the [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call to record your website’s page views with any additional information about the viewed page. X Pixel automatically fetches all the page-related properties.

A sample `page` call is shown below:
    
    
    rudderanalytics.page();