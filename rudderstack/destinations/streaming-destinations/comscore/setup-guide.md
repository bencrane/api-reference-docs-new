# comScore Setup Guide

Set up comScore as a destination in RudderStack.

* * *

  * __3 minute read

  * 


This guide will help you set up comScore as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to comScore.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web
  * Refer to it as **Comscore** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Android (Java)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Swift)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Android (Java)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), set up a source.
  2. Go to the **Overview** tab of your source and select **Add Destination** > **Create new destination**.

[![Add new destination in RudderStack dashboard](/docs/images/event-stream-destinations/add-new-destination.webp)](</docs/images/event-stream-destinations/add-new-destination.webp>)

  3. Select **comScore** from the list of destinations. Then, click **Continue**.


## Connection settings

Setting| Description  
---|---  
Publisher ID| Enter the client ID/C2 value associated with your mobile app.  
  
See FAQ for more information on obtaining this value.  
  
## Web SDK settings

Setting| Description  
---|---  
Use device mode to send events| This setting is turned on by default as this is a device mode-only integration.  
Map RudderStack page properties to comScore parameters| Use this setting to map the RudderStack `page` event properties to specific comScore parameters.  
  


> ![warning](/docs/images/warning.svg)If you do not specify these mappings, RudderStack uses the [default mappings](<>) instead.  
  
## Android/iOS SDK settings

Setting| Description  
---|---  
App Name| Enter your source app name. RudderStack includes this parameter in the events to specify the source app for getting the tags and data.  
Only auto update when app is in foreground| This setting is turned on by default and updates your app usage data only when the application runs in the foreground.  
Auto update when app is in foreground and background| Turn on this setting to update your app usage data when the application is running in the foreground and background.  
  


> ![warning](/docs/images/warning.svg)If turned on, this setting overrides the **Only auto update when app is in foreground** setting.  
  
Auto update interval| Use this setting to specify the time interval between the updates.  
  


> ![info](/docs/images/info.svg)This setting is applicable only if the auto updates are turned on.  
  
Use device mode to send events| This setting is turned on by default as this is a device mode-only integration.  
  
## Other settings

Setting| Description  
---|---  
Client-side event filtering| These settings let you specify which events should be blocked or allowed to flow through to comScore.  
  
See [Client-side Event Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) for more information.  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs.  
  
See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
## FAQ

#### Where can I find the comScore Publisher ID?

You can find the comScore Publisher ID by logging in to your comScore Direct account.

##### **Mobile**

  1. Log in to your [comScore Direct account](<https://direct.comscore.com/>).
  2. Go to the **Mobile app** tab.
  3. Click **Get Tag** and copy the C2 value.

[![comScore Publisher ID](/docs/images/event-stream-destinations/comscore-c2-value.webp)](</docs/images/event-stream-destinations/comscore-c2-value.webp>)

##### **Web**

  1. Log in to your [comScore Direct account](<https://direct.comscore.com/clients/Default.aspx>).
  2. Click **Get Tag**.

[![comScore Get Tag option](/docs/images/event-stream-destinations/get-tag-comscore.webp)](</docs/images/event-stream-destinations/get-tag-comscore.webp>)

  3. In the **Website Tag** popup, copy the value corresponding to the **C2** field.

[![comScore Publisher ID](/docs/images/event-stream-destinations/comscore-publisher-id-tag.webp)](</docs/images/event-stream-destinations/comscore-publisher-id-tag.webp>)