# Setup Guide

Send your event data from RudderStack to Drip.

* * *

  * __2 minute read

  * 


This guide will help you set up Drip as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Drip.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **Drip** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Drip native SDK from the `https://tag.getdrip.com` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Drip SDK successfully.

## Get started

Once you have confirmed that the source supports sending events to Drip, follow these steps:

  * From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. From the list of destinations, select **Drip**.
  * Give a name to the destination and click **Next**. You should then see the following screen:


[![](/docs/images/3%20%2827%29.webp)](</docs/images/3%20%2827%29.webp>)Connection Settings for Drip

  * Next, enter your Drip **Account ID**. To get your **Account ID** , [sign in](<https://login.getdrip.com/login/email>) to your Drip dashboard and go to **Settings** \- **Account**. Scroll down to see your Account ID.

![](https://user-images.githubusercontent.com/59817155/128679489-3cce8c00-3203-4ec6-ac7b-ae883fcd4e69.png)

  * Enter your Drip **API Token**. To get your Drip API token, go to **Settings** \- **User Settings** in your Drip dashboard.

![](https://user-images.githubusercontent.com/59817155/128698438-9e37b1ca-eb3b-4217-9deb-53a47ded5119.png)

> ![info](/docs/images/info.svg)
> 
> The API token is required when using cloud mode to send your data.

  * Enter your **Campaign ID**. To get your campaign ID, go to **Campaigns** \- **Email Series** and choose the relevant campaign. The last part of the URL is the campaign ID, e.g. `https://www.getdrip.com/account_id/campaigns/campaign_id`.


> ![info](/docs/images/info.svg)
> 
> If the Campaign ID is provided, RudderStack will try to subscribe the users by default.

> ![success](/docs/images/tick.svg)
> 
> You can also send your Campaign ID via the `identify` call, which takes a higher precedence.

  * **User Creation Mode** This option lets you create the user with their `email` using the `track` call, if the user doesn’t already exist.
  * **Use device-mode to send events** : Enable this option to send events via the web [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).
  * Finally, click **Next**. That’s it! Drip will now be enabled as a destination in RudderStack.