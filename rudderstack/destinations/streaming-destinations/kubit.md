# Kubit

Send your event data from RudderStack to Kubit.

* * *

  * __less than a minute

  * 


[Kubit](<https://www.kubit.ai/>) is a self-service product analytics platform with no-code integration that facilitates efficient data discovery. With Kubit, you can better understand your users’ behavior and use the insights to drive customer retention and your product growth.

> ![success](/docs/images/tick.svg)
> 
> Kubit consumes data from your cloud data warehouse directly, so you don’t have to configure it as a destination in RudderStack. For more information, refer to the [Kubit documentation](<https://docs.kubit.ai/docs>).

[![Kubit workflow](/docs/images/event-stream-destinations/kubit-workflow.webp)](</docs/images/event-stream-destinations/kubit-workflow.webp>)

> ![info](/docs/images/info.svg)
> 
> This destination currently supports only `identify` and `track` calls.

## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call lets you identify a visiting user and associate them to their actions. It also lets you record the traits about them like their name, email address, etc.

A sample `identify` call is as shown:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com",
    })
    

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you record the user events along with any associated properties.

A sample `track` call is as shown:
    
    
    rudderanalytics.track("Order Completed", {
      orderId: "A123",
      price: "5.67",
      currency: "USD",
    })