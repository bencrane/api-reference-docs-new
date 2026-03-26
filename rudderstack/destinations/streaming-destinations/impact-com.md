# impact.com

Send your event data from RudderStack to impact.com.

* * *

  * __5 minute read

  * 


[impact.com](<https://impact.com/>) is a global partnership management platform that helps in managing and scaling different partnerships, such as affiliates, influencers, strategic business partners, mobile apps, commerce content publishers, B2B, and more.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/impact>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **impact.com** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to impact.com, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Impact Radius**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully configure impact.com as a destination, you will need to configure the following settings:

  * **Account SID** : Enter the account SID present in the **Settings** > **API** option in the [impact.com dashboard](<https://app.impact.com/login.user>).
  * **API Key** : Enter the auth token present in the **Settings** > **API** option in the impact.com dashboard.
  * **Campaign Id** : Enter the campaign ID present in the **Account** > **Programs** option in your the impact.com dashboard:

[![Campaign ID Impact](/docs/images/event-stream-destinations/campaign-id-impact.webp)](</docs/images/event-stream-destinations/campaign-id-impact.webp>)

  * **Impact App Id** : Enter the system app ID present in the **Settings** > **Mobile Apps** option in the impact.com dashboard.
  * **Event Type Id** : Enter the ID present in the **Settings** > **Event Type** option in the impact.com dashboard.
  * **Enable to hash email** : Enable this setting to hash the `email` field in SHA1 format. Keep it disabled in case it is already hashed.


> ![warning](/docs/images/warning.svg)
> 
> impact.com expects the `email` field in a hashed format. Otherwise, the events will fail. Hence, if you are sending the `email` in a plain text format, make sure to enable this setting.

  * **Additional parameters mapping** : Enter the property mappings from RudderStack to impact.com for any additional parameters (other than the default ones mentioned in the sections below).
  * **Custom mapping for Products** : Enter the custom property mappings for the `products` array.
  * **Enable Identify Events** : Enable this setting to send the `identify` events.
  * **Enable Page Events** : Enable this setting to send the `page` events.
  * **Enable Screen Events** : Enable this setting to send the `screen` events.
  * **Action Event Names** : Enter the list of event names you want to track as user actions.
  * **Install Event Names** : Enter the list of event names corresponding to the app install events.


## Identify

You can send an [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to impact.com via the [`PageLoad` endpoint](<https://integrations.impact.com/impact-brand/reference/create-a-pageload>). It allows impact.com to update the user identifiers for an accurate correlation.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4el9Zt1WSfVJIVo4GRlm", {
      email: "alex@example.com",
    });
    

### Property mappings

The following table lists the mappings between RudderStack and impact.com properties:

RudderStack property| impact.com property  
---|---  
`context.device.id`| `AppleIfv`  
`context.app.name`| `AppName`  
`context.app.build`| `AppPackage`  
`context.app.version`| `AppVer`  
`settings.campaignId`| `CampaignId`  
`context.traits.email`  
`properties.email`| `CustomerEmail`  
`userId`| `CustomerId`  
`anonymousId`| `CustomProfileId`  
`context.network.carrier`| `DeviceCarrier`  
`context.locale`| `DeviceLocale`  
`context.device.manufacturer`| `DeviceMfr`  
`context.device.model`| `DeviceModel`  
`context.device.type`  
`context.os.name`| `DeviceOs`  
`context.os.version`| `DeviceOsVer`  
`timestamp`  
`originalTimestamp`| `EventDate`  
`context.device.id`| `GoogAId`  
`context.ip`| `IpAddress`  
`context.page.url`  
`properties.url`  
`context.page.referrer`  
`context.referrer.url`| `PageUrl`  
`context.referrer.url`  
`context.page.referrer`| `ReferringUrl`  
`context.userAgent`| `UserAgent`  
`context.device.advertisingId`| `AppleIfa`  
  
> ![info](/docs/images/info.svg)
> 
> At least one of the `userId`, `anonymousId`, `context.device.id`, or `context.device.advertisingId` parameters is required to make an `identify` call successfully.

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you capture user events along with the properties associated with them.

RudderStack sends the `track` events listed in the **Action Event Names** and **Install Event Names** dashboard settings to impact.com using the [`Conversions` endpoint](<https://integrations.impact.com/impact-brand/reference/submit-a-conversion>). All the other `track` events are sent using the [`PageLoad` endpoint](<https://integrations.impact.com/impact-brand/reference/create-a-pageload>).

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Order Completed", {
      order_id: "1234",
      shipping: 22,
      tax: 1,
      discount: 1.5,
      coupon: "ImagePro",
      currency: "USD",
      products: [{
          sku: "G-32",
          name: "Monopoly",
          price: 14,
          quantity: 1,
          category: "Games",
          brand: "top"
        },
        {
          sku: "G-34",
          name: "Monopoly",
          price: 16,
          quantity: 3,
          category: "Games",
          brand: "top"
        },
      ],
    })
    

### Property mappings

The following table lists the mappings between RudderStack and impact.com properties:

RudderStack property| impact.com property  
---|---  
`properties.orderId`  
`properties.order_id`  
`properties.transactionID`  
`properties.checkout_id`  
Required| `OrderId`  
`timestamp`  
`originalTimestamp`  
Required| `EventDate`  
`event`  
Required, if settings.eventTypeId is absent.| `EventTypeCode`  
`settings.eventTypeId`  
Required, if event is absent.| `EventTypeId`  
`context.device.adTrackingEnabled`| `TrackingConsent`  
`context.device.advertisingId`| `AppleIfa`  
`context.device.id`| `AppleIfv`  
`context.app.name`| `AppName`  
`context.app.build`| `AppPackage`  
`context.device.id`| `AndroidId`  
`context.app.version`| `AppVer`  
`settings.campaignId`| `CampaignId`  
`context.referrer.id`  
`properties.clickId`| `ClickId`  
`properties.currency`| `CurrencyCode`  
`context.traits.email`  
`properties.email`| `CustomerEmail`  
`userId`| `CustomerId`  
`context.traits.status`| `CustomerStatus`  
`anonymousId`| `CustomProfileId`  
`context.network.carrier`| `DeviceCarrier`  
`context.locale`| `DeviceLocale`  
`context.device.manufacturer`| `DeviceMfr`  
`context.device.model`| `DeviceModel`  
`context.device.type`  
`context.os.name`| `DeviceOs`  
`context.os.version`| `DeviceOsVer`  
`context.device.advertisingId`| `GoogAId`  
`context.ip`  
`request_ip`| `IpAddress`  
`properties.products[i].brand`| `ItemBrand{i}`  
`properties.products[i].category`| `ItemCategory{i}`  
`properties.products[i].name`| `ItemName{i}`  
`properties.products[i].price`| `ItemPrice{i}`  
`properties.products[i].coupon`| `ItemPromoCode{i}`  
`properties.products[i].quantity`| `ItemQuantity{i}`  
`properties.products[i].sku`| `ItemSku{i}`  
`context.location.latitude`| `Latitude`  
`context.location.longitude`| `Longitude`  
`properties.discount`| `OrderDiscount`  
`properties.coupon`  
`properties.coupon_id`| `OrderPromoCode`  
`properties.shipping`| `OrderShipping`  
`properties.tax`| `OrderTax`  
`context.referrer.url`  
`context.page.referrer`| `ReferringUrl`  
`context.page.url`  
`properties.url`  
`context.page.referrer`  
`context.referrer.url`| `PageUrl`  
`context.userAgent`| `UserAgent`  
  
> ![info](/docs/images/info.svg)
> 
> Apart from the required properties mentioned above, at least one of the `context.referrer.id`/`properties.clickId`, `userId`, `anonymousId`, `properties.coupon`/`properties.coupon_id`, `context.device.id`, `context.device.advertisingId`, or `context.device.id` is required to make a `track` call successfully.

## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) method lets you record your website’s page views with any additional relevant information about the viewed page. You can send a `page` call to impact.com via the [`PageLoad` endpoint](<https://integrations.impact.com/impact-brand/reference/create-a-pageload>).

A sample `page` call is as shown:
    
    
    rudderanalytics.page("category", "name", {
          path: "path",
          url: "url",
          title: "title"
        }
    

> ![info](/docs/images/info.svg)
> 
> The property mappings for `page` call are exactly the same as `identify` call. Refer to the property mappings section for more details.

## Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) call lets you record whenever your user views their mobile screen, with any additional relevant information about the screen. You can send a `screen` call to impact.com via the [`PageLoad` endpoint](<https://integrations.impact.com/impact-brand/reference/create-a-pageload>).

A sample `screen` call is as shown:
    
    
    [
      [RSClient sharedInstance] screen: @ "Sample Screen Name"
      properties: @ {
        @ "prop_key": @ "prop_value"
      }
    ];
    

> ![info](/docs/images/info.svg)
> 
> The property mappings for `screen` call are exactly the same as `identify` call. Refer to the property mappings section for more details.

## FAQ

#### How can I debug the impact.com errors?

Any errors may arise due to the failed pathing, invalid parameters, authentication errors, and network unavailability. Refer to the [impact.com Errors documentation](<https://integrations.impact.com/impact-brand/reference/errors>) for more information. Additionally, you can also refer to their [Rate Limits documentation](<https://integrations.impact.com/impact-brand/reference/rate-limits>) for more information on the API call limits.