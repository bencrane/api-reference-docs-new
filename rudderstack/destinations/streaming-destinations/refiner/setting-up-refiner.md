# Setup Guide

Set up Refiner as a destination in RudderStack.

* * *

  * __3 minute read

  * 


This guide will help you set up Refiner as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Refiner.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web, Cloud, Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Unity, AMP , Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Refiner** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Refiner, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Refiner**.
  2. Assign a name to your destination and click **Continue**.


## Connection settings

To successfully set up Refiner as a destination, you need to configure the following settings:

  * **Refiner REST API Key** : Enter your Refiner REST API key.
  * **Refiner Web Client API Key** : Enter your web client API key.


> ![info](/docs/images/info.svg)
> 
> For more information on obtaining the Refiner REST API key and web client API key, refer to the FAQ section below.

  * **Map Rudder user attributes to Refiner contact traits** : Use this setting to map specific properties from the RudderStack event to Refiner’s contact traits.
  * **Map Rudder account attributes to Refiner account traits** : Use this setting to map specific properties from the RudderStack event to Refiner’s account traits.
  * **Client-side Events Filtering** : This setting lets you specify which events should be blocked or allowed to flow through to Refiner. For more information on this setting, refer to the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide.
  * **Use device mode to send events** : Enable this setting to send your events to Refiner via [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


## FAQ

#### Where can I find the Refiner REST API key and web client API key?

To get your Refiner REST API key and web client API key, follow these steps:

  1. Log into your [Refiner dashboard](<https://app.refiner.io/>).
  2. From the left sidebar, click the **Integrations** icon and go to **REST API**. You will find the REST API Key listed here under **Secret API Key** :

[![Refiner REST API key](/docs/images/event-stream-destinations/refiner-rest-api-key.webp)](</docs/images/event-stream-destinations/refiner-rest-api-key.webp>)

  3. To get your Refiner web client API key, click the **Settings** icon from the left sidebar and go to **Web Client**. You will find the API key listed here:

[![Refiner web client API key](/docs/images/event-stream-destinations/refiner-web-client-api-key.webp)](</docs/images/event-stream-destinations/refiner-web-client-api-key.webp>)