# TVSquared

Send your event data from RudderStack to TVSquared.

* * *

  * __3 minute read

  * 


[TVSquared](<https://tvsquared.com/>) is a television attribution platform that specializes in enterprise-scale cross-screen and multi-touch TV attribution and measurement.

RudderStack supports TVSquared as a destination where you can seamlessly send your event data.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **TVSquared** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the TVSquared native SDK from the `http://tvsquared.com` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the TVSquared SDK successfully.

## Get started

Once you have confirmed that the platform supports sending events to TVSquared, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **TVSquared**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully set up TVSquared as a destination, configure the following settings:

  * **Brand Id (Site ID)** : Enter the unique identifier indicating the TVSquared client to which the traffic belongs. It is of the format `TV-XXXXXXX-1` with a variable-length numeric value replacing `X`.
  * **Client Id (Collector Id)** : Enter the Client ID used to distribute the traffic and manage the load on the TVSquared servers effectively. It is numeric and can contain one or more values.
  * **Custom Metrics** : The **Property Name** values added in this field are sent to TVSquared for the events containing those event properties, along with the other defined TVSquared properties. For example, if the property added in the dashboard is `shipping` , then the shipping value is sent to TVSquared. A sample snippet for this is shown:


    
    
    rudderanalytics.track('Order Completed', {
      order_id: '5d4c7cb5',
      revenue: 99.9,
      shipping: 13.99,
      tax: 20.99,
      products: [
      ]
    });
    

  * **Client-side Events Filtering** : This setting lets you specify which events should be blocked or allowed to flow through to TVSquared. See [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) for more information.


## Page

When you make a [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call, RudderStack makes a call to TVSquared to record a page view.
    
    
    rudderanalytics.page('new category',
    'page name',
    {
      url: 'url',
      path: '/path'
    });
    

## Track

Calling the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) method triggers TVSquared’s `Action Tracker` method.

By default, TVSquared accepts the following properties in your `track` events:

  * `revenue`
  * `product type (category)`
  * `action id (order_id)`
  * `promo (promotion_id)`


> ![info](/docs/images/info.svg)
> 
> All the above parameters are optional. There is no requirement to add these to measure the uplift from TV. However, you can use this data for more detailed analysis as required. If there is no value to pass, RudderStack sets an empty string instead.

A sample `track` call is as shown:
    
    
    rudderanalytics.track('Order Completed', {
      order_id: '5d4c7cb5',
      category: 'category',
      revenue: 99.9,
      shipping: 13.99,
      tax: 20.99,
      products: [
    
      ],
      promotion_id: 'PROMO_1234'
    });