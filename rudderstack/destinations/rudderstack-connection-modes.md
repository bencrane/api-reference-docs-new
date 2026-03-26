# Connection Modes: Cloud, Device, and Hybrid

Learn the difference between cloud mode, device mode, and hybrid mode when sending event data to your destinations.

* * *

  * __5 minute read

  * 


This guide explains the differences between the two main RudderStack connection modes - **cloud mode** and **device mode**. It also give an overview on **hybrid mode** , the new connection mode that lets you send events to destinations by leveraging both the cloud and device modes.

## What are connection modes in RudderStack?

RudderStack’s workflow is simple - it receives the event data from the **sources** and routes this data to the **destinations**. The connection modes determine how RudderStack tracks, transforms, and routes this event data.

There are primarily two connection modes through which you can send your event data from your source apps to the desired destinations via RudderStack:

  * Cloud mode
  * Device mode


For some selective destinations, RudderStack also supports a hybrid mode connection which routes the event through both the cloud and device modes.

## Cloud mode

In this mode, the SDK sends the event data directly to the RudderStack server. RudderStack then transforms this data and routes it to the desired destination. This transformation is done in the RudderStack backend, using RudderStack’s [Transformer](<https://github.com/rudderlabs/rudder-transformer>) module.

> ![success](/docs/images/tick.svg)
> 
> When you send events via cloud mode, you also get the flexibility to use [RudderStack Transformations](<https://www.rudderstack.com/docs/transformations/overview/>) to implement custom logic on the events before forwarding them to the destinations.

### How cloud mode works

  1. The SDK sends the event data directly to the RudderStack server (backend).
  2. RudderStack transforms the events into a destination-specific format.
  3. The transformed events are then routed to the destination.


Suppose you want to analyze your website data in Google Analytics. To do so, you can use RudderStack’s [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>).

RudderStack defines a [fixed event structure](<https://www.rudderstack.com/docs/event-spec/standard-events/>). If you track your events in this format, RudderStack takes care of transforming the events as required by Google Analytics. You can start by [adding a JavaScript source](<https://www.rudderstack.com/docs/dashboard-guides/sources/#adding-a-source>) and connecting it to the [Google Analytics destination](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-analytics-ga/>) in your RudderStack dashboard.

Then, enable event tracking on your website by [adding the JavaScript SDK snippet](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/quickstart/#step-1-install-rudderstack-javascript-sdk>).

The SDK will automatically track and send the events to RudderStack. RudderStack then transforms this data into the required format and sends it to Google Analytics.

[![RudderStack Cloud Mode](/docs/images/rs-cloud/rudderstack-cloud-mode.webp)](</docs/images/rs-cloud/rudderstack-cloud-mode.webp>)

> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * RudderStack’s [warehouse destinations](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>) support sending data only through cloud mode.
>   * All the RudderStack server-side SDKs support sending events only through cloud mode. This is because the server-side SDKs operate in the RudderStack backend and cannot load any additional destination-specific SDKs.
> 


## Device mode

In device mode, RudderStack sends the event data to the destinations directly from your client (web or mobile app).

> ![warning](/docs/images/warning.svg)
> 
> RudderStack does not support the [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/>) functionality in device mode.

The RudderStack SDKs first load the native client libraries on your website or mobile app. These libraries allow RudderStack to use the data you collect on your device to call the destination APIs - without sending it to the RudderStack servers first.

### How device mode works

Suppose you want to send your event data from your mobile app to Firebase via the RudderStack Android (Java) SDKAndroid (Java) refers to the legacy RudderStack Android SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the Android (Kotlin) SDK instead. (or any other mobile SDK). You can start by [adding an Android (Java) source](<https://www.rudderstack.com/docs/dashboard-guides/sources/#adding-a-source>) and connecting it to the [Firebase destination](<https://www.rudderstack.com/docs/destinations/streaming-destinations/firebase/>) in the RudderStack dashboard.

The RudderStack SDK will first download the Firebase SDK, transform the events natively, and then send them over to Firebase.

[![RudderStack device mode](/docs/images/rs-cloud/rudderstack-device-mode.webp)](</docs/images/rs-cloud/rudderstack-device-mode.webp>)

For some destinations, you can use the [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) to send the events via device mode. To do so, enable the **Use native SDK to send events** option under the destination-specific connection settings in the RudderStack dashboard:

[![RudderStack web SDK settings](/docs/images/rs-cloud/web-device-mode-settings.webp)](</docs/images/rs-cloud/web-device-mode-settings.webp>)

## Hybrid mode

In hybrid mode, RudderStack sends certain event data to the destination directly from your client while routing the remaining events through the RudderStack server.

> ![info](/docs/images/info.svg)
> 
> Hybrid mode is currently available for the following destinations:
> 
>   * [GA4](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-analytics-4/>)
>   * [Braze](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/>)
>   * [Leanplum](<https://www.rudderstack.com/docs/destinations/streaming-destinations/leanplum/>)
>   * [Rockerbox](<https://www.rudderstack.com/docs/destinations/streaming-destinations/rockerbox/>)
> 


Hybrid mode features include:

  * A singular connection capturing critical event data automatically generated by the native SDKs.
  * All the benefits of cloud mode like:
    * Faster site
    * Reliable data collection
    * First-party data capture


## FAQ

#### Which connection mode should I choose?

  * Use cloud mode if you wish to run a faster site with reliable data collection and first-party data capture.
  * If you are planning to work with the destinations that record information directly on your users’ devices, choose device mode. There is a possibility that these destinations might not function correctly if they are not loaded directly on the device.


#### How to check which connection mode is supported by the destination?

The easiest way to check the connection mode supported by the destination is to go refer to the individual destination’s [documentation](<https://www.rudderstack.com/docs/destinations/overview/>).

The supported connection modes are mentioned for every destination in the **Getting Started** section of their respective documentation, as seen below:

[![Getting Started section in destination docs](/docs/images/rs-cloud/getting-started-connection-modes.webp)](</docs/images/rs-cloud/getting-started-connection-modes.webp>)

Some RudderStack destinations support sending events via both the cloud and device mode, for example:

  * [Google Analytics](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-analytics-ga/>)
  * [HubSpot](<https://www.rudderstack.com/docs/destinations/streaming-destinations/hubspot/>)
  * [Intercom](<https://www.rudderstack.com/docs/destinations/streaming-destinations/intercom/>)
  * [Kissmetrics](<https://www.rudderstack.com/docs/destinations/streaming-destinations/kissmetrics/>)
  * [Branch.io](<https://www.rudderstack.com/docs/destinations/streaming-destinations/branchio/>)
  * [Braze](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/>)
  * [Customer.io](<https://www.rudderstack.com/docs/destinations/streaming-destinations/customer-io/>)
  * [Facebook App Events](<https://www.rudderstack.com/docs/destinations/streaming-destinations/facebook-app-events/>)


#### What are the benefits of using cloud mode to send events to the destination?

In cloud mode, the event data is sent from the sources directly to the RudderStack server. RudderStack takes care of the event transformation and ensuring the format matches the destination’s requirements. Since this transformation happens in the RudderStack server itself, your page size as well as the load times are not affected at all.

#### Can I use an event forwarding or data plane proxy in the device mode?

Yes, you can use an event forwarding/data plane proxy while sending events to your destinations via device mode. The default vendor API endpoint will still work as expected.