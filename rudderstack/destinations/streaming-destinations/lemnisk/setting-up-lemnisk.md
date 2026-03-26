# Setup Guide

Set up Lemnisk as a destination in RudderStack.

* * *

  * __3 minute read

  * 


This guide will help you set up Lemnisk as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Lemnisk.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **Lemnisk Marketing Automation** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Lemnisk, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Lemnisk Marketing Automation**.
  2. Assign a name to your destination and click **Continue**.


## Connection settings

To send events to Lemnisk via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>), you need to configure the following settings:

  * **Cloud Mode** : Select one of the below options from the dropdown and enter the relevant details:


#### Web Cloud Mode

  * **Write Key** : Enter the unique write key of your Lemnisk data source.
  * **Region URL** : Enter the Lemnisk region URL.


#### Server-side Cloud Mode

  * **X-API-Key** : Enter the Lemnisk X-API-Key.
  * **X-API-PassKey** : Enter the Lemnisk X-API-PassKey.
  * **Write Key** : Enter the unique write key of your Lemnisk data source.
  * **Source ID** : Enter the Lemnisk Source ID.
  * **Region URL** : Enter the Lemnisk region URL.


> ![info](/docs/images/info.svg)
> 
> Contact your Lemnisk Customer Success Manager to obtain any of the above details.

#### None of the above (Select this if you want to use device mode only)

  * **Client-side Events Filtering** : This setting lets you specify which events should be blocked or allowed to flow through to Lemnisk. For more information on this setting, refer to the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide.
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


The below settings are visible only when a JavaScript source is connected to Lemnisk:

  * **Client ID** : Enter the unique ID generated for your Lemnisk account. Contact your Lemnisk Customer Success Manager to obtain the client ID.
  * **Use device mode to send events:** Make sure this option is enabled if you want to send events using the [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).
  * **Write Key** : Enter the unique write key of your Lemnisk data source.


## FAQ

#### How do I verify if the events are passing to Lemnisk correctly?

You can verify the events coming via Rudderstack in the [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/>) tab. In Lemnisk, go to **Sources** and click on a particular source. If the integration is successful, you can see the events under the **Live Events** section. Make sure that the event payload is correct.