# Setup Guide Beta

Set up and configure X Pixel as a destination in RudderStack.

* * *

  * __2 minute read

  * 


This guide will help you set up X Pixel as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to X Pixel.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Beta
  * **Supported sources:** Web
  * Refer to it as **XPixel** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> While using a Content Security Policy (CSP) header on your website, you need to [allowlist](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) the `ads-twitter.com`, `ads-api.twitter.com`, and `analytics.twitter.com` domains in the `img-src` and `connect-src` directives to to see results with X Pixel.

## Setup

In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **XPixel**.

### Connection settings

Setting| Description  
---|---  
Destination name| Assign a name to uniquely identify the destination.  
Pixel ID| Enter your Pixel ID of your X pixel event source.  
  
### Configuration settings

The [Client-side Event Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) setting lets you specify which events should be discarded or allowed to flow through to X Pixel.

Setting| Description  
---|---  
Choose if you want to turn on events filtering| Choose from either of the **No events filtering** , **Filter via allowlist** , and **Filter via denylist** options to specify if and how you want to filter the events.  
Allowlisted/Denylisted events| If you have selected either of the **Filter via allowlist** or **Filter via denylist** options in the previous setting, use this setting to specify the events you want to allow or discard while flowing to X Pixel.  
  
### Event mapping

Setting| Description  
---|---  
External Event mappings| Click **Set-up mapping** to map the RudderStack events to X Pixel events. RudderStack also provides the JSON mapper to set these mappings.  
  
## Next steps

  * [Send events in device mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/xpixel/device-mode/>)


## FAQ

#### How can I verify that X Pixel is correctly placed on my website?

You can leverage the [X Pixel Helper](<https://business.x.com/en/help/campaign-measurement-and-analytics/pixel-helper.html>) to verify the X Pixel placement. It shares the tracking status of the X Pixel and relevant events, and also includes the error codes depending on the issue.

Download the Google Chrome extension for X Pixel Helper [here](<https://chrome.google.com/webstore/detail/twitter-pixel-helper/jepminnlebllinfmkhfbkpckogoiefpd?hl=en-US>).