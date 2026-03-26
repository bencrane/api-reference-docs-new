# Ninetailed Web Device Mode Integration Beta

Send events to Ninetailed using RudderStack web device mode.

* * *

  * __2 minute read

  * 


> ![info](/docs/images/info.svg)
> 
> RudderStack recommends sending events to Ninetailed in device mode over the cloud mode.

After you have successfully instrumented Ninetailed as a destination in RudderStack, follow this guide to correctly send your events to Ninetailed in [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/Ninetailed>).

> ![info](/docs/images/info.svg)
> 
> In web device mode, RudderStack uses the native [Ninetailed SDK](<https://docs.ninetailed.io/for-developers/experience-sdk/sending-events>) to send the events.
> 
> As mentioned in the [Setup Guide](<https://www.rudderstack.com/docs/destinations/streaming-destinations/ninetailed/setup-guide/>), you need to [install the Ninetailed SDK](<https://docs.ninetailed.io/for-developers/experience-sdk/getting-started>) as an npm package before sending the events.

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to send a [`identify`](<https://docs.ninetailed.io/for-developers/experience-sdk/sending-events#identify>) event to Ninetailed.

A sample `identify` call is as shown:
    
    
    rudderanalytics.identify("12345", {
      firstname: "Alex",
      city: "New Orleans",
      country: "USA",
      phone: "8005550100",
      email: "alex@example.com"
    })
    

### Supported mappings

RudderStack maps the following properties to the corresponding Ninetailed fields:

RudderStack property| Ninetailed property| Data type  
---|---|---  
`userId`| `userId`| String  
`traits`| `traits`| Object  
  
## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) API to send a [`track`](<https://docs.ninetailed.io/for-developers/experience-sdk/sending-events#track>) event to Ninetailed.

A sample `track` call is as shown:
    
    
    rudderanalytics.track("Product Reviewed", {
      review_id: "86ac1cd43",
      product_id: "9578257311",
      rating: 3.0,
      review_body: "Good product."
    });
    

### Supported mappings

RudderStack maps the following properties to the corresponding Ninetailed fields:

RudderStack property| Ninetailed property| Data type  
---|---|---  
`event`  
Required| `event`| String  
`properties`| `properties`| Object  
  
## Page

You can use the [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call to send a [`page`](<https://docs.ninetailed.io/for-developers/experience-sdk/sending-events#page>) event to Ninetailed.

A sample `page` call is shown below:
    
    
    rudderanalytics.page();
    

### Supported mappings

RudderStack maps the following properties to the corresponding Ninetailed fields:

RudderStack property| Ninetailed property| Data type  
---|---|---  
`properties`| `properties`| Object