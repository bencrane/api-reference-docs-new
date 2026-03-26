# Setup Guide

Set up and configure Google Tag Manager as a destination in RudderStack.

* * *

  * __3 minute read

  * 


This guide will help you set up Google Tag Manager as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Google Tag Manager.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **Google Tag Manager** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Google Tag Manager native SDK from the `https://www.googletagmanager.com/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Google Tag Manager SDK successfully.

## Setup

In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Google Tag Manager**.

### Connection settings

Setting| Description  
---|---  
Container ID| Your Google Tag Manager container ID. You can get it by going to the **Admin** section of your [Google Tag Manager dashboard](<https://tagmanager.google.com/#/admin/>).  
Custom Domain URL| Specify your domain URL (for example, `https://your-domain.com`) used to load the Tag Manager scripts instead of Google’s domain (`https://www.googletagmanager.com/`).  
Environment ID| Specify the ID of the [environment](<https://support.google.com/tagmanager/answer/6311518?hl=en>) used for the Tag Manager container.  
Authorization Token| Specify the authorization token for the above environment.  
  
See FAQ for more information on obtaining the environment ID and token.  
Client-side Events Filtering| This setting lets you specify which events should be blocked or allowed to flow through to Google Tag Manager.  
  
For more information on this setting, see the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide.  
  
### Web SDK settings

Setting| Description  
---|---  
Use device mode to send events| This setting is turned on by default as this is a web device mode-only integration.  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
> ![info](/docs/images/info.svg)
> 
> You can load Google Tag Manager on any page where you initialize the RudderStack snippet and call the `page` event.

## Load RudderStack as a custom HTML tag

You can also load RudderStack as a custom tag in Google Tag Manager. However, loading Google Tag Manager through RudderStack is recommended, by following the steps described in the above section.

The following image demonstrates how you can add RudderStack as a custom HTML tag which can then be called through Google Tag Manager:

[![RudderStack as a custom tag](/docs/images/event-stream-destinations/rudderstack-custom-html-gtm.webp)](</docs/images/event-stream-destinations/rudderstack-custom-html-gtm.webp>)

## Next steps

  * [Send events in device mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-tag-manager/device-mode/>)


## FAQ

#### Where can I find the Google Tag Manager Container ID?

You can find your Tag Manager container ID in the admin section of your [Google Tag Manager dashboard](<https://tagmanager.google.com/#/admin/>). It is present in the format `GTM-XXXXXXX`.

[![](/docs/images/event-stream-destinations/rudderstack-container-id.webp)](</docs/images/event-stream-destinations/rudderstack-container-id.webp>)

#### How can I obtain the Environment ID and Authorization Token fields for the Google Tag Manager destination?

  1. Define your environment in the Google Tag Manager dashboard. Click the **Environments** option in the **Container** menu to get started. See [Define environments in Google Tag Manager](<https://support.google.com/tagmanager/answer/6311518?hl=en#defineEnvironments>) for the detailed steps.

[![Environments option in GTM dashboard](/docs/images/event-stream-destinations/gtm-env-id-token-1.webp)](</docs/images/event-stream-destinations/gtm-env-id-token-1.webp>)

  2. Go to **Custom Environments** and select the environment you created above.
  3. Click **Actions** > **Get Snippet**.

[![Get snippet option in GTM dashboard](/docs/images/event-stream-destinations/gtm-env-id-token-2.webp)](</docs/images/event-stream-destinations/gtm-env-id-token-2.webp>)

  4. Copy the `gtm_auth` and `gtm_preview` values in the snippet.

[![Auth token and Environment ID fields in GTM snippet](/docs/images/event-stream-destinations/gtm-env-id-token-3.webp)](</docs/images/event-stream-destinations/gtm-env-id-token-3.webp>)

  5. Specify the values for `gtm_auth` and `gtm_preview` in the **Authorization Token** and **Environment ID** destination settings in the RudderStack dashboard, respectively.


#### I am getting a 404 error when using Google Tag Manager. What should I do?

If you are getting a 404 error on the JavaScript console of your web page related to the Google Tag Manager, verify if you have published your Google Tag Manager Container. Follow [this guide](<https://support.google.com/tagmanager/answer/6107163?hl=en>) for more information.