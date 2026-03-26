# Singular Destination Setup Guide

Set up Singular as a destination in RudderStack.

* * *

  * __3 minute read

  * 


This guide will help you set up Singular as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Singular.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Flutter, React Native , Cordova, AMP , Cloud, Warehouse, Shopify, Web, Unity
  * Refer to it as **Singular** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
AMP| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Java)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cloud| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cordova| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Swift)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
React Native| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
Shopify| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Unity| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Warehouse| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Android (Java)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cordova| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
React Native| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Set up Singular destination in RudderStack

In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Singular**.

### Connection settings

Setting| Description  
---|---  
API key| Enter your Singular API key.  
Secret| Enter your Singular secret. It is required for device mode integrations with the RudderStack iOS (Obj-C) and Android (Java) SDKs.  
Session event name| Enter the event names to be used as session events. This setting is applicable only for sending session events to Singular in [cloud mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/singular/cloud-mode/>).  
  


> ![warning](/docs/images/warning.svg)Configure this field only if you are not using Singular SDK for [session management](<https://support.singular.net/hc/en-us/articles/360037640812-Server-to-Server-Integration-Guide#h_01S2S004>).  
>   
> See Considerations for session event name section below for more information.  
  
Use device mode to send events| When using the Android (Java) / iOS (Obj-C) source, turn on this setting to send events in [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>). Then, follow the [Singular Device Mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/singular/device-mode/>) guide for steps on adding the Singular integration to your project.  
Client-side events filtering| Specify which events should be blocked or allowed to flow through to Singular.  
  
See [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) for more information.  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs.  
  
See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
#### Considerations for session event name

The Singular SDK manages session events automatically. Hence, configure the **Session Event Name** dashboard setting only if you are not initializing the Singular SDK separately in your application (outside of RudderStack).

> ![warning](/docs/images/warning.svg)
> 
> Configuring the **Session Event Name** in RudderStack while the Singular SDK is already managing session events will cause RudderStack to send session events as well, resulting in duplicate session events in Singular.

### Unity SDK settings

Setting| Description  
---|---  
Match ID mapping| Use this setting to map Singular’s match ID either of the following event fields:  
  


  * `context.device.advertisingId`
  * `properties.match_id`

  
  
## FAQ

#### Where can I find the Singular API key and secret?

To obtain your Singular API key and secret, log into your [Singular dashboard](<https://app.singular.net/login?redir=%2F#/>) and navigate to **Settings** > **SDK Keys** :

[![Singular API key](/docs/images/event-stream-destinations/singular-api-key.webp)](</docs/images/event-stream-destinations/singular-api-key.webp>)