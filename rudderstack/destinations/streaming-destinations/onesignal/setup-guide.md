# Setup Guide

Set up and configure OneSignal as a destination in RudderStack.

* * *

  * __2 minute read

  * 


This guide will help you set up OneSignal as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to OneSignal.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **OneSignal** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **OneSignal**.
  2. Assign a name to the destination and click **Continue**.


### Connection settings

Setting| Description  
---|---  
App ID| Enter your OneSignal App ID.  
Event version to use| Select the OneSignal API to use. RudderStack provides the following options:  
  


  * Device Model (Deprecated)
  * User Model (Recommended)

See the [OneSignal documentation](<https://documentation.onesignal.com/docs/user-model-migration-guide>) for more information.  
Toggle on to add a device/subscription using email| Turn on this setting to add a new device to your OneSignal app using the email.  
Toggle on to add a device/subscription using phone number| Toggle on this setting to add a new device to your OneSignal app using the phone number.  
Toggle on to concatenate event name with properties| Turn on this setting to concatenate the event names with properties.  
  
For example, if `add_to_cart` is an event and `brand` is a property, the event will be sent as `add_to_cart_brand` tag.  
Allowed Property List| Enter the properties you want to add as device [tags](<https://documentation.onesignal.com/docs/add-user-data-tags>), if present in the payload.  
  
**Note** : RudderStack considers the properties mentioned under this setting only for the `track` and `group` calls.  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
## Next steps

  * [Send events via User Model API](<https://www.rudderstack.com/docs/destinations/streaming-destinations/onesignal/user-model/>)
  * [Send events via Device Model API (Deprecated)](<https://www.rudderstack.com/docs/destinations/streaming-destinations/onesignal/device-model/>)


## FAQ

#### Where can I find the OneSignal App ID?

  1. Log in to your [OneSignal dashboard](<https://dashboard.onesignal.com/>).
  2. Go to your app’s **Settings** > **Keys & IDs**.
  3. You will find the OneSignal App ID:

[![OneSignal license code and API key](/docs/images/event-stream-destinations/onesignal-app-id.webp)](</docs/images/event-stream-destinations/onesignal-app-id.webp>)