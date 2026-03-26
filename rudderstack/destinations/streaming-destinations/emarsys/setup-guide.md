# Setup Guide Beta

Set up and configure Emarsys as a destination in RudderStack.

* * *

  * __3 minute read

  * 


This guide will help you set up Emarsys as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Emarsys.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Beta
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Unity, AMP , React Native , Flutter, Cordova, Web, Cloud, Shopify, Warehouse
  * Refer to it as **Emarsys** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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

In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Emarsys**.

> ![info](/docs/images/info.svg)
> 
> The Emarsys account you use for the set up must have admin permissions.

### Connection settings

Setting| Description  
---|---  
Name| Assign a name to uniquely identify the destination.  
Emarsys Username| Enter your Emarsys user name.  
Emarsys User Secret| Enter your Emarsys user secret.  
  
### Configuration settings

Configure the below settings to receive your data correctly in Emarsys.

Setting| Description  
---|---  
Custom Identifier Field Settings| Choose a custom identifier from the dropdown which is populated with your Emarsys properties list. If not provided, RudderStack considers `email` as the default custom identifier.  
  
If you have chosen any custom identifier while creating the contact list in Emarsys, choosing the same identifier while sending data to that contact list is recommended. RudderStack looks for the same identifier key while creating the event payload.  
  
You must include this custom identifier field in the **Custom Property Mapping** section.  
Default Contact List Field Settings| Choose a default contact list from the dropdown which is populated from your Emarsys account.  
Discard empty contact properties| This setting is turned on by default and discards the empty string values while retaining the opt-in status of that contact.  
  
If you turn off the setting and send an empty string for a field, RudderStack will not filter it and any created email (which is opted in), will be opted out for any campaign.  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
### Mappings

**Custom Property Mapping** : Click **Set-up mapping** to map the RudderStack event properties to Emarsys contact fields. RudderStack maps these properties from the `message.context.traits` or `message.traits` objects.

**External Event mappings** : Click **Set-up mapping** to map the RudderStack events to Emarsys external events.

## Next steps

  * [Send events in cloud mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/emarsys/cloud-mode/>)