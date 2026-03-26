# What's New in JavaScript SDK v3

> Version: Latest (v3)v1.1

# What's New in JavaScript SDK v3

Understand the newly introduced features in JavaScript SDK v3.

* * *

  * __3 minute read

  * 


This guide details the new features introduced in JavaScript SDK v3.

## Event dispatching for initialization and ready phases

The SDK v3 supports dispatching two new events to document - `RSA_Initialised` and `RSA_Ready` \- when it is in the initialized and ready phases respectively.

These events provide a reference to the analytics instance (`analyticsInstance`) whenever you want to use it to invoke any API method, for example, `getUserId`.

You can listen to the above events as follows:
    
    
    <script>
       document.addEventListener('RSA_Initialised', function(e) {
         console.log('RSA_Initialised', e.detail.analyticsInstance);
       })
       
       document.addEventListener('RSA_Ready', function(e) {
         console.log('RSA_Ready', e.detail.analyticsInstance);
       })
       
    </script>
    

You can use this feature as an alternative to the `ready` API method and the [`onLoaded` load option](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#loading-options>) for orchestration with JavaScript frameworks and libraries. It is useful in cases where relevant business logic is in functions that cannot be declared alongside the analytics integration or they need to be declared on a decoupled code base for some reason.

## Batching in XHRQueue plugin

Batching feature is available only when using the [`XhrQueue`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#plugins>) plugin to send events to data plane.

The XhrQueue plugin leverages the [`queueOptions`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#queueopts>) load option to control the behavior of the persistence queue that buffers events in local storage before sending them to the data plane.

You can enable and configure batch mode to send events to the data plane using the `queueOptions.batch` object while loading the SDK, as shown:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      queueOptions: {
        minRetryDelay: 1000, // ms
        batch: {
          enabled: true,
          maxItems: 100,
          maxSize: 1024 * 512 // 512 KB
          flushInterval: 60000 // ms
        },
        ...
      },
      ...
    });
    

The following table details the `queueOptions.batch` object parameters:

Parameter| Data type| Description| Default value  
---|---|---|---  
`enabled`| Boolean| Determines if the SDK should activate the batching functionality.| false  
`maxItems`| Integer| Maximum number of events in a batch.| 100  
`maxSize`| Integer| Maximum batch payload size.| 512 KB (Also, the maximum configurable value)  
`flushInterval`| Integer| Minimum interval between two batch requests.| 60000 ms  
  
> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * `queueOptions.batch` is an optional object, meaning batching is disabled by default.
>   * The SDK makes a batch request when either of the following criteria is met:
>     * `maxItems` in a batch is reached.
>     * `maxSize` of the batch is reached.
>     * Time period of `flushInterval` ms has elapsed since the last batch request.
> 


## Debugging

The SDK v3 exposes the following objects globally that can assist in debugging:

Name| Description  
---|---  
`window.rudderAnalyticsBuildType`| Denotes the SDK build type that has been loaded based on browser capabilities (`modern` or `legacy`).  
`window.RudderStackGlobals`| Contains some SDK application-level values, `preloadBuffer` (before it is consumed) and the SDK instance state per write key. You can use it to debug and see values in state at any point in time.  
  
## Server-side cookies for Intelligent Tracking Prevention (ITP)

The JavaScript SDK v3 implements server-side cookies to achieve:

  * Extended lifespan compared to the client-managed cookies
  * Consistent and uniform user experience across all browsers


You can leverage the `useServerSideCookies` configuration option of the JavaScript SDK’s [`load` API](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#loading-options>) to make network requests to the website’s server and set cookies via the response headers.

See [Server-side Cookies in JavaScript SDK v3](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/server-side-cookies/>) for more information on this feature.

  


  * [![](/docs/images/previous.svg)Previous](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/breaking-changes/>)
  * [Next ![](/docs/images/next.svg)](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/sdk-hardening/>)