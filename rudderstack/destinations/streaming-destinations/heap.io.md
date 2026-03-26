# Heap.io Destination

Send your event data from RudderStack to Heap.io.

* * *

  * __3 minute read

  * 


[Heap.io](<https://heap.io/>) is a popular analytics platform built for marketers, product managers, and customer success teams.

RudderStack supports Heap.io as a destination to which you can send your event data in real-time.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/heap>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Heap.io** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Heap native SDK from the`https://cdn.heapanalytics.com/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Heap SDK successfully.

## Setup

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/signup?type=freetrial>), add the source. Then, from the list of destinations, select **Heap.io**.
  2. Assign a name to your destination and click **Next**.


### Connection settings

Setting| Description  
---|---  
App ID| Enter your Heap App ID.  
  
### Event filtering settings

Setting| Description  
---|---  
Client-side Events Filtering| Specify which events should be blocked or allowed to flow through to Heap.  
  
See the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide for more information.  
  
### Web SDK settings

Setting| Description  
---|---  
Use device mode to send events| Turn on this toggle to send events from your JavaScript SDK in [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs.  
  
See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to capture the relevant details about the visiting user.

> ![warning](/docs/images/warning.svg)
> 
> `userId` or `anonymousId` is a **required** field to send the `identify` call successfully.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com",
    })
    

### Supported traits mapping

RudderStack maps the following user traits to the corresponding Heap properties:

RudderStack property| Heap property  
---|---  
`userId`  
`traits.userId`  
`traits.id`  
`context.traits.userId`  
`context.traits.id`  
`anonymousId`  
Required| `identity`  
`traits`  
`context.traits`| `properties`  
  
> ![info](/docs/images/info.svg)
> 
> If `idempotencyKey` is present in `traits` or `context.traits`, it is removed before sending to Heap.

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to track your user actions and their associated properties.

> ![warning](/docs/images/warning.svg)
> 
> `userId` or `anonymousId` is a **required** field to send the `track` call successfully.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Order Completed", {
      userId: "1hKOmRA4GRlm",
      order_id: "12345",
      category: "clothing",
      revenue: 99.9,
      shipping: 13.99,
      tax: 10.99,
      promotion_id: "NEW_PROMO_10",
    })
    

### Supported properties mapping

RudderStack maps the following event properties to the corresponding Heap properties:

RudderStack property| Heap property  
---|---  
`userId`  
`traits.userId`  
`traits.id`  
`context.traits.userId`  
`context.traits.id`  
`anonymousId`  
Required| `identity`  
`event`  
Required| `event`  
`properties`| `properties`  
`timestamp`  
`originalTimestamp`| `timestamp`  
`properties.idempotencyKey`| `idempotency_key`  
  
> ![info](/docs/images/info.svg)
> 
> RudderStack maps `properties.idempotencyKey` to the top-level `idempotency_key` field in the Heap event. It is then removed from the nested properties object to match the Heap API specification.

## FAQ

#### Where can I find my Heap App ID?

  1. Log in to your [Heap account](<https://heapanalytics.com/app/settings/projects>).
  2. Go to **App** > **Settings** > **Projects** , and copy the required development or production App ID.