# Facebook Conversions Cloud Mode Integration

Send events to Facebook Conversions using RudderStack cloud mode.

* * *

  * __10 minute read

  * 


RudderStack supports sending event data to Facebook Conversions only in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

## Page

RudderStack sends the [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call to Facebook Pixel with the event type as `pageView`.

You can also pass properties in your `page` call - RudderStack automatically sends them along with the event ID to Facebook.

A sample `page` call is shown:
    
    
    rudderanalytics.page()
    

## Track

> ![warning](/docs/images/warning.svg)
> 
> This destination does not strictly adhere to the [RudderStack Ecommerce Event Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to custom events as they occur in your web application.

A sample `track` call is shown:
    
    
    rudderanalytics.track("Product Added", {
      order_ID: "123",
      category: "boots",
      product_name: "pink_boots",
      price: 49.99,
      currency: "EUR",
      checkinDate: "Thu Mar 24 2018 17:46:45 GMT+0000 (UTC)",
    })
    

## `data` object format

Whenever you make a `track` call, RudderStack sends a request to Facebook’s `/events` endpoint with a `data` object.

A sample `data` object is shown:
    
    
    data = [{
      "event_name": "Product Purchased",
      "event_time": 1697553987,
      "user_data": {
        "em": [
          "309a0a5c3e211326ae75ca18196d301a9bdbd1a882a4d2569511033da23f0abd"
        ],
        "ph": [
          "254aa248acb47dd654ca3ea53f48c2c26d641d23d7e2e93a1ec56258df7674c4",
          "6f4fcb9deaeadc8f9746ae76d97ce1239e98b404efe5da3ee0b7149740f89ad6"
        ],
        "client_ip_address": "<ip>",
        "client_user_agent": "$CLIENT_USER_AGENT",
        "fbc": "fb.1.1554763741205.AbCdEfGhIjKlMnOpQrStUvWxYz1234567890",
        "fbp": "fb.1.1558571054389.1098115397"
      },
      "custom_data": {
        "currency": "USD",
        "value": 123.45,
        "contents": [{
          "id": "product123",
          "quantity": 1,
          "delivery_category": "home_delivery"
        }]
      },
      "event_source_url": "http://example.com/product/123",
      "action_source": "website"
    }]
    

The `data` object has the following parts:

### Common data

The common data parameters are set at the root level of the `data` object sent as a part of the event payload.

The following table lists the mappings between the RudderStack properties and the Facebook properties included in `common_data`:

RudderStack property| Facebook property  
---|---  
`event`  
Required| `event_name`  
`timestamp`  
`originalTimestamp`  
Required| `event_time`  
`context.page.url`  
`properties.url`| `event_source_url`  
`traits.opt_out`  
`context.traits.opt_out`  
`properties.opt_out`| `opt_out`  
`traits.event_id`  
`context.traits.event_id`  
`properties.event_id`  
`messageId`| `event_id`  
`traits.action_source`  
`context.traits.action_source`  
`properties.action_source`| `action_source`  
  
> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * If your event does not contain any of `traits.action_source`, `context.traits.action_source`, or `properties.action_source`, then RudderStack falls back to the value specified in the **Action Source** dashboard setting.
>   * Do not set `action_source` to any value other than the following - otherwise you will get a **Invalid Action Source type** error:
>     * `email`
>     * `website`
>     * `phone_call`
>     * `chat`
>     * `physical_store`
>     * `system_generated`
>     * `app`, and
>     * `other`
> 


### User data

The following table lists the mappings between the RudderStack properties and the Facebook properties included in `user_data`:

RudderStack property| Facebook property| Hashing needed?  
---|---|---  
`userId`  
`traits.userId`  
`context.traits.userId`  
`traits.id`  
`context.traits.id`  
`anonymousId`  
Required| `externalId`| Yes  
`traits.email`  
`context.traits.email`| `em`| Yes  
`traits.phone`  
`context.traits.phone`| `ph`| Yes  
`traits.gender`  
`context.traits.gender`| `ge`| Yes  
`traits.birthday`  
`context.traits.birthday`| `db`| Yes  
`traits.lastname`  
`traits.lastName`  
`traits.last_name`  
`context.traits.lastname`  
`context.traits.lastName`  
`context.traits.last_name`| `ln`| Yes  
`traits.firstname`  
`traits.firstName`  
`traits.first_name`  
`context.traits.firstname`  
`context.traits.firstName`  
`context.traits.first_name`| `fn`| Yes  
`traits.name`  
`context.traits.name`| `name`| -  
`traits.address.city`  
`context.traits.address.city`| `ct`| Yes  
`traits.address.state`  
`context.traits.address.state`| `st`| Yes  
`traits.address.zip`  
`context.traits.address.zip`| `zp`| Yes  
`traits.address.country`  
`context.traits.address.country`| `country`| Yes  
`context.ip`  
`request_up`| `client_ip_address`| -  
`context.userAgent`| `client_user_agent`| -  
`context.fbc`| `fbc`| -  
`context.fbp`| `fbp`| -  
`context.subscription_id`| `subscription_id`| -  
`context.lead_id`| `lead_id`| -  
`context.fb_login_id`| `fb_login_id`| -  
`context.device.advertisingId`| `madId`| -  
`properties.anon_id`  
`context.device.advertisingId`| `anon_id`| -  
  
After the payload is formed, Facebook checks if `name` field exists. If yes, it is split into `fn` and `ln` fields. Facebook does not hash the values of `user_data` parameters if you send an `integrations` object in your event as below:
    
    
    "integrations": {
      "fb_conversions": {
        "hashed": true
      }
    }
    

> ![info](/docs/images/info.svg)
> 
> RudderStack accepts any of the following names for Facebook Conversions in the `integrations` object:
> 
>   * `fb_conversions`
>   * `fb conversions`
>   * `FacebookConversions`
>   * `Facebook Conversions`
>   * `FB Conversions`
>   * `Facebook_Conversions`
> 


### Custom data

RudderStack flattens the `custom_data` object before sending it Facebook along with the `user_data` and `common_data` fields in the `data` object.

Note that:

  * RudderStack sends the properties present in `custom_data` as is, without any change.
  * It also excludes `opt_out`, `event_id`, and `action_source` from the event properties.


The following table explains how RudderStack maps and sets the properties in the specific Facebook fields:

> ![warning](/docs/images/warning.svg)
> 
> Each of the below parameters are applicable/valid only for certain events.
> 
> See Standard events mapping for more information on the properties mapped for each Facebook property according to the event.

RudderStack property| Facebook property  
---|---  
Array of product IDs from `properties.products` like `product.product_id`, `product.sku`, `product.id`.| `content_ids`  
Array of object containing `id`, `quantity`, and `item_price` formed for each product in `properties.products`.| `contents`  
`properties.content_type`| `content_type`  
`properties.category`| `content_category`  
  
  * `properties.content_name` or `properties.contentName` if `properties.products` array is **not** present.
  * `properties.name` or `properties.product_name` if `properties.products` array is present.

| `content_name`  
`properties.currency` \- defaulted to `USD` if no value is present.| `currency`  
`properties.revenue`  
`properties.value`  
`properties.price`  
`properties.total`| `value`  
`content_ids.length`| `num_items`  
`properties.query`| `search_string`  
  
Note that `content_category` must be of type String. For more information on this field, see [Facebook developer documentation](<https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/custom-data>).

  * If `content_category` is passed as an array, RudderStack merges the array elements as a comma-separated string.
  * If `content_category` is passed as an object, RudderStack throws an error: `"Category must be must be a string."`


### Allowlist/denylist PII

Facebook identifies the following standard fields as PII:

  * `email`
  * `firstName`
  * `lastName`
  * `first_name`
  * `last_name`
  * `gender`
  * `city`
  * `country`
  * `phone`
  * `state`
  * `zip`
  * `birthday`


> ![info](/docs/images/info.svg)
> 
> The PII allowlist/denylist checks (configurable via the [Event mapping settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/fb-conversions/setup-guide/#pii-properties>)) apply only to the standard Facebook PII fields listed above. They **do not affect** any other properties or top-level RudderStack identifiers like `anonymousId` or `userId`.

If any of the above PII properties are present in an event, RudderStack checks whether they are allowlisted or denylisted in the dashboard settings, and processes them accordingly:

  * If the property is not allowlisted, RudderStack drops it.

  * If the property is denylisted, RudderStack checks if the [Hash Denylist PII Property](<https://www.rudderstack.com/docs/destinations/streaming-destinations/fb-conversions/setup-guide/#pii-properties>) toggle is enabled in the dashboard:

    * If the toggle is disabled, RudderStack drops the property
    * If the toggle is enabled, RudderStack hash-encrypts the property before sending it to Facebook


As mentioned above, if you send an `integrations` object within your event with `hashed` set to `true`, RudderStack does not hash the property again.
    
    
    "integrations": {
      "fb_conversions": {
        "hashed": true
      }
    }
    

### App data

> ![info](/docs/images/info.svg)
> 
> RudderStack includes this data only if `action_source` in the `data object` is set to `app`.

The following table lists the mappings between the RudderStack properties and the Facebook properties:

RudderStack property| Facebook property  
---|---  
`a2` if `context.device.type` = `android`  
`i2` if `context.device.type` = `ios`  
Required| `extinfo.0`  
`context.device.adTrackingEnabled`  
Required| `advertiser_tracking_enabled`  
`context.os.version`  
Required| `extinfo.4`  
`properties.application_tracking_enabled`  
Required| `application_tracking_enabled`  
`anonymousId`| `user_data.anon_id`  
`context.app.namespace`| `extinfo.1`  
`context.app.build`| `extinfo.2`  
`context.app.version`| `extinfo.3`  
`context.device.model`| `extinfo.5`  
`context.device.advertisingId`| `user_data.madid`  
`context.locale`| `extinfo.6`  
`context.abv_timezone`| `extinfo.7`  
`context.network_carrier`| `extinfo.8`  
`context.screen_width`| `extinfo.9`  
`context.screen_height`| `extinfo.10`  
`context.screen_density`| `extinfo.11`  
`context.cpu_cores`| `extinfo.12`  
`context.ext_storage_size`| `extinfo.13`  
`context.avl_storage_size`| `extinfo.14`  
`context.timezone`| `extinfo.15`  
`properties.campaignId`  
`context.traits.campaignId`  
`context.campaign.name`| `campaign_ids`  
`properties.install_referrer`| `install_referrer`  
`properties.installer_package`| `installer_package`  
`properties.url_schemes`| `url_schemes`  
`properties.windows_attribution_id`| `windows_attribution_id`  
  
## Standard events mapping

RudderStack maps the following events to the Facebook standard events by default:

RudderStack Event| Facebook Standard Event  
---|---  
`Checkout Started`| `InitiateCheckout`  
`Order Completed`| `Purchase`  
`Product Added`| `AddToCart`  
`Product Added to Wishlist`| `AddToWishlist`  
`Payment Info Entered`| `AddPaymentInfo`  
`Product List Viewed`| `ViewContent`  
`Products Searched`| `Search`  
`Product Viewed`| `ViewContent`  
  
> ![info](/docs/images/info.svg)
> 
> You can also use the [Custom Event Mapping](<https://www.rudderstack.com/docs/destinations/streaming-destinations/fb-conversions/setup-guide/#event-mapping>) dashboard setting to override the above default mappings.

See the [Ecommerce Events Specification](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>) for more information on the above events.

Note that:

  * For the `Purchase` standard event (mapped to `Order Completed` event), `properties.revenue` is a required field. Also, RudderStack sends the `delivery_category` field along with `id`, `item_price` and `quantity` as a part of the `custom_data.contents` object.

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
Checkout Started| `products.$.product_id/products.$.sku/products.$.id`| `content_ids`  
`category`  
`currency`  
`revenue`| `content_category`  
`currency`  
`value`  
`products.$.product_id/products.$.sku/products.$.id`  
`products.$.quantity/quantity`  
`product.$.price/price`| `contents.id`  
`contents.quantity`  
`contents.item_price`  
Product List Viewed| `products.$.product_id/products.$.sku/products.$.id`| `content_ids`  
`category`  
`contentName`  
`currency`  
`value`| `content_category`  
`content_name`  
`currency`  
`value`  
`products.$.product_id/products.$.sku/products.$.id`  
`products.$.quantity/quantity`  
`product.$.price`| `contents.id`  
`contents.quantity`  
`contents.item_price`  
Product Viewed| `product_id/sku/id`  
`product_name/name`  
`category`  
`currency`| `content_ids`  
`content_name`  
`content_category`  
`currency`  
`product_id/sku/id`  
`quantity`  
`price`| `contents.id`  
`contents.quantity`  
`contents.item_price`  
Product Added| `product_id/sku/id`  
`product_name/name`  
`currency`| `content_ids`  
`content_name`  
`currency`  
`product_id/sku/id`  
`quantity`  
`price`| `contents.id`  
`contents.quantity`  
`contents.item_price`  
Order Completed| `products.$.product_id/products.$.sku/products.$.id`| `content_ids`  
`contentName`  
`currency`  
`revenue`| `content_name`  
`currency`  
`value`  
`products.$.delivery_category`/`properties.delivery_category`  
`products.$.product_id/products.$.sku/products.$.id`  
`products.$.quantity/quantity`  
`product.$.price/price`| `contents.delivery_category`  
`contents.id`  
`contents.quantity`  
`contents.item_price`  
Products Searched| `query`  
`product_id/sku/id`  
`category`  
`currency`  
`value`| `search_string`  
`content_ids`  
`content_category`  
`currency`  
`value`  
  
`product_id/sku/id`  
`quantity`  
`price`| `contents.id`  
`contents.quantity`  
`contents.item_price`  
Product Added to Wishlist| `products.$.product_id/products.$.sku/products.$.id`| `content_ids`  
`category`  
`contentName`  
`currency`  
`value`| `content_category`  
`content_name`  
`currency`  
`value`| `products.$.product_id/products.$.sku/products.$.id`  
`products.$.quantity/quantity`  
`product.$.price/price`| `contents.id`  
`contents.quantity`  
`contents.item_price`  
Payment Info Entered| `products.$.product_id/products.$.sku/products.$.id`| `content_ids`  
`category`  
`currency`  
`value`| `content_category`  
`currency`  
`value`  
`products.$.product_id/products.$.sku/products.$.id`  
`products.$.quantity/quantity`  
`product.$.price/price`| `contents.id`  
`contents.quantity`  
`contents.item_price`  
  
> ![info](/docs/images/info.svg)
> 
> For all the standard events mentioned above:
> 
>   * Default values for the `currency` and `quantity` properties are `USD` and `1` respectively.
>   * `content_ids` field is populated from the `products` array. If the `products` array is not present in the `properties`, `content_ids` is set to an empty array resulting in `num_items` being set to `0`.
> 


### Other standard events

If you map your event to any of the following Facebook standard events, then RudderStack treats it as a standard event as well:

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


For any properties you want to send with these events, you must specify them in the [Event Mapping](<https://www.rudderstack.com/docs/destinations/streaming-destinations/fb-conversions/setup-guide/#event-mapping>) settings.

> ![info](/docs/images/info.svg)
> 
> For the above-mentioned events and [custom events](<https://www.rudderstack.com/docs/destinations/streaming-destinations/fb-conversions/setup-guide/#custom-event>), Rudderstack sends `content_ids` and `num_items` to Facebook as a part of `properties` in the appropriate format.

## Deduplication

Facebook allows you to send events via your web browser and your server via the Conversion API. Depending on how you send your events with this duel setup, there is a possibility of Facebook receiving redundant/duplicate events. Hence, to get an accurate representation of your data, Facebook [deduplicates the incoming events](<https://www.facebook.com/business/help/823677331451951?id=1205376682832142>).

### Using `event_id`

Facebook’s (and RudderStack’s) **recommended** deduplication strategy is to leverage the `event_name` and `event_id` properties. When two events coming into Facebook meet the following criteria, they are deduplicated.

  * They are sent within 48 hours of each other.
  * They are received by the same Facebook Pixel ID.
  * They have the same `event_name`, for example, `Purchase`.
  * They have the same `event_id`.
    * The `event_id` must be unique to that specific event and same for both of the events. For example, the `event_id` could be a purchase order number.


You can set the `event_id` as a unique identifier in the event’s `traits`, `context.traits`, or the `properties` object. RudderStack automatically picks up the `event_name` from the event.

> ![info](/docs/images/info.svg)
> 
> If you don’t set the `event_id`, RudderStack uses `messageId` and maps it to Facebook’s `eventId`.

For more information on the `event_id` deduplication logic, see the [Facebook developer documentation](<https://developers.facebook.com/docs/marketing-api/conversions-api/deduplicate-pixel-and-server-events/#event-id-and-event-name---recommended>).

### Using `fbp` and `external_id`

> ![warning](/docs/images/warning.svg)
> 
> This deduplication strategy is not recommended as it has a few drawbacks:
> 
>   * It will always discard the server event if Facebook identifies a redundant event.
>   * It only works for deduplicating events sent first from the browser and then the server.
>   * There is no deduplication if two consecutive browser events with the same information are sent to Facebook. The same is true if two server events with the same information are sent to Facebook.
> 


For this approach, it is necessary to send an event, first from the browser and then from the server. Note that both events must have the same `event_name`, the same `fbp` parameter, and the same `external_id`.

If the browser event is received before the server event and both events have the same `event_name` and the same `fbp` and `external_id`, then the server event is discarded.

RudderStack maps the `event_name` from the event sent to Facebook. The `fbp` parameter is taken from the `context.fbp` key-value pair. Finally, the `external_id` will be the `userId` or `anonymousId` (if `userId` is not present).

For more information on the `fbp` and `external_id` deduplication logic, see the [Facebook developer documentation](<https://developers.facebook.com/docs/marketing-api/conversions-api/deduplicate-pixel-and-server-events/#fbp-or-external-id>).

## Sending custom `content_type`

You can send a custom [`content_type`](<https://developers.facebook.com/docs/meta-pixel/get-started/advantage-catalog-ads#content-type>) field by specifying it in the `properties.content_type` field of your event.

RudderStack sets the value of `content_type` in the following priority order:

  1. It gives the highest priority to `properties.content_type` in your event.
  2. If `properties.content_type` is absent, RudderStack sets the `content_type` to `product` by default, except in the following cases:


  * If **Product List Viewed** event is sent:
    * with `products` array, then the `content_type` is set to `product`.
    * without the `products` array, then the `content_type` is set to `product_group`.
  * If **Product Viewed** event is not mapped in RudderStack dashboard (default mapping is set to **View Content** event) but is sent:
    * with `products` array, then the `content_type` is set to `product`.
    * without the `products` array, then the `content_type` is set to `product_group`.
  * If any other event is mapped to the Facebook standard event **View Content** in the RudderStack dashboard and is sent:
    * with `products` array, then the `content_type` is set to `product`.
    * without the `products` array, then the `content_type` is set to `product_group`.


> ![info](/docs/images/info.svg)
> 
> `product` and `product_group` are the only two acceptable values for `content_type`.

## FAQ

#### How can I view the conversion events in my Facebook Ads dashboard?

  1. Log in to your [Facebook Ads Manager](<https://www.facebook.com/adsmanager>) account.
  2. Click the **All tools** hamburger menu in the left sidebar.

[![Events Manager in Facebook dashboard](/docs/images/event-stream-destinations/fb-conversions-events-manager.webp)](</docs/images/event-stream-destinations/fb-conversions-events-manager.webp>)

  3. Select **Events Manager**.
  4. Select the data source associated with your ad campaign.

[![Events Manager data sources](/docs/images/event-stream-destinations/fb-conversions-events.webp)](</docs/images/event-stream-destinations/fb-conversions-events.webp>)

Here, you can view your conversion events tracked by Facebook Pixel, app, or offline event sets - this includes the standard and custom events that you have set up.

See the [Events Manager documentation](<https://en-gb.facebook.com/business/help/898185560232180?id=1205376682832142>) for more information on viewing and managing your events.