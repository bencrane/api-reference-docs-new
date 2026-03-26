# Google Optimize

Send your event data from RudderStack to Google Optimize.

* * *

  * __3 minute read

  * 


[Google Optimize](<https://marketingplatform.google.com/about/optimize/>) is Google’s free website optimization tool that lets you run different website tests to tailor personalized user experiences and increase your conversion rate.

RudderStack supports Google Optimize as a destination to which you can seamlessly send your website data for efficient A/B testing.

> ![success](/docs/images/tick.svg)
> 
> Once you add Google Optimize as a destination in RudderStack, RudderStack loads the [Optimize snippet](<https://support.google.com/optimize/answer/7513085>) on your website. Then, it loads the Google Analytics snippet(if not already present). This snippet natively measures all Optimize experiments and then sends the data to Optimize for creating the reports.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **Google Optimize** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Web| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Google Optimize native SDK from the `https://www.googleoptimize.com/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Google Optimize SDK successfully.

## Get started

Once you have confirmed that your source platform supports sending events to Google Optimize, follow these steps:

  * From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. From the list of destinations, select **Google Optimize**.
  * Assign a name to the destination and click **Next**. You should then see the following screen:

[![Google Optimize connection settings](/docs/images/event-stream-destinations/google-optimize-connection-settings-1.webp)](</docs/images/event-stream-destinations/google-optimize-connection-settings-1.webp>)

### Connection settings

The connection settings required to configure Google Optimize as a destination in RudderStack are listed below:

  * **Load Google Analytics** : Enable this setting **only if** Google Analytics is not installed on your website already.


> ![info](/docs/images/info.svg)
> 
> Disable this setting if you have already configured [Google Analytics 4](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-analytics-4/>) as a destination in RudderStack, or already installed the [global site tag](<https://support.google.com/optimize/answer/9183119#zippy=%2Cexample-global-site-tag-with-google-analytics>) on your website.

  * **Tracking ID** : If you have enabled the **Load Google Analytics** option, enter the corresponding tracking ID here.


> ![info](/docs/images/info.svg)
> 
> For more information on finding the Google Analytics tracking ID, refer to the FAQs section below.

  * **Container ID** : Enter your Google Optimize container ID here.


> ![info](/docs/images/info.svg)
> 
> You can find the Container ID by going to the **User Settings** option in your [Google Optimize dashboard](<https://optimize.google.com/optimize/home/#/accounts>).

[![Google Optimize container ID](/docs/images/event-stream-destinations/google-optimize-container-id.webp)](</docs/images/event-stream-destinations/google-optimize-container-id.webp>)

  * **Async mode** : Enable this setting to use the asynchronous version of Google Optimize.


> ![success](/docs/images/tick.svg)
> 
> We recommend enabling this setting if you want your pages to load faster and if your target visitors are likely to be on slow connections (3G or slower). However, for experimentation purposes, this setting should be **disabled**.

> ![info](/docs/images/info.svg)
> 
> Refer to this [Optimize support page](<https://support.google.com/optimize/answer/7513085?hl=en&ref_topic=6197443>) to learn more about the differences between the synchronous and asynchronous versions of Google Optimize.

  * **Anti-flicker snippet** : Enable this setting to install the anti-flicker snippet.


> ![warning](/docs/images/warning.svg)
> 
> Enabling this setting can impact page performance. Refer to this [support page](<https://support.google.com/optimize/answer/7100284>) for more information on the anti-flicker snippet.

  * As this destination supports sending events only via web device mode, the **Use device mode to send events** option will be always enabled.


Finally, click **Next** to complete the setup. Google Optimize will now be enabled as a destination in RudderStack.

## FAQ

#### Where do I get the Google Analytics tracking ID?

To get the Google Analytics tracking ID, follow these steps:

  1. Go to the **Admin** section of your [Google Analytics account](<https://analytics.google.com/analytics/web/#/>) in the bottom left corner.
  2. Then, select an account in the **Account** column, followed by a property in the **Property** column.
  3. Under **Property** , click **Tracking Info** \- **Tracking Code**. Your tracking ID will be displayed at the top of the resulting page.

[![Google Analytics tracking ID](/docs/images/event-stream-destinations/google-optimize-ga-tracking-id.webp)](</docs/images/event-stream-destinations/google-optimize-ga-tracking-id.webp>)

#### How do I link Google Optimize with Google Analytics?

To link your Google Optimize container to a Google Analytics property or view, refer to this [support page](<https://support.google.com/optimize/answer/7008374?hl=en&ref_topic=7310368>).