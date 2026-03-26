# Setup Guide

Set up Rockerbox as a destination in RudderStack.

* * *

  * __3 minute read

  * 


This guide will help you set up Rockerbox as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Rockerbox.

## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), go to **Directory** > **Destinations** > **Cloud Destinations** and search for **Rockerbox**.
  2. Connect your source and click **Continue**.


### Connection settings

Configure the following settings to set up Rockerbox as a destination in RudderStack:

  * **Name** : Assign a name to uniquely identify the destination.
  * **Advertiser Id** : Enter your [Rockerbox Advertiser ID](<https://help.rockerbox.com/article/5t050dmcxv-webhooks#requirements:~:text=or%20other%20formats-,Server%2Dside%20specs,-You%20will%20need>). It is a required field for sending events to Rockerbox via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>). To obtain this ID, contact your Rockerbox account manager.


### Connection mode

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** AMP , Android (Java) , Android (Kotlin) , Cordova, Cloud, Flutter, iOS (Obj-C) , iOS (Swift) , React Native , Unity, Warehouse, Web, Shopify
  * Refer to it as **Rockerbox** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Rockerbox native SDK from `https://${host}/assets/${library}.js` domain. See the [source code](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/Rockerbox/browser.js#L20-L21>) for obtaining the `host` and `library` values.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Rockerbox SDK successfully.

### Send events in hybrid mode

Hybrid mode lets you use a destination in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>) and [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) simultaneously, meaning you can route some calls through server-side and others through the client-side SDK.

For the Rockerbox destination, RudderStack supports:

  * `identify` and `page` calls in device mode
  * `track` calls in cloud mode


## Configuration settings

After completing the initial setup, configure the following settings to correctly receive your data in Rockerbox.

### Web SDK settings

The following settings are applicable **only if** you are sending events to Rockerbox via web device mode:

  * **Client Auth ID** : Enter your Rockerbox Client Auth ID. You can obtain the Client Auth ID from your **Rockerbox All Pages** tag available in the Rockerbox Attribution platform. For more information, see [Rockerbox documentation](<https://help.rockerbox.com/article/unydvsq7jr-site-direct-all-pages-pixel#:~:text=Your%20pixel%20will%20have%20an%20alphanumeric%20ID%20instead%20of%20the%20CLIENT_AUTH_ID%20placeholder>).
  * **Custom Domain** : Enter the custom domain from where you want to load the pixels.


> ![info](/docs/images/info.svg)
> 
> Rockerbox lets you use a Custom Tracking Domain to load the Rockerbox trackers and pixels from your website’s domain (for example, `rb.mysite.com`) instead of `getrockerbox.com`. For more details, see [Rockerbox documentation](<https://help.rockerbox.com/article/iel8eh361t-cname-integration>).

  * **Enable Cookie Sync** : Enable this setting if you are using a custom domain. It ensures that the Custom Tracking Domain functionality works as expected.


### Other settings

  * **Client-side event filtering** : This setting lets you specify which events should be blocked or allowed to flow through to Rockerbox and is applicable only if you’re sending events via the **web device mode**. See [Client-side Event Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide for more information.
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


### Event mapping

  * **Map your RudderStack events to Rockerbox Events** : This setting lets you map the RudderStack events/properties to the Rockerbox custom events and properties. Click **Set up mapping** and specify the mappings. RudderStack also provides the JSON mapper to set the mappings.

[![JSON mapper](/docs/images/event-stream-destinations/json-mapper.webp)](</docs/images/event-stream-destinations/json-mapper.webp>)

> ![success](/docs/images/tick.svg)
> 
> You can map multiple **RudderStack events** for one **Rockerbox event** and vice versa.