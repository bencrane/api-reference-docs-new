# Braze Destination Setup Guide

Set up and configure Braze as a destination in RudderStack.

* * *

  * __5 minute read

  * 


This guide will help you set up Braze as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Braze.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Braze** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
AMP| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Java)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)  
Cloud| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cordova| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)  
iOS (Swift)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)  
React Native| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
Shopify| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Unity| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Warehouse| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Android (Java)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Swift)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
React Native| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Important considerations

Review the following considerations before using the Braze integration with RudderStack.

### Device mode support for Flutter and React Native

Device mode support for Flutter and React Native sources (as seen in the above table) applies to mobile (Android and iOS) platforms only. If you are deploying a Flutter app to the web, you can send events to Braze via the Flutter SDK in cloud mode only.

As a workaround, you can create a separate [JavaScript source](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) in RudderStack and use its [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) for the web build of your Flutter apps to send events to these destinations in web device mode.

### Domain allowlisting for web device mode

In the web device mode integration, that is, when using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Braze native SDK from the `https://js.appboycdn.com/` domain.

Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Braze SDK successfully.

## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), set up a source.
  2. Go to the **Overview** tab of your source and select **Add Destination** > **Create new destination**.

[![Add new destination in RudderStack dashboard](/docs/images/event-stream-destinations/add-new-destination.webp)](</docs/images/event-stream-destinations/add-new-destination.webp>)

  3. Select **Braze** from the list of destinations. Then, click **Continue**.


## Connection settings

Setting| Description  
---|---  
Destination name| Assign a name to uniquely identify the destination.  
Enable Platform-specific App Identifier Keys  
Beta| 

> ![announcement](/docs/images/announcement.svg)This feature is currently in **Beta** and behind a feature flag. It is expected to be generally available by March 31, 2026.  
>   
> Contact [RudderStack Support](<mailto:support@rudderstack.com>) to enable this feature for your account.

Toggle on this setting to configure platform-specific App Identifier keys (Android, iOS, and web) for proper data attribution in Braze.  
  
**Note** :  
  


  * This setting is applicable only when sending events in **device** or **hybrid** mode.
  * Once toggled on, the appropriate fields for entering the platform-specific keys are displayed based on the connected sources.


> ![warning](/docs/images/warning.svg)To use this setting, your device mode integration needs to be on a specific minimum version. See [this section](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/device-mode/#how-api-key-selection-works>) for the supported versions.  
  
Default App Identifier Key| Enter your Braze Default App Identifier Key.  
  


> ![info](/docs/images/info.svg)RudderStack uses this key as a fallback if platform-specific keys are unavailable.  
  
REST API Key| Enter the REST API key associated with your project required for **cloud mode connections**.  
  
**Note** : When creating a new Braze Rest API Key for your app, make sure to select the following [permissions](<https://www.braze.com/docs/api/basics/#rest-api-key-permissions>):  
  
| Permission| Description  
---|---  
users.track| For creating/updating users and registering events.  
users.identify| For identity resolution of identified and anonymous users.  
users.delete| For [deleting users](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/cloud-mode/#delete-a-user>).  
users.alias.new and users.merge| For aliasing users.  
users.export.ids| For [deduplication](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/trait-deduplication/>).  
Data Center| Specify the [data center](<https://www.braze.com/docs/user_guide/data/data_centers/#list-of-data-centers>) associated with your Braze account. See Supported Braze data centers for more information.  
  
**Note** : To get your data center details, log in to your Braze account and note your URL.  
  
#### Supported Braze data centers

Data center region| Dashboard URL  
---|---  
Australia| https://dashboard.au-01.braze.com  
Europe| https://dashboard-01.braze.eu  
https://dashboard-02.braze.eu  
US| https://dashboard-01.braze.com  
https://dashboard-02.braze.com  
https://dashboard-03.braze.com  
https://dashboard-04.braze.com  
https://dashboard-05.braze.com  
https://dashboard-06.braze.com  
https://dashboard-07.braze.com  
https://dashboard-08.braze.com  
  
### Event settings

Setting| Description  
---|---  
Enable subscription groups in group call| Turn on this setting to send the subscription group status in your [`group`](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/cloud-mode/#group>) events.  
  
**Note** : This setting is available only in cloud mode.  
Use Custom Attributes Operation| Turn on this setting to use Braze’s [nested custom attributes](<https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/array_of_objects/>) functionality to create segments and personalize your messages using a custom attribute object. For more information, see [Send user traits as nested custom attributes](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/cloud-mode/#send-user-traits-as-nested-custom-attributes>).  
  
**Note** : This setting is available only in cloud mode.  
  
### Deduplication settings

Setting| Description  
---|---  
Deduplicate Traits| Turn on this setting to enable traits [deduplication](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/trait-deduplication/>) for the `identify` and `track` calls.  
  
### Web SDK settings

Configure the following settings to send events to Braze in [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>):

Setting| Description  
---|---  
Show Braze logs| Turn on this setting to show Braze logs to the customers.  
Use web push notifications| Turn on this setting to use [push notifications for web](<https://www.braze.com/docs/developer_guide/platform_integration_guides/web/push_notifications/integration#step-1-configure-your-sites-service-worker>).  
  
**Note** : This feature requires you to set up a [service worker](<https://www.braze.com/docs/developer_guide/platform_integration_guides/web/push_notifications/integration>) on your site.  
Enable HTML in-app messages| Turn on this setting to enable HTML in-app messages.  
Track events for anonymous users| Turn on this setting to track anonymous user activity and send this information to Braze.  
  
### Other settings

Setting| Description  
---|---  
Client-side Events Filtering| This setting lets you specify which events should be blocked or allowed to flow through to Braze. For more information on this setting, see [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>).  
OneTrust Cookie Categories| This setting lets you associate the [OneTrust](<https://www.rudderstack.com/docs/data-governance/consent-management/onetrust/javascript/>) cookie consent groups to Braze.  
  
## Next steps

  * [Send events in cloud mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/cloud-mode/>)
  * [Send events in device mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/device-mode/>)
  * [Send events in hybrid mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/hybrid-mode/>)


## FAQ

#### Where can I find the Braze Default App Identifier Key?

  1. Log in to your [Braze dashboard](<https://dashboard.braze.com/auth>).
  2. Go to **Settings** > **APIs and Identifiers**.
  3. Go to the **App Identifiers** section:

[![Braze Default API Key](/docs/images/event-stream-destinations/braze-default-api-key.webp)](</docs/images/event-stream-destinations/braze-default-api-key.webp>)

  4. The Default App Identifier Key for your specific app is listed here.

[![Braze Default API Key](/docs/images/event-stream-destinations/braze-default-api-key-2.webp)](</docs/images/event-stream-destinations/braze-default-api-key-2.webp>)

#### Where can I find the Braze REST API Key?

  1. Log in to your [Braze dashboard](<https://dashboard.braze.com/auth>).
  2. Go to **Settings** > **APIs and Identifiers**.
  3. Go to the **API Keys** section:

[![Braze REST API Key](/docs/images/event-stream-destinations/braze-rest-api-key.webp)](</docs/images/event-stream-destinations/braze-rest-api-key.webp>)

  4. You can find the REST API Key for your workspace listed here.

[![Braze REST API Key](/docs/images/event-stream-destinations/braze-rest-api-key-2.webp)](</docs/images/event-stream-destinations/braze-rest-api-key-2.webp>)