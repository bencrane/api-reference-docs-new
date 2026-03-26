# Olark Destination

Send your event data from RudderStack to Olark.

* * *

  * __3 minute read

  * 


[Olark](<https://www.olark.com/>) is a cloud-based live chat platform to connect with your customers in an effective and timely manner. It provides various features like automated messages, team management, real-time reporting, searchable transcripts, and more.

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/Olark>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **Olark** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Olark, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Olark**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully configure Olark as a destination, you will need to configure the following settings:

  * **Site ID** : Enter your Olark site ID. This is a required field - RudderStack uses it to initialize the Olark native web SDK.
  * **Group ID** : Enter your Olark group ID. For more information on getting this ID, refer to the FAQ section below.
  * **Record Live Chat Events** : Enable this setting to allow RudderStack to automatically record your Olark Live Chat events as `track` events.
    * **Update Event Name in track call** : Use this setting to update your `track` event name.
      * **Mapping to update the event name in track call** : Use this setting to map the standard Olark Live Chat events with your custom `track` event names.
  * **Client-side Events Filtering** : This setting lets you specify which events should be blocked or allowed to flow through to Olark. For more information, refer to the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide.
  * **Use device mode to send events** : As this is a [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>)-only destination, this setting is enabled by default and cannot be disabled.
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to update the user information in Olark, like name, email address, phone number, and custom fields like customer ID.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com"
      age: 25
    })
    

### Supported mappings

RudderStack maps the following **optional** user traits to the corresponding Olark properties:

RudderStack property| Mouseflow property| Data type  
---|---|---  
`email`| `emailAddress`| String  
`traits`| custom fields| Object  
`name`  
`firstName` \+ `lastName`| `fullName`| String  
`phone`| `phoneNumber`| String  
  
## Track

If you enable the **Record Live Chat Events** dashboard setting, RudderStack records the Olark Live Chat events based on the user’s interactions and sends them as [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) events. You can then view and analyze these events using other tools (connected to the same source in RudderStack).

You can also set custom names for your `track` events and map them to the Olark standard events by enabling the **Update event name in track call** setting.

[![Mapping track events to Olark standard Live Chat events](/docs/images/event-stream-destinations/olark-track-event-mapping.webp)](</docs/images/event-stream-destinations/olark-track-event-mapping.webp>)

RudderStack supports the following standard Live Chat events:

  * Start Chat
  * Chat Message Sent
  * Chat Message Received


## FAQ

#### Where can I find the Olark group ID?

  1. Log in to your [Olark dashboard](<>).
  2. From the left sidebar, go to **Team** > **Groups** and click the relevant group for which you want the ID.
  3. Click **Show embed code**. Your group ID will be listed here:

[![Olark group ID](/docs/images/event-stream-destinations/olark-group-id.webp)](</docs/images/event-stream-destinations/olark-group-id.webp>)