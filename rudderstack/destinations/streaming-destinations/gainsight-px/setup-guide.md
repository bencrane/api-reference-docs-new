# Setup Guide

Set up and configure Gainsight PX as a destination in RudderStack.

* * *

  * __3 minute read

  * 


This guide will help you set up Gainsight PX as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Gainsight PX.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **Gainsight PX** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Gainsight PX native SDK from the `https://web-sdk.aptrinsic.com` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Gainsight PX SDK successfully.

## Setup

In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Gainsight PX**.

### Connection settings

Setting| Description  
---|---  
Name| Assign a name to uniquely identify the destination.  
API Key| Enter the API key required for using the [Gainsight PX REST API](<https://gainsightpx.docs.apiary.io/#>).  
  
Generate the key by going to your [Gainsight PX dashboard](<https://app.aptrinsic.com/authentication/login>) and navigating to **Administration** > **Integrations** > **Rest API**.  
Product Tag Key| Enter the product tag key by going to **Administration** > **Products** in your Gainsight PX dashboard.  
User Attribute Mapping| Use this setting to map your RudderStack event properties to custom user attributes in Gainsight PX.  
Account Attribute Mapping| Use this setting to map your RudderStack event properties to custom account attributes in Gainsight PX.  
Global Context Mapping| Use this setting to map the key-value pairs for the [Gainsight PX global context metadata](<https://support.gainsight.com/PX/Engagements/02Engagement_Configuration/Use_Global_Context>).  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
## Create custom attributes

You can create custom attributes for the `User` and `Account` objects in Gainsight PX and map them to your RudderStack event properties.

To create custom properties:

  1. Log in to your [Gainsight PX dashboard](<https://app.aptrinsic.com/authentication/login>).
  2. Navigate to **Administration** > **Attributes**.
  3. Click the **New Attribute** button as shown:

[![](/docs/images/event-stream-destinations/gainsight-px-create-attribute.webp)](</docs/images/event-stream-destinations/gainsight-px-create-attribute.webp>)

You can map these attributes to your event properties in the RudderStack dashboard using these connection settings:

[![](/docs/images/event-stream-destinations/gainsightpx-mapping-settings.webp)](</docs/images/event-stream-destinations/gainsightpx-mapping-settings.webp>)

## Next steps

  * [Send events in cloud mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/gainsight-px/cloud-mode/>)


## FAQ

#### Where can I find the Gainsight PX product tag key?

  1. Log in to your [Gainsight PX dashboard](<https://app.aptrinsic.com/authentication/login>).
  2. Go to **Administration** > **Products**. You will see the product tag key listed here:

[![](/docs/images/event-stream-destinations/gainsight-px-product-key.webp)](</docs/images/event-stream-destinations/gainsight-px-product-key.webp>)

See the [Gainsight PX documentation](<https://support.gainsight.com/PX/Install_PX/Install_PX_Web/Install_Gainsight_PX_on_Your_Web_App>) for more information on the setup.