# TikTok Ads Offline Events

Send your event data from RudderStack to TikTok Ads Offline Events.

* * *

  * __3 minute read

  * 


[TikTok Ads](<https://ads.tiktok.com>) Offline Events let you track and send your conversions data after a user clicks your TikTok ad but does not directly proceed to sale in the online mode.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/tiktok_ads_offline_events>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** AMP , Android (Java) , Android (Kotlin) , Cordova, Cloud, Flutter, iOS (Obj-C) , iOS (Swift) , React Native , Unity, Warehouse, Web, Shopify
  * Refer to it as **TikTok Ads Offline Events** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
AMP| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Java)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cloud| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cordova| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Swift)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
React Native| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Shopify| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Unity| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Warehouse| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to TikTok Ads Offline Events, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **TikTok Ads Offline Events**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully configure TikTok Ads Offline Events as a destination, you will need to configure the following settings:

  * **Access Token** : Enter your TikTok access token (also called Long Term Access Token) by following the steps mentioned in the [Authorization](<https://ads.tiktok.com/marketing_api/docs?id=1738373141733378>) and [Authentication](<https://ads.tiktok.com/marketing_api/docs?id=1738373164380162>) sections of the TikTok documentation.
  * **Mapping to trigger the TikTok Ads Offline standard events for the respective events** : Enter the **Event Name** and select the corresponding **Standard Event** from the dropdown you want to trigger when that event is called. You can specify multiple standard events for one event name and vice versa.
  * **Hash Contextual User Properties (SHA-256)** : Use this setting to hash the user properties like `email` and `phone` using SHA-256 encryption.


## Track

> ![warning](/docs/images/warning.svg)
> 
> This destination does not strictly adhere to the [RudderStack Ecommerce Event Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you capture the offline user events along with the associated properties.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Start Payment", {
      checkout_id: "12345",
      order_id: "1234",
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
          name: "GI Joe",
          price: 4.99,
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
    

### Standard events

To send a `track` event as a standard TikTok Ads Offline Event, you must specify the event mapping in the RudderStack dashboard’s connection settings:

[![TikTok Ads Offline standard events](/docs/images/event-stream-destinations/tiktok-ads-offline-standard-events.webp)](</docs/images/event-stream-destinations/tiktok-ads-offline-standard-events.webp>)

RudderStack automatically maps the following events to the corresponding TikTok Ads Offline standard events:

RudderStack maps the following events to the corresponding TikTok Ads Events:

RudderStack event| TikTok Ads event  
---|---  
`ClickButton`| `ClickButton`  
`CompleteRegistration`| `CompleteRegistration`  
`Contact`| `Contact`  
`Download`| `Download`  
`Search`| `Search`  
`SubmitForm`| `SubmitForm`  
`Subscribe`| `Subscribe`  
`ViewContent`| `ViewContent`  
  
RudderStack also maps the following [ecommerce events](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>):

RudderStack event| TikTok Ads event  
---|---  
`Checkout Started`| `InitiateCheckout`  
`Checkout Step Completed`| `CompletePayment`  
`Order Completed`| `PlaceAnOrder`  
`Payment Info Entered`| `AddPaymentInfo`  
`Product Added`| `AddToCart`  
`Product Added to Wishlist`| `AddToWishlist`  
  
### Property mapping

RudderStack maps the following event properties to the corresponding TikTok Ads Offline Events fields:

RudderStack property| TikTok Ads Offline event property  
---|---  
`message.event`  
Required| `event`  
`properties.eventSetId`  
Required| `event_set_id`  
`timestamp`  
Required| `timestamp`  
`properties.eventId`  
`properties.messageId`| `event_id`  
`traits.phone`  
`context.traits.phone`| `context.user.phone_numbers`  
`traits.email`  
`context.traits.email`| `context.user.emails`  
`properties.order_id`  
`properties.orderId`| `properties.order_id`  
`properties.shop_id`  
`properties.shopId`| `properties.shop_id`  
`context.channel`| `properties.event_channel`  
`properties.value`  
`properties.revenue`  
`properties.total`| `properties.value`  
`properties.currency`| `properties.currency`  
`properties.name`  
`properties.products.name`| `properties.contents.content_name`  
`properties.contentType`  
`properties.products.name`| `properties.contents.content_type`  
`properties.category`  
`properties.products.category`| `properties.contents.content_category`  
`properties.productId`  
`properties.products.productId`| `properties.contents.content_id`  
`properties.price`  
`properties.products.price`| `properties.contents.price`  
`properties.price`  
`properties.products.price`| `properties.contents.price`  
`properties.quantity`  
`properties.products.quantity`| `properties.contents.quantity`  
  
> ![info](/docs/images/info.svg)
> 
> RudderStack **internally** sets the property `partner_name` to `RudderStack` while sending the above properties to TikTok Ads Offline Events.