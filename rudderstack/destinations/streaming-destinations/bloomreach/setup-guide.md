# Setup Guide Beta

Set up and configure Bloomreach as a destination in RudderStack.

* * *

  * __2 minute read

  * 


This guide will help you set up Bloomreach as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Bloomreach.

> ![info](/docs/images/info.svg)
> 
> See the [Bloomreach Catalog](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/bloomreach-catalog/>) destination documentation if you want to sync the catalog data from your warehouse to Bloomreach.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Beta
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Shopify, Warehouse
  * Refer to it as **bloomreach** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Setup

In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Bloomreach**.

### Connection settings

Setting| Description  
---|---  
Name| Assign a name to uniquely identify the destination.  
API Base URL| Enter the URL of your Bloomreach instance. You can find it under the **Project settings** > **Access management** > **API** in the Bloomreach dashboard.  
API Key| Enter the [API key](<https://documentation.bloomreach.com/engagement/reference/authentication#private-api-access>) from Bloomreach dashboard.  
API Secret| Enter the [API secret](<https://documentation.bloomreach.com/engagement/reference/authentication#private-api-access>) from Bloomreach dashboard.  
Project Token| Enter the [project token](<https://documentation.bloomreach.com/engagement/docs/project-settings-2#project---general>) for your project under the Bloomreach instance. You can find it under the **Project settings** > **Access management** > **API** in the Bloomreach dashboard.  
Hard ID| Enter the [hard ID](<https://documentation.bloomreach.com/engagement/docs/customer-identification#hard-id>) to be used in Bloomreach to identify a customer. The value provided here must exist in your Bloomreach project.  
See also: [Send multiple hard and soft IDs](<https://www.rudderstack.com/docs/destinations/streaming-destinations/bloomreach/cloud-mode/#send-multiple-hard-and-soft-ids>)  
Soft ID| Enter the [soft ID](<https://documentation.bloomreach.com/engagement/docs/customer-identification#soft-id>) to be used in Bloomreach to identify a customer. The value provided here must exist in your Bloomreach project.  
See also: [Send multiple hard and soft IDs](<https://www.rudderstack.com/docs/destinations/streaming-destinations/bloomreach/cloud-mode/#send-multiple-hard-and-soft-ids>)  
  
### Configuration settings

Configure the below settings to receive your data correctly in Bloomreach.

Setting| Description  
---|---  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
## Next steps

  * [Send events in cloud mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/bloomreach/cloud-mode/>)