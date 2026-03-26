# LiveChat

Send your event data from RudderStack to LiveChat.

* * *

  * __4 minute read

  * 


[LiveChat](<https://www.livechat.com/>) is a live chat software and customer service platform. It lets you manage user interactions across multiple channels and deliver more effective customer service.

RudderStack supports LiveChat as a destination where you can seamlessly send your event data.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **livechat** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the LiveChat native SDK from the`https://cdn.livechatinc.com/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the LiveChat SDK successfully.

## Get started

Once you have confirmed that the source platform supports sending events to LiveChat, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **LiveChat**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully configure LiveChat as a destination, you will need to configure the following settings:

[![LiveChat connection settings](/docs/images/event-stream-destinations/livechat-connection-settings-1.webp)](</docs/images/event-stream-destinations/livechat-connection-settings-1.webp>)

  * **License ID** : Enter your LiveChat license ID.


> ![info](/docs/images/info.svg)
> 
> For more information on obtaining your LiveChat license ID, refer to the FAQ section below.

  * **Record Live Chat Events** : Enable this setting to allow RudderStack to automatically record your LiveChat interactions as `track` events.

[![LiveChat connection settings](/docs/images/event-stream-destinations/livechat-connection-settings-2.webp)](</docs/images/event-stream-destinations/livechat-connection-settings-2.webp>)
    * **List of Events** : If **Record Live Chat Events** setting is enabled, enter the list of LiveChat interactions for RudderStack to track.
    * **Update Event Name in track call** : Use this setting to map the standard LiveChat callback events with custom event names.
[![LiveChat connection settings](/docs/images/event-stream-destinations/livechat-connection-settings-3.webp)](</docs/images/event-stream-destinations/livechat-connection-settings-3.webp>)

> ![info](/docs/images/info.svg)
> 
> For more information on this setting, refer to the Mapping events section below.

  * **Client-side Events Filtering** : This setting lets you specify which events should be blocked or allowed to flow through to LiveChat.


[![LiveChat connection settings](/docs/images/event-stream-destinations/livechat-connection-settings-4.webp)](</docs/images/event-stream-destinations/livechat-connection-settings-4.webp>)

> ![info](/docs/images/info.svg)
> 
> For more information on this setting, refer to the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide.

  * **Use device mode to send events** : As this is a [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>)-only destination, this setting is enabled by default and cannot be disabled.


## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) events to send all user-related information to LiveChat.

RudderStack sends various **optional** `identify` properties by calling the following LiveChat functions:

RudderStack property| LiveChat function  
---|---  
`context.traits.email`| [`set_customer_email`](<https://developers.livechat.com/docs/extending-chat-widget/javascript-api#set-customer-email>)  
`message.traits`| [`set_custom_variables`](<https://developers.livechat.com/docs/extending-chat-widget/javascript-api#set-session-variables>)  
`context.traits.name`| [`set_customer_name`](<https://developers.livechat.com/docs/extending-chat-widget/javascript-api#set-customer-name>)  
  
> ![info](/docs/images/info.svg)
> 
> RudderStack also leverages the `userId` present in the event to set a custom variable called `User ID`.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com",
      cart_value: "cart",
      "order date": "05/21/2019"
    });
    

## Track

If you enable the **Record Live Chat Events** dashboard setting, RudderStack records the LiveChat interactions and sends them as [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) events. You can then view and analyze these events in the other tools (connected to the same source in RudderStack).

> ![info](/docs/images/info.svg)
> 
> RudderStack only tracks the CTA interactions specified in the **List of Events** field in the dashboard settings. If this setting is not specified, RudderStack tracks all interactions specified in the Supported events section below.

### Supported events

RudderStack automatically records and sends the following [LiveChat callbacks](<https://developers.livechat.com/docs/extending-chat-widget/javascript-api#callbacks>):

LiveChat event| `track` event name| Description  
---|---|---  
[`onReady`](<https://developers.livechat.com/docs/extending-chat-widget/javascript-api#on-ready>)| `Ready`| When the chat widget has finished loading.  
[`onAvailabilityChanged`](<https://developers.livechat.com/docs/extending-chat-widget/javascript-api#on-availability-changed>)| `Availability Changed`| When the availability has changed for the current group.  
[`onVisibilityChanged`](<https://developers.livechat.com/docs/extending-chat-widget/javascript-api#on-visibility-changed>)| `Visibility Changed`| When the visibility of the chat widget has changed.  
[`onCustomerStatusChanged`](<https://developers.livechat.com/docs/extending-chat-widget/javascript-api#on-customer-status-changed>)| `Customer Status Changed`| When the customer’s status has changed.  
[`onNewEvent`](<https://developers.livechat.com/docs/extending-chat-widget/javascript-api#on-new-event>)| `New Event`| Called in case of both the incoming and outgoing events.  
[`onFormSubmitted`](<https://developers.livechat.com/docs/extending-chat-widget/javascript-api#on-form-submitted>)| `Form Submitted`| Called after a form is submitted in the chat.  
[`onRatingSubmitted`](<https://developers.livechat.com/docs/extending-chat-widget/javascript-api#on-rating-submitted>)| `Rating Submitted`| When the customer has rated a chat or cancelled the previous rating.  
[`onGreetingDisplayed`](<https://developers.livechat.com/docs/extending-chat-widget/javascript-api#on-greeting-displayed>)| `Greeting Displayed`| When the greeting is displayed to a customer.  
[`onGreetingHidden`](<https://developers.livechat.com/docs/extending-chat-widget/javascript-api#on-greeting-hidden>)| `Greeting Hidden`| When the customer cancels the greeting.  
[`onRichMessageButtonClicked`](<https://developers.livechat.com/docs/extending-chat-widget/javascript-api#on-rich-message-button-clicked>)| `Rich Message Button Clicked`| When the customer clicks the rich message button.  
  
### Mapping events

You can also update the standard LiveChat callback events with custom event names by enabling the **Update Event Name in track call** setting in the RudderStack dashboard and specifying the required mapping:

[![LiveChat event mapping](/docs/images/event-stream-destinations/livechat-event-mapping.webp)](</docs/images/event-stream-destinations/livechat-event-mapping.webp>)

Based on the mappings set in the above image, RudderStack replaces the standard event names `Ready` and `Availability Changed` with `new ready` and `new availability changed` respectively.

## FAQ

#### Where can I find the LiveChat license ID?

To get your LiveChat license ID, follow these steps:

  1. Log into your [LiveChat dashboard](<https://my.livechatinc.com/>).
  2. In the bottom left corner, click the **Settings** icon and go to **Website**.
  3. You can find the license ID included in the installation snippet:

[![LiveChat license ID](/docs/images/event-stream-destinations/livechat-license-id.webp)](</docs/images/event-stream-destinations/livechat-license-id.webp>)