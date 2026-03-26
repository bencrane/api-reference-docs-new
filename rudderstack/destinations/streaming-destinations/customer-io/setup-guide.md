# Setup Guide

Set up and configure Customer.io as a destination in RudderStack.

* * *

  * __4 minute read

  * 


This guide will help you set up Customer.io as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Customer.io.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Customer IO** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using the [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Customer.io native SDK from the `https://assets.customer.io/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Customer.io SDK successfully.

## Setup

In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Customer.io**.

### Connection settings

Setting| Description  
---|---  
Destination name| Assign a name to uniquely identify the destination.  
Site ID| Enter your Customer.io site ID.  
API key| Enter your Customer.io API key.  
Data center| Choose your Customer.io data center from **US** or **EU**.  
  
**Note** : To send events to the EU data center using [RudderStack Open Source](<https://app.rudderstack.com/signup?type=opensource>), you should be using [`rudder-transformer`](<https://github.com/rudderlabs/rudder-transformer>) v1.42.0 or later.  
  
### Configuration settings

Configure the below settings depending on your connection mode:

#### Cloud mode settings

Setting| Description  
---|---  
Event sent after setting device token| Enter the name of the event that RudderStack fires immediately after setting the device token. This lets RudderStack send the device token to Customer.io immediately.  
  
#### Device mode settings

Configure the below device mode settings depending on your source:

##### Web SDK

Setting| Description  
---|---  
Event sent after setting device token| Enter the name of the event that RudderStack fires immediately after setting the device token. This lets RudderStack send the device token to Customer.io immediately.  
Send page name in SDK mode| If this setting is toggled on, RudderStack sends the page name to Customer.io. Otherwise, Customer.io fetches the page name in the form of a URL.  
Enable in-app message support| Toggle on this setting to send in-app messages to your website using the native web SDK.  
  
For more information on setting up in-app messages for your website, see the [Customer.io documentation](<https://customer.io/docs/journeys/in-app-getting-started/#javascript-snippet>).  
  
##### Mobile SDK

Setting| Description  
---|---  
Event sent after setting device token| Enter the name of the event that RudderStack fires immediately after setting the device token. This lets RudderStack send the device token to Customer.io immediately.  
Automatically track device attributes in SDK mode| Automatically track device attributes in the SDK mode through the Customer.io mobile SDK.  
  
**Note** : This setting is toggled on by default - toggle it off to track the attributes manually.  
Minimum number of tasks in background queue| This setting is available only for the **Android (Java)** source and lets you specify the minimum number of tasks to be kept in the background queue.  
  
**Note** : By default, RudderStack sets this value set to `10`.  
Delay in seconds for background queue| This setting is available only for the **Android (Java)** source and lets you specify the delay (in seconds) for the events to be kept in the background queue.  
  
**Note** : By default, RudderStack sets this value set to `30`.  
  
### Other settings

Setting| Description  
---|---  
Client-side Events Filtering| This setting lets you specify which events should be blocked or allowed to flow through to Customer.io. See the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide for more information.  
  
### Consent settings

Setting| Description  
---|---  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
## Next steps

  * [Send events in cloud mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/customer-io/cloud-mode/>)
  * [Send events in device mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/customer-io/device-mode/>)


## FAQ

#### Where can I find the Customer.io API key and site ID?

  1. Sign in to your [Customer.io dashboard](<https://fly.customer.io/>).
  2. In the left panel, click **Settings** and select **Account Settings**.
  3. Then, click **API Credentials**. You should find the site ID and API key for your project listed here.

[![Customer.io site ID and API key](/docs/images/event-stream-destinations/customerio-siteid-apikey.webp)](</docs/images/event-stream-destinations/customerio-siteid-apikey.webp>)