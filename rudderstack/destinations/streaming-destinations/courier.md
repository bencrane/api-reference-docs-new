# Courier

Send data from RudderStack to Courier.

* * *

  * __2 minute read

  * 


[Courier](<https://www.courier.com/>) is an API and web studio for development teams to manage product-triggered notifications (email, chat, in-app, SMS, push, etc.) in one place.

> ![info](/docs/images/info.svg)
> 
> This destination is maintained by [Courier](<https://www.courier.com/docs/external-integrations/rudderstack>). For any issues, contact the Courier [support team](<mailto:support@courier.com>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **Courier** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Courier, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Courier**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully configure Courier as a destination, you will need to configure the following settings:

  * **API Key** : Enter your Courier API key. For more information on obtaining the API key, refer to the FAQ section.


## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to sync users from RudderStack to Courier. If a user already exists in Courier, RudderStack updates the user profile with the latest values.

A sample `identify` event is shown below:
    
    
    rudderanalytics.identify('1hKOmRA4GRlm', {
      name: 'Alex Keener',
      email: 'alex@example.com',
      avatar: 'https://example.com/avatars/alexkeener.webp',
      role: 'CEO'
    });
    

You can view the synced users in Courier’s [Users](<https://app.courier.com/users>) page or access them via Courier API’s.

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to ingest events into Courier, which can further be mapped to [Courier Automations](<https://www.courier.com/features/automations/>).

A sample `track` call is shown below:
    
    
    rudderanalytics.track('Cart checkout', {
      product: 'shoe-123',
      // additional properties
    })
    

The `track` events appear on Courier Studio on the [Rudderstack integration](<https://app.courier.com/channels/rudderstack>) page. For example, the `Cart checkout` event is mapped to `Send shipping details` automation:

[![Courier API Key](/docs/images/event-stream-destinations/courier-rudderstack-event.webp)](</docs/images/event-stream-destinations/courier-rudderstack-event.webp>)

## FAQ

#### Where can I find the Courier API key?

  1. Log in to your [Courier dashboard](<https://app.courier.com/>).
  2. Go to your app’s **Settings** > **API Keys**. You will find the Courier API key listed here:

[![Courier API Key](/docs/images/event-stream-destinations/courier-api-key.webp)](</docs/images/event-stream-destinations/courier-api-key.webp>)

> ![info](/docs/images/info.svg)
> 
> Copy the key based on the environment or scope you want to configure.