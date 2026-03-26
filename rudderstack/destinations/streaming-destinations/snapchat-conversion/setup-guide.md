# Snapchat Conversion Setup Guide

Set up and configure Snapchat Conversion as a destination in RudderStack.

* * *

  * __4 minute read

  * 


This guide will help you set up Snapchat Conversion as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Snapchat.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Snapchat Conversion** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Snapchat Conversion, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Snapchat Conversion**.
  2. Assign a name to your destination and click **Continue**.


### Connection settings

Setting| Description  
---|---  
API Token| Enter the API token generated from your Snapchat dashboard.  
API Version| Select the Conversions API version from the dropdown. RudderStack recommends using the Conversions API v3 as v2 is deprecating soon.  
Pixel ID| Enter your Snap Pixel ID required for sending the web and offline events.  
Snap App ID| Enter your Snapchat App ID required for sending the app events. See [Generate your Snap App ID](<https://ads.tiktok.com/marketing_api/docs?id=1701890914536450>) for more information on generating this ID.  
App ID| Enter the unique app ID associated with your application required for sending the app events.  
  
**Note** : The **App ID** is different from **Snap App ID**. It should be a numeric value for iOS and in a human-readable string format in case of Android. See the [Conversions API reference](<https://marketingapi.snapchat.com/docs/conversion.html#conversion-parameters>) for more information.  
Map your events with Snapchat Standard Events| Enter the event name and select the corresponding [Snapchat standard event](<https://marketingapi.snapchat.com/docs/conversion.html#conversion-parameters:~:text=42ef%2Dba77%2D9dd9a9eb2dc1-,event_type,-Event%20type%20required>) from the dropdown to be triggered when you send the RudderStack event.  
  
You can specify multiple Snapchat standard events for one RudderStack event and vice versa.  
  
### Other settings

Setting| Description  
---|---  
Enable Event Deduplication| Turn on this setting to deduplicate the events.  
Deduplication key| This setting is visible if **Enable Event Deduplication** is toggled on. Enter the property name to map to a standard Snapchat Conversion property `client_dedup_id` which Snapchat uses to deduplicate the events.  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
## FAQ

#### Where can I find the Conversions API token?

  1. Go to your [Snap Ads Manager](<https://ads.snapchat.com/>) account.
  2. Click **Create Ads** option in the top left section of the dashboard and go to **Business Details** > **Conversions API Tokens**. You will find all API tokens associated with your account listed here.
  3. To generate a new Conversions API token, click **Generate Token**.

[![Snap Conversions API token](/docs/images/event-stream-destinations/snap-conversions-api-token.webp)](</docs/images/event-stream-destinations/snap-conversions-api-token.webp>)

#### Where can I find the Pixel ID associated with my account?

  1. Go to your [Snap Ads Manager](<https://ads.snapchat.com/>) account.
  2. Click **Create Ads** option in the top left section of the dashboard and go to **Events Manager**.
  3. Then, click **Setup Snap Pixel**. You will see the following options:

[![Snap Conversions set up Pixel](/docs/images/event-stream-destinations/snap-conversions-setup-pixel.webp)](</docs/images/event-stream-destinations/snap-conversions-setup-pixel.webp>)

  4. Select **Pixel Code** and click **Continue**.
  5. You will see the Snap Pixel ID at the top left of the resulting window:

[![Snap Conversions Pixel ID](/docs/images/event-stream-destinations/snap-conversions-pixel-id.webp)](</docs/images/event-stream-destinations/snap-conversions-pixel-id.webp>)

#### Where can I find the App ID associated with my application?

  1. Go to your [Snap Ads Manager](<https://ads.snapchat.com/>) account.
  2. Click **Create Ads** option in the top left section of the dashboard and go to **Apps**. You will find the **App ID** associated with all your apps listed here.


To add a new app:

  1. Click **Add an App**.
  2. You can either create a new Snap App ID or importing an existing App ID.
  3. Then, enter your **App Name** and the relevant app ID/URL depending on your app’s platform.
  4. Finally, add any postbacks and click **Continue** to finish the setup.

[![Snap Conversions add new app](/docs/images/event-stream-destinations/snap-conversions-add-new-app.webp)](</docs/images/event-stream-destinations/snap-conversions-add-new-app.webp>)