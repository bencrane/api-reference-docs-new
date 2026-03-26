# Setup Guide

Set up Optimizely Feature Experimentation as a destination in RudderStack.

* * *

  * __5 minute read

  * 


This guide will help you set up Optimizely Feature Experimentation as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Optimizely.

## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), go to **Directory** > **Destinations** > **Cloud Destinations** and search for **Optimizely Fullstack**.
  2. Connect your source and click **Continue**.


### Connection settings

Configure the following settings to set up Optimizely Feature Experimentation as a destination in RudderStack:

  * **Name** : Assign a name to uniquely identify the destination.
  * **Datafile URL** : Enter the datafile URL of your environment by going to **Settings** > **Environments** in your [Optimizely dashboard](<https://app.optimizely.com/signin>).
  * **Account ID** : Enter your Optimizely account ID by going to **Account Settings** > **Plan**.
  * **Campaign ID** : Enter your Optimizely campaign ID by going to **Experiments** > **API Names** > **Experiment Details**.
  * **Experiment ID** : Enter the Optimizely experiment ID by going to **Experiments** > **API Names** > **Experiment Details**.


> ![info](/docs/images/info.svg)
> 
> For more information on obtaining the Optimizely Account ID, Campaign ID, and Experiment ID, see [Optimizely documentation](<https://docs.developers.optimizely.com/web-experimentation/docs/locate-ids-used-for-apis#account-id>).

### Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **Optimizely Fullstack** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
AMP| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Java)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cloud| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cordova| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
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
Device mode  
Android (Java)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
### Configuration settings

After completing the initial setup, configure the following settings to correctly receive your data in Optimizely:

#### **Page settings**

The following settings are applicable **only** for [cloud mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/optimizely-feature-experimentation/cloud-mode/>). They let you specify how you want to send your `page` calls to Optimizely:

> ![success](/docs/images/tick.svg)
> 
> These settings are also applicable for the `screen` events.

  * **Track Categorized Pages** : To track categorized pages, turn on this setting and use the RudderStack Page Name/Category to Optimizely event mappings setting to map your `page`/`screen` `category` to the specific Optimizely event name.
  * **Track Named Pages** : To track named pages, turn on this setting and use the RudderStack Page Name/Category to Optimizely event mappings setting to map your `page`/`screen` `name` to the specific Optimizely event name.


> ![warning](/docs/images/warning.svg)
> 
> Make sure to create the events first in your Optimizely dashboard. For more information on creating events, see [Optimizely documentation](<https://docs.developers.optimizely.com/feature-experimentation/docs/create-events>).

#### **Destination settings**

  * **Track Known Users** : By default, this setting is enabled. RudderStack tracks only the known users and maps `userId` to Optimizely’s visitor ID. When disabled, RudderStack maps `anonymousId` to the Optimizely visitor ID.


> ![info](/docs/images/info.svg)
> 
> Optimizely does not alias known and unknown users.

  * **Anonymize IP** : If enabled, Optimizely stores the user’s truncated IP.
  * **Enrich Decisions** : Enable this setting to allow Optimizely to perform enhanced data collection and analysis using their **Enriched Events Export** functionality. For more information on this feature, see [Optimizely documentation](<https://docs.developers.optimizely.com/experimentation-data/docs/enriched-events-export>).


> ![info](/docs/images/info.svg)
> 
> The Enrich Events Export feature is available only in the paid Optimizely plan.

  * **Project ID** : Enter your Optimizely project ID. You can find this ID by going to **Experiments** > **API Names** > **Experiment Details**.


> ![info](/docs/images/info.svg)
> 
> Sending your Project ID to Optimizely is highly recommended.

The following settings are applicable only if you’re sending events via [device mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/optimizely-feature-experimentation/device-mode/>):

  * **Send the experiment and variation information** : RudderStack sends the experiment-related data to the other destinations as `track` calls by triggering the `Experiment Viewed` event every time an Optimizely live variable is accessed. This setting is enabled by default.
  * **Non-Interaction Event** : RudderStack sends an `Experiment Viewed` event as a non-interaction event to Google Analytics. This setting is enabled by default.


#### **Other settings**

  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.
  * **Client-side Events Filtering** : This setting is applicable only if you’re sending events via [device mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/optimizely-feature-experimentation/device-mode/>). It lets you specify which events should be blocked or allowed to flow through to Optimizely. See [Client-side Event Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) for more information on this feature.


> ![info](/docs/images/info.svg)
> 
> If you plan to send events to Optimizely Feature Experimentation via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>), you will need some additional configuration. See [Send events via device mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/optimizely-feature-experimentation/device-mode/#adding-optimizely-to-your-mobile-project>) for more details.

#### **Event mapping**

> ![info](/docs/images/info.svg)
> 
> By default, RudderStack sends the event name to Optimizely if you do not configure the event mapping in the dashboard settings.

  * **RudderStack to Optimizely event and attribute mappings** : Click **Set up mapping** to map your RudderStack events to specific Optimizely events. RudderStack also provides the JSON mapper to set these mappings.

[![Optimizely Feature Experimentation event mapping](/docs/images/event-stream-destinations/optimizely-fullstack-event-mapping.webp)](</docs/images/event-stream-destinations/optimizely-fullstack-event-mapping.webp>)

> ![warning](/docs/images/warning.svg)
> 
> Make sure to create the events in Optimizely first before setting the mappings.

To map your RudderStack user traits to specific Optimizely attributes, go to the **Custom attributes** tab. You can also use the JSON mapper to set these mappings.

[![Optimizely Feature Experimentation attribute mapping](/docs/images/event-stream-destinations/optimizely-fullstack-attribute-mapping.webp)](</docs/images/event-stream-destinations/optimizely-fullstack-attribute-mapping.webp>)

> ![warning](/docs/images/warning.svg)
> 
> Make sure to create the attributes in Optimizely first by going to **Audiences** > **Attributes** section.
> 
> For more information on defining attributes in Optimizely, see [Optimizely documentation](<https://docs.developers.optimizely.com/full-stack-experimentation/docs/define-attributes>).

  * **RudderStack Page Name/Category to Optimizely event mappings** : This setting is visible only if you turn on any of the following Page settings:

    * **Track Categorized Pages**
    * **Track Named Pages**


Click **Set up mapping** to map your RudderStack page name or category to specific Optimizely events.

[![Optimizely Feature Experimentation page name and category mapping](/docs/images/event-stream-destinations/optimizely-fullstack-page-mapping.webp)](</docs/images/event-stream-destinations/optimizely-fullstack-page-mapping.webp>)