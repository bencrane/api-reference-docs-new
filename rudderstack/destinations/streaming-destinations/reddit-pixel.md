# Reddit Pixel

Send your event data from RudderStack to Reddit Pixel.

* * *

  * __3 minute read

  * 


[Reddit Pixel](<https://ads.reddit.com/>) is a JavaScript snippet that you can add to your website to track user actions on your website after interacting with your ad on Reddit.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **Reddit Pixel** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Reddit Pixel native SDK from the `https://www.redditstatic.com/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Reddit Pixel SDK successfully.

## Get started

Once you have confirmed that the source platform supports sending events to Reddit Pixel, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Reddit Pixel**.
  2. Assign a name to your destination and click **Continue**.


## Connection settings

To successfully configure Reddit Pixel as a destination, configure the following settings:

  * **Pixel ID** : Enter your Reddit Pixel ID.
  * **Mapping to trigger the Reddit Pixel events for the respective events set here** : Use this setting to map custom event names to the standard Reddit Pixel events.
  * **Client-side Events Filtering** : This setting lets you specify which events should be blocked or allowed to flow through to Reddit Pixel. Refer to the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide for more information.
  * **Use device mode to send events** : As this is a web device mode-only destination, this setting is enabled by default and cannot be disabled.
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to update the user’s signup information.

A sample `identify` call is as shown:
    
    
    rudderanalytics.identify()
    

## Page

When you make a [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call, the `track` event is sent as `PageVisit` to `rdt('track,'PageVisit')`. RudderStack ignores any parameter sent to `rudderanalytics.page()`.

A sample `page` call is as shown:
    
    
    rudderanalytics.page()
    

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you capture user events along with the properties associated with them.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Product Added")
    

### Property mappings

The following table lists the event mapping from RudderStack to Reddit Pixel’s standard events:

RudderStack event| Reddit Pixel standard event  
---|---  
`Product Added`| `Add to Cart`  
`Product Added to Wishlist`| `Add to Wishlist`  
`Order Completed`| `Purchase`  
  
The following table lists the custom events mapping from RudderStack to Reddit Pixel’s standard events:

RudderStack event| Reddit Pixel standard event  
---|---  
`Lead`| `Lead`  
`View Content`| `ViewContent`  
`Search`| `Search`  
  
> ![warning](/docs/images/warning.svg)
> 
> Reddit Pixel does not support any other custom events apart from the ones mentioned above.

## FAQ

#### Where can I find the Pixel ID in Reddit Pixel?

  1. Log in to the [Reddit Ads Manager account](<https://accounts.reddit.com/adsregister>).
  2. Select **Events Manager** from the drop-down menu in the top-left corner.

[![](/docs/images/event-stream-destinations/reddit-pixel-id-1.webp)](</docs/images/event-stream-destinations/reddit-pixel-id-1.webp>)

  3. Select **Set Up Reddit Pixel** and choose from one of the below options according to your requirement:

[![](/docs/images/event-stream-destinations/reddit-pixel-id.webp)](</docs/images/event-stream-destinations/reddit-pixel-id.webp>)

Based on the selected option, you will find your Pixel ID on the next screen.

See [Reddit Pixel documentation](<https://business.reddithelp.com/helpcenter/s/article/Install-the-Reddit-Pixel-on-your-website>) for more information on setting up the Reddit Pixel.