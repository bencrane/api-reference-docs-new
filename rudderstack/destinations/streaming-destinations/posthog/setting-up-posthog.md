# Setup Guide

Set up PostHog as a destination in RudderStack.

* * *

  * __4 minute read

  * 


This guide will help you set up PostHog as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to PostHog.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **PostHog** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
AMP| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Java)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cloud| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cordova| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Swift)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
React Native| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Shopify| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Unity| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Warehouse| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the PostHog native SDK either from the `https://app.posthog.com` domain or your instance URL.
> 
> Based on your website’s content security policy, you might need to [allowlist the required domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the PostHog SDK successfully.

## Get started

Once you have confirmed that the source platform supports sending events to PostHog, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **PostHog**.
  2. Assign a name to your destination and click **Continue**.


## Connection settings

To successfully configure PostHog as a destination, you will need to configure the following settings:

[![PostHog connection settings](/docs/images/event-stream-destinations/posthog-connection-settings.webp)](</docs/images/event-stream-destinations/posthog-connection-settings.webp>)

  * **Team API Key** : Enter your PostHog team API key. This is a mandatory field. For more information on obtaining your PostHog Team API Key, refer to the FAQ section below.
  * **Instance URL** : Enter your PostHog instance URL.


> ![info](/docs/images/info.svg)
> 
> If you are hosting your own PostHog instance, add the URL of your instance without the trailing slash. So, the URL will look something like `https://[your-instance].com`.

  * **Client-side Events Filtering** : This setting lets you specify which events should be blocked or allowed to flow through to PostHog. For more information on this setting, refer to the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide.
  * **Use updated mapping for Group calls** : Enable this setting to send the `group` traits as event properties to PostHog. It is strongly recommended to enable this setting to send all your `group` events to PostHog correctly.


> ![warning](/docs/images/warning.svg)
> 
> **This setting is applicable only when sending events via cloud mode**. RudderStack uses the updated group mappings in device mode by default. For more information on this setting, refer to the [Updated group mapping](<https://www.rudderstack.com/docs/destinations/streaming-destinations/posthog/posthog-cloud-mode/#updated-group-mapping>) section.

### Web device mode settings

This section lists some of the other configurable settings when sending events to PostHog via [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).

  * **Use device mode to send events** : If enabled, RudderStack will send the events to PostHog via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).

  * **Enable Local Storage for Persistence** : Enable this option to reduce the amount of data stored in the cookies by storing it locally instead.

  * **PostHog Person Profile option** : Choose the required option from the dropdown to create a [person profile](<https://posthog.com/docs/data/persons>) in PostHog:

    * **Always** : Captures the [identified events](<https://posthog.com/docs/libraries/js#anonymous-vs-identfied-events>) for all users.
    * **Identified Only** : Captures the [anonymous events](<https://posthog.com/docs/libraries/js#anonymous-vs-identfied-events>) by default. Identified events are captured only for users having a person profile.

See the [PostHog documentation](<https://posthog.com/docs/libraries/js#how-to-capture-anonymous-events>) for more information on these settings.

  * **Enable autocapture with PostHog** : Enable this option to allow PostHog to send [auto-captured](<https://posthog.com/docs/integrations/js-integration#usage>) events.

  * **Allow PostHog to automatically capture pageview events** : Enable this setting to allow the PostHog web SDK to send a page view event every time it is loaded on a page.

  * **Disable session recording** : Enable this setting to stop PostHog from recording the user sessions. For more information on PostHog’s session recording feature, refer to the [PostHog documentation](<https://posthog.com/manual/recordings/>).

  * **Additional headers to pass with XHR requests to PostHog API** : Add a list of key-value pairs in this field. The RudderStack web SDK will then forward these headers on the event requests sent to PostHog.

  * **Property denylist** \- Add a list of traits or event properties that you want the PostHog SDK to filter.


## FAQ

#### Where can I find the PostHog Team API Key?

To get your PostHog Project API Key or Team API Key, follow the steps below:

  1. Login to your PostHog dashboard.
  2. Go to the **Settings** tab under the **Project** section in the left sidebar.
  3. You can find the Team API key under **Project API Key** or **Team API Key**.