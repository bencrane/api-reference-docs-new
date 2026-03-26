# TikTok Ads Cloud Mode Integration

Send events to TikTok Ads using RudderStack cloud mode.

* * *

  * __4 minute read

  * 


RudderStack lets you send your event data to TikTok Ads via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * This integration supports both [Events 1.0](<https://business-api.tiktok.com/portal/docs?id=1739657891856385>) and [Events 2.0](<https://business-api.tiktok.com/portal/docs?id=1771101276978178>) API for sending events to TikTok. RudderStack recommends using the Events 2.0 API to send your events as TikTok will sunset the Events 1.0 API by the second half of 2024.
>   * To send custom events to TikTok Ads using [RudderStack Open Source](<https://app.rudderstack.com/signup?type=opensource>), use [`rudder-transformer`](<https://github.com/rudderlabs/rudder-transformer>) v1.52.0 or later.
> 


Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/tiktok_ads>).

## Track

Use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to capture user events along with the associated properties.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Order Completed", {
      checkout_id: "12345",
      order_id: "1234",
      affiliation: "Apple Store",
      total: 20,
      revenue: 15.0,
      shipping: 22,
      tax: 1,
      discount: 1.5,
      coupon: "ImagePro",
      currency: "USD",
      contentType: "product",
      products: [{
          product_id: "123",
          sku: "G-32",
          name: "Monopoly",
          price: 14,
          quantity: 1,
          category: "Games",
          url: "https://www.website.com/product/path",
          image_url: "https://www.website.com/product/path.jpg",
        },
        {
          product_id: "345",
          sku: "F-32",
          name: "UNO",
          price: 3.45,
          quantity: 2,
          category: "Games",
        },
      ],
    })
    

### Event mapping

> ![warning](/docs/images/warning.svg)
> 
> This destination does not strictly adhere to the [RudderStack Ecommerce Event Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).

You can use the [Event mapping settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/tiktok-ads/setup/#event-settings>) in the dashboard to map your events to the below [TikTok standard events](<https://ads.tiktok.com/help/article/supported-standard-events>):

**List of supported TikTok standard events**  


  * `Add Payment Info`
  * `Add to Cart`
  * `Add to Wishlist`
  * `Application Approval`
  * `Click Button`
  * `Complete Payment`
  * `Complete Registration`
  * `Contact`
  * `Customize Product`
  * `Download`
  * `Find Location`
  * `Initiate Checkout`
  * `Lead`
  * `Place an Order`
  * `Purchase`
  * `Schedule`
  * `Search`
  * `Submit Application`
  * `Submit Form`
  * `Subscribe`
  * `Start Trial`
  * `View Content`

  


> ![warning](/docs/images/warning.svg)
> 
> TikTok has recently updated the following standard events:
> 
>   * `Submit Form` is renamed to `Lead`.
>   * `Complete Payment` is renamed to `Purchase`.
> 

> 
> Although TikTok still supports the old events (`Submit Form` and `Complete Payment`), RudderStack recommends using the new events (`Lead` and `Purchase`) to avoid any issues.

Note that RudderStack automatically maps the following standard [ecommerce events](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>) to the corresponding TikTok standard events:

RudderStack event| TikTok Ads event  
---|---  
`Product Added to Wishlist`| `Add to Wishlist`  
`Product Added`| `Add to Cart`  
`Checkout Started`| `Initiate Checkout`  
`Payment Info Entered`| `Add Payment Info`  
`Checkout Step Completed`| `Complete Payment`  
`Order Completed`| `Place an Order`  
  
### Property mapping

RudderStack maps the following **optional** event properties to the corresponding TikTok Ads fields:

RudderStack property| TikTok Ads property  
---|---  
`timestamp`  
Required| `event_time`  
`properties.eventId`  
`properties.event_id`  
`messageId`| `event_id`  
`properties.limited_data_use`| `limited_data_use`  
`properties.contents`| `properties.contents`  
`properties.contentType`  
`properties.content_type`| `properties.content_type`  
`properties.query`| `properties.search_string`  
`properties.shopId`  
`properties.shop_id`| `properties.shop_id`  
`properties.orderId`  
`properties.order_id`| `properties.order_id`  
`properties.currency`| `properties.currency`  
`properties.value`| `properties.value`  
`properties.description`| `properties.description`  
`properties.query`| `properties.query`  
`properties.ttclid`| `user.ttclid`  
`properties.ttp`  
`properties.context.user.ttp`| `user.ttp`  
`properties.context.user.email`  
`context.user.email`  
`traits.email`  
`context.traits.email`  
`properties.email`  
| `user.email`  
`properties.context.user.phone`  
`traits.phone`  
`context.traits.phone`  
`properties.phone`| `user.phone`  
`properties.city`  
`context.traits.city`  
`context.traits.address.city`| `user.city`  
`properties.country`  
`context.traits.country`  
`context.traits.address.country`| `user.country`  
`properties.state`  
`context.traits.address.state`  
`context.traits.state`| `user.state`  
`properties.att_status`| `user.att_status`  
`properties.appId`  
`properties.app_id`| `app.app_id`  
`properties.appName`  
`properties.app_name`| `app.app_name`  
`properties.appVersion`  
`properties.app_version`| `app.app_version`  
`properties.callBack`| `ad.callback`  
`properties.campaignId`  
`properties.campaign_id`| `ad.campaign_id`  
`properties.adId`  
`properties.ad_id`| `ad.ad_id`  
`properties.creativeId`  
`properties.creative_id`| `ad.creative_id`  
`properties.isRetargeting`  
`properties.is_retargeting`| `ad.is_retargeting`  
`properties.attributed`| `ad.attributed`  
`properties.attributionType`  
`properties.attribution_type`| `ad.attribution_type`  
`properties.attributionProvider`  
`properties.attribution_provider`| `ad.attribution_provider`  
`properties.leadId`  
`properties.lead_id`| `lead.lead_id`  
`properties.leadEventSource`  
`properties.lead_event_source`| `lead.lead_event_source`  
`properties.context.page.url`  
`properties.url`  
`context.page.url`| `page.url`  
`properties.context.page.referrer`  
`properties.referrer`  
`context.page.referrer`| `page.referrer`  
`context.locale`| `user.locale`  
`context.user.email`  
`traits.email`  
`context.traits.email`| `user.email`  
`context.traits.phone`  
`traits.phone`| `user.phone`  
`context.ip`  
`request_ip`| `user.ip`  
`context.userAgent`| `user.user_agent`  
`context.traits.city`  
`context.traits.address.city`| `user.city`  
`context.traits.country`  
`context.traits.address.country`| `user.country`  
`context.traits.address.state`  
`context.traits.state`| `user.state`  
`context.device.advertisingId`| `user.idfa`  
`context.device.id`| `user.idfv`  
`context.device.advertisingId`| `user.gaid`  
`context.app.namespace`| `app.app_id`  
`context.app.name`| `app.app_name`  
`context.app.version`| `app.app_version`  
`firstName`| `user.first_name`  
`lastName`| `user.last_name`  
`zipcode`| `user.zip_code`  
  
Note that the `properties.ttclid` to `user.ttclid` mapping corresponds to the `properties.clickId` to `context.ad.callback` mapping in Events 1.0 API.

> ![warning](/docs/images/warning.svg)
> 
> TikTok will sunset the [Events 1.0](<https://business-api.tiktok.com/portal/docs?id=1739657891856385>) API by the second half of 2024. RudderStack recommends using the [Events 2.0](<https://business-api.tiktok.com/portal/docs?id=1771101276978178>) API to send your events.

RudderStack property| TikTok Ads property  
---|---  
`properties.eventId`| `event_id`  
`timestamp`| `timestamp`  
`properties.testEventCode`| `test_event_code`  
`properties.contents`| `properties.contents`  
`properties.currency`| `properties.currency`  
`properties.clickId`| `context.ad.callback`  
`properties.value`| `properties.value`  
`properties.description`| `properties.description`  
`properties.query`| `properties.query`  
`properties.context.ad` or `context.ad`| `context.ad`  
`properties.context.page` or `context.page`| `context.page`  
`properties.context.user`| `context.user`  
`context.ip`| `context.ip`  
`context.userAgent`| `context.user_agent`  
From `externalId` `tiktokExternalId`| `user.external_id`  
  
For custom events, RudderStack maps only the [standard fields](<https://github.com/rudderlabs/rudder-transformer/blob/0e1429663d167a2c5cded0d9130374eb586a18c0/src/v0/destinations/tiktok_ads/data/TikTokTrack.json>) supported by TikTok Ads and drops all other fields in the event. See [TikTok Ads standard fields](<https://business-api.tiktok.com/portal/docs?id=1741601162187777>) documentation for more information.

## FAQ

#### I see a 40002 response code with ‘No permission to operate pixel code’ error message, what can I do?

This error code is related to the authentication of your TikTok account. For more information, refer to the [TikTok documentation](<https://ads.tiktok.com/gateway/docs/index?identify_key=2b9b4278e47b275f36e7c39a4af4ba067d088e031d5f5fe45d381559ac89ba48&language=ENGLISH&doc_id=1701890979375106#item-link-FAQ>).