# Setup Guide

Set up Iterable as a destination in RudderStack.

* * *

  * __5 minute read

  * 


This guide will help you set up Iterable as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Iterable.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Iterable** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Iterable, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Iterable**.
  2. Assign a name to your destination and click **Continue**.


## Connection settings

To successfully configure Iterable as a destination, you will need to configure the following settings:

  * **Iterable API Key** : Enter your Iterable API key. You can obtain it by going to the **API Configuration Settings** section in your Iterable account.


### Other settings

  * **Map All Pages to Single Event Name** : If this setting is enabled, all pages will be tracked to Iterable with the same event name.
    * For `page` events, RudderStack will set the event name as `Loaded a Page`.
    * For `screen` events, RudderStack will set the event name as `Loaded a Screen`.
  * **Track All Pages** : If this setting is enabled, all page events will be sent to Iterable.
  * **Track Categorized Pages** : If this setting is enabled, only pages with a category present will be tracked.
  * **Track Named Pages** : If this setting is enabled, RudderStack will track only the pages having a name.
  * **Create new user if userID exists** : If enabled, RudderStack creates a new user in Iterable if `userId` is present in the event using the `preferUserId` parameter. For more information, see Iterable’s [Update user data API](<https://api.iterable.com/api/docs#users_updateUser>).
  * **Merge top-level objects** : If enabled, Iterable merges the top-level objects instead of overwriting them using the `mergeNestedObjects` parameter. For more information, see Iterable’s [Update user data API](<https://api.iterable.com/api/docs#users_updateUser>).


### Web SDK settings

The following settings are applicable if you’re sending the events to Iterable via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) using the [Iterable web SDK (Beta)](<https://github.com/Iterable/iterable-web-sdk>):

> ![info](/docs/images/info.svg)
> 
> It is highly recommended to use this method if you want to leverage Iterable’s web push notifications feature for your website.

  * **Use device mode to send events** : Enable this setting to send your events to Iterable via web device mode.
  * **Mapping to trigger the getInApp messages** : Use this setting to specify the event names for which you want to trigger the website push notifications.
  * **Mapping to trigger the purchase events** : Use this setting to specify the event names for which you want to trigger the Iterable purchase events.
  * **Identifier to identify a user over a session** : Select the identifier from **Email** and **UserID**. RudderStack uses this identifier to uniquely identify a user during the session.
  * **Trigger a track event for web in-app push** : Enable this setting to track your website in-app push notifications.
  * **Package Name** : Enter the name of your website for which the in-app notifications are shown.


### In-app message settings

The following settings let you customize the on-screen position, timing, content, and behavior of the in-app notifications:

  * Time (in ms) for messages to animate in and out
  * Space (px or %) between screen bottom & messages
  * Space (px or %) between screen right & messages
  * Space (px or %) between screen top & messages
  * Wait time for next message
  * Control how to open links
  * Screen Reader Text
  * Focus Element
  * Color of Close button
  * Size of Close button
  * Position
  * Space between button & container top
  * Space between button & container side
  * Custom pathname
  * Prevent user dismissing in-app message by clicking outside message
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


## Send data to Iterable catalogs

> ![info](/docs/images/info.svg)
> 
> This feature requires access to the `catalog` API. Contact your Iterable customer success manager to add the catalog feature to your Iterable account.

RudderStack supports sending data to your Iterable [catalog](<https://support.iterable.com/hc/en-us/articles/360033215152-Using-Catalog->) when connected to a [Reverse ETL](<https://www.rudderstack.com/docs/sources/reverse-etl/>) source.

While connecting a Reverse ETL source to the Iterable destination using the [Visual Data Mapper](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/visual-data-mapper/#use-visual-data-mapper>), you can see the Iterable catalogs listed in the **Object** dropdown :

[![Iterable catalog](/docs/images/event-stream-destinations/iterable-catalog-object.webp)](</docs/images/event-stream-destinations/iterable-catalog-object.webp>)

You can then map the catalog fields with warehouse columns where `Item ID` is a **required** field:

[![Iterable catalog](/docs/images/event-stream-destinations/iterable-catalog.webp)](</docs/images/event-stream-destinations/iterable-catalog.webp>)

> ![warning](/docs/images/warning.svg)
> 
> Verify that your Iterable account has access to the `catalog` API if RudderStack returns only the **User** object in the dropdown and does not show any catalog objects.

## FAQ

#### Where can I find the Iterable API key?

You can get the Iterable API key by navigating to **Integrations** > **API Keys**. For more information, refer to this [Iterable documentation](<https://support.iterable.com/hc/en-us/articles/360043464871-API-Keys>).

#### What does the **Track Named Pages** setting imply?

If the **Track Named Pages** setting is enabled in the RudderStack dashboard, RudderStack will only track the pages that have a name assigned to them.

#### What does the **Track Categorized Pages** imply?

If the **Track Categorized Pages** setting is enabled in the RudderStack dashboard, RudderStack will only track the pages that have a category assigned to them.