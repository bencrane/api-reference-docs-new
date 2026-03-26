# Setup Guide

Send your event data from RudderStack to TikTok Ads.

* * *

  * __4 minute read

  * 


This guide will help you set up TikTok Ads as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to TikTok Ads.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web, Cloud, iOS (Obj-C) , iOS (Swift) , Android (Java) , Android (Kotlin) , Unity, AMP , Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **TikTok Ads** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the TikTok Ads native SDK from the `https://analytics.tiktok.com` domain. Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the TikTok Ads SDK successfully.

## Setup

In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **TikTok Ads**.

### Connection settings

Setting| Description  
---|---  
Event version to use| Select the TikTok Ads Events API version to use from the dropdown.  
  


> ![warning](/docs/images/warning.svg)RudderStack recommends using the [Events 2.0 API](<https://business-api.tiktok.com/portal/docs?id=1771101276978178>) to send your events as [Events 1.0 API will be sunset](<https://business-api.tiktok.com/portal/docs?id=1739657891856385>) by the second half of 2024.  
  
Access Token| Enter the access token (also called long-term access token). You can generate it by following the steps mentioned in [Authorization](<https://ads.tiktok.com/marketing_api/docs?id=1701890912382977>) and [Authentication](<https://ads.tiktok.com/marketing_api/docs?id=1701890914536450>) topics of the TikTok documentation.  
Pixel Code| Enter the TikTok Ads pixel code. See [TikTok documentation](<https://ads.tiktok.com/gateway/docs/index?identify_key=2b9b4278e47b275f36e7c39a4af4ba067d088e031d5f5fe45d381559ac89ba48&language=ENGLISH&doc_id=1701890979375106#item-link-Where%20to%20Find%20pixel_code>) for more information on obtaining the pixel code.  
Hash Contextual User Properties (SHA-256)| If this setting is turned on, RudderStack hashes the contextual user properties like `external_id`, `email`, `phone_number` in the SHA-256 format.  
  
### Event settings

> ![warning](/docs/images/warning.svg)
> 
> Note the following before configuring the event mappings in the RudderStack dashboard:
> 
>   * You must [create the standard events in Events Manager](<https://ads.tiktok.com/help/article/standard-events-parameters?lang=en#anchor-1>) along with the required fields. Otherwise, RudderStack will send the events but they will not be visible in your TikTok dashboard.
>   * Before sending the event properties, make sure they are configured for the respective standard events in your TikTok dashboard, otherwise they will be discarded.
> 


Setting| Description  
---|---  
Mapping to trigger the TikTok Ads standard events for the respective events| Enter the event name and select the corresponding [TikTok Ads standard event](<https://ads.tiktok.com/help/article?aid=10028>) to be triggered when that event is called. You can specify multiple **Standard Events** for one **Event Name** and vice versa.  
Send custom events| Turn on this setting to send custom events to TikTok Ads.  
  
Note that:  
  


  * To send custom events to TikTok Ads using [RudderStack Open Source](<https://app.rudderstack.com/signup?type=opensource>), you should be using [`rudder-transformer`](<https://github.com/rudderlabs/rudder-transformer>) v1.52.0 or later.
  * For custom events, RudderStack maps only the [standard fields](<https://github.com/rudderlabs/rudder-transformer/blob/0e1429663d167a2c5cded0d9130374eb586a18c0/src/v0/destinations/tiktok_ads/data/TikTokTrack.json>) supported by TikTok Ads and drops all other fields in the event. See [TikTok Ads standard fields](<https://business-api.tiktok.com/portal/docs?id=1741601162187777>) documentation for more information.

  
  
Note that RudderStack supports the following TikTok [standard events](<https://ads.tiktok.com/help/article/standard-events-parameters?lang=en>):

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

### Event filtering settings

Setting| Description  
---|---  
Client-side Events Filtering| This setting lets you specify which events should be blocked or allowed to flow through to TikTok Ads when sending events via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>). For more information on this setting, see [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>).  
  
### Web device mode settings

Setting| Description  
---|---  
Use device mode to send events| Turn on this setting to send events from the JavaScript SDK to Tiktok Ads via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
## FAQ

#### How do I create a pixel in TikTok Ads?

See [TikTok documentation](<https://ads.tiktok.com/help/article/get-started-pixel?lang=en>) for detailed steps on creating a pixel.

#### How can I verify if my data is delivered to TikTok successfully?

You can use this [Google Chrome extension](<https://chrome.google.com/webstore/detail/tiktok-pixel-helper/aelgobmabdmlfmiblddjfnjodalhidnn>) to troubleshoot your Pixel installation for any errors and verify if your events are delivered to TikTok.