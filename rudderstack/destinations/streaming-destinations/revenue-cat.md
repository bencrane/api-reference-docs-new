# Revenue Cat

Send your event data from RudderStack to Revenue Cat.

* * *

  * __4 minute read

  * 


[Revenue Cat](<https://www.revenuecat.com/>) is an in-app subscription platform that lets you analyze and grow your cross-platform app subscriptions.

RudderStack supports Revenue Cat as a destination to which you can seamlessly send your event data.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/revenue_cat>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web, Cloud, Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Unity, AMP , Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Revenue Cat** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Revenue Cat, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Revenue Cat**.
  2. Assign a name to the destination and click **Continue**.


### Connection settings

To successfully configure Revenue Cat as a destination, you will need to configure the following settings:

[![Revenue Cat connection settings](/docs/images/event-stream-destinations/rev-cat-connection-settings.webp)](</docs/images/event-stream-destinations/rev-cat-connection-settings.webp>)

  * **Public API Key** : Enter your Revenue Cat public API key.


> ![info](/docs/images/info.svg)
> 
> For more information on getting your Revenue Cat public API key, refer to the FAQ section below.

  * **X-Platform** : Select your app platform from the dropdown.


## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) method lets you identify a user and associate them to their actions. It also lets you record any traits about them like their name, email, etc.

RudderStack uses the `identify` call to create or update new subscribers in Revenue Cat. It maps `userId` (a required trait in every event) to Revenue Cat’s `app_user_id` before sending the data via the [`subscribers`](<https://docs.revenuecat.com/reference/subscribers>) API.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm",{
        email: "alex@example.com",
        phone: "+1-202-555-0146",
    })
    

### Traits mapping

RudderStack maps the following `identify` traits to the corresponding Revenue Cat attributes:

RudderStack trait| Revenue Cat attribute  
---|---  
`userId` (Required)| `app_user_id`  
`name`| `$displayName`  
`email`| `$email`  
`phone`| `$phoneNumber`  
`apnsTokens`| `$apnsTokens`  
`fcmTokens`| `$fcmTokens`  
`context.ip`, `request_ip`| `$ip`  
`appsflyerId`| `$appsflyerId`  
`iterableUserId`| `$iterableUserId`  
`mparticleId`| `$mparticleId`  
`onesignalId`| `$onesignalId`  
`airshipChannelId`| `$airshipChannelId`  
`clevertapId`| `$clevertapId`  
  
The following `identify` traits are also mapped to the corresponding Revenue Cat attributes:

> ![warning](/docs/images/warning.svg)
> 
> Revenue Cat **cannot modify** these attributes so you must send them **only once**.

RudderStack trait| Revenue Cat attribute  
---|---  
`idfa`/ `advertisingId`| `$idfa`  
`idfv`/ `device.id`| `$idfv`  
`gpsAdId`| `$gpsAdId`  
`advertisingId`| `$androidId`  
`campaign.name`| `$campaign`  
`creative`| `$creative`  
`keyword`| `$keyword`  
`mediaSource`| `$mediaSource`  
`ad`| `$ad`  
`addGroup`| `$adGroup`  
`adjustId`| `$adjustId`  
`fbAnonId`| `$fbAnonId`  
`iterableCampaignId`| `$iterableCampaignId`  
`iterableTemplateId`| `$iterableTemplateId`  
`mixpanelDistinctId`| `$mixpanelDistinctId`  
`amazonAdId`| `$amazonAdId`  
  
> ![warning](/docs/images/warning.svg)
> 
> The values for `iterableCampaignId` and `iterableTemplateId` must be valid non-negative, non-decimal integers. Otherwise, RudderStack will reject and skip these fields.

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) method lets you capture user events along with the properties associated with them.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Order Completed", {
      userId: "1hKOmRA4GRlm",
      currency: "USD",
      fetch_token: "12456",
      products: [{
          product_id: "123454387",
          name: "Game",
          price: 15.99,
          introductory_price: "24",
          is_restore: true,
          presented_offering_identifier: "123",
        }
      ],
    });
    

### Event mapping

> ![warning](/docs/images/warning.svg)
> 
> This destination does not strictly adhere to the [RudderStack Ecommerce Event Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).

RudderStack maps the `Order Completed` event to Revenue Cat’s `Purchase` event before sending it across via the [`receipts`](<https://docs.revenuecat.com/reference/receipts>) API. To do so, RudderStack requires the `userId` (mapped to `app_user_id`) and `fetch_token` properties to be present in the event.

### Property mapping

RudderStack maps the following event properties to the corresponding Revenue Cat attributes:

RudderStack property| Revenue Cat attribute| Comments  
---|---|---  
`userId` (Required)| `app_user_id`| -  
`fetch_token` (Required)| `fetch_token`| This must be a Base64 encoded **receipt file** for iOS, **receipt token** for Android, **receipt** for Amazon, and **subscription token** in case of Stripe.  
`currency`| `currency`| -  
`payment_mode`| `payment_mode`| -  
`product_id`, `products.product_id`| `product_id`| This is required for Google and should be the Apple, Google, or Amazon SKU or product identifier.  
`price`| `price`| -  
`introductory_price`| `introductory_price`| -  
`is_restore`| `is_restore`| -  
`presented_offering_identifier`| `presented_offering_identifier`| -  
  
## FAQ

#### Where can I find the Revenue Cat public API key?

To find the Revenue Cat public API key, follow these steps:

  1. Log into your [Revenue Cat dashboard](<https://app.revenuecat.com/>).
  2. From the top navigation bar, go to **Projects** and select your app:

[![Revenue Cat project in the dashboard](/docs/images/event-stream-destinations/rev-cat-project.webp)](</docs/images/event-stream-destinations/rev-cat-project.webp>)

  3. Under **Project settings** , select **API Keys**. You will find your public API keys under **Public app-specific API keys** :

[![Revenue Cat public API key](/docs/images/event-stream-destinations/rev-cat-public-api-key.webp)](</docs/images/event-stream-destinations/rev-cat-public-api-key.webp>)