# Detect Ad-blocked Pages

> Version: Latest (v3)v1.1

# Detect Ad-blocked Pages

Detect ad-blocked pages via the RudderStack JavaScript SDK.

* * *

  * __2 minute read

  * 


The JavaScript SDK lets you send a page view containing the relevant markers that determine whether a page is ad-blocked. You can analyze this data to find what percentage of your website’s pages are affected by ad blockers.

## How the feature works

The JavaScript SDK makes a `HEAD` request to the [source config endpoint](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#loading-options>) (by default, it is `https://api.rudderstack.com/sourceConfig`) with a query parameter that ad blockers typically block (`?view=ad`). It then determines if the ad blockers are active depending on whether the request succeeds or fails.

Thus, it is a good way to identify how many user sessions have active ad blockers.

> ![info](/docs/images/info.svg)
> 
> This feature **will not work** if the JavaScript SDK itself is unable to load successfully due to ad blockers.
> 
> Hence, RudderStack recommends using this feature if you are serving the JavaScript SDK over a [custom domain](<https://www.rudderstack.com/docs/user-guides/how-to-guides/custom-domains/>).

## Send ad-blocked page view

To send an ad-blocked page view, load the JavaScript SDK as shown:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
        sendAdblockPage: true,
        sendAdblockPageOptions: {
            integrations: {
                All: false,
                Amplitude: true
            }
        },
        ...
    });
    

Replace the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) and [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) in the above snippet with their actual values.

The properties included in the above snippet are explained below:

Property| Description  
---|---  
`sendAdblockPage`| Enables the JavaScript SDK to send an additional `page` event along with the actual event whenever you make the `page` call and the SDK detects that ad blockers are active on that web page.  
`sendAdblockPageOptions`| The JavaScript SDK makes an implicit `page` call with the specified options.  
  
With `sendAdblockPageOptions` (containing the [`IntegrationOpts`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#integrationopts>) object), you can specify the destinations to which you want to forward this `page` call. See [Filtering selective destinations](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/>) for more information.

The implicit `page` call semantics are shown:
    
    
    rudderanalytics.page(
        "RudderJS-Initiated",
        "ad-block page request", {
            path: "/ad-blocked"
        },
        sendAdblockPageOptions
    );
    

  * [![](/docs/images/previous.svg)Previous](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/register-custom-integrations/>)
  * [Next ![](/docs/images/next.svg)](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/autotrack-page-metrics/>)