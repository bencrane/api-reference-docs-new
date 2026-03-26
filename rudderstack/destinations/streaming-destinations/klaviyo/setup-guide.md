# Setup Guide

Set up and configure Klaviyo as a destination in RudderStack.

* * *

  * __3 minute read

  * 


This guide will help you set up Klaviyo as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Klaviyo.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Klaviyo** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Klaviyo native SDK from `https://static.klaviyo.com/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Klaviyo SDK successfully.

## Setup

In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Klaviyo**.

### Connection settings

Setting| Description  
---|---  
Name| Assign a name to uniquely identify the destination.  
Public API Key| Enter the unique public API key from your [Klaviyo dashboard](<https://www.klaviyo.com/login>) (under **Settings** > **Account**).  
Private API Key| Enter the private API key from your [Klaviyo dashboard](<https://www.klaviyo.com/login>) (under **Settings** > **Account**). This key lets you add users to a list or subscribe them using personalised emails/SMS.  
API Version to use| Select the relevant API version from the dropdown:  
  


  * 2024-10-15
  * 2023-02-22 (**deprecated**)

  
  
### Configuration settings

Configure the below settings to receive your data correctly in Klaviyo.

Setting| Description  
---|---  
List ID| Enter the default list ID to which you want to add or subscribe the identified users.  
Consent| Select the consent type from **E-mail** , **SMS** , or both. `consent` is a Klaviyo-specific property that you need to include in your events if you run a GDPR-compliant business.  
  
**Note** : You can also override this setting by specifying the `consent` field in your event properties.  
Enable this option to make email or phone as primary identifier| Turn on this setting to set a custom attribute `_id` and `$email` as the primary identifier when passed in `traits.email`/`properties.email`. RudderStack **does not** set `$id` field to the `userId` while sending the events.  
  
When disabled, RudderStack uses `userId` (`anonymousId`, if `userId` is absent) for mapping the user with a unique identifier. In case `userId` and `anonymousId` are absent, RudderStack sends `email` or `phone` as the user’s primary identifier.  
  
Note that:

  * This setting is applicable only for the `identify` and `track` calls.
  * Use this setting only if you are experiencing issues with duplicate profiles created in your Klaviyo account.

  
Enable to flatten user/event properties| Turn on this setting to flatten the following data before sending it to Klaviyo:

  * User properties in `identify` calls.
  * Event properties in `track` calls.

  
  
### Consent settings

Configure the below settings for cloud or web device mode based on your setup:

Setting| Description  
---|---  
Consent management provider| Select the relevant consent management provider from the dropdown.  
  
**Note** : You can add multiple consent management providers by clicking **Add group condition**.  
Enter consent category IDs| Enter the consent category IDs you defined while setting up the consent management provider.  
  
## Next steps

  * [Send events in cloud mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/klaviyo/cloud-mode/>)
  * [Send events in device mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/klaviyo/device-mode/>)