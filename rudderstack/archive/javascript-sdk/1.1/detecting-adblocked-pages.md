# Detect Ad-blocked Pages

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk>)

# Detect Ad-blocked Pages

Detect ad-blocked pages via the RudderStack JavaScript SDK.

* * *

  * __2 minute read

  * 


The JavaScript SDK lets you send a page view containing the relevant markers that determine whether a page is ad-blocked. You can analyze this data to find what percentage of your website’s page views are affected by adblockers.

## Sending an ad-blocked page view

To send an ad-blocked page view, load the JavaScript SDK as shown:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
        sendAdblockPage: true,
        sendAdblockPageOptions: {
            integrations: {
                All: false,
                Amplitude: true
            }
        }
    });
    

> ![info](/docs/images/info.svg)
> 
> Replace the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) and [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) in the snippet with their actual values.

The properties included in the above snippet are explained below:

  * **`sendAdblockPage`** : Enables the JavaScript SDK to make a call to load the [Google AdSense](<https://www.google.com/adsense/start/>) library. If RudderStack fails to load this library, it concludes that an adblocker is enabled on the page.


> ![info](/docs/images/info.svg)
> 
> Since most adblockers block the request to the Google AdSense servers, this approach is assumed to be a good measure to detect the ad-blocked pages.

  * **`sendAdblockPageOptions`** : If the `sendAdblockPage` property is set to `true`, the JavaScript SDK makes an implicit `page` call about the ad-blocked pages.


With `sendAdblockPageOptions` (containing the [`IntegrationOpts`](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/load-js-sdk/#integrationopts>) object), you can specify the destinations to which you want to forward this `page` call.

Refer to the [Filtering selective destinations](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/filtering/#filtering-destinations>) guide for more information on filtering the destinations.

The implicit `page` call semantics is shown below:
    
    
    rudderanalytics.page(
        "RudderJS-Initiated",
        "ad-block page request", {
            path: "/ad-blocked",
            title: "error in script loading:: src::  http://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js id:: ad-block"
        },
        sendAdblockPageOptions
    );
    

  * [![](/docs/images/previous.svg)Previous](</docs/archive/javascript-sdk/1.1/version-migration-guide/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/javascript-sdk/1.1/javascript-sdk-enhancements/>)