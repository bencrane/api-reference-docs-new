# Facebook Pixel Web Device Mode Integration

Send events to Facebook Pixel using RudderStack web device mode.

* * *

  * __10 minute read

  * 


After you have successfully instrumented Facebook Pixel as a destination in RudderStack, follow this guide to correctly send your events to Facebook Pixel in [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).

Find the open source JavaScript SDK code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/FacebookPixel>).

> ![warning](/docs/images/warning.svg)
> 
> **Important: Consent management and privacy compliance**
> 
> Facebook Pixel uses the `fbclid` parameter to identify users on the Facebook platform. This identifier can be considered personal information under privacy laws like CIPA (California Information Privacy Act). Therefore, you must implement proper [consent management](<https://www.rudderstack.com/docs/destinations/streaming-destinations/fb-pixel/setup-guide/#other-settings>) **before** enabling Facebook Pixel tracking to ensure compliance with applicable privacy regulations.
> 
> See the following resources for more information on using RudderStack’s consent management feature:
> 
>   * [Consent Management Overview](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>)
>   * [Consent Management in JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/consent-management/>)
> 


## Page

When you make the `page` call, RudderStack sends the data to Facebook Pixel with the event type as `pageView`. You can also pass properties to `page` \- RudderStack automatically sends these properties along with the event ID to Pixel.

A sample `page` call is as shown:
    
    
    rudderanalytics.page()
    

## Track

The `track` call lets you track custom events as they occur in your web application.

A sample call looks like the following code snippet:
    
    
    rudderanalytics.track("Product Added", {
      order_ID: "123",
      category: "boots",
      product_name: "yellow_cowboy_boots",
      price: 99.95,
      currency: "EUR",
      revenue: 2000,
      value: 3000,
      checkinDate: "Thu Mar 24 2018 17:46:45 GMT+0000 (UTC)",
    })
    

In addition to the above call, a `contentType` in the integrations options can be available. If present, it will precede the default value or dashboard settings of `contentType`.
    
    
    rudderanalytics.track(
      "Product Added",
      {
        order_ID: "123",
        category: "boots",
        product_name: "yellow_cowboy_boots",
        price: 99.95,
        currency: "EUR",
        revenue: 2000,
        value: 3000,
        checkinDate: "Thu Mar 24 2018 17:46:45 GMT+0000 (UTC)",
      },
      {
        "Facebook Pixel": { contentType: "mycustomtype" },
      }
    )
    

> ![info](/docs/images/info.svg)
> 
> String is the only valid data type for the `category` field. However, you can pass an array of string values which will be concatenated using a delimiter (,) before sending the events.

## Standard events

> ![warning](/docs/images/warning.svg)
> 
> This destination does not strictly adhere to the [RudderStack Ecommerce Event Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).

RudderStack maps the event name in the payload to the Facebook standard event before sending it to Facebook Pixel. The properties are sent as the standard events require them. Refer to the [Ecommerce Events Specification](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>) for more information.

RudderStack maps the following events to the Facebook standard events by default:

RudderStack Event| Facebook Standard Event  
---|---  
`Product List Viewed`| `ViewContent`  
`Product Viewed`| `ViewContent`  
`Product Added`| `AddToCart`  
`Order Completed`| `Purchase`  
`Products Searched`| `Search`  
`Checkout Started`| `InitiateCheckout`  
Click **here** to see the full list of supported Facebook standard events  


  * `AddToCart`
  * `AddToWishlist`
  * `AddPaymentInfo`
  * `Lead`
  * `CompleteRegistration`
  * `Contact`
  * `CustomizeProduct`
  * `Donate`
  * `FindLocation`
  * `InitiateCheckout`
  * `Purchase`
  * `Schedule`
  * `Search`
  * `StartTrial`
  * `SubmitApplication`
  * `Subscribe`
  * `ViewContent`


> ![info](/docs/images/info.svg)
> 
> You can use the **RudderStack to Facebook event mappings** [dashboard setting](<https://www.rudderstack.com/docs/destinations/streaming-destinations/fb-pixel/setup-guide/#event-mapping-settings>) to override the default mappings specified in the table above.

Note that:

  * For the `Purchase` standard event, `properties.revenue` is a required field.

  * For the `Products Searched` event, the `query` property must be a string.

  * If you map an event with the `ViewContent` standard event using the RudderStack dashboard setting and don’t send the `products` array in the `message.properties` object:
        
        "properties": {
          "phone": 1-202-555-0146,
          "email": "alex@example.com",
          "category": "clothing",
          "list_id": "1234",
          "testDimension": true,
          "testMetric": true
        }
        

Then, `content_ids` is mapped to `properties.category` value (`clothing` in this case) and `quantity` is set to `1` inside the `contents` object.


The below table elaborates the property mappings between RudderStack and Facebook corresponding to the RudderStack event:

RudderStack event| RudderStack property| Facebook property  
---|---|---  
Product List Viewed| `products.$.product_id`  
`products.$.sku`  
`products.$.id`| `content_ids`  
`category`  
`contentName`  
`currency`  
`value`| `content_category`  
`content_name`  
`currency`  
`value`  
`products.$.product_id`  
`products.$.sku`  
`products.$.id`  
`products.$.quantity`  
`quantity`  
`products.$.price`  
`price`| `contents.id`  
`contents.quantity`  
`contents.item_price`  
Product Viewed| `product_id`  
`sku`  
`id`  
`product_name`  
`name`  
`category`  
`currency`| `content_ids`  
`content_name`  
`content_category`  
`currency`  
`product_id`  
`sku`  
`id`  
`quantity`  
`price`| `contents.id`  
`contents.quantity`  
`contents.item_price`  
Product Added| `product_id`  
`sku`  
`id`  
`product_name`  
`name`  
`currency`| `content_ids`  
`content_name`  
`currency`  
`product_id`  
`sku`  
`id`  
`quantity`  
`price`| `contents.id`  
`contents.quantity`  
`contents.item_price`  
Order Completed| `products.$.product_id`  
`products.$.sku`  
`products.$.id`| `content_ids`  
`contentName`  
`currency`  
`revenue`| `content_name`  
`currency`  
`value`  
`products.$.delivery_category`  
`properties.delivery_category`  
`products.$.product_id`  
`products.$.sku`  
`products.$.id`  
`products.$.quantity`  
`quantity`  
`products.$.price`  
`price`| `contents.delivery_category`  
`contents.id`  
`contents.quantity`  
`contents.item_price`  
Products Searched| `query`  
`product_id`  
`sku`  
`id`  
`category`  
`currency`  
`value`| `search_string`  
`content_ids`  
`content_category`  
`currency`  
`value`  
  
`product_id`  
`sku`  
`id`  
`quantity`  
`price`| `contents.id`  
`contents.quantity`  
`contents.item_price`  
Checkout Started| `products.$.product_id`  
`products.$.sku`  
`products.$.id`| `content_ids`  
`category`  
`currency`  
`revenue`| `content_category`  
`currency`  
`value`  
`products.$.product_id`  
`products.$.sku`  
`products.$.id`  
`products.$.quantity`  
`quantity`  
`products.$.price`  
`price`| `contents.id`  
`contents.quantity`  
`contents.item_price`  
  
> ![info](/docs/images/info.svg)
> 
> In the above table, the default values for the `currency` and `quantity` properties are `USD` and `1` respectively.
> 
> **Fallback behavior** : When both `products[].price` and top-level `price` are present, `products[].price` takes mapping precedence for Facebook’s `contents.item_price` field.

### Other standard events

If you map your event to any of the following Facebook standard events, then RudderStack treats it as a standard event as well:

  * `AddToWishlist`
  * `AddPaymentInfo`
  * `Lead`
  * `CompleteRegistration`
  * `Contact`
  * `CustomizeProduct`
  * `Donate`
  * `FindLocation`
  * `Schedule`
  * `StartTrial`
  * `SubmitApplication`
  * `Subscribe`


## Legacy events

You can map events to the legacy conversion Pixel IDs in the RudderStack dashboard. The events specified in the mapping are sent to Facebook with the mapped Pixel ID.

Note that the conversion events only support `currency` and `value` as their event properties.

## Custom events and properties

RudderStack supports sending custom events and properties to Facebook — it automatically flattens all properties from your event into Facebook’s `custom_data` field.

#### Custom events

You can use custom events to send an event that does not appear in any of the mappings.

A sample custom event is shown below:
    
    
    rudderanalytics.track("Video Watched", {
      // All properties become custom_data
      video_title: "Product Demo",
      video_duration: 120,
      completion_rate: 0.85,
      user_engagement: "high"
    })
    

#### How custom properties work

  * **Automatic processing** : All properties in the `properties` object are included in Facebook’s `custom_data` field.
  * **Property flattening** : RudderStack flattens the properties to match Facebook’s API format.
  * **Reserved exclusions** : Certain properties (`opt_out`, `event_id`, `action_source`) are excluded from custom data.
  * **Special arrays** : Properties like `content_ids` and `contents` are preserved as arrays.


#### Standard event with custom properties

RudderStack also supports sending standard Facebook events along with custom properties. An example is shown below:
    
    
    rudderanalytics.track("Purchase", {
      // Standard ecommerce properties
      revenue: 150.00,
      currency: "USD",
      products: [
        {
          product_id: "PROD_123",
          price: 75.00,
          quantity: 2,
          category: "electronics"
        }
      ],
      
      // Custom properties (sent as custom_data to Facebook)
      customer_segment: "premium",
      campaign_id: "summer_sale_2024",
      store_location: "downtown",
      payment_method: "credit_card",
      discount_applied: 10.00,
      loyalty_points_earned: 150
    })
    

> ![info](/docs/images/info.svg)
> 
> Custom properties are automatically processed and sent to Facebook Pixel. No additional configuration is required beyond setting up your PII handling preferences in the RudderStack dashboard.

## PII handling

The Facebook Pixel integration handles Personally Identifiable Information (PII) based on your [dashboard configuration](<https://www.rudderstack.com/docs/destinations/streaming-destinations/fb-pixel/setup-guide/#pii-properties-settings>) to ensure compliance with privacy regulations.

> ![warning](/docs/images/warning.svg)
> 
> Make sure your PII handling configuration complies with applicable privacy laws and Facebook’s data policies.

Click **here** to see the complete list of PII properties that RudderStack denylists by default.  


  * `email`
  * `firstName`
  * `lastName`
  * `firstname`
  * `lastname`
  * `first_name`
  * `last_name`
  * `gender`
  * `city`
  * `country`
  * `phone`
  * `state`
  * `zip`
  * `postalCode`
  * `birthday`


#### How PII handling works

  * **Detection** : Properties are checked against the default PII list and your custom denylist.

  * **Processing** : PII properties are either:

    * Excluded from the event payload entirely
    * Hashed using SHA-256
    * Included if allowlisted


## Deduplication

Facebook Pixel lets you send events via your web browser and server by leveraging the Conversion API.

Depending on how you send your events with this dual set-up, redundant events may be received by Facebook. Therefore, Facebook tries to [deduplicate events](<https://www.facebook.com/business/help/823677331451951?id=1205376682832142>) coming in to help get accurate representation of your data.

#### `event_id` method (Recommended)

Facebook’s recommended deduplication strategy is to leverage the `event_name` and `event_id` properties. Multiple events coming into Facebook are deduplicated if they meet the following criteria:

  * They are sent within 48 hours of each other
  * They are received by the same Facebook Pixel ID
  * They have the same `event_name`, for example, `Purchase`
  * They have the same `event_id`


> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * The `event_id` must be unique to that specific event and the same for both events coming from the Pixel and Conversion API. For example, the `event_id` could be the purchase order number.
>   * You can set the `event_id` in `traits` , `context.traits` or `properties` object as a unique identifier.
>   * If you don’t set the `event_id`, RudderStack uses `messageId` to map to Facebook’s `eventId`.
> 


The `event_name` will be picked up from the name of the event. For more information on the logic behind the `event_id` deduplication, see the [Facebook documentation](<https://developers.facebook.com/docs/marketing-api/conversions-api/deduplicate-pixel-and-server-events/#event-id-and-event-name---recommended>).

#### `fbp` and `external_id` method (Not Recommended)

For this approach, it is necessary to first send an event from the browser, then from the server. Both events must have the same `event_name`, and the same `fbp` parameter and the same `external_id`.

> ![warning](/docs/images/warning.svg)
> 
> If the browser event is received before the server event and both events have the same `event_name`, `fbp`, and `external_id`, then the server event is discarded.

A few shortcomings of this deduplication method are listed below:

  * This method only works for deduplicating events sent first from the browser and then the server.
  * It will always discard the server event if Facebook identifies a redundant event.
  * There will be no deduplication if two consecutive browser events with the same information are sent to Facebook. The same is true if two server events with the same information are sent to Facebook.


RudderStack maps the `event_name` from the name of the sent event. The `fbp` parameter is taken from the `context.fbp` key-value pair. Finally, the `external_id` will just be the `userId` or `anonymousId` (if `userId` is not present).

For more information on the logic behind the `fbp` and `external_id` deduplication, see the [Facebook documentation](<https://developers.facebook.com/docs/marketing-api/conversions-api/deduplicate-pixel-and-server-events/#fbp-or-external-id>).

## Timestamps

The Facebook Pixel integration uses two timestamp formats:

#### 1\. Event timestamps (`event_time`)

  * **Format** : Unix timestamp (in seconds)
  * **Purpose** : Event occurrence time
  * **Example** : `1597383030`
  * **Validation** : Must be within 7 days of occurrence (62 days for physical store events)


#### 2\. Travel/accommodation date fields

  * **Format** : ISO 8601 without timezone

  * **Purpose** : Specific date/time for travel and accommodation events

  * **Examples** :

    * Date only: `2025-10-09`
    * Date and time: `2025-10-09T14:30:00`
  * **Supported fields** : `checkinDate`, `checkoutDate`, `departingArrivalDate`, `departingDepartureDate`, `returningArrivalDate`, `returningDepartureDate`, `travelEnd`, `travelStart`


#### Automatic timestamp conversion

RudderStack converts ISO 8601 timestamps to Unix seconds for `event_time`, as described below. This setup ensures accurate event tracking and compatibility with Facebook’s Conversions API.

**Timezone handling**

  * **Event Time** : Converted to UTC Unix timestamp
  * **Travel Dates** : ISO 8601 without timezone (treated as UTC)
  * **Validation** : Events must be within 7 days of occurrence


**Best practices**

  * Send timestamps in ISO 8601 format. RudderStack converts them to Unix seconds.
  * Use date-only for travel fields when time is not needed.
  * Ensure timestamps are within Facebook’s time window.
  * Use UTC to avoid timezone issues.


**Error handling**

  * Invalid timestamps are rejected.
  * Events older than 7 days (62 days for physical store) are rejected.
  * Future events beyond 1 minute are rejected.


## Send custom `content_type` field

You can send a custom [`content_type`](<https://developers.facebook.com/docs/meta-pixel/get-started/advantage-catalog-ads#content-type>) field by specifying it in the `properties.content_type` field of your event.

RudderStack sets the value of `content_type` in the following priority order:

  1. It gives the highest priority to `properties.content_type` in your event.
  2. If `properties.content_type` is absent, RudderStack sets the `content_type` to `product` by default, except in the following cases:


**Case 1: If Product List Viewed event is sent**

Scenario| Outcome  
---|---  
Event sent with `products` array| `content_type` is set to `product`  
Event sent without `products` array| `content_type` is set to `product_group`  
  
**Case 2: If Product Viewed event is sent but not mapped in the RudderStack dashboard**

Scenario| Outcome  
---|---  
Event sent with `products` array| `content_type` is set to `product`  
Event sent without `products` array| `content_type` is set to `product_group`  
  
**Case 3: If you send any other event mapped to the View Content standard event in the RudderStack dashboard**

Scenario| Outcome  
---|---  
Event sent with `products` array| `content_type` is set to `product`  
Event sent without `products` array| `content_type` is set to `product_group`  
  
> ![info](/docs/images/info.svg)
> 
> The `content_type` parameter accepts only two values — `product` and `product_group`.

## Validation and error handling

The Facebook Pixel integration validates events and may reject them for the following reasons:

#### Event validation errors

Error| Resolution  
---|---  
Invalid event duration| Events must not be older than 7 days (62 days for physical store), or more than 1 minute in the future  
Invalid product array| `products` must be an array of objects  
Invalid query type| Search queries must be string, number, or boolean  
Invalid revenue| Revenue must be convertible to a number  
Missing required fields| Standard events must not miss required properties