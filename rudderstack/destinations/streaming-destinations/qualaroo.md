# Qualaroo

Send your event data from RudderStack to Qualaroo.

* * *

  * __4 minute read

  * 


[Qualaroo](<https://qualaroo.com/>) is a customer survey and user feedback platform. It lets you survey your users to understand how they are using your product and what they think of it.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **Qualaroo** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Qualaroo, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Qualaroo**.
  2. Assign a name to your destination and click **Continue**.


## Connection settings

To successfully configure Qualaroo as a destination, you will need to configure the following settings:

  * **Customer ID** : Enter your Qualaroo customer ID.
  * **Site Token** : Enter your Qualaroo site token.


> ![info](/docs/images/info.svg)
> 
> For more information on obtaining your Qualaroo customer ID and site token, refer to the FAQ section below.

  * **Record Qualaroo Events** : Enable this setting to allow RudderStack to automatically record your Qualaroo callback events as `track` events. You can then view and analyze these events using other tools (connected to the same source in RudderStack). For more information, refer to the Recording Qualaroo callback events section below.
    * **List of Events** : Select the list of events from dropdown which RudderStack automatically records as `track` events.
    * **Update Event Name in track call** : Enable this setting to update the event name in the `track` call.
      * **Mapping to update the Event Name in track call** : Use this setting to map your events with the standard Qualaroo callback events.
  * **Client-side Events Filtering** : This setting lets you specify which events should be blocked or allowed to flow through to Qualaroo. For more information on this setting, refer to the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide.
  * **Use device mode to send events** : As this is a [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>)-only destination, this setting is enabled by default and cannot be disabled.
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to send user-related information to Qualaroo.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("alex@example.com", {
      name: "Alex Keener",
      age: 25
    })
    

RudderStack uses Qualaroo’s [Identity API](<https://help.qualaroo.com/hc/en-us/articles/201956628-Using-the-Identity-API-call>) method to send the user information.

> ![info](/docs/images/info.svg)
> 
> If an empty string is passed as an identifier, Qualaroo considers the user to be an unknown visitor or a user with no account.

### Supported mapping

The following table lists the mappings between the RudderStack and Qualaroo properties:

RudderStack property| Qualaroo property  
---|---  
`userId`  
`context.traits.email`  
`context.traits.userId`  
`context.traits.id`| `identify`  
`context.traits`| `traits`  
  
## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to track user activities and send this information to Qualaroo.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Product Viewed")
    

RudderStack maps the event name to Qualaroo’s `Triggered event` property. It then calls the `_kiq.push(['set', ...])` method and passes the trait as `Triggered event: event`.

> ![warning](/docs/images/warning.svg)
> 
> Qualaroo does not accept any `track` event properties.

### Recording Qualaroo callback events

You can use the **Record Qualaroo Events** dashboard setting to allow RudderStack to automatically record your specified Qualaroo callback events as `track` events. You can then view and analyze these events using other tools (connected to the same source in RudderStack).

Use the **List of Events** dashboard setting to specify the callback events to be automatically recorded:

[![List of Qualaroo events to be recorded automatically](/docs/images/event-stream-destinations/qualaroo-event-list.webp)](</docs/images/event-stream-destinations/qualaroo-event-list.webp>)  


RudderStack supports recording the following [Qualaroo callback events](<https://help.qualaroo.com/hc/en-us/articles/201447336-Using-Event-Handler-Callbacks>):

Event name| Description  
---|---  
`show`| When a survey is displayed.  
`close`| When a visitor submits the survey.  
`submit`| When a visitor replies to a question.  
`noTargetMatch`| When no surveys are set to fire.  
  
You can also map your `track` events to the standard Qualaroo callback events using the **Mapping to update the Event Name in track call** dashboard setting:

[![Map events to standard Qualaroo events](/docs/images/event-stream-destinations/qualaroo-update-event-name.webp)](</docs/images/event-stream-destinations/qualaroo-update-event-name.webp>)

## Page

You can use the [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call to send any page-related information to Qualaroo.

A sample `page` call is shown below:
    
    
    rudderanalytics.page("Home")
    

RudderStack concatenates the page’s `name` and `category` and maps it to Qualaroo’s `Viewed Page` property. It then calls the `_kiq.push(['set', ...])` method and passes the trait as `Viewed Page: name+category`.

> ![warning](/docs/images/warning.svg)
> 
> Qualaroo does not accept any `page` event properties.

## FAQ

#### Where can I find the Qualaroo customer ID and site token?

To get your Qualaroo customer ID and site token, follow these steps:

  1. Log into your [Qualaroo dashboard](<https://app.qualaroo.com/dashboard>).
  2. Click the **Install Code** option:

[![Install code option in Qualaroo dashboard](/docs/images/event-stream-destinations/qualaroo-install-code.webp)](</docs/images/event-stream-destinations/qualaroo-install-code.webp>)

  3. Click **Paste code in website source code or GTM**.
  4. In the **Copy the Code** section, look for `s.src` and note the mentioned URL:

[![Qualaroo JavaScript URL](/docs/images/event-stream-destinations/qualaroo-js-url.webp)](</docs/images/event-stream-destinations/qualaroo-js-url.webp>)

Suppose your URL is `https://cl.qualaroo.com/ki.js/12345/j8N.js`, then `12345` is the customer ID and `j8N` is the site token.