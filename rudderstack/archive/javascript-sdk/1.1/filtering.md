# Events and Destinations Filtering in JavaScript SDK

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk>)

# Events and Destinations Filtering in JavaScript SDK

Filter events for your allowlist or denylist via the RudderStack JavaScript SDK.

* * *

  * __less than a minute

  * 


This guide covers how to achieve the following filtering operations:

  * Filtering events while sending them to the specified destinations.
  * Filtering destinations where the SDK sends the event data.


## Filtering events

When sending events to a destination via [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>), you can specify which events should be discarded or allowed to flow through - by allowlisting or denylisting them using the [Client-side Event Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) feature.

## Filtering destinations

You can send the event data only to the selective destinations by passing an [integrations](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/load-js-sdk/#integrationopts>) object in the **loadOptions** parameter. RudderStack then loads or sends events only to the specified and enabled destinations.

  * A sample snippet to send event data only to the **Amplitude** and **Intercom** destinations:


    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
        integrations: {
            All: false,
            "Amplitude": true,
            "Intercom": true
        }
    });
    

  * A sample `track` method to send event data only to the **Amplitude** destination:


    
    
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
    

The [destination](<https://www.rudderstack.com/docs/destinations/streaming-destinations/>) name inside the `integrations` object should exactly be the same as displayed in the [RudderStack dashboard](<https://app.rudderstack.com/directory>).

  * [![](/docs/images/previous.svg)Previous](</docs/archive/javascript-sdk/1.1/data-storage-cookies/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/javascript-sdk/1.1/version-migration-guide/>)