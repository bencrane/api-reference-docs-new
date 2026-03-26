# JavaScript SDK FAQ

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk>)

# JavaScript SDK FAQ

Solutions to some commonly faced issues while using the RudderStack JavaScript SDK.

* * *

  * __2 minute read

  * 


This guide contains the answers to some commonly-asked questions about setting up, using and troubleshooting the JavaScript SDK.

#### Should I disable ad blockers on my browser?

Yes, it is important to ensure that no ad blockers are running on your browser, as they restrict the JavaScript SDK script from executing and storing user information in the browser.

#### Can I load multiple instances of RudderStack JavaScript SDK?

No, it is not possible to load multiple instances of the JavaScript SDK, as it is bound to exceed the maximum stack call size and give you an error.

#### How can I verify if the SDK sends the data to the desired destinations?

To verify if the SDK is transmitting the events to the specified destinations, go to the **Network tab** of the JavaScript console in your browser.

[![Sample page call](/docs/images/sample-page-call.webp)](</docs/images/sample-page-call.webp>)[![Sample track call](/docs/images/sample-track-call.webp)](</docs/images/sample-track-call.webp>)

If you cannot see any outbound requests, verify if you have installed and set up the JavaScript SDK correctly. Also, check if any adblockers are enabled on your browser.

#### What is the size limit on the event requests?

The [JavaScript SDK](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/>) exhibits the following behavior:

  * If the event size exceeds 32KB, the SDK logs an error message but forwards it to the RudderStack data plane (backend).
  * If you send the event using [`sendBeacon`](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/javascript-sdk-enhancements/#sending-events-using-beacon>), the SDK batches the events with a size limit of 64KB on the **entire** batch payload. If a single event’s size exceeds 64KB, the browser might drop the event. Note that this is applicable for the JavaScript SDK v1.1.


#### Can I send the event data to specific destinations only?

Yes, you can send your [event data only to the specific destinations](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/filtering/#filtering-destinations>) by stopping the SDK from loading the other [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) integrations.

#### What is the “Reserved Keyword” error?

When using the JavaScript SDK, you may run into the following error:
    
    
    Warning! : Reserved keyword used in traits -->  id with track call.
    

This is because one or more keys in your `traits` or `properties` object have the same value as a reserved keyword.

RudderStack reserves the following keywords as keys for a standard event payload, and you should avoid using these while naming your event traits and properties:
    
    
    "anonymous_id";
    "id";
    "sent_at";
    "received_at";
    "timestamp";
    "original_timestamp";
    "event_text";
    "event";
    

#### How can I differentiate between events sent from a mobile device or from a website using a laptop?

The events tracked via JavaScript SDK contain `context.userAgent` that contain information on the user agent of the device.

  * [![](/docs/images/previous.svg)Previous](</docs/archive/javascript-sdk/1.1/service-worker/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/>)