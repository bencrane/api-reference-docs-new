# Track

Get started with the RudderStack Track API call.

* * *

  * __4 minute read

  * 


The `track` call lets you record the user’s actions along with any properties associated with them.

> ![info](/docs/images/info.svg)
> 
> Each user action is called an event. Every event has a name associated with it, for example, `Product Reviewed`. This event can have properties associated with it, like `review_id` and `rating`.

> ![success](/docs/images/tick.svg)
> 
> For ecommerce-specific events, refer to [Ecommerce events specification](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).

## Event Names

It is recommended that events have a descriptive human readable name. This allows everyone (include you 6 months from now) to instantly understand the meaning of an event.

Vague or abstract names like ProdRV and Event2 should be avoided. Instead focus on unique unabiguous names like **Product Reviewed** and **Order Submitted**. A common framework is to use nouns and past tense verbs.

> ![success](/docs/images/tick.svg)
> 
> Identity data (user traits) will be automatically added to `track` calls from the most recent `identify` call, so you do not need to add it manually. This information will be included in a `traits` object in the `context` fields of the payload. Note that `track` calls also automatically handle `anonymousId` values associated with the user.
> 
> See our [Identify](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) doc for more details.

## Sample payload

Here is a sample payload for the `track` event after removing [Common fields](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/>):
    
    
    {
      "type": "track",
      "event": "Product Reviewed",
      "properties": {
        "review_id": "86ac1cd43",
        "product_id" : "9578257311",
        "rating" : 3.0,
        "review_body" : "OK for the price. It works but the material feels flimsy."
      }
    }
    

The corresponding event that generates the above payload via the [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) is:
    
    
    rudderanalytics.track("Product Reviewed", {
      review_id: "86ac1cd43",
      product_id: "9578257311",
      rating: 3.0,
      review_body: "OK for the price. It works but the material feels flimsy."
    })
    

## Send a sample `track` call

Use RudderStack’s **Event Playground app** to send sample events to RudderStack and test the data flow without any instrumentation.

Click **Send** to see the API call in the **Network** tab of your browser’s developer tools.

Follow these steps to use the **Event Playground app** to send test events to your account:

  1. Sign in to the [RudderStack dashboard](<https://app.rudderstack.com/>). Note the [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) at the top of the default **Connections** page.

[![Data plane URL](/docs/images/general/data-plane-url.webp)](</docs/images/general/data-plane-url.webp>)

  2. Set up a [source](<https://www.rudderstack.com/docs/dashboard-guides/sources/#add-a-source>) and note its [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination. ](</docs/resources/glossary/#write-key>).

[![JavaScript SDK source write key](/docs/images/get-started/quickstart/js-write-key.webp)](</docs/images/get-started/quickstart/js-write-key.webp>)

  3. Click **Use My Account** in the **Event Playground app** below and specify the write key and data plane URL obtained in the above steps.


  4. Click **Save**.
  5. Select the required **API Method** from the dropdown. You can also edit the relevant fields or traits/properties.
  6. Click **Send to my account** to send the event.
  7. Go to the [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/#view-source-live-events>) viewer of your source (set up in Step 2) to verify that the event is successfully received.


## Track fields

Apart from the [Common fields](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/>), the `track` call accepts the following fields:

**Field**| **Type**| **Presence**| **Description**  
---|---|---|---  
`event`| String| Required| Name of the user action  
`properties`| Object| Optional| Includes the properties associated with the event. For more information, check the Properties section below.  
  
## Properties

Properties are additional contextual information that are associated with a `track` event, that give more clarity of your users’ actions.

RudderStack has reserved some standard properties listed in the following table and handles them in a special manner.

**Property**| **Type**| **Description**  
---|---|---  
`revenue`| Number| The revenue amount as a result of an event. For e.g., a product worth $20.00 would result in a `revenue` of `20.00`.  
`currency`| String| The currency of the revenue as a result of the event, set in ISO 4127 format. If this is not set, RudderStack assumes the revenue is in USD.  
`value`| String| An abstract value associated with an event, to be used by various teams.  
  
> ![success](/docs/images/tick.svg)
> 
> Different destinations recognize some of the above data points differently.
> 
> With RudderStack, you don’t have to worry about these inconsistencies across destinations. Our open source destination transformer code handles these destination-specific conversions automatically.
> 
> For example, Mixpanel has a `track_charges` method for tracking revenue. In this case, you can pass the `revenue` property and RudderStack will handle the conversion automatically through our destination transformer code. You can see the Mixpanel transformer code in our [open source Github repo](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/mp>).