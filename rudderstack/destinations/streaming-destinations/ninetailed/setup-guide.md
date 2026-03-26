# Setup Guide Beta

Set up and configure Ninetailed as a destination in RudderStack.

* * *

  * __2 minute read

  * 


This guide will help you set up Ninetailed as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Ninetailed.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Beta
  * **Supported sources:** Web, iOS (Obj-C) , iOS (Swift) , Android (Java) , Android (Kotlin) , Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Ninetailed** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> For the web device mode integration, that is, when using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, you need to first [install the Ninetailed SDK](<https://docs.ninetailed.io/for-developers/experience-sdk/getting-started>) as an npm package before sending the events.

## Setup

In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Ninetailed**.

### Connection settings

Setting| Description  
---|---  
Destination name| Assign a name to uniquely identify the destination.  
Organization ID (API Key)| Enter your Ninetailed organization ID.  
  
**Note** : This setting is not applicable for the web device mode integration.  
  
### Advanced settings

Configure the below settings to receive your data correctly in Ninetailed.

Setting| Description  
---|---  
Environment slug| Select your Ninetailed environment (main/development) from the dropdown.  
Send page calls in device mode| Turn on this setting to send [`page`](<https://www.rudderstack.com/docs/destinations/streaming-destinations/ninetailed/device-mode/#page>) calls to Ninetailed in device mode.  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
## Next steps

  * [Send events in cloud mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/ninetailed/cloud-mode/>)
  * [Send events in device mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/ninetailed/device-mode/>)


## FAQ

#### **Where can I find the Ninetailed organization ID (API key)?**

  1. Log in to your [Ninetailed dashboard](<https://app.ninetailed.io/>).
  2. Click your organization name on the top left corner and select your environment.

[![Ninetailed environment ID](/docs/images/event-stream-destinations/ninetailed-environment.webp)](</docs/images/event-stream-destinations/ninetailed-environment.webp>)

  3. In the left sidebar, click **API Key**. You should be able to see your API key for the environment listed here.

[![Ninetailed API key](/docs/images/event-stream-destinations/ninetailed-apikey-environmentid.webp)](</docs/images/event-stream-destinations/ninetailed-apikey-environmentid.webp>)