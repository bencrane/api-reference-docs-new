# Setup Guide Beta

Set up and configure Koddi as a destination in RudderStack.

* * *

  * __2 minute read

  * 


This guide will help you set up Koddi as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Koddi.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Beta
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Shopify, Warehouse
  * Refer to it as **Koddi** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Setup

In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Koddi**.

### Connection settings

Setting| Description  
---|---  
Destination name| Assign a name to uniquely identify the destination.  
API Base URL| Enter your API Base URL, which is of the format `https://{clientname}.koddi.io/event-collection/beacon`, where `clientName` is your company’s name. You can also contact the Koddi team to obtain this value.  
Client Name| Enter your company’s name. You can also contact the Koddi team to obtain this value.  
  
### Configuration settings

Configure the below [Click event](<https://www.rudderstack.com/docs/destinations/streaming-destinations/koddi/cloud-mode/#ad-clicks>) settings to receive your data correctly in Koddi.

Setting| Description  
---|---  
testVersionOverride| Turn on this toggle to add a testing parameter to be used for A/B testing. Once enabled, you can send the `test_version_override` field in the [Click event](<https://www.rudderstack.com/docs/destinations/streaming-destinations/koddi/cloud-mode/#ad-clicks>) to Koddi.  
overrides| Enable this setting to [override the auction results](<https://developers.koddi.com/reference/clicks-1#inputs>). Once enabled, you can send the `overrides` field in the [Click event](<https://www.rudderstack.com/docs/destinations/streaming-destinations/koddi/cloud-mode/#ad-clicks>) to Koddi.  
  
## Next steps

  * [Send events in cloud mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/koddi/cloud-mode/>)