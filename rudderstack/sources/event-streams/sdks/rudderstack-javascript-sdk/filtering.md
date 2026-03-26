# How to Filter Events in JavaScript SDK

> Version: Latest (v3)v1.1

# How to Filter Events in JavaScript SDK

Filter events sent to downstream destinations using the JavaScript SDK.

* * *

  * __2 minute read

  * 


This guide covers the following event filtering use cases:

  * Send all events to specific destinations (web device mode only)
  * Filter destinations at the event level
  * Filter client-side events before sending them to destinations (web device mode only)


## Filter destinations while loading the SDK

You can filter all events sent to [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) destinations by passing an [integrations](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#integrationopts>) object in the [`load` API](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#loading-options>) options. RudderStack then loads and sends events only to the allowed (and enabled) destinations.

> ![info](/docs/images/info.svg)
> 
> The `integrations` object in the `load` API only controls the loading of the device mode destinations. The data is **not** propagated to the individual event payloads automatically.
> 
> To [use the globally-defined integration options at the event level](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#useglobalintegrationsconfiginevents>), set the `useGlobalIntegrationsConfigInEvents` option of the `load` API to `true`.

A sample snippet to send event data only to the **Amplitude** and **Intercom** destinations:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
        integrations: {
            All: false,
            "Amplitude": true,
            "Intercom": true
        }
    });
    

## Filter destinations at event level

You can control filtering a single event to the allowed (and enabled) destinations.

A sample `track` event instrumentation to send the event only to the **Amplitude** destination:
    
    
    rudderanalytics.track(
        "Order Completed", {
            revenue: 30,
            currency: "USD",
            user_actual_id: 12345
        }, {
            integrations: {
                All: false,
                "Amplitude": true
            }
        }
    );
    

> ![warning](/docs/images/warning.svg)
> 
> The destination name in the `integrations` object should match the name exactly as displayed in the [RudderStack dashboard](<https://app.rudderstack.com/directory>). It should **not** be the name that you assigned to the destination while setting it up in RudderStack.
> 
> ![](/docs/images/dashboard-guides/amplitude-destination-name-webapp.webp)

### Use the global integrations object

You can also use the globally-defined `integrations` object ( [`useGlobalIntegrationsConfigInEvents`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#useglobalintegrationsconfiginevents>) option of the `load` API) to enforce the destination filtering settings at the event level **if** it is not defined in the event already.

> ![info](/docs/images/info.svg)
> 
> The SDK gives precedence to the `integrations` object defined at the event level over the globally-defined `integrations` object.

## Client-side event filtering

To implement client-side event filtering for [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) destinations, you can configure the [filtering options](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/#event-filtering-options>) in the RudderStack dashboard. This allows you to control which `track` events are sent to specific destinations without modifying your SDK implementation.

**No additional SDK configuration is required**. The JavaScript SDK automatically respects and applies the filtering rules you have set up in the dashboard.

  


  * [![](/docs/images/previous.svg)Previous](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/faq/>)
  * [Next ![](/docs/images/next.svg)](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/dynamic-configuration/>)