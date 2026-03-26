# Google Analytics 4 Hybrid Mode

Send events to Google Analytics 4 using RudderStack hybrid mode.

* * *

  * __2 minute read

  * 


RudderStack’s [hybrid mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#hybrid-mode>) lets you send your event data to Google Analytics 4 via both the native SDK ([device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>)) and the Google Analytics 4 Measurement Protocol ([cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>)).

To use GA4 connection in hybrid mode, you can select **Hybrid mode** while [setting up the connection modes](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-analytics-4/setup-guide/#connection-mode>). This option is available only for the `gtag.js` web SDK.

> ![info](/docs/images/info.svg)
> 
> We recently updated our Google Analytics 4 hybrid mode destination to support new instrumentation options. See the [release note](<https://www.rudderstack.com/docs/releases/ga4-hybrid-mode-updates/>) for more information.

## Why use hybrid mode?

Unlike GA Universal, GA4’s server-side tracking (cloud mode) is less independent and may require support from client-side tracking (device mode). As noted in Google’s docs, Measurement Protocol is meant to [augment automatic collection](<https://developers.google.com/analytics/devguides/collection/protocol/ga4>) via gtag, Tag Manager, and Google Analytics, not replace them.

Through a single hybrid mode deployment, you would have access to a fuller, more unified and accurate set of attribution data with the least impact on performance (resulting from a combination of client-side and server-side tracking).

Specifically, a hybrid instrumentation may make sense for those who prefer to maintain the benefits of cloud mode—including a faster site, more reliable data collection, and first-party data capture, while also capturing data required for attribution, sessionization, geolocation, and conversions for Google Ads Remarketing.

## How does hybrid mode work?

RudderStack sends `page` calls via device mode and all other calls via cloud mode. The purpose of sending `page` calls via device mode is to capture attribution information (such as UTM parameters) that is only available in device mode.

Further, RudderStack stitches the `page` call information with the rest of the cloud mode events using Google’s `clientID` and `sessionID`.

[![GA4 hybrid mode](/docs/images/event-stream-destinations/ga4-hybrid-mode.webp)](</docs/images/event-stream-destinations/ga4-hybrid-mode.webp>)