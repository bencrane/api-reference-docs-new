# SnapEngage

Send your event data from RudderStack to SnapEngage.

* * *

  * __4 minute read

  * 


[SnapEngage](<https://snapengage.com/>) is an enterprise chat platform. It offers chatbots and live chat integrations to drive conversions, reduce response times, and increase customer satisfaction.

RudderStack supports SnapEngage as a destination where you can seamlessly send your event data.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **SnapEngage** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
0| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
1| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the SnapEngage native SDK from the `https://storage.googleapis.com/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the SnapEngage SDK successfully.

## Get started

Once you have confirmed that the source platform supports sending events to SnapEngage, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **SnapEngage**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully configure SnapEngage as a destination, you will need to configure the following settings:

[![SnapEngage connection settings](/docs/images/event-stream-destinations/snapengage-connection-settings-1.webp)](</docs/images/event-stream-destinations/snapengage-connection-settings-1.webp>)[![SnapEngage connection settings](/docs/images/event-stream-destinations/snapengage-connection-settings-2.webp)](</docs/images/event-stream-destinations/snapengage-connection-settings-2.webp>)

  * **Widget ID** : Enter your SnapEngage widget ID.


> ![info](/docs/images/info.svg)
> 
> For more information on obtaining your SnapEngage widget ID, refer to the FAQ section below.

  * **Record Live Chat Events** : Enable this setting to allow RudderStack to automatically record your SnapEngage Live Chat events as `track` events.
  * **Update Event Name in track call** : If **Record Live Chat Events** is enabled, enable this setting to update the event names in the `track` call.
    * **Mapping to update the Event Name in track call** : Use this setting to map the standard SnapEngage events with your custom event names.
  * **Client-side Events Filtering** : This setting lets you specify which events should be blocked or allowed to flow through to SnapEngage.


> ![info](/docs/images/info.svg)
> 
> For more information on this setting, refer to the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide.

  * **Use device mode to send events** : As this is a [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>)-only destination, this setting is enabled by default and cannot be disabled.


## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to set the user’s email and username in SnapEngage through their [SDK](<https://developer.snapengage.com/javascript-api/#javascript-api>).

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify(
      "1hKOmRA4GRlm", {
        email: "alex@example.com",
        name: "Alex Keener"
      }
    );
    

### Supported mappings

The following table lists the mappings between the RudderStack and SnapEngage properties:

RudderStack property| SnapEngage property| Data type| Presence  
---|---|---|---  
`traits.email` / `context.traits.email`| `email`| String| Required  
`traits.name` / `context.traits.name`| `name`| String| Optional  
  
## Track

If you enable the **Record Live Chat Events** dashboard setting, RudderStack records the SnapEngage Live Chat events based on the user’s interactions and sends them as [track](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) events. You can then view and analyze these events using other tools (connected to the same source in RudderStack).

### Supported events

RudderStack automatically records and sends the following Live Chat events:

  * [Live Chat Conversation Started](<https://developer.snapengage.com/javascript-api/#startchat-event>)


    
    
    SnapEngage.setCallback("StartChat", function() {
      window.rudderanalytics.track(
        "Live Chat Conversation Started", {}, {
          context: {
            integration: {
              name: 'snapengage',
              version: '1.0.0'
            }
          }
        }
      );
    });
    

  * [Live Chat Conversation Ended](<https://developer.snapengage.com/javascript-api/#close-event>)


    
    
    SnapEngage.setCallback("Close", function() {
      window.rudderanalytics.track(
        "Live Chat Conversation Ended", {}, {
          context: {
            integration: {
              name: 'snapengage',
              version: '1.0.0'
            }
          }
        }
      );
    });
    

  * [Live Chat Message Sent](<https://developer.snapengage.com/javascript-api/#chatmessagesent-event>)


    
    
    SnapEngage.setCallback("ChatMessageSent", function() {
      window.rudderanalytics.track(
        "Live Chat Message Sent", {}, {
          context: {
            integration: {
              name: 'snapengage',
              version: '1.0.0'
            }
          }
        }
      );
    });
    

  * [Live Chat Message Received](<https://developer.snapengage.com/javascript-api/#chatmessagereceived-event>)


    
    
    SnapEngage.setCallback("ChatMessageReceived", function(agent) {
      window.rudderanalytics.track(
        "Live Chat Message Received", {
          agentUsername: agent
        }, {
          context: {
            integration: {
              name: 'snapengage',
              version: '1.0.0'
            }
          }
        }
      );
    });
    

  * [Button Clicked](<https://developer.snapengage.com/javascript-api/#button-event>)


    
    
    SnapEngage.setCallback("InlineButtonClicked", function() {
      window.rudderanalytics.track(
        "Inline Button Clicked", {}, {
          context: {
            integration: {
              name: 'snapengage',
              version: '1.0.0'
            }
          }
        }
      );
    });
    

### Mapping events

You can also update the standard SnapEngage Live Chat events with custom event names. Enable the **Update Event Name in track call** dashboard setting in RudderStack and specify the required mapping:

[![SnapEngage event name mapping](/docs/images/event-stream-destinations/snapengage-event-mapping.webp)](</docs/images/event-stream-destinations/snapengage-event-mapping.webp>)

From the mappings set in the above image, RudderStack replaces the event names `"Live Chat Conversation Started"` and `"Live Chat Message Sent"`with `"User Started Chat"` and `"Submit"` respectively.

## FAQ

#### Where can I find the SnapEngage widget ID?

To get your SnapEngage widget ID, follow these steps:

  1. Log into your [SnapEngage dashboard](<https://www.snapengage.com/app/>).
  2. In the sidebar, select the widget under **Current Widget** for which you want the widget ID.
  3. Go to **Settings** > **Get the Code**. You will find the widget ID under **(Advanced) Widget ID** :

[![SnapEngage widget ID](/docs/images/event-stream-destinations/snapengage-widget-id.webp)](</docs/images/event-stream-destinations/snapengage-widget-id.webp>)