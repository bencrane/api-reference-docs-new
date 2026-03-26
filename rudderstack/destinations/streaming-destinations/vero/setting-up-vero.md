# Setup Guide

Set up Vero as a destination in RudderStack.

* * *

  * __2 minute read

  * 


This guide will help you set up Vero as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Vero.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** AMP , Android (Java) , Android (Kotlin) , Cordova, Cloud, Flutter, iOS (Obj-C) , iOS (Swift) , React Native , Unity, Warehouse, Web, Shopify
  * Refer to it as **Vero** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Vero native SDK from the `https://d3qxef4rp70elm.cloudfront.net/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Vero SDK successfully.

## Get started

Once you have confirmed that the source supports sending events to Vero, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Vero**.
  2. Assign a name to your destination and click **Continue**.


## Connection settings

To successfully set up Vero as a destination in RudderStack, you need to configure the following settings:

[![Vero connection settings](/docs/images/event-stream-destinations/vero-connection-settings.webp)](</docs/images/event-stream-destinations/vero-connection-settings.webp>)

  * **Authentication Token** : Enter your Vero authentication token.
  * **API key** : Enter your Vero API key.


> ![info](/docs/images/info.svg)
> 
> For more information on obtaining your Vero authentication token and API key, refer to the FAQ section below.

### Web device mode settings

If you are sending events to Vero via [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>), then you need to configure the following settings:

  * **Client-side Events Filtering** : This optional setting lets you specify which events should be blocked or allowed to flow through using the SDK’s [client-side event filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) feature.
  * **Use device-mode to send events** : Enable this option to send events via [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


## FAQ

#### Where can I find the Vero API Key and Authentication Token?

To obtain your Vero API key and authentication token, follow these steps:

  1. Log into your [Vero dashboard](<https://app.getvero.com/>).
  2. In the left panel, go to **Settings** and scroll down to find the **API Credentials** section. You will find the **API Key** and **Auth Token** listed here:

[![Vero auth token and api key](/docs/images/event-stream-destinations/vero-authentication-token.webp)](</docs/images/event-stream-destinations/vero-authentication-token.webp>)