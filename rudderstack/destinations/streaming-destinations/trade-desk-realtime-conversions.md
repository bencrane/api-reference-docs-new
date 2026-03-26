# The Trade Desk Real Time Conversions Beta

Send your event data from RudderStack to The Trade Desk.

* * *

  * __5 minute read

  * 


[The Trade Desk](<https://www.thetradedesk.com/us>) is a leading digital advertising technology platform for efficient campaign management. It offers comprehensive tools to target audiences across diverse channels like video, mobile, and display.

RudderStack lets you send real-time conversion events data to The Trade Desk via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>) using [The Trade Desk Real-Time Conversion Events API](<https://partner.thetradedesk.com/v3/portal/data/doc/DataConversionEventsApi>). Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/main/src/cdk/v2/destinations/the_trade_desk>).

## Setup

In your [RudderStack dashboard](<https://app.rudderstack.com/>), go to **Directory** > **Destinations** > **Cloud Destinations** and search for **The Trade Desk Real Time Conversions**.

### Connection settings

Configure the following settings to set up The Trade Desk Real Time Conversions as a destination in RudderStack:

  * **Name** : Specify a unique name to identify the destination in RudderStack.
  * **Advertiser ID** : Enter the advertiser ID from the **Advertiser Preferences** page in the The Trade Desk dashboard.
  * **Tracking Tag ID** : Enter the tracking tag ID. [Contact your The Trade Desk representative](<https://www.thetradedesk.com/us/contact-us>) to obtain it.


### Connection mode

Destination Information  
---  
  
  * **Status:** Beta
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **The Trade Desk Real Time Conversions** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
  
### Event mapping

Click **Set-up mapping** to map your RudderStack events/properties to specific The Trade Desk Real Time Conversions events/properties. RudderStack also provides the JSON mapper to set these mappings.

Use **Event** tab to map the respective events:

[![Optimizely Feature Experimentation event mapping](/docs/images/event-stream-destinations/trade-desk-event-mapping.webp)](</docs/images/event-stream-destinations/trade-desk-event-mapping.webp>)

Use **Custom properties** tab to map the custom properties (`td1` to `td10`) by entering the property path from where RudderStack maps it to the corresponding The Trade Desk Real Time Conversions’ custom property:

[![Optimizely Feature Experimentation attribute mapping](/docs/images/event-stream-destinations/trade-desk-property-mapping.webp)](</docs/images/event-stream-destinations/trade-desk-property-mapping.webp>)

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you capture user events along with the properties associated with them.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Product Added", {
      product_id: "622c6f5d5cf86a4c77358033",
      sku: "8472-998-0112",
      category: "Games",
      name: "Cones of Dunshire",
      brand: "Wyatt Games",
      variant: "expansion pack",
      price: 49.99,
      quantity: 5,
      coupon: "PREORDER15",
      position: 1,
      url: "https://www.website.com/product/path",
      image_url: "https://www.website.com/product/path.webp",
    })
    

### Supported events

RudderStack supports all [The Trade Desk Real Time Conversions events](<https://partner.thetradedesk.com/v3/portal/data/doc/DataConversionEventsApi#event-mapping>). Out of these, RudderStack maps the following standard [ecommerce events](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>) as:

RudderStack event| The Trade Desk Real Time Conversions event  
---|---  
Product Added| `addtoCart`  
Order Completed| `purchase`  
Product Viewed| `viewitem`  
Checkout Started| `startcheckout`  
Cart Viewed| `viewcart`  
Product Added to Wishlist| `wishlistitem`  
  
You can map the rest of The Trade Desk Real Time Conversions events (listed below) in the RudderStack dashboard in the **Map RudderStack to The Trade Desk Events** setting:

  * searchitem
  * searchcategory
  * login
  * messagebusiness
  * direction
  * sitevisit


RudderStack sends all the other unmapped events as is.

### Property mappings

The following table details the property mappings between RudderStack and The Trade Desk Real Time Conversions:

RudderStack| The Trade Desk Real Time Conversions| Note  
---|---|---  
<tracking-tag-id> Required| `tracker_id`| This value is populated from the RudderStack dashboard’s **Tracking Tag ID** setting.  
<advertiser-id>  
Required| `adv`| This value is populated from the RudderStack dashboard’s **Advertiser ID** setting.  
`value`| `value`| More information.  
`currency`| `currency`| -  
`event`| `event_name`| More information.  
`context.ip`  
`request_ip`| `client_ip`| -  
`context.page.referrer`| `referrer_url`| -  
-| `adid`| Unique advertising ID for the event. RudderStack maps this property from `externalId` in the `context` object. More information.  
-| `adid_type`| Type of advertising ID, specified in the `adid` property. RudderStack maps this property from `externalId` in the `context` object. More information.  
`messageId`| `imp`| 36-character string (including dashes) that serves as the unique ID for the impression to which the event is attributed.  
`order_id`| `order_id`| -  
`products`| `items`| More information  
<td>| `td1` to `td10`| This value for custom fields is populated from the RudderStack dashboard’s **Map RudderStack to The Trade Desk Events** setting.  
-| `privacy_settings`| More information.  
-| `data_processing_option`| More information.  
  
#### `adid` mapping

RudderStack maps the advertising ID (`adid`) from `context.device.advertisingId` if the `os` information is provided in `context.os.name`.

RudderStack maps the type of advertising ID (`adid_type`) as:

  * `AAID` if os’s name is `android`
  * `NAID` if os’s name is `windows`
  * `IDFA` if os’s name is `ios`


Sample `context` object:
    
    
    {
       "app": {
          "build": "1.0.0",
          "name": "RudderLabs Android SDK",
          "namespace": "com.rudderlabs.javascript",
          "version": "1.0.5"
       },
       "device": {
          "adTrackingEnabled": true,
          "advertisingId": "test-advertisingId",
          "id": "test-id",
          "manufacturer": "Google",
          "model": "AOSP on IA Emulator",
          "name": "generic_x86_arm",
          "type": "ios",
          "attTrackingStatus": 3
       },
    
       "locale": "en-GB",
       "os": {
          "name": "ios",
          "version": ""
       }
    }
    

If the device information is absent, you can also pass the advertising ID (`adid`) in the context’s `externalId` object:
    
    
    {
      "externalId": [
        {
          "type": "daid",
          "id": "test-daid"
        }
      ]
    }
    

#### `value` mapping

For `Product Added`, `Product Viewed`, and `Product Added to Wishlist` events, RudderStack maps `price*quantity` to The Trade Desk Real Time Conversions’ `value` field.

For `Order Completed`, and `Checkout Started` events, RudderStack maps `revenue`/`value` to The Trade Desk Real Time Conversions’ `value` field.

#### `items` mapping

For `Order Completed`, `Checkout Started`, and `Cart Viewed event` events, RudderStack maps the individual products inside the `products` array to The Trade Desk Real Time Conversions’ `item` array.

For single product events, that is, `Product Added`, `Product Viewed`, and `Product Added to Wishlist`, RudderStack maps the root-level properties to single item in the `items` array of The Trade Desk Real Time Conversions:

RudderStack property| The Trade Desk Real Time Conversions property  
---|---  
`product_id`/`sku`  
Required| `item_code`  
`name`| `name`  
`quantity`| `qty`  
`price`| `price`  
`category_id`| `cat`  
  
#### `privacy_settings` mapping

RudderStack maps the following privacy settings (`privacy_settings`) from the `integration` object:

RudderStack| The Trade Desk Real Time Conversions| Notes  
---|---|---  
`privacy_type` Required| `privacy_type`| Allowed values are: `GDPR`/`CCPA`/`GPP`  
`is_applicable` Required| `is_applicable`| Boolean property indicating if the value specified in the `privacy_type` property is applicable.  
`consent_string` Required| `consent_string`| User’s consent when the privacy regulations are in effect.  
  
Sample `integration` object:
    
    
    {
      All: true,
      THE_TRADE_DESK: {
        privacy_settings: [
          {
            privacy_type: 'GDPR',
            is_applicable: 1,
            consent_string: 'ok',
          },
        ],
      },
    };
    

#### `data_processing_option` mapping

RudderStack maps the following data processing options (`data_processing_option`) from the `integration` object:

RudderStack| The Trade Desk Real Time Conversions| Note  
---|---|---  
`policies` Required| `policies`| Pass the users’ opt-out choices. Currently, The Trade Desk Real Time Conversions only supports the `LDU` (Limited data use) policy.  
`region`  
Required| `region`| Two-letter state. For example, `US-CO`.  
  
Sample `integration` object:
    
    
    {
      All: true,
      THE_TRADE_DESK: {
        policies: ['LDU'],
        region: 'US-CA'
      },
    };