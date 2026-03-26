# Google Analytics 360

Send your event data from RudderStack to Google Analytics 360.

* * *

  * __3 minute read

  * 


[Google Analytics 360](<https://marketingplatform.google.com/about/analytics-360/>) is the enterprise version of Google Analytics that allows you to get actionable insights from your data. It provides enterprise teams with all standard [Google Analytics features](<https://www.rudderstack.com/learn/GA4/what-are-the-new-features-of-google-analytics-4-ga4/>) along with more sophisticated analytics capabilities and the ability to export your data and insights to BigQuery. You also get SLA obligations, guaranteed uptime, extended support, and more.

RudderStack supports sending real-time customer events to Google Analytics 360.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/ga360>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Google Analytics 360** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Google Analytics 360 native SDK from the `https://www.google-analytics.com/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Google Analytics 360 SDK successfully.

Then, perform the steps below:

  * Choose a source for which you would like to add Google Analytics 360 as a destination.
  * From the list of destinations, select **Google Analytics 360**. Then, assign a name to the destination and click **Next**.
  * You should then see the following **Connection Settings** page:

[![](/docs/images/1%20%2820%29.webp)](</docs/images/1%20%2820%29.webp>)[![](/docs/images/2%20%2826%29.webp)](</docs/images/2%20%2826%29.webp>)[![](/docs/images/3%20%2823%29.webp)](</docs/images/3%20%2823%29.webp>)

  * **Tracking ID** is a required field to configure the destination. You can configure the other options as per your preference.
  * To add a transformation, click **Create New Transformation**. Otherwise, click **Next**.


> ![info](/docs/images/info.svg)
> 
> Refer to the [Transformations](<https://www.rudderstack.com/docs/transformations/overview/>) guide for more details on this feature.

  * The destination is now configured and enabled.

[![](/docs/images/final.webp)](</docs/images/final.webp>)

You can now start sending your real-time events and view them in Google Analytics 360 by going to your Google Analytics 360 dashboard and navigating to **Realtime** \- **Events**.

> ![info](/docs/images/info.svg)
> 
> For details on the supported events and other additional features refer to the [Google Analytics documentation](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-analytics-ga/>).

## FAQ

#### Can I anonymize an IP Address in Google Analytics 360?

Yes, you can. Turn on the **Anonymize IP Addresses** setting under the **Other Settings** option in the RudderStack dashboard while configuring Google Analytics 360.

This setting lets Google Analytics anonymize the address at the earliest possible stage of the data collection.

> ![info](/docs/images/info.svg)
> 
> For more information and other FAQs, refer to the [Google Analytics documentation](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-analytics-ga/>).