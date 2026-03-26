# Axeptio

Step-by-step guide on sending your event data from RudderStack to Axeptio.

* * *

  * __3 minute read

  * 


[Axeptio](<https://www.axeptio.eu/>) is a cookie and consent management platform. It enables you to use interesting widgets and compelling UI to enhance users’ cookie/consent experience while keeping your web performance intact.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **Axeptio** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Web| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Axeptio, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Axeptio**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully configure Axeptio as a destination, you will need to configure the following settings:

  * **Client ID** : Enter your Axeptio client ID. For more information on obtaining the client ID, refer to the FAQ section below.
  * **Toggle it on to send data through callback** : Enable this setting to allow RudderStack to track and record the callback events from the Axeptio SDK as `track` events.
  * **Client-side Events Filtering** : This setting lets you specify which events should be blocked or allowed to flow through to Axeptio. For more information on this setting, refer to the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide.
  * **Use device mode to send events** : Enable this setting to send your events to Axeptio via [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).


> ![info](/docs/images/info.svg)
> 
> You can keep it disabled if you only want to load the Axeptio SDK natively and not send any events.

  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


## Tracking callback events

The Axeptio SDK triggers events whenever a user interacts with the cookie/consent widgets integrated with your website.

By enabling the **Toggle it on to send data through callback** setting in the RudderStack dashboard, RudderStack tracks and records the interaction events as [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) events. You can then view and analyze these events in the other tools (connected to the same source in RudderStack).

RudderStack maps the name and the payload of the triggered interaction event to the `track` event name and properties respectively.

## FAQ

#### Where can I find the Axeptio client ID?

To get the client ID associated with your Axeptio project, follow these steps:

  1. Log into your [Axeptio dashboard](<https://admin.axeptio.eu/>).
  2. Click the settings icon on your project. You should be able to see the **Project ID** listed here:

[![Axeptio client ID](/docs/images/event-stream-destinations/axeptio-client-id.webp)](</docs/images/event-stream-destinations/axeptio-client-id.webp>)

You can also find the client ID in the code snippet to integrate into your website. Click the settings icon on your project and go to **Integration** to find the client ID:

[![Axeptio client ID](/docs/images/event-stream-destinations/axeptio-client-id-2.webp)](</docs/images/event-stream-destinations/axeptio-client-id-2.webp>)

> ![info](/docs/images/info.svg)
> 
> Axeptio client ID is the same as the project ID.