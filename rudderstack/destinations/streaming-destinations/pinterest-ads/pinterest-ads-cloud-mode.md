# Pinterest Tag Cloud Mode Integration

Send events to Pinterest Tag using cloud mode.

* * *

  * __6 minute read

  * 


RudderStack lets you send your event data to [Pinterest Conversions API](<https://s.pinimg.com/ct/docs/conversions_api/dist/v3.html>) via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>). It sends the event calls in a [batch](<https://www.rudderstack.com/docs/api/http-api/#batch>), where each batch can contain upto 1000 events.

> ![warning](/docs/images/warning.svg)
> 
>   * To use Pinterest Tag’s cloud mode (Pinterest conversions API), contact [Pinterest Support](<https://help.pinterest.com/en/contact>) to enable the beta access.
>   * Pinterest is migrating to API v5 and will deprecate support for API v3 on June 30, 2023. Hence, it is recommended to [configure Pinterest Tag](<https://www.rudderstack.com/docs/destinations/streaming-destinations/pinterest-ads/setting-up-pinterest-ads/#connection-settings>) as a destination in RudderStack using API v5.
> 


Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/pinterest_tag>).

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call allows you to capture the users’ conversion events.

RudderStack maps the `track` events as specified in the **Map Your Events To Pinterest Events** connection setting in the dashboard.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Order Completed", {
      event_id: 'eventIDordercompleted',
      order_id: "transactionId",
      value: 35.00,
      revenue: 31.98,
      currency: 'USD',
      products: [{
        product_id: '123454387',
        price: 3.00,
        quantity: 2,
        currency: 'USD',
        position: 1,
        value: 6.00,
      }]
    }, {
      traits: {
        email: "alex@example.com",
        lastname: "Keener",
        firstname: "Alex",
        action_source: "offline" // or app_ios / app_android / web
      }
    });
    

### Ecommerce conversion tracking

> ![warning](/docs/images/warning.svg)
> 
> This destination does not strictly adhere to the [RudderStack Ecommerce Event Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).

You can use the [Ecommerce Events Specification](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>) for sending the events while instrumenting your site with the RudderStack SDK.

The following table mentions how the specific RudderStack `track` Ecommerce events are mapped to standard Pinterest Conversion Events:

RudderStack event| Pinterest event  
---|---  
Order Completed| `checkout`  
Product Added| `add_to_cart`  
Products Searched| `search`  
Product List Filtered| `search`  
  
You can also track a custom event that you want to include in the conversion reporting. It will be mapped to a custom Pinterest event, for example:
    
    
    rudderanalytics.track("custom event")
    

### Standard Pinterest events

Pinterest supports the following nine standard events that can be mapped and tracked for reporting. Any event apart from these is treated as a user-defined event.

  * `checkout`
  * `add_to_cart`
  * `page_visit`
  * `signup`
  * `watch_video`
  * `lead`
  * `search`
  * `view_category`
  * `custom`


## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record your website’s page views with any additional relevant information about the viewed page.

  * **`view_category`** : RudderStack sends this event if both the `name` and `category` fields are present. The below sample event contains both the fields and is mapped to the Pinterest’s `view_category` event:


    
    
    rudderanalytics.page("Best Seller", "Games", {
      path: "/best-seller/games/1",
      url: "https://www.estore.com/best-seller/games/1",
      title: "Best selling games offered by EStore",
      search: "estore bestseller games",
      referrer: "https://www.google.com/search?q=estore+bestseller",
      testDimension: "true",
    })
    

  * **`page_visit`** : RudderStack sends this event if only `name` field is present and drops any additional properties. The below sample event contains only `name` and is mapped to the Pinterest’s `page_visit` event:


    
    
    rudderanalytics.page("Best Seller", {
      path: "/best-seller/1",
    })
    

## Common field mappings

The following table lists the mappings specific for Pinterest Conversion API and are relevant for both the `track` and `page` calls:

RudderStack property| Pinterest Tag property| Description  
---|---|---  
`message.event`  
Required| `event_name`| Type of the user event.  
`context.traits.action_source`  
`properties.action_source`  
`message.channel`  
Required| `action_source`  
| Source indicating the occurence of conversion event.  
`timestamp`  
Required| `event_time`| Unix timestamp (in UTC) in seconds indicating when the user conversion event occurred.  
`destination.Config.advertiserId`  
Required| `advertiser_id`| Pinterest Advertiser ID.  
Integrations Object `messageId`| `event_id`| Deduplication key from the dashboard setting or `messageId`. The dashboard setting is given higher priority.  
`pageUrl`| `event_source_url`| URL of the web conversion event.  
`context.device.adTrackingEnabled`| `opt_out`| 

  * When `action_source` is **web** or **offline** , it defines whether the user has opted out of tracking for web conversion events.
  * When `action_source` is **app_android** or **app_ios** , it defines whether the user has enabled **Limit Ad Tracking** on their iOS device or opted out of **Ads Personalization** on their Android device.

  
`destination.Config.appId`| `app_id`| App store’s App ID.  
`context.app.name`  
`properties.appName`| `app_name`| Name of the app.  
`context.app.version`  
`properties.appVersion`| `app_version`| Version of the app.  
`context.device.manufacturer`  
`properties.manufacturer`| `device_brand`| Brand of the user device.  
`context.device.model`  
`properties.deviceModel`| `device_model`| Model of the user device.  
`context.device.type`  
`properties.deviceType`| `device_type`| Type of the user device.  
`context.os.version`| `os_version`| Version of the device’s operating system.  
`context.locale`| `language`| Two-character ISO-639-1 language code indicating the user’s language.  
`properties.partnerName`| `partner_name`| Third party partner’s name responsible for sending the event to Conversions API on behalf of the advertiser.  
  
The naming convention is `ss-<partnername>` (in lowercase), for example, `ss-shopify`.  
`context.network.carrier`| `device_carrier`| User device’s mobile carrier.  
`context.network.wifi`| `wifi`| Whether the event occurred when the user’s device was connected to Wi-Fi.  
  
> ![info](/docs/images/info.svg)
> 
> For mobile sources, if `context.device.adTrackingEnabled` is `true`, `opt_out` will be set as `false` and vice-versa.

## User field mappings

The following table lists the mappings for fields carrying the user information for `track` and `page` calls:

RudderStack property| Pinterest Tag property| Data Type  
---|---|---  
`properties.email`  
`context.traits.email`| `em`| Array of strings with SHA-256 encoding  
`properties.phone`  
`context.traits.phone`| `ph`| Array of strings with SHA-256 encoding  
`properties.clickId`| `click_id`| String  
`context.traits.gender`| `ge`| Array of strings with SHA-256 encoding  
`context.traits.birthday`| `db` (YYYYMMDD format)| Array of strings with SHA-256 encoding  
`context.traits.lastName`| `ln`| Array of strings with SHA-256 encoding  
`context.traits.firstName`| `fn`| Array of strings with SHA-256 encoding  
`traits.address.city`  
`context.traits.address.city`| `ct`| Array of strings with SHA-256 encoding  
`traits.address.state`  
`context.traits.address.state`| `st` (Two-letter code)| Array of strings with SHA-256 encoding  
`traits.address.zip`  
`context.traits.address.zip`| `zp`| Array of strings with SHA-256 encoding  
`traits.address.country`  
`context.traits.address.country`| `country` (Two-character ISO-3166 country code)| Array of strings with SHA-256 encoding  
`userId`  
`traits.userId`  
`traits.id`  
`context.traits.userId`  
`context.traits.id`  
`anonymousId`| `external_id`| Array of strings with SHA-256 encoding  
`context.device.advertisingId`| `hashed_maids`| Array of strings with SHA-256 encoding  
`context.ip`  
`context.requestIP`  
`properties.ip`  
`properties.clientIpAddress`| `client_ip_address`| String  
`context.userAgent`| `client_user_agent`| String  
  
> ![warning](/docs/images/warning.svg)
> 
> To send the `track` or `page` events successfully, you need to include **at least one** of the following user properties:
> 
>   * `em`
>   * `hashed_maids`
>   * Combination of `client_ip_address` and `client_user_agent`
> 


## Custom field mappings

The following table lists the custom fields mappings for `track` and `page` calls:

RudderStack property| Pinterest Tag property| Data Type  
---|---|---  
`properties.currency`| `currency`| String  
`properties.value`  
`properties.total`  
`properties.revenue`| `value`| String  
`properties.product_id`  
`properties.product_sku`  
`properties.products[index].product_id`  
`properties.products[index].product_sku`| `content_ids`| Array of strings  
`properties.price`  
`properties.products[index].price`| `contents.[index].item_price`| Array of strings  
`properties.quantity`  
`properties.products[index].quantity`| `contents.[index].quantity`| Integer  
`properties.numOfItems` (if not present, sum of quantity)| `num_items`| Integer  
`properties.order_id`| `order_id`| String  
`properties.query`| `search_string`| String  
`properties.contentName`| `content_name`| String  
`properties.contentCategory`| `content_category`| String  
`properties.np`| `np`| String  
`properties.product_id`  
`properties.product_sku`  
`properties.products[index].product_id`  
`properties.products[index].sku`| `contents.[index].id`| String  
`properties.name`  
`properties.products[index].name`| `contents.[index].item_name`| String  
`properties.category`  
`properties.products.[index].category`| `contents.[index].item_category`| String  
`properties.brand`  
`properties.products.[index].brand`| `contents.[index].item_brand`| String  
  
## Limited Data Processing (LDP)

Starting January 1, 2023, you can use Pinterest’s [Limited Data Processing (LDP)](<https://developers.pinterest.com/docs/conversions/conversion-management/#Understanding%20Limited%20Data%20Processing>) flag to limit how Pinterest uses certain data to help the advertisers comply with the users’ privacy settings in accordance with the CCPA (California Consumer Privacy Act).

The following table lists the event properties **required to enable Limited Data Processing** and their mappings with the Pinterest fields:

RudderStack property| Pinterest property| Data type| Description  
---|---|---|---  
`properties.optOutType`| `custom_data.opt_out_type`| String| Set this field to `LDP`.  
`traits.address.state`  
`context.traits.address.state`| `st`| Array of strings with SHA-256 encoding| Should be a two-letter code  
`traits.address.country`  
`context.traits.address.country`| `country`| Array of strings with SHA-256 encoding| Should be a two-character ISO-3166 country code  
  
## FAQ

#### How can I verify if my events are being sent to Pinterest Conversions API?

Follow these steps to see your events in Pinterest Conversions API:

  1. Login to your [Pinterest ads manager](<https://ads.pinterest.com/>) account.
  2. Click the **Ads** tab and select **Conversions** from the dropdown.
  3. Select **API for conversions** from the dropdown to see your events.


> ![info](/docs/images/info.svg)
> 
> To see **API for conversions** option in the dropdown, you need to set up your Pinterest dashboard using the Pinterest Tag. For more information on using the Pinterest Tag, refer to the [Pinterest Tag Device Mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/pinterest-ads/pinterest-ads-device-mode/>) documentation.

[![](/docs/images/event-stream-destinations/pinterest-tag-events-cloud.webp)](</docs/images/event-stream-destinations/pinterest-tag-events-cloud.webp>)