# Setup Guide

Set up Engage as a destination in RudderStack.

* * *

  * __2 minute read

  * 


This guide will help you set up Engage as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Engage.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Engage** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Engage, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Engage**.
  2. Assign a name to your destination and click **Continue**.


## Connection settings

To successfully set up Engage as a destination, you need to configure the following settings:

  * **Public Key** : Enter your Engage public key. For more information on obtaining your Engage public key, refer to the FAQ section below.
  * **Private Key** : Enter your Engage private key here. This key is required for deleting a user or updating their email in Engage.
  * **List IDs** : Enter your Engage list ID. You can get it by logging into your Engage dashboard and going to **Lists** > clicking your list > **Subscription and Settings** > **Your list ID**.
  * **Client-side Events Filtering** : This setting lets you specify which events should be blocked or allowed to flow through to Engage. For more information on this setting, refer to the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide.
  * **Use device mode to send events** : Enable this setting to send your events to Engage via [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).


## FAQ

#### Where can I find the Engage Public Key and Private Key?

To get your Engage public key and private key, follow these steps:

  1. Log into your [Engage dashboard](<https://app.engage.so/auth/login>).
  2. Navigate to **Settings** > **Account** > **Your API Key** :

[![Public and Private Key in Engage dashboard](/docs/images/event-stream-destinations/engage-public-private-key.webp)](</docs/images/event-stream-destinations/engage-public-private-key.webp>)