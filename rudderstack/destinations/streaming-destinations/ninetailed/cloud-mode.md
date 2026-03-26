# Ninetailed Cloud Mode Integration Beta

Send events to Ninetailed using RudderStack cloud mode.

* * *

  * __less than a minute

  * 


> ![info](/docs/images/info.svg)
> 
> RudderStack recommends sending events to Ninetailed in device mode over the cloud mode.

After you have successfully instrumented Ninetailed as a destination in RudderStack, follow this guide to correctly send your events to Ninetailed in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/main/src/cdk/v2/destinations/ninetailed>).

> ![info](/docs/images/info.svg)
> 
> RudderStack leverages the Ninetailed [Experience API](<https://docs.ninetailed.io/for-developers/experience-api>) for sending the events.

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create or update a user profile in Ninetailed.

A sample `identify` call is as shown:
    
    
    rudderanalytics.identify("12345", {
      firstname: "Alex",
      city: "New Orleans",
      country: "USA",
      phone: "8005550100",
      email: "alex@example.com"
    })
    

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) API to record user events and the associated properties.

A sample `track` call is as shown:
    
    
    rudderanalytics.track("Product Reviewed", {
      review_id: "86ac1cd43",
      product_id: "9578257311",
      rating: 3.0,
      review_body: "Good product."
    });