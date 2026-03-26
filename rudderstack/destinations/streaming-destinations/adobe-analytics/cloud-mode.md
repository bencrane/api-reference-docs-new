# Adobe Analytics Cloud Mode Integration

Send events to Adobe Analytics using RudderStack cloud mode.

* * *

  * __2 minute read

  * 


RudderStack lets you send your event data to Adobe Analytics via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/develop/src/v0/destinations/adobe_analytics>).

## Track

RudderStack categorizes the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) events sent to Adobe into the following three types:

  1. User tracking events
  2. [Ecommerce events](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adobe-analytics/ecommerce-events/>)
  3. [Heartbeat (video) events](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adobe-analytics/adobe-analytics-heartbeat/>)


A sample `track` call is as shown:
    
    
    rudderanalytics.track("User clicked link", {
      category: "click",
      label: "URL click"
    })
    

Note that:

  * Before sending the user tracking and heartbeat `track` events, you must [map them in the RudderStack dashboard](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adobe-analytics/setting-up-adobe-analytics-in-rudderstack/#connection-settings>).
  * RudderStack sends the ecommerce events to Adobe if they conform to the following mapping:

RudderStack ecommerce event| Adobe event  
---|---  
`Product Viewed`| `prodView`  
`Product List Viewed`| `prodView`  
`Product Added`| `scAdd`  
`Product Removed`| `scRemove`  
`Order Completed`| `purchase`  
`Cart Viewed`| `scView`  
`Checkout Started`| `scCheckout`  
`Cart Opened`| `scOpen`  
`Opened Cart`| `scOpen`  
  
## Page

RudderStack sends a page view event to Adobe Analytics whenever you make a [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call.

A sample `page` call is as shown:
    
    
    // Passing page category, name and properties
    rudderanalytics.page("category", "name", {
      path: "path",
      url: "url",
      title: "title",
      search: "search",
      referrer: "referrer",
    })
    

If this call is made, the `pageName` of the `window.s` variable will be set as **Viewed Page name**. RudderStack also sends other information like `referrer`,`url`, etc.

> ![info](/docs/images/info.svg)
> 
> For every `page` call, RudderStack sets the mappings done in the dashboard as contextual data, eVars, hiers, lists and props. It calls the `t()` method to compile all the set variables and sends them to Adobe Analytics.

## Overriding Adobe parameters

When sending data to Adobe Analytics via cloud mode, RudderStack lets you override the values of certain Adobe parameters in the final XML payload by passing the following event properties:

Property name| Data type| Description  
---|---|---  
`overrideEvars`| Object| Sets the value of the `eVar` tag.  
  
**Example** :  
  

    
    
    {  
      “evar1”: “value1”,  
      “evar2”: “value2”,  
    }  
  
`overrideHiers`| Object| Sets the value of the `hier` tag.  
  
**Example** :  
  

    
    
    {  
      “hier1”: “oh1”,  
      “hier2”: “oh2”,  
    }  
  
`overrideLists`| Object| Sets the value of the `list` tag.  
  
**Example** :  
  

    
    
    {  
      “list1”: “bike, fazer90”  
    }  
  
`overrideCustomProperties`| Object| Sets the value of the `prop` tag.  
  
**Example** :  
  

    
    
    {  
      “property1”: “somevalue”  
    }  
  
`overrideEventString`| String| Sets the value of the event string.  
  
**Example** : `scAdd`  
`overrideProductString`| String| Sets the value of the product string.  
  
**Example** :  
  

    
    
    ";product1;Games;event1=1"  
  
`overrideEventName`| String| Fallback for events that are neither mapped or ecommerce events.  
  
**Example** : `tracking event`  
`overridePageView`| Boolean| Send link and page values exclusively. If set to `true`, RudderStack sends page-related tags to Adobe, otherwise it sends link-related tags.