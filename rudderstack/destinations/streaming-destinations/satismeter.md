# SatisMeter Destination

Send your event data from RudderStack to SatisMeter.

* * *

  * __4 minute read

  * 


[SatisMeter](<https://clarity.microsoft.com/>) is a customer feedback collection tool. It helps you derive real-time insights on customer satisfaction and monitor your products’ performance.

RudderStack supports SatisMeter as a destination where you can seamlessly send your event data.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **SatisMeter** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to SatisMeter, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **SatisMeter**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully configure SatisMeter as a destination, you will need to configure the following settings:

  * **Write Key** : Enter your SatisMeter write key for authentication. For more information on obtaining the write key, refer to the FAQ section below.
  * **Identify Anonymous Users** : Enable this setting to allow RudderStack to identify anonymous users using `anonymousId`.
  * **Record SatisMeter Events** : Enable this setting to allow RudderStack to automatically record your SatisMeter events as [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) events.
    * **List of Events** : Specify the list of events to be automatically tracked.
    * **Update Event Name in track call** : Enable this setting to update your `track` event names before sending them to other destinations.
      * **Mapping to update the event name in the track call** : Use this setting to map the standard SatisMeter events automatically recorded by RudderStack to custom `track` event names.


For more information on these settings, refer to the Automatically recording SatisMeter events section below.

  * **Client-side Events Filtering** : This setting lets you specify which events should be blocked or allowed to flow through to SatisMeter. For more information on this setting, refer to the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide.
  * **Use device mode to send events** : As this is a [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>)-only destination, this setting is enabled by default and cannot be disabled.
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to identify a user interacting with the SatisMeter survey.

> ![info](/docs/images/info.svg)
> 
> You must send the `createdAt` trait in your `identify` calls to keep a record of how long the user has interacted with the survey.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com",
      createdAt: "2022-02-01T19:14:18.381Z"
    });
    

### Supported mappings

RudderStack maps the following `identify` traits to the corresponding SatisMeter properties:

RudderStack property| SatisMeter property  
---|---  
`userId`  
Required, if **Identify Anonymous User** setting is disabled in the dashboard.| `userId`  
[`anonymousId`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#anonymous-id>)  
If **Identify Anonymous User** setting is enabled in the dashboard.| `userId`  
`context.traits.createdAt`  
Required| `traits.createdAt`  
`context.traits`| `traits`  
  
## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to [trigger a SatisMeter survey](<https://support.satismeter.com/hc/en-us/articles/6980449391891-User-events>).

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Response Submitted")
    

> ![warning](/docs/images/warning.svg)
> 
> You must send an `identify` call to identify a user before making a `track` call that records their survey interaction. Otherwise, SatisMeter maps this interaction to an anonymous user.

### Supporting mappings

RudderStack maps the following event properties to the corresponding SatisMeter properties:

RudderStack event/property| SatisMeter event/property| Data type  
---|---|---  
`event`  
Required| `event`| String  
  
> ![warning](/docs/images/warning.svg)
> 
> SatisMeter does not accept any `track` event properties except the event name.

### Automatically recording SatisMeter events

If you enable the **Record SatisMeter Events** setting in the dashboard, RudderStack automatically tracks and records the events listed in the **List of Events** fields as `track` events. You can then view and analyze these events using other tools (connected to the same source in RudderStack).

[![SatisMeter write key](/docs/images/event-stream-destinations/record-satismeter-events.webp)](</docs/images/event-stream-destinations/record-satismeter-events.webp>)

In the above image, RudderStack automatically records the standard SatisMeter events `Display`, `Complete`, `Progress`, and `Dismiss` as `track` events.

You can also update the standard SatisMeter event names by enabling the **Update Event Name in track call** dashboard setting and specifying the mapping:

[![SatisMeter write key](/docs/images/event-stream-destinations/satismeter-update-track-event-name.webp)](</docs/images/event-stream-destinations/satismeter-update-track-event-name.webp>)

In the above example, RudderStack renames the standard SatisMeter event `Complete` to `Survey Completed` before sending it to the other destinations.

## FAQ

#### Where can I find the SatisMeter write key?

To get your SatisMeter write key ID, follow these steps:

  1. Log into your [SatisMeter dashboard](<https://app.satismeter.com/>).
  2. Select your project and go to **Settings** > **Installation** to find your SatisMeter write key:

[![SatisMeter write key](/docs/images/event-stream-destinations/satismeter-write-key.webp)](</docs/images/event-stream-destinations/satismeter-write-key.webp>)