# Google Analytics 4 Setup Guide

Set up Google Analytics 4 as a destination in RudderStack.

* * *

  * __9 minute read

  * 


Follow the below steps to set up Google Analytics 4 as a destination in RudderStack:

  1. From the list of destinations in [RudderStack dashboard](<https://app.rudderstack.com/>), select **Google Analytics 4**.
  2. Select an existing source from the displayed ones or set up a new source to connect to **Google Analytics 4** and click **Continue**.


## Connection settings

To successfully configure Google Analytics 4 as a destination, configure the following settings:

  * **Name** : Assign a name to your destination.

  * **API Secret** : Enter the API Secret generated through the Google Analytics dashboard. It can be created in the Google Analytics dashboard under **Admin** > **Data Streams** > **Choose your stream** > **Measurement Protocol** > **Create**.

  * **Client Type** : Select the client type as `gtag` or `Firebase` from the dropdown:

    * **`gtag`** \- Supported for both cloud and device mode. If you select `gtag`, enter the following:
      * **Measurement ID** : Enter the Measurement ID which is the identifier for a data stream. It can be found in the Google Analytics dashboard under **Admin** > **Data Streams** > **Choose your stream** > **Measurement ID**.
    * **`Firebase`** \- Supported only for cloud mode. If you select `Firebase`, enter the following:
      * **Firebase App Id** : Enter the Firebase App ID which is the identifier for Firebase app. It can be found in the Firebase dashboard under **Project Settings** > **General**.


Refer to the FAQ section for more information on how to obtain the API secret, Measurement ID, and Firebase App ID.

  * **SDK Base URL** : Enter the custom domain you want to use as the native SDK’s base URL. RudderStack loads the `gtag.js` in the `{SDK_Base_URL}/gtag/js?id=${measurementId}` format. The default value for the SDK base URL is `https://www.googletagmanager.com/`.


## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **Google Analytics 4 (GA4)** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
AMP| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Java)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cloud| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cordova| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Swift)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
React Native| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Shopify| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Unity| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Warehouse| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Android (Java)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Google Analytics 4 native SDK from `https://www.googletagmanager.com/` domain. To load the native SDK from a custom domain, use the **SDK Base URL** setting in the RudderStack dashboard. Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Google Analytics 4 SDK successfully.

### Connection mode comparison: hybrid vs. cloud vs. device

The following table lays out a detailed comparison to help you choose a connection mode:

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * RudderStack makes the primary decision on how to track and stitch events together based on the `client_id` and `session_id` parameters.
>   * Server-side session tracking supports only a subset of user dimensions. Google’s Measurement Protocol API does not support the reserved fields like location, demographics, [predefined user dimensions](<https://support.google.com/analytics/answer/9268042?hl=en&ref_topic=11151952>), and device-specific information.
> 


| Device mode| Cloud mode| Hybrid mode with [client ID override](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-analytics-4/setup-guide/#hybrid-mode>) (RECOMMENDED)| Hybrid mode without client ID override (Requires SDK configuration)  
---|---|---|---|---  
**Description**|  RudderStack’s SDK loads the native client libraries.| Sends data server-side to [Google’s Measurement Protocol API](<https://developers.google.com/analytics/devguides/collection/protocol/ga4>).| Automatically configures a single connection that captures attribution data from `page` calls (sent via device mode) and all other calls via cloud mode.| Automatically configures a single connection that captures attribution data from `page` calls (sent via device mode) and all other calls via cloud mode.  
**Client ID**|  Fetches the `client_id` automatically generated by `gtag`.| You can send a custom `client_id` via `externalID`. Otherwise, RudderStack sends an `anonymousId` or `rudderId`. See [Mapping `client_id`](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-analytics-4/cloud-mode/#mapping-client_id>) for more information.| Overrides the `client_id` with RudderStack’s `anonymousID`. (RudderStack utilizes a cookie that adds an `rs_` prefix to the existing Measurement ID)| Fetches the `client_id` automatically generated by `gtag`.  
**Session ID**|  Fetches the `session_id` automatically generated by `gtag`.| Passes `session_id` automatically but you can customize it using [these mappings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-analytics-4/cloud-mode/#tracking-active-users-and-sessions>).| Overrides `session_id` with the RudderStack’s `session_id`.| Fetches the `session_id` automatically generated by `gtag`.  
**Considerations**|  Offers full information capture but it’s worth noting potential impacts the performance, page speed, data resilience, and first-party data capture.| Google’s Measurement Protocol doesn’t support passing certain reserved fields, including attribution data.| Introducing a custom `client_id` may cause fragmentation in multi-domain implementations. You may observe a potential momentary spike in session count while switching from device mode initially.| Buffer the SDK with a slight delay to avoid a potential race condition whereby the SDK events reach GA4 prior to the events sent via server-side.  
**Required actions**|  NA| To capture full attribution data, you must pass it as custom dimensions or instrument a parallel client-side integration.| Ensure that the [override setting](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-analytics-4/setup-guide/#hybrid-mode>) is enabled in the RudderStack dashboard. To ensure accurate cross-platform analytics, check that other cookies (such as Google Ads) also include the appropriate `rs_` prefix.| Instrument your SDK to buffer.  
  
**For example:**  
`rudderanalytics.load(`  
`"write_key",`  
`"dataplane_url",`  
`{`  
`bufferDataPlaneEventsUntilReady: true`  
`}`  
`);`  
  
## Configuration settings

In the **Configuration** tab of your destination, you can configure the below-mentioned cloud and device mode settings:

### Cloud mode

  * **Debug via Validation Server** : Enable this setting to check the validation responses in the [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/>) tab. Debug mode is supported via GA4’s validation server endpoint.


> ![warning](/docs/images/warning.svg)
> 
> As per the [GA4 documentation](<https://developers.google.com/analytics/devguides/collection/protocol/ga4/validating-events?client_type=gtag>), any responses sent to the validation server will not show up in the reports.

  * **Filter user traits** : Enter the list of user traits which you do not want RudderStack to send to GA4. You can use this field to filter sensitive PII fields like email, phone number, credit card number, etc. from your events and prevent them from being sent to GA4.


> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * This setting is applicable to all the [RudderStack connection modes](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/>).
>   * To specify multiple traits, press the enter key after each trait.
> 


### Device mode

  * **Filter user traits** : Enter the list of user traits which you do not want RudderStack to send to GA4. You can use this field to filter sensitive PII fields like email, phone number, credit card number, etc. from your events and prevent them from being sent to GA4. To specify multiple traits, press the enter key after each trait.
  * **Choose how to capture pageviews** : Select **RudderStack JS SDK** or **gtag Automated Capture** from the dropdown depending on whether you want to send the page view events through the RudderStack JS SDK, or through automatic collection on each page load using GA4 Enhanced Measurement (gtag) respectively. See the [GA4 documentation](<https://developers.google.com/analytics/devguides/collection/ga4/views?client_type=gtag>) for more information.
  * **Debug via DebugView** : This setting lets you monitor the device mode events in [DebugView](<https://support.google.com/analytics/answer/7201382>). It displays the events and user properties that GA4 collects in realtime. With this feature, you can troubleshoot issues as you install your tags or go through a user’s live activity.
  * **Include URL and Search as Page View properties** : Enable this setting to send the following properties along with any other custom property to the `page` call of the RudderStack SDK:
    * `url`
    * `search`


> ![info](/docs/images/info.svg)
> 
> Google Analytics 4 has a limit on the number of unique properties per event name. The default `page_view` event supports the properties mentioned in the [Automatically collected events in Google Analytics 4](<https://support.google.com/analytics/answer/9234069?hl=en&ref_topic=6317484>) guide.

### Hybrid mode

  * **Debug via Validation Server** : If you enable this setting, then RudderStack sends the cloud mode events (`track` and `group` calls) to the GA4 validation server. These events will **not show up** in your reports.
  * **Filter user traits** : Enter the list of user traits which you do not want RudderStack to send to GA4. You can use this field to filter sensitive PII fields like email, phone number, credit card number, etc. from your events and prevent them from being sent to GA4. To specify multiple traits, press the enter key after each trait.
  * **Choose how to capture pageviews** : Select **RudderStack JS SDK** or **gtag Automated Capture** from the dropdown depending on whether you want to send the page view events through the RudderStack JS SDK, or through automatic collection on each page load using GA4 Enhanced Measurement (gtag) respectively. See the [GA4 documentation](<https://developers.google.com/analytics/devguides/collection/ga4/views?client_type=gtag>) for more information.


> ![warning](/docs/images/warning.svg)
> 
> Make sure that your Google Analytics Measurement configuration matches this pageview capture setting.

  * **Debug via DebugView** : If this setting is enabled, then the device mode events (`page` calls) will be visible under the [GA4 DebugView](<https://support.google.com/analytics/answer/7201382>) section.
  * **Include URL and Search as Page View properties** : Enable this setting to send the following properties along with any other custom property to the `page` call of the RudderStack SDK:
    * `url`
    * `search`
  * **Override gtag client ID & session ID**: Enable this setting to override the gtag `client_id` and `session_id` with RudderStack’s `anonymousId` and `session_id` to ensure that the attribution is properly unified across the `page` and `track` events.


> ![warning](/docs/images/warning.svg)
> 
> If you are transitioning to the GA4 hybrid mode from device mode, enabling this setting could lead to a momentary spike in session counts. To avoid this scenario, disable this setting and [buffer the SDK](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-analytics-4/setup-guide/#connection-mode-comparison:~:text=device%20mode%20initially.-,Buffer%20the%20SDK,-with%20a%20slight>) instead.
> 
> For all other scenarios, you can enable this setting.

### Other settings

  * **Choose if you want to turn on events filtering** : This option is applicable only if you’re sending events to Google Analytics 4 via **web device mode**. See [Client-side Event Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) for more information. | Consent management settings | Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature. |


## FAQ

#### How do I obtain the Measurement Id?

  1. Log in to the [Google Analytics](<https://analytics.google.com/analytics/web/>) dashboard.
  2. Go to the **Admin** section in the left sidebar.
  3. Select the relevant account and property.
  4. Click **Data Streams** and select the stream to get the Measurement Id:

[![](/docs/images/event-stream-destinations/measurement-id.webp)](</docs/images/event-stream-destinations/measurement-id.webp>)

#### How do I obtain the API Secret?

  1. Login to [Google Analytics](<https://analytics.google.com/analytics/web/>) dashboard.
  2. Go to the **Admin** section in the left sidebar.
  3. Select the relevant account and property.
  4. Click **Data Streams** and select the stream.
  5. Click **Measurement Protocol API secrets** to get the API Secret:

[![](/docs/images/event-stream-destinations/api-secret.webp)](</docs/images/event-stream-destinations/api-secret.webp>)

#### How do I obtain the Firebase App ID?

  1. Login to [Google Analytics](<https://analytics.google.com/analytics/web/>) dashboard.
  2. Go to the **Admin** section in the left sidebar.
  3. Select the relevant account and property.
  4. Click **Data Streams** and select the stream to get the **Firebase App Id** :

[![](/docs/images/event-stream-destinations/firebase-app-id.webp)](</docs/images/event-stream-destinations/firebase-app-id.webp>)

#### How can I prevent RudderStack from sending PII fields to Google Analytics 4?

To prevent RudderStack from sending sensitive PII data in your events to GA4, specify the user traits in **Filter user traits** while configuring your destination settings.

> ![info](/docs/images/info.svg)
> 
> To specify multiple traits, press the enter key after each trait.

[![](/docs/images/event-stream-destinations/ga4-pii.webp)](</docs/images/event-stream-destinations/ga4-pii.webp>)