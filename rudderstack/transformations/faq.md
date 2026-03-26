# Transformations FAQ

Answers to some of the commonly asked questions related to RudderStack’s Transformations feature.

* * *

  * __6 minute read

  * 


## Transformations

#### Are there any sample user transformations I can refer to?

See the [Transformation Templates](<https://www.rudderstack.com/docs/transformations/templates/>) guide for a list of prebuilt JavaScript functions that you can use to create transformations and implement use cases on your event data.

You can also check the [Sample RudderStack Transformations](<https://github.com/rudderlabs/sample-user-transformers>) GitHub repository.

#### Is the transformation connected to a source or destination?

A transformation is always connected to a destination. RudderStack gives you the option to add a transformation while setting up a destination:

[![Connecting a transformation](/docs/images/features/connecting-a-transformation.webp)](</docs/images/features/connecting-a-transformation.webp>)

#### Can I connect multiple transformations to a destination?

No, it is not possible to connect multiple transformations to a destination. Instead, you can implement multiple use-cases in the same transformation, for example, event filtering followed by cleaning.

#### Can I write a transformation that can be applied to a small batch of events?

Yes, you can use the `transformBatch` function to apply a transformation to a batch of events.

> ![info](/docs/images/info.svg)
> 
> For more information, see the [Applying transformation on a batch of events](<https://www.rudderstack.com/docs/transformations/usage/#apply-transformation-on-batch-of-events>) section.

#### What is the supported Python version for Python transformations?

RudderStack uses Python 3.11 for Python transformations (available only in the RudderStack Cloud [Growth](<https://rudderstack.com/pricing/>) and [Enterprise](<https://www.rudderstack.com/enterprise-quote/>) plans).

#### What is a referenced transformation?

If a library `L` is [imported by the transformations](<https://www.rudderstack.com/docs/transformations/libraries/>) `T1`, `T2`, and `T3`, then `T1`, `T2`, and `T3`are called the referenced transformations to `L`.

#### I used to write transformations like `function transform(events) {}`. Why am I not able to create new transformations this way?

By default, RudderStack supports writing functions that transform a single event instead of a batch of events. You can now define your transformation in the following manner:
    
    
    export function transformEvent(event, metadata) {
        return event;
    }
    
    
    
    def transformEvent(event, metadata):
        return event
    

#### Can I update my existing version v0 transformation code to the the latest version?

You cannot update an existing `Version: V0` transformation to the current version.

Instead, you can [create a new transformation](<https://www.rudderstack.com/docs/transformations/create/#adding-a-transformation>) based on the [`transformEvent` function](<https://www.rudderstack.com/docs/transformations/usage/#apply-transformation-on-single-event>), then reconnect your destinations with this transformation. Finally, delete the existing `Version: V0` transformation.

#### What are transformation and library revisions?

Using the [Event filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>), you can create and store a transformation or library as a draft without publishing them. These are called revisions.

Once the revisions meet the test criteria, you can restore and publish them for production use.

#### Which JavaScript functions are not supported in transformations?

JavaScript transformations run in an isolated environment — no Node.js modules (like `fs`, `require`) or browser APIs (like `window`, `btoa`) are available.

Only standard JavaScript features are supported.

## Device mode transformations

#### While sending events in device mode, how should I choose between event filtering and transformations?

You can choose any based on your requirements:

  * **[Event filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>)** : When you just want to filter out the events based on the event names. The event filtering takes place within the SDK and is **only applicable** for the `track` events.
  * **Transformations** : Transformations is a generic feature which can be used to manipulate the events, mask data, enrich events, implement specific actions on events. It involves a call to an external RudderStack service.


In case you plan to use both the above-mentioned features, your events will be filtered (based on the [event filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) settings in the RudderStack dashboard) and transformed (based on the applied transformation) before being sent to the destination.

#### Is there any added performance cost to using the transformations in device mode?

Yes, RudderStack makes a network call for each event (in case of JavaScript SDK) or a batch of events (in case of mobile SDKs) when the transformations are used in device mode.

#### Can I switch back to the previous version of an SDK while using a transformation in device mode?

  * **For Mobile SDKs** : Yes, you can switch back to the previous SDK version. However, the transformation might not be supported in the previous version.
  * **For JavaScript SDK** : It depends on the SDK installation method:
    * If installed through RudderStack CDN, it’s not possible to downgrade the SDK version.
    * If installed through NPM, it’s possible to downgrade the SDK version. However, the transformation might not be supported in the previous version.


#### Will my event be lost in case of a network error while using a transformation in device mode?

**No events are lost in case of mobile SDK’s** as they are saved locally in the database before being sent to the destination. Once sent successfully, they’re removed from the database.

However, there is a chance of events getting lost while sending them via JavaScript SDK in case of a network error as they are not persisted. However, the SDK retries multiple times before dropping the event.

## Libraries

#### How does RudderStack test any library updates?

If you update a library that is referenced in any transformation, RudderStack tests the new library code along with the transformation code against the default event payload. This ensures that the transformation does not break due to any changes in the library.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack currently does not support testing libraries with custom events.

#### Can I test my library with sample events?

RudderStack currently does not support testing libraries with custom events. It provides a default payload against which you can test the library code along with any referenced transformations.

#### Why am I not able to update my library?

If you update a library, [RudderStack tests the new library code](<https://www.rudderstack.com/docs/transformations/faq/#how-does-rudderstack-test-any-library-updates>) along with the referenced transformation code. This ensures that the transformation does not break due to any changes in the library.

If you’re unable to update the library, it is likely that that the transformation is breaking because of the changes. Add the referenced transformation code and test the changes thoroughly.

#### What is a referenced library?

If a transformation `T` [imports a library](<https://www.rudderstack.com/docs/transformations/libraries/>) `L` in its code, then `L` is called as a referenced library to `T`.

#### I cannot import libraries into my existing transformations. What should I do?

If you cannot import libraries into your existing transformations, there is a strong likelihood that your existing transformations are based on the older version (`Version: V0`). To confirm if your transformation is based on an older version, check if your transformation has **Version: V0** :

[![v0 transformations](/docs/images/features/older-transformation.webp)](</docs/images/features/older-transformation.webp>)

To import the libraries in a transformation, follow these steps:

  1. Create a new transformation by following the steps in the [Adding a transformation](<https://www.rudderstack.com/docs/transformations/create/#adding-a-transformation>) section.
  2. Add the updated transformation code as specified in the [`transformEvent` function](<https://www.rudderstack.com/docs/transformations/usage/#apply-transformation-on-single-event>) section.
  3. Connect the transformation to your destination. For more information, see [Connecting a transformation to the destination](<https://www.rudderstack.com/docs/transformations/manage/#connect-transformation-to-destination>) section.
  4. You can then import libraries in the transformation. For more information, see [Using libraries in transformations](<https://www.rudderstack.com/docs/transformations/libraries/>).


## IP allowlisting

#### Which RudderStack IPs should I allowlist while making external API calls?

Depending on your use case and the API endpoints you are trying to access, you will need to allowlist certain RudderStack IP addresses.

> ![info](/docs/images/info.svg)
> 
> Allowlisting is required when the external APIs you call restrict access by IP address.

  * **For testing transformations that leverage external API calls**


Make sure that the API providers allowlist the following IPs depending on your RudderStack region:

Region  
---  
**US**| **EU**  
  
  * 3.216.35.97
  * 18.214.35.254
  * 23.20.96.9
  * 34.198.90.241
  * 34.211.241.254
  * 44.236.60.231
  * 52.38.160.231
  * 54.147.40.62
  * 100.20.239.77

| 

  * 3.64.201.167
  * 3.66.99.198
  * 3.123.104.182
  * 3.125.132.33
  * 18.196.167.201
  * 18.198.90.215

  
  
  * **For production use cases**


Make sure that the API providers allowlist the following IPs depending on your RudderStack plan and region:

Plan| Region  
---|---  
| **US**| **EU**  
Free, Starter, and Growth| 

  * 3.216.35.97
  * 18.214.35.254
  * 23.20.96.9
  * 34.198.90.241
  * 34.211.241.254
  * 52.38.160.231
  * 54.147.40.62

| 

  * 3.123.104.182
  * 3.125.132.33
  * 18.198.90.215
  * 18.196.167.201

  
Enterprise| 

  * 3.216.35.97
  * 34.198.90.241
  * 44.236.60.231
  * 54.147.40.62
  * 100.20.239.77

| 

  * 3.66.99.198
  * 3.64.201.167
  * 3.123.104.182
  * 3.125.132.33

  
  
> ![warning](/docs/images/warning.svg)
> 
> **Limitation on port usage**
> 
> Note that RudderStack blocks all outbound traffic from the standard ports **1** to **1023** except for `HTTP (80)` and `HTTPS (443)` — this is applicable for both the EU and US clusters.
> 
> Make sure to use a different port for the service you are trying to access via the transformation.