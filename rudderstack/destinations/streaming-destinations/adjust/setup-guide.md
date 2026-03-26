# Adjust Destination Setup Guide

Set up Adjust as a destination in RudderStack.

* * *

  * __3 minute read

  * 


This guide will help you set up Adjust as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Adjust.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Unity, Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Adjust** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Android (Java)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
Cloud| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cordova| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Swift)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
React Native| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Shopify| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Unity| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
Warehouse| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Android (Java)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Swift)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Unity| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), set up a source.
  2. Go to the **Overview** tab of your source and select **Add Destination** > **Create new destination**.

[![Add new destination in RudderStack dashboard](/docs/images/event-stream-destinations/add-new-destination.webp)](</docs/images/event-stream-destinations/add-new-destination.webp>)

  3. Select **Adjust** from the list of destinations. Then, click **Continue**.


## Connection settings

Setting| Description| Applicable connection modes  
---|---|---  
App Token| Enter your Adjust app token.| Cloud and Device modes  
Send to production environment in Adjust| Turn on this toggle to send the data to the production environment in Adjust.  
  
By default, RudderStack sends the data to the Adjust sandbox environment.| Cloud and Device modes  
Client-side events filtering| This setting lets you specify which events should be blocked or allowed to flow through to Adjust.  
  
See the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide for more information on this feature.| Device mode  
Map events to Adjust event tokens| This setting lets you map the RudderStack events to Adjust’s [event tokens](<https://help.adjust.com/en/article/add-events#manage-your-events>).  
  
See the FAQ for more information on creating an event token in Adjust.| Cloud and Device modes  
RudderStack parameters to Adjust partner parameters| This setting lets you map your event properties to specific Adjust [partner parameters](<https://help.adjust.com/en/article/receive-custom-event-data-with-partner-parameters>).| Cloud and Device modes  
Delay time before SDK initialization| Use this setting to initiate a delay in loading the SDK for the first time.| Device mode  
Use device mode to send events| Turn on this toggle to send events to Adjust in [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).  
  


> ![warning](/docs/images/warning.svg)Do not add native Adjust SDK to your project as it will prevent you from integrating it successfully.

| Device mode  
Enable Install Attribution| Turn on this toggle to automatically track the `Install Attributed` event when the app is installed for the first time.  
  
See the [App install attribution](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/device-mode/#app-install-attribution>) section for more information on this feature.| Device mode  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs.  
  
See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/>) for more information on this feature.| Cloud and Device modes  
  
## Next steps

After setting up your Adjust destination in RudderStack:

  * See the [Adjust Cloud Mode Integration](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/cloud-mode/>) guide to understand how RudderStack maps and sends events to Adjust in cloud mode
  * See the [Adjust Device Mode Integration](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/device-mode/>) guide to understand how RudderStack maps and sends events to Adjust in device mode
  * See the detailed [FAQ](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/faq/>) guide for answers to the commonly asked questions on this integration


## FAQ

#### Where can I find the Adjust app token?

To get your Adjust app token, follow these steps:

  1. Log into your [Adjust dashboard](<https://dash.adjust.com/#/>).
  2. Find your app and select the app options caret (^):

[![Adjust app token](/docs/images/event-stream-destinations/adjust-app-token-1.webp)](</docs/images/event-stream-destinations/adjust-app-token-1.webp>)

  3. You will find your app token listed here.

[![Adjust app token](/docs/images/event-stream-destinations/adjust-app-token-2.webp)](</docs/images/event-stream-destinations/adjust-app-token-2.webp>)

#### How can I create a new event token in Adjust?

To create a new event token, follow these steps:

  1. Log into your [Adjust dashboard](<https://dash.adjust.com/#/>).
  2. Find your app and select the app options caret (^):

[![Adjust app token](/docs/images/event-stream-destinations/adjust-app-token-1.webp)](</docs/images/event-stream-destinations/adjust-app-token-1.webp>)

  3. Go to **All Settings** > **Events** :

[![Adjust event token](/docs/images/event-stream-destinations/adjust-event-token.webp)](</docs/images/event-stream-destinations/adjust-event-token.webp>)

  4. Under **CREATE NEW EVENT** , enter the name of the event token and click **CREATE**.