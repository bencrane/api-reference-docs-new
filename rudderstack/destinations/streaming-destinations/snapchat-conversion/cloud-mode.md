# Snapchat Conversion Cloud Mode Integration

Send events to Snapchat’s Conversion API using RudderStack cloud mode.

* * *

  * __6 minute read

  * 


After you have [successfully instrumented](<https://www.rudderstack.com/docs/destinations/streaming-destinations/snapchat-conversion/setup-guide/>) Snapchat Conversion as a destination in RudderStack, follow this guide to correctly send your events to Snapchat in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>) by leveraging their [Conversions API](<https://businesshelp.snapchat.com/s/article/conversions-api?language=en_US>).

> ![warning](/docs/images/warning.svg)
> 
> You must generate the events at least 28 days before for them to be eligible for reporting via the Conversions API.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/snapchat_conversion>).

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) event to capture user actions along with their associated properties and send this information to Snapchat.

Note that:

  * RudderStack tracks and sends the web, mobile, and offline events to Snapchat via their v3 endpoint (`https://tr.snapchat.com/v3/{ID}/events`), where `{ID}` is the Advertiser ID associated with your Snapchat business account.
  * It uses Bearer authentication leveraging the Snap API token for authenticating all requests. OAuth is not supported currently.


A sample `track` call is shown below:
    
    
    rudderanalytics.track("Order Completed", {
      order_id: "1234",
      currency: "USD",
      products: [{
          product_id: "345676543",
          price: 7.99
        },
      ],
    }, {
      context: {
        traits: {
          email: "alex@example.com",
          phone: "+1-202-555-0146"
    
        }
      }
    })
    

RudderStack recommends passing at least one of the following fields to send a `track` event to Snapchat successfully:

  * `email`
  * `phone`
  * `idfa`
  * `ip` and `userAgent`


You can also send the `eventConversionType` property in your `track` events to determine the type of event to send to Snapchat (web, mobile, or offline).

Snapchat event type| `eventConversionType` property value  
---|---  
`WEB`| `web`  
`MOBILE_APP`| `mobile` / `mobile_app`  
`OFFLINE`| `offline`  
  
> ![warning](/docs/images/warning.svg)
> 
> Make sure to specify the exact property values.

If `eventConversionType` is not found in the event, RudderStack checks if `channel` is present. If `channel` is absent too, RudderStack automatically sets `eventConversionType` to `OFFLINE`.

An example highlighting the use of `eventConversionType` is shown:
    
    
    rudderanalytics.track("Products Searched", {
    query: "HDMI cable",
    eventConversionType: "mobile"
    });
    

### Event mappings

> ![warning](/docs/images/warning.svg)
> 
> This destination does not strictly adhere to the [RudderStack Ecommerce Event Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).

RudderStack automatically maps the following ecommerce events to the corresponding Snapchat Conversion events:

RudderStack event| Snapchat Conversion event  
---|---  
Products Searched| `SEARCH`  
Product List Viewed| `VIEW_CONTENT`  
Promotion Viewed| `AD_VIEW`  
Promotion Clicked| `AD_CLICK`  
Product Viewed| `VIEW_CONTENT`  
Product Added| `ADD_CART`  
Checkout Started| `START_CHECKOUT`  
Payment Info Entered| `ADD_BILLING`  
Order Completed| `PURCHASE`  
Product Added to Wishlist| `ADD_TO_WISHLIST`  
  
RudderStack **does not automatically map** the following events and passes their properties as is, without any modification:

  * `ACHIEVEMENT_UNLOCKED`
  * `APP_INSTALL`
  * `APP_OPEN`
  * `COMPLETE_TUTORIAL`
  * `INVITE`
  * `LIST_VIEW`
  * `LEVEL_COMPLETE`
  * `LOGIN`
  * `PAGE_VIEW`
  * `RATE`
  * `RESERVE`
  * `SAVE`
  * `SIGN_UP`
  * `SHARE`
  * `SPENT_CREDITS`
  * `START_TRIAL`
  * `SUBSCRIBE`


### Property mappings

RudderStack property| Snapchat Conversion property  
---|---  
`properties.brands`  
Array| `custom_data.brands`  
`properties.click_id`| `user_data.sc_click_id`  
`properties.uuid_c1`| `user_data.sc_cookie1`  
`properties.att_status`| `app_data.advertiser_tracking_enabled`  
`properties.idfv`  
`context.device.id`| `user_data.idfv`  
`properties.adId`  
`context.device.advertisingId`| `user_data.madid`  
`properties.item_ids`| `custom_data.content_ids`  
`properties.category`| `custom_data.content_category`  
`properties.number_items`  
`properties.quantity`| `custom_data.num_items`  
`properties.price`  
`properties.value`  
`properties.revenue`  
(`properties.products.price` * `properties.products.quantity`)| `custom_data.value`  
`properties.currency`| `custom_data.currency`  
`properties.search_string`| `custom_data.search_string`  
`properties.client_dedup_id`  
`properties.transaction_id`  
`properties.transactionId`| `event_id`  
`properties.eventConversionType`| `action_source`  
`properties.products.$.product_id`  
`properties.products.$.sku`  
`properties.products.$.id`| `custom_data.contents.$.id`  
`properties.products.$.price`| `custom_data.contents.$.Item_price`  
`properties.products.$.quantity`| `custom_data.contents.$.quantity`  
`properties.products.$.delivery_category`| `custom_data.contents.$.delivery_category`  
`properties.$.product_id`  
`properties.$.sku`  
`properties.$.id`| `custom_data.contents.$.id`  
`properties.$.price`| `custom_data.contents.$.Item_price`  
`properties.$.quantity`| `custom_data.contents.$.quantity`  
`properties.$.delivery_category`| `custom_data.contents.$.delivery_category`  
`context.ip`  
`request_ip`| `user_data.client_ip_address`  
`context.userAgent`| `user_data.client_user_agent`  
`context.page.url`  
`properties.url`| `event_source_url`  
`traits.firstName`  
`traits.firstname`  
`traits.first_name`  
`context.traits.firstName`  
`context.traits.firstname`  
`context.traits.first_name`  
Transformed and sent as hashed value by RudderStack.| `user_data.fn`  
`traits.lastName`  
`traits.lastname`  
`traits.last_name`  
`context.traits.lastName`  
`context.traits.lastname`  
`context.traits.last_name`  
Transformed and sent as hashed value by RudderStack.| `user_data.ln`  
`traits.address.city`  
`context.traits.address.city`  
Transformed and sent as hashed value by RudderStack.| `user_data.ct`  
`traits.email`  
`context.traits.email`  
`properties.email`  
Transformed and sent as hashed value by RudderStack.| `user_data.em`  
`traits.phone`  
`context.traits.phone`  
`properties.phone`  
Transformed and sent as hashed value by RudderStack.| `user_data.ph`  
`traits.gender`  
`context.traits.gender`  
Transformed and sent as hashed value by RudderStack.| `user_data.ge`  
`traits.state`  
`context.traits.state`  
Transformed and sent as hashed value by RudderStack.| `user_data.st`  
`traits.country`  
`context.traits.country`  
Transformed and sent as hashed value by RudderStack.| `user_data.country`  
  
Click the relevant event to understand how RudderStack tracks the event properties and maps them to the corresponding Snapchat Conversion properties:

**Checkout Started**  
RudderStack property| Snapchat Conversion property  
---|---  
`properties.order_id`  
`properties.orderId`| `transaction_id`  
`properties.category`| `item_category`  
`properties.quantity`  
`properties.number_items`| `number_items`  
`properties.currency`| `currency`  
`properties.search_string`| `search_string`  
`properties.client_dedup_id`| `client_dedup_id`  
`properties.price`  
`properties.value`  
`properties.revenue`| `price`  
**Order Completed**  
RudderStack property| Snapchat Conversion property  
---|---  
`properties.order_id`  
`properties.orderId`| `transaction_id`  
`properties.category`  
`properties.item_category`| `item_category`  
`properties.quantity`  
`properties.number_items`| `number_items`  
`properties.currency`| `currency`  
`properties.client_dedup_id`| `client_dedup_id`  
`properties.price`  
`properties.value`  
`properties.revenue`| `price`  
**Payment Info Entered**  
RudderStack property| Snapchat Conversion property  
---|---  
`properties.checkout_id`  
`properties.transactionId`| `transaction_id`  
`properties.item_ids`| `item_ids`  
`properties.category`| `item_category`  
`properties.quantity`  
`properties.number_items`| `number_items`  
`properties.currency`| `currency`  
`properties.search_string`| `search_string`  
`properties.client_dedup_id`| `client_dedup_id`  
`properties.price`  
`properties.value`  
`properties.revenue`| `price`  
`properties.signUpMethod`  
`properties.sign_up_method`| `sign_up_method`  
`properties.client_dedup_id`| `client_dedup_id`  
**Product Added**  
RudderStack property| Snapchat Conversion property  
---|---  
`properties.transaction_id`  
`properties.transactionId`| `transaction_id`  
`properties.product_id`| `item_ids`  
`properties.category`| `item_category`  
`properties.quantity`  
`properties.number_items`| `number_items`  
`properties.currency`| `currency`  
`properties.search_string`| `search_string`  
`properties.client_dedup_id`| `client_dedup_id`  
`properties.price`  
`properties.value`  
`properties.revenue`| `price`  
`properties.signUpMethod`  
`properties.sign_up_method`| `sign_up_method`  
`properties.client_dedup_id`| `client_dedup_id`  
**Product Added to Wishlist**  
RudderStack property| Snapchat Conversion property  
---|---  
`properties.transaction_id`  
`properties.transactionId`| `transaction_id`  
`properties.product_id`| `item_ids`  
`properties.category`| `item_category`  
`properties.quantity`  
`properties.number_items`| `number_items`  
`properties.currency`| `currency`  
`properties.search_string`| `search_string`  
`properties.client_dedup_id`| `client_dedup_id`  
`properties.price`  
`properties.value`  
`properties.revenue`| `price`  
`properties.signUpMethod`  
`properties.sign_up_method`| `sign_up_method`  
`properties.client_dedup_id`| `client_dedup_id`  
**Product List Viewed**  
RudderStack property| Snapchat Conversion property  
---|---  
`properties.transaction_id`  
`properties.transactionId`| `transaction_id`  
`properties.product_id`| `item_ids`  
`properties.category`| `item_category`  
`properties.quantity`  
`properties.number_items`| `number_items`  
`properties.currency`| `currency`  
`properties.search_string`| `search_string`  
`properties.client_dedup_id`| `client_dedup_id`  
`properties.price`  
`properties.value`  
`properties.revenue`| `price`  
`properties.signUpMethod`  
`properties.sign_up_method`| `sign_up_method`  
`properties.client_dedup_id`| `client_dedup_id`  
**Product Viewed**  
RudderStack property| Snapchat Conversion property  
---|---  
`properties.transaction_id`  
`properties.transactionId`| `transaction_id`  
`properties.product_id`| `item_ids`  
`properties.category`| `item_category`  
`properties.quantity`  
`properties.number_items`| `number_items`  
`properties.currency`| `currency`  
`properties.search_string`| `search_string`  
`properties.client_dedup_id`| `client_dedup_id`  
`properties.price`  
`properties.value`  
`properties.revenue`| `price`  
`properties.signUpMethod`  
`properties.sign_up_method`| `sign_up_method`  
`properties.client_dedup_id`| `client_dedup_id`  
**Products Searched**  
RudderStack property| Snapchat Conversion property  
---|---  
`properties.transaction_id`  
`properties.transactionId`| `transaction_id`  
`properties.query`  
`properties.search_string`| `search_string`  
`properties.item_ids`| `item_ids`  
`properties.category`| `item_category`  
`properties.quantity`  
`properties.number_items`| `number_items`  
`properties.currency`| `currency`  
`properties.client_dedup_id`| `client_dedup_id`  
`properties.price`  
`properties.value`  
`properties.revenue`| `price`  
`properties.signUpMethod`  
`properties.sign_up_method`| `sign_up_method`  
`properties.client_dedup_id`| `client_dedup_id`  
**Promotion Clicked**  
RudderStack property| Snapchat Conversion property  
---|---  
`properties.transaction_id`  
`properties.transactionId`| `transaction_id`  
`properties.item_ids`| `item_ids`  
`properties.category`| `item_category`  
`properties.quantity`  
`properties.number_items`| `number_items`  
`properties.currency`| `currency`  
`properties.search_string`| `search_string`  
`properties.client_dedup_id`| `client_dedup_id`  
`properties.price`  
`properties.value`  
`properties.revenue`| `price`  
`properties.signUpMethod`  
`properties.sign_up_method`| `sign_up_method`  
`properties.client_dedup_id`| `client_dedup_id`  
**Promotion Viewed**  
RudderStack property| Snapchat Conversion property  
---|---  
`properties.transaction_id`  
`properties.transactionId`| `transaction_id`  
`properties.item_ids`| `item_ids`  
`properties.category`| `item_category`  
`properties.quantity`  
`properties.number_items`| `number_items`  
`properties.currency`| `currency`  
`properties.search_string`| `search_string`  
`properties.client_dedup_id`| `client_dedup_id`  
`properties.price`  
`properties.value`  
`properties.revenue`| `price`  
`properties.signUpMethod`  
`properties.sign_up_method`| `sign_up_method`  
`properties.client_dedup_id`| `client_dedup_id`  
**Signup**  
RudderStack property| Snapchat Conversion property  
---|---  
`properties.signUpMethod`  
`properties.sign_up_method`| `sign_up_method`  
`properties.transaction_id`  
`properties.transactionId`| `transaction_id`  
`properties.item_ids`| `item_ids`  
`properties.category`| `item_category`  
`properties.quantity`  
`properties.number_items`| `number_items`  
`properties.currency`| `currency`  
`properties.search_string`| `search_string`  
`properties.client_dedup_id`| `client_dedup_id`  
`properties.price`  
`properties.value`  
`properties.revenue`| `price`  
  
| `properties.client_dedup_id` | `client_dedup_id` |

**Other mappings**  
RudderStack property| Data type| Snapchat Conversion property  
---|---|---  
`properties.description`| String| `description`  
`properties.brands`| Array of brands| `brands`  
`properties.event_tag`| String| `event_tag`  
`properties.click_id`| String| `click_id`  
`properties.level`| String| `level`  
`properties.uuid_c1`| String| `uuid_c1`  
`properties.customer_status`  
Can be one of `new`, `returning`, or `activated`.| String| `customer_status`  
`properties.data`| String| `data`  
`properties.att_status`  
Can be one of `AUTHORIZED`, `RESTRICTED`, or `NOT_DETERMINED`.| String| `att_status`  
`properties.sign_up_method`| String| `sign_up_method`  
`properties.advertiser_cookie_1`| String| `advertiser_cookie_1`  
`properties.delivery_method`  
Can be one of `in_store`, `curbside`, or `delivery`.| String| `delivery_method`  
`properties.eventConversionType`| String| `event_conversion_type`  
`context.device.model`| String| `device_model`  
`traits.country`  
`context.traits.country`| String| `country`  
`traits.region`  
`context.traits.region`| String| `region`  
`context.userAgent`| String| `user_agent`  
`traits.firstName`  
`traits.firstname`  
`traits.first_name`  
`context.traits.firstName`  
`context.traits.firstname`  
`context.traits.first_name`| String| `hashed_first_name_sha`  
`traits.middleName`  
`traits.middlename`  
`traits.middle_name`  
`context.traits.middleName`  
`context.traits.middlename`  
`context.traits.middle_name`| String| `hashed_middle_name_sha`  
`traits.lastName`  
`traits.lastname`  
`traits.last_name`  
`context.traits.lastName`  
`context.traits.lastname`  
`context.traits.last_name`| String| `hashed_last_name_sha`  
`traits.address.city`  
`context.traits.address.city`| String| `hashed_city_sha`  
`traits.state`  
`context.traits.state`| String| `hashed_state_sha`  
`traits.zipcode`  
`context.traits.zipcode`  
`traits.zip`  
`context.traits.zip`| String| `hashed_zip`  
  
### `extinfo` mapping

This section lists the mappings for the [`extinfo` object](<https://developers.snap.com/api/marketing-api/Conversions-API/Parameters#extinfo>).

RudderStack property| `extinfo` index  
---|---  
`context.device.type`| `0`  
  
RudderStack **automatically sets** the value to `i2` for Apple or `a2` for Android, depending on the source.  
`context.app.namespace`| `1`  
`context.app.build`| `2`  
`context.app.version`| `3`  
`context.device.model`| `4`  
`context.locale`| `5`  
`moment().tz(context.timezone)?.format('z');`| `6`  
  
See [Moment Timezone documentation](<https://momentjs.com/timezone/docs/>) for more information. RudderStack uses this package to get the timezone abbreviation string.  
`context.network.carrier`| `7`  
`context.screen.width`| `8`  
`context.screen.height`| `9`  
`context.screen.density`| `10`  
`properties.cpu_cores`| `11`  
`properties.storage`| `12`  
`properties.free_storage`| `13`  
`context.timezone`| `14`  
  
> ![info](/docs/images/info.svg)
> 
> If a value for any of the above properties is missing in the event, then RudderStack sets the corresponding `extinfo` index to an empty string.

## Page

You can use the [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call to record your website’s page views, with any additional relevant information about the viewed page.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack processes `page` calls as `track` calls with the Snapchat event set to `page_view`.
> 
> Hence, all the required fields for `track` events are required here as well.

A sample `page` call sent to Snapchat is shown below:
    
    
    rudderanalytics.page("Help", "Help Page", {
      name: "Contact Customer Care",
      request_ip: "203.0.113.0",
      context: {
        userAgent: "ABC"
      }
    })