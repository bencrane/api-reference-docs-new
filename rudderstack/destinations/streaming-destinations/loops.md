# Loops Beta

Send your event data from RudderStack to Loops.

* * *

  * __3 minute read

  * 


[Loops](<https://loops.so>) is an email platform for SaaS companies for sending marketing and transactional emails from the same platform.

> ![info](/docs/images/info.svg)
> 
> This integration is built by the Loops team. [Contact the Loops support team](<mailto:help@loops.so>) for any assistance.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/develop/src/cdk/v2/destinations/loops>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Beta
  * **Supported sources:** Web, Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Unity, AMP , Cloud, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Loops** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the platform supports sending events to Loops, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Loops**.
  2. Assign a name to your destination and click **Continue**.


### Connection settings

Setting| Description  
---|---  
API Key| Specify your Loops API key.  
  
## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) event to create or update contacts in Loops.

A sample `identify` call is as shown:
    
    
    rudderanalytics.identify("1hKOmRA4GRlmr123", {
      email: "alex@example.com", // Required for new contacts
      name: "Alex Keener",
      country: "United States",
    })
    

Make sure to pass the unique user identifier as the first parameter in your `identify` call.

Note that:

  * `email` is a **required** field for adding new contacts in Loops.
  * The existing contacts are updated in Loops based on the provided `userId` property. If an existing contact in Loops doesn’t have a `userId`, Loops attempts to match based on the provided `email`.
  * The `identify` traits are automatically added to the contact record as properties.


### Manage mailing list subscriptions

To manage a contact’s mailing list subscriptions, add a `mailingLists` property to match the expected [API format](<https://loops.so/docs/api-reference/update-contact#param-mailing-lists>):
    
    
    rudderanalytics.identify("1hKOmRA4GRlmr123", {
      email: "alex@example.com",
      name: "Alex Keener",
      country: "United States",
      mailingLists: {
        clxf1nxlb000t0ml79ajwcsj0: true,
        clxf2q43u00010mlh12q9ggx1: false
      },
    })
    

In the above example, the contact with the identifier `1hKOmRA4GRlmr123` is added to the mailing list with the ID `clxf1nxlb000t0ml79ajwcsj0` and unsubscribed from the mailing list with the ID `clxf2q43u00010mlh12q9ggx1`.

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) event to send user actions to Loops, which in turn are used to trigger [loops](<https://loops.so/docs/loop-builder>).

The event name should match the name of the event in Loops. Data sent in the `properties` object will be sent as [event properties](<https://loops.so/docs/events/properties>) to Loops, for use in your emails.

Create events and define their expected properties in [Settings > Events](<https://app.loops.so/settings?page=events>) in your Loops dashboard.

A sample `track` call sent to Loops is shown below:
    
    
    rudderanalytics.track("Signup", {
      firstName: "Alex",
      email: "alex@example.com",
      plan: "Pro"
    })
    

Note that:

  * You should identify the contact before sending a `track` event so that the event can be associated with a specific contact in Loops.
  * RudderStack persists any values in `context.traits` from your previous `identify` call in the `track` event properties and updates the contact record in Loops accordingly.


## FAQ

#### Where can I find the Loops API key?

  1. Go to your [Loops API Settings page](<https://app.loops.so/settings?page=api>).
  2. Generate or use an existing API key.
  3. Copy the key and paste it in the **API Key** field in the RudderStack dashboard.