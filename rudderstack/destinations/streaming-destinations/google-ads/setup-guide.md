# Google Ads Destination Setup Guide

Set up Google Ads as a destination in RudderStack.

* * *

  * __4 minute read

  * 


This guide will help you set up Google Ads as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Google Ads.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **Google Ads** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Google Ads native SDK from the `https://www.googletagmanager.com/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Google Ads SDK successfully.

## Setup

In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Google Ads**.

### Connection settings

Setting| Description  
---|---  
Ecommerce event spec support for track events| This setting is turned on by default and causes RudderStack to follow the [Ecommerce Event Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>) to send the `track` events to Google Ads.  
Allow identify calls for the Google Ads destination| Turn on this setting to allow RudderStack to send `identify` calls (used to define enhanced conversion fields) to Google Ads.  
Conversion ID| Enter your [Google Ads Conversion ID](<https://support.google.com/tagmanager/answer/6105160?hl=en>).  
Map RudderStack events to standard Google Ads events| Use this setting to map custom events to the standard Google Ads events.  
  
### Track event settings

Setting| Description  
---|---  
Track Conversions| This setting is turned on by default and sends your conversion events to Google Ads. You can disable it to prevent RudderStack from sending the conversion events.  
Enable Conversion Events Filtering| This setting is visible if **Track Conversions** setting is toggled on.  
  
Use it to enter a list of events you want to send as conversion events in the **Events to Track Conversions** setting. If toggled off, RudderStack sends all the events to Google Ads as conversion events.  
Track Dynamic Remarketing| Turn on this setting to send your [dynamic remarketing](<https://support.google.com/google-ads/answer/7305793>) events.  
Enable Dynamic Remarketing Events Filtering| This setting is visible if **Track Dynamic Remarketing** setting is toggled on.  
  
Use it to enter a list of events you want to send as dynamic remarketing events in the **Events to Track Dynamic Remarketing** setting. If turned off, RudderStack sends all events as dynamic remarketing events.  
  
### Event filtering settings

Setting| Description  
---|---  
Client-side Events Filtering| Specify which events should be blocked or allowed to flow through to Google Ads. See the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide for more information.  
  
### Page load conversion settings

For `page` calls, you can configure the following settings for multiple instances:

Setting| Description  
---|---  
Conversion Label| Specify the conversion label from Google Ads.  
Name| Enter the name of the `page` event associated with the page load conversion.  
Default Conversion Label| Specify the name to set as the default conversion label.  
  
### Click event conversion settings

Setting| Description  
---|---  
Conversion Label| Specify the conversion label from Google Ads.  
Name| Enter the name of the `track` event to send to Google Ads.  
  
### Other settings

Setting| Description  
---|---  
Send Page View| Turn on this setting to automatically send your `page` events to Google Ads.  
Conversion Linker| This setting is toggled on by default. Turn off this setting if you don’t want the global site tag (`gtag.js`) to set first-party cookies on your website domain. See the [Google Ads documentation](<https://support.google.com/google-ads/answer/7521212?hl=en>) for more information on this feature.  
  
**Note** : Turning off this feature can lead to less accurate conversion measurements.  
Disable Ad Personalization| Turn on this setting to disable ad personalization programmatically.  
Send Event Label As Conversion for Conversion Events| Turn on this setting to set the conversion events label to `conversion`. Otherwise, RudderStack sets the label to the respective event name.  
Allow Enhanced Conversions| Turn on this setting to [send enhanced conversions](<https://support.google.com/google-ads/answer/12785474>) programmatically.  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
Use device mode to send events| As this is a [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>)-only integration, this is turned on by default and **cannot** be toggled off.  
  
## Next steps

  * [Send events in device mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-ads/device-mode/>)


## FAQ

#### How do I get the conversion ID in Google Ads?

You can get the conversion ID from your global site tag snippet.

For example, a sample conversion ID would look like `AW-123456789`.

#### How do I get the conversion label for Google Ads?

You can find the value of the **Conversion Label** from your event snippet.

For example, a event snippet can look like `send_to: 'AW-123456789/bpg3CMiIjLMBELXBp8wC'`. The corresponding conversion label in this case is `bpg3CMiIjLMBELXBp8wC`.