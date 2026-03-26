# Setup Guide

Set up DCM Floodlight as a destination in RudderStack.

* * *

  * __5 minute read

  * 


This guide will help you set up DCM Floodlight as a destination in RudderStack.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **DCM Floodlight** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the DCM Floodlight native SDK from the `https://www.googletagmanager.com/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the DCM Floodlight SDK successfully.

## Get started

Once you have confirmed that the source platform supports sending events to DCM Floodlight, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **DCM Floodlight**.
  2. Assign a name to the destination and click **Next**.


## Connection settings

To successfully configure DCM Floodlight as a destination, you will need to configure the following settings:

[![DCM Floodlight connection settings](/docs/images/event-stream-destinations/dcm-floodlight-connection-settings.webp)](</docs/images/event-stream-destinations/dcm-floodlight-connection-settings.webp>)

  * **DoubleClick Advertiser ID:** Enter your Advertiser ID visible in the **Campaigns** or **Activities** tab in your dashboard.


> ![info](/docs/images/info.svg)
> 
> Refer to the FAQ section for more information on obtaining the Advertiser ID.

  * **Activity Tag:** Enter the Floodlight Activity Tag (`cat`) to define the same parameter value across all conversion events. Alternatively, you can define this value for each conversion event mapping in the **Floodlight Activity Tag** field below.
  * **Group Tag:** Enter the Floodlight Group Tag (`type`) to define the same parameter value across all group conversion events. Alternatively, you can define this value for each conversion event in the **Floodlight Group Tag** field below.


> ![info](/docs/images/info.svg)
> 
> For more information on finding `cat` and `type` in your Campaign Manager dashboard, refer to the FAQ section below.

### Conversion events

[![DCM Floodlight connection settings](/docs/images/event-stream-destinations/dcm-floodlight-connection-settings-2.webp)](</docs/images/event-stream-destinations/dcm-floodlight-connection-settings-2.webp>)

  * **RudderStack Event Name:** Enter your RudderStack event name which will be mapped to the Floodlight tag.
  * **Floodlight Activity Tag:** Enter the `cat` of your tag string. If left blank, RudderStack will pick the value from the **Activity Tag** field mentioned above.
  * **Floodlight Group Tag:** Enter the `type` of your tag string. If left blank, RudderStack will pick the value from the **Group Tag** field mentioned above.
  * **Floodlight Counting Method** : Specify the counting method for the conversion event. RudderStack uses this as a fallback value if `properties.countingMethod` is not present in the event.
  * **Fire as Sales Tag:** Enable the toggle button for Sales tag. Keep it disabled if it is a Counter tag.


> ![info](/docs/images/info.svg)
> 
>   * **Counter tag** : Used to count the number of conversions. It is supposed to be placed on the confirmation page after a sale with information about the `ord` property passed to the tag.
>   * **Sales tag** : Used to count the number of conversions, the total number of sales that take place, and the total associated revenue. It is supposed to be placed on the confirmation page after a sale with information about the sales, like `cost`, `qty`, or `ord` properties passed to the tag.
> 


  * **Custom Floodlight variables:** Enter the custom Floodlight variables to capture additional reporting data beyond the usual metrics (like visits and revenue).


> ![info](/docs/images/info.svg)
> 
> For more information on finding the custom Floodlight variables, refer to the FAQ section below.

### Client-side events filtering

[![DCM Floodlight connection settings](/docs/images/event-stream-destinations/dcm-floodlight-connection-settings3.webp)](</docs/images/event-stream-destinations/dcm-floodlight-connection-settings3.webp>)

> ![info](/docs/images/info.svg)
> 
> This option is applicable only if you’re sending events to DCM Floodloght via web device mode. Refer to the [Client-side Event Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide for more information on this feature.

### Web device mode settings

> ![info](/docs/images/info.svg)
> 
> All the settings mentioned in this section are applicable only for the [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).

[![DCM Floodlight connection settings](/docs/images/event-stream-destinations/dcm-floodlight-connection-settings4-new.webp)](</docs/images/event-stream-destinations/dcm-floodlight-connection-settings4-new.webp>)

  * **Use device mode to send events** : Enable this setting to send events via the [RudderStack device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).


> ![info](/docs/images/info.svg)
> 
> You can change the setting to enable or disable device mode to send events at any point. However, it takes some time for the new changes to be reflected.

  * **Tag Format** : Select the tag format from the dropdown. RudderStack supports both the **Global site tag** and the **Iframe** tag. Note that your conversion events configured in the RudderStack dashboard must be of the same tag format.


> ![info](/docs/images/info.svg)
> 
> It is highly recommended to use the global site tag instead of the iframe tag. For more information, refer to the [Campaign Manager 360 Help Center](<https://support.google.com/campaignmanager/answer/7564930#zippy=%2Ci-use-iframe-or-image-tags-directly-on-my-site-for-desktop-and-mobile-web>).

  * **Conversion Linker** : Enabled by default, it sets the first-party cookies on your site’s domain.
  * **Allow ad personalization signals** : Enabled by default, it lets the global site tag to collect remarketing data.


> ![warning](/docs/images/warning.svg)
> 
> The **Conversion Linker** and **Allow ad personalization signals** settings are only applicable for the global site tag.

  * **DoubleClick Id** : Enable this setting if you want to use the Google’s cookie matching functionality. Also, provide the below:
  * **Google Network Id** : Enter the Google Network ID (NID) for the bidder account.


Finally, click **Next** to enable DCM Floodlight as a destination in RudderStack.

## FAQ

#### Where can I find the activity tag string (cat) and group tag string (type)?

In your Campaign Manager dashboard, go to **Floodlight** > **Activities**. Here you can see all activity names along with their **Activity tag string** (`cat`) and Group tag string (`type`):

[![DCM Floodlight cat and type strings](/docs/images/event-stream-destinations/dcm-floodlight-cat-vs-type.webp)](</docs/images/event-stream-destinations/dcm-floodlight-cat-vs-type.webp>)

#### Where can I find the Advertiser ID?

To get the Advertiser ID, go to your [Campaign Manager 360](<https://campaignmanager.google.com/>) account and navigate to the **Campaigns** or **Activities** tab in your dashboard to obtain the `Advertiser ID`:

[![DCM Floodlight advertiser ID](/docs/images/event-stream-destinations/dcm-floodlight-advertiser-id.webp)](</docs/images/event-stream-destinations/dcm-floodlight-advertiser-id.webp>)

#### Where can I find the custom Floodlight variables?

To create custom Floodlight variables, refer to this [Campaign Manager guide](<https://support.google.com/campaignmanager/answer/2823222?hl=en>).

You can find the custom Floodlight variables for your activities by going to **Floodlight** > **Activities**. Then, click any activity to view the custom variables associated with it:

[![DCM Floodlight custom variables](/docs/images/event-stream-destinations/dcm-floodlight-custom-variables.webp)](</docs/images/event-stream-destinations/dcm-floodlight-custom-variables.webp>)

#### How can I get the reports of the events in DCM Floodlight?

In your Campaign Manager dashboard, you get two reporting options under **Report Builder** \- **Instant Reporting** and **Offline Reporting** :

[![DCM Floodlight report builder](/docs/images/event-stream-destinations/dcm-floodlight-report-builder.webp)](</docs/images/event-stream-destinations/dcm-floodlight-report-builder.webp>)

To generate an offline report of the events, follow these steps:

  1. Go to **New** > **Floodlight**.
  2. Select the **Floodlight Configuration** and other fields like **Activities** , **Dimensions** , and **Metrics** as per your requirement.

[![DCM Floodlight report settings](/docs/images/event-stream-destinations/dcm-floodlight-report-settings.webp)](</docs/images/event-stream-destinations/dcm-floodlight-report-settings.webp>)

> ![info](/docs/images/info.svg)
> 
> It may take up to 24 hours for your events to reflect in the reports.

#### What are unattributed cookie conversions?

A conversion is said to be unattributed if the user has a DoubleClick cookie but it is converted without any exposure. This means that the user did not click or view any ad from the advertiser within Floodlight, or the interaction happened outside the lookback window.