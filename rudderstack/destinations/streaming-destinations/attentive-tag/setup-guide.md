# Attentive Tag Setup Guide

Set up Attentive Tag as a destination in RudderStack.

* * *

  * __2 minute read

  * 


This guide will help you set up Attentive Tag as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Attentive Tag.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Attentive Tag** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), set up a source.
  2. Go to the **Overview** tab of your source and select **Add Destination** > **Create new destination**.

[![Add new destination in RudderStack dashboard](/docs/images/event-stream-destinations/add-new-destination.webp)](</docs/images/event-stream-destinations/add-new-destination.webp>)

  3. Select **Attentive Tag** from the list of destinations. Then, click **Continue**.


## Connection settings

Setting| Description  
---|---  
Name| Assign a name to uniquely identify the destination in RudderStack.  
API Key| Specify the Attentive Tag API key for the app you created in your Attentive dashboard.  
Signup Source ID| Specify the signup method ID present in the **Sign-up Units** option in the Attentive dashboard.  
  
## Advanced settings

Setting| Description  
---|---  
Enable new Identify flow  
Beta| Toggle on this setting to use RudderStack’s new Identify flow for better user management.  
  
If enabled, the `identify` calls will sync user data using Attentive’s [Identity](<https://docs.attentivemobile.com/openapi/reference/tag/Identity/>) and [Custom Attributes](<https://docs.attentivemobile.com/openapi/reference/tag/Custom-Attributes/#tag/Custom-Attributes>) APIs.  
  
If this setting is toggled off, RudderStack uses the legacy [subscription](<https://www.rudderstack.com/docs/destinations/streaming-destinations/attentive-tag/cloud-mode/#subscribing-users>) / [unsubscription](<https://www.rudderstack.com/docs/destinations/streaming-destinations/attentive-tag/cloud-mode/#unsubscribing-users>) flows instead.  
  
See [Use new Identify flow](<https://www.rudderstack.com/docs/destinations/streaming-destinations/attentive-tag/cloud-mode/#use-new-identify-flow>) for more information on this feature.  
  
## Other settings

Setting| Description  
---|---  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs.  
  
See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
## Next steps

  * [Send events in cloud mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/attentive-tag/cloud-mode/>)


## FAQ

#### Where can I find the Attentive Tag API Key?

  1. In your [Attentive dashboard](<https://ui.attentivemobile.com/>), go to **Marketplace**.
  2. Create an app by clicking **Create App**.
  3. Click **Create** to see the API key for the app:

[![Attentive Tag Connection Settings](/docs/images/event-stream-destinations/attentive-tag-connection-settings-1.webp)](</docs/images/event-stream-destinations/attentive-tag-connection-settings-1.webp>)

#### Where can I find the Attentive Tag Signup Source ID?

  1. Go to the **Sign-up Units** option in your [Attentive dashboard](<https://ui.attentivemobile.com/>).
  2. Locate the ID next to **Sign-up method** , as shown:

[![Attentive Tag Connection Settings](/docs/images/event-stream-destinations/attentive-tag-connection-settings-2.webp)](</docs/images/event-stream-destinations/attentive-tag-connection-settings-2.webp>)