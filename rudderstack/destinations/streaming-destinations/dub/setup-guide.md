# Dub Destination Setup Guide Beta

Set up Dub as a destination in RudderStack.

* * *

  * __3 minute read

  * 


This guide will help you set up Dub as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Dub.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Beta
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Dub** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), set up a source.
  2. Go to the **Overview** tab of your source and select **Add Destination** > **Create new destination**.

[![Add new destination in RudderStack dashboard](/docs/images/event-stream-destinations/add-new-destination.webp)](</docs/images/event-stream-destinations/add-new-destination.webp>)

  3. Select **Dub** from the list of destinations. Then, click **Continue**.


## Connection settings

Setting| Description  
---|---  
Name| Assign a name to uniquely identify the destination in RudderStack.  
API key  
Required| Your Dub API key used for authentication. It must follow the format `dub_` followed by alphanumeric characters.  
  


> ![warning](/docs/images/warning.svg)Note that:  
>   
> 
> 
>   * Your Dub API key must have the relevant permissions to create conversion events.
>   * Make sure to secure your API key — anyone with access to this key can send conversion events to your Dub account.
> 
  
  
Convert amount to cents| This setting is toggled on by default. When enabled, RudderStack multiplies monetary amounts by 100 before sending them to Dub, thereby converting dollars to cents as required by Dub’s API.  
  
If this setting is disabled, RudderStack sends the specified amount value as is, without any conversion.  
  
See the [Dub documentation](<https://dub.co/docs/conversions/sales/introduction?dub_id=CTUiZfhX4cU7BsBJ#currency-conversion-support>) for more information on currency conversion support.  
  
## Configuration settings

Setting| Description  
---|---  
Event mappings| Map your RudderStack events to Dub’s `LEAD_CONVERSION` or `SALES_CONVERSION` events.  
  


> ![warning](/docs/images/warning.svg)To successfully deliver events to Dub, you must:  
>   
> 
> 
>   * Configure the event mappings via this setting
>   * Include the `clickId` parameter in those events.
> 
See the [Cloud Mode Integration](<https://www.rudderstack.com/docs/destinations/streaming-destinations/dub/cloud-mode/>) guide for detailed mapping instructions.  
  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs.  
  
See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  


> ![info](/docs/images/info.svg)When consent management is enabled, RudderStack only sends events to Dub when the user has provided appropriate consent.  
  
## Next steps

After setting up your Dub destination in RudderStack:

  * See the [Dub Cloud Mode Integration](<https://www.rudderstack.com/docs/destinations/streaming-destinations/dub/cloud-mode/>) guide to understand how RudderStack maps and sends events to Dub
  * Send test events to verify your setup is working correctly
  * See the detailed [FAQ](<https://www.rudderstack.com/docs/destinations/streaming-destinations/dub/faq/>) guide for answers to the commonly asked questions on this integration


## FAQ

#### Where can I find my Dub API key?

  1. Log in to your Dub dashboard.
  2. Click the profile in the left sidebar to see **Settings**.

[![Dub API Key Links](/docs/images/event-stream-destinations/dub-api-key-2.webp)](</docs/images/event-stream-destinations/dub-api-key-2.webp>)

  3. Go to the **API Keys** section and copy your API key — it should start with `dub_` followed by alphanumeric characters.

[![Dub API Key Links](/docs/images/event-stream-destinations/dub-api-key-3.webp)](</docs/images/event-stream-destinations/dub-api-key-3.webp>)