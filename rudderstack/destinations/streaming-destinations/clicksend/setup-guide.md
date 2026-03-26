# Setup Guide Beta

Set up and configure ClickSend as a destination in RudderStack.

* * *

  * __2 minute read

  * 


This guide will help you set up ClickSend as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to ClickSend.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Beta
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Unity, AMP , React Native , Flutter, Cordova, Web, Cloud, Shopify, Warehouse
  * Refer to it as **Clicksend** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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

In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **ClickSend**.

### Connection settings

Setting| Description  
---|---  
Name| Assign a name to uniquely identify the destination.  
Clicksend API Username| Enter your [Clicksend API Username](<https://help.clicksend.com/article/dghaoyf7tg-api-credentials>).  
Clicksend API key| Enter your [ClickSend API key](<https://help.clicksend.com/article/dghaoyf7tg-api-credentials>).  
  
### Configuration settings

Setting| Description  
---|---  
Scheduling Unit| Choose the default time unit from the dropdown for which you want to schedule the text messages.  
Default scheduling tenure| Enter the default duration after which the scheduled text messages must be sent.  
Default source| Enter your default method of sending the text messages. For example, Wordpress, PHP, C#, etc.  
Default Sender ID| Enter your [ClickSend sender ID](<https://help.clicksend.com/article/4kgj7krx00-what-is-a-sender-id-or-sender-number>).  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
## Next steps

  * [Send events in cloud mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/clicksend/cloud-mode/>)