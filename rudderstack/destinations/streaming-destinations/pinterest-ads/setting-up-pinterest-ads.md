# Setup Guide

Set up Pinterest Tag as a destination in RudderStack.

* * *

  * __5 minute read

  * 


This guide will help you set up Pinterest Tag as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Pinterest.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Pinterest Tag** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Pinterest Tag native SDK from the `https://s.pinimg.com/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Pinterest Tag SDK successfully.

## Get started

Once you have confirmed that the source platform supports sending events to Pinterest Tag, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Pinterest Tag**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully configure Pinterest Tag as a destination, configure the following settings:

  * **Tag ID** : Enter your Pinterest Tag ID (required only for sending events via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>)).

  * **App Store App ID** : Enter the App Id from your App Store (required only for sending events using an iOS source).

  * **API Version** : Select the [Pinterest Tag API version](<https://developers.pinterest.com/docs/getting-started/migration/>) from the dropdown and enter the following values (required only for sending events via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>)):

**V3(deprecating soon)** :

    * **Pinterest Advertiser ID** : Enter the Advertiser ID of your Pinterest account.  
  


**V5** :

    * **Ad Account ID** : Enter your Pinterest’s Ad Account ID.
    * **Conversion Token** : Enter the Conversion Token associated with your Pinterest account.


### Other settings

  * **Send as test event** : RudderStack marks the event as test requests if this setting is turned on. It does not record the event but the API still returns the same response messages.


> ![info](/docs/images/info.svg)
> 
> Use this setting to verify if your requests are working and the events are constructed correctly.

  * **Enable hashing for user data conversions** : This setting is on by default and hashes your user data using SHA256 encoding.

  * **Enable Event Deduplication** : Turn on this setting to deduplicate the events. Then, specify the following:

    * **Deduplication key** : Enter the key using which Pinterest Tag should use to deduplicate the events.
  * **Enable Enhanced Match on Page Load** : This setting is on by default and attaches the hashed email address on the initial page load. Any further calls made to Pinterest will be an Enhanced Match.

When turned off, all visits made to your site become anonymous. However, you can still identify any user by making the `identify()` call.

RudderStack supports [Pinterest Enhanced Match](<https://help.pinterest.com/en/business/article/enhanced-match>) when the following conditions are met:

    * A user is identified every time they visit your site.
    * A user visits your site anonymously but is identified at a later stage by making an `identify()` call.

If you use RudderStack’s `identify()` method to use Pinterest’s Enhanced Match, you can only collect this information for successive events. Pinterest does not retroactively update the values for the past events.

  * **Send external_id for user** : Turn on this setting to send the user’s [`external_id`](<https://developers.pinterest.com/docs/conversions/external-id/>) to Pinterest Tag (applicable only for sending events via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>)).

  * **Send as custom event** : Turn on this setting to send an unmapped event as a Pinterest custom event. If an event is neither mapped in the **Map Your Events To Pinterest Events** dashboard setting nor is one of the [ecommerce tracking events](<https://www.rudderstack.com/docs/destinations/streaming-destinations/pinterest-ads/pinterest-ads-cloud-mode/#ecommerce-conversion-tracking>), it will be sent as a custom event.

  * **Custom Properties** : Enter any custom properties which should be sent to Pinterest (applicable only for sending events via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>)). For more information on using the custom properties, refer to the [Custom properties](<https://www.rudderstack.com/docs/destinations/streaming-destinations/pinterest-ads/pinterest-ads-device-mode/#custom-properties>) section.

  * **Map Your Events To Pinterest Events** : Use this field to map RudderStack events to Pinterest Standard Conversion Events.


> ![info](/docs/images/info.svg)
> 
> Note that RudderStack gives the highest priority to the event mapping specified in this setting.
> 
>   * If not specified, it gives priority to the [standard ecommerce event mappings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/pinterest-ads/pinterest-ads-device-mode/#ecommerce-conversion-tracking>).
>   * If **Send as custom event** toggle is turned on, then RudderStack sends the event with name `custom` to Pinterest.
>   * If none of the above qualifies:
>     * RudderStack sends the event name to Pinterest as is and it is shown as an `unknown` event in the Pinterest dashboard.
> 


### Client-side events filtering

This setting is applicable only if you are sending events to Pinterest Tag via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>). Refer to the [Client-side Event Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide for more information.

### Consent Settings

Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.

### Web SDK Settings

  * **Use device-mode to send events** : If you are using the [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, this setting is on by default and cannot be turned off.


## FAQ

#### How do I get the Pinterest Tag ID?

  1. Log in to your [Pinterest Ads dashboard](<https://ads.pinterest.com/>).
  2. Click the **Ads** dropdown and go to **Conversions**.
  3. In the Pinterest Tag Manager, click **Get Started** and you will see your Tag ID:

[![](/docs/images/event-stream-destinations/tag-id-pinterest.webp)](</docs/images/event-stream-destinations/tag-id-pinterest.webp>)

#### How do I get the Ad account ID?

Refer to the [Pinterest documentation](<https://developers.pinterest.com/docs/conversions/conversions/#Find%20your%20ad_account_id>) to get the Pinterest Ad account ID.

#### How to get the conversion token?

Refer to the [Pinterest documentation](<https://developers.pinterest.com/docs/conversions/conversions/#Get%20the%20conversion%20token#Get%20the%20conversion%20token>) to get the conversion token associated with your account.