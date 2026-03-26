# Pipedream Destination

Send your event data from RudderStack to Pipedream.

* * *

  * __2 minute read

  * 


[Pipedream](<https://pipedream.com/>) lets you build and automate processes that connect APIs. It supports open source triggers and actions for hundreds of integrations.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/pipedream>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Pipedream** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
  
## Get started

Once you have confirmed that the source platform supports sending events to Pipedream, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Pipedream**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully configure Pipedream as a destination, you will need to configure the following settings:

  * **Pipedream URL** : Enter the URL associated with your Pipedream workflow. This is the endpoint where RudderStack sends the events.


> ![info](/docs/images/info.svg)
> 
> RudderStack supports both `HTTP` and `HTTPS` URLs. For `HTTPS`, make sure that you have a valid TLS certificate for successful event delivery.

  * **URL Method** : Choose the request method from the dropdown. RudderStack uses this method to send the HTTP requests to the configured endpoint. By default, it is set to **POST**.
  * **Headers** : Use this setting to add custom headers for your events while sending requests to your webhook. By default, RudderStack automatically adds the following headers for the **POST** and **PUT** requests:

Key| Value  
---|---  
`User-Agent`| `RudderStack`  
`Content-Type`| `application/json`  
  
> ![info](/docs/images/info.svg)
> 
>   * To add a dynamic header to your events, you can use RudderStack’s [Transformations](<https://www.rudderstack.com/docs/transformations/overview/>) feature. For more information, refer to the [Dynamic header support](<https://www.rudderstack.com/docs/destinations/webhooks/setup-guide/#add-dynamic-header-to-events>) section or this [sample transformation](<https://www.rudderstack.com/docs/transformations/templates/#dynamic-headers>).
>   * You can also add a dynamic path to your base URL. For more information, refer to the [Dynamically changing the endpoint URL](<https://www.rudderstack.com/docs/destinations/webhooks/setup-guide/#add-dynamic-path-to-base-url>) section or this [sample transformation](<https://www.rudderstack.com/docs/transformations/templates/#dynamic-path>).
> 


## Supported events

This destination supports all event types listed in the [RudderStack Event Specification](<https://www.rudderstack.com/docs/event-spec/standard-events/>) guide.

## FAQ

#### Where can I find the Pipedream URL?

  1. Log in to your [Pipedream dashboard](<>).
  2. From the left sidebar, go to **Workflows** and select your workflow. Your Pipedream URL will be listed here:

[![Pipedream workflow URL](/docs/images/event-stream-destinations/pipedream-url.webp)](</docs/images/event-stream-destinations/pipedream-url.webp>)