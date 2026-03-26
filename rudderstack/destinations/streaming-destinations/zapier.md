# Zapier Destination

Send your event data from RudderStack to Zapier.

* * *

  * __2 minute read

  * 


[Zapier](<https://zapier.com/>) is a powerful automation tool that lets you automate your work across 5000+ applications.

RudderStack supports Zapier as a destination where you can seamlessly send your event data.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **Zapier** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), set up a source.
  2. Go to the **Overview** tab of your source and select **Add Destination** > **Create new destination**.

[![Add new destination in RudderStack dashboard](/docs/images/event-stream-destinations/add-new-destination.webp)](</docs/images/event-stream-destinations/add-new-destination.webp>)

  3. Select **Zapier** from the list of destinations.
  4. Assign a name to the destination and click **Continue**.


## Connection settings

Setting| Description  
---|---  
Zap URL| Enter your Zap URL.  
Mapping Track Events to a particular Zap| Use this setting to send `track` events with the specified **Event Name** to the corresponding **Zap URL**.  
Mapping Page/Screen Events to a particular Zap| Use this setting to send your `page`/`screen` events with the specified **Event Name** to the corresponding **Zap URL**.  
  
## Send events to Zapier

You can send specific `track`, `page`, or `screen` events to a particular Zap URL by configuring them in the dashboard settings.

Note that:

  * RudderStack supports sending only [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>), [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>), and [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) events to Zapier.
  * RudderStack **does not transform** or map any data before sending it to Zapier. It sends the raw event payloads to the specified **Zap URL** as is, without any modification.


## FAQ

#### Where can I find the Zap URL?

To get your Zap/Zapier URL, you need to first create a Zap by following these steps:

  1. Log in to your [Zapier dashboard](<https://zapier.com/app/dashboard>) and click **Create Zap**.
  2. In the **App Events** section, search for webhooks and select **Webhooks by Zapier**.
  3. Under **Event** , select the **Catch Raw Hook** option and click **Continue**.

[![Zapier connection settings](/docs/images/event-stream-destinations/create-zap-1.webp)](</docs/images/event-stream-destinations/create-zap-1.webp>)

  4. In the **Test Trigger** section, you will find your Zap URL or the webhook URL where you can send all requests. Copy and use this URL to set up the Zapier destination in RudderStack.

[![Zapier connection settings](/docs/images/event-stream-destinations/create-zap-2.webp)](</docs/images/event-stream-destinations/create-zap-2.webp>)

  5. **Important** : Complete the setup by connecting the trigger to an application, that is, the downstream tool where all data is sent.

[![Zapier connection settings](/docs/images/event-stream-destinations/create-zap-3.webp)](</docs/images/event-stream-destinations/create-zap-3.webp>)