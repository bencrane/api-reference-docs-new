# Setup Guide Beta

Set up and configure LinkedIn Ads as a destination in RudderStack.

* * *

  * __3 minute read

  * 


This guide will help you set up LinkedIn Ads as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to LinkedIn Ads.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Linkedin Ads** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Setup

In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **LinkedIn Ads**.

### Connection settings

Setting| Description  
---|---  
Destination name| Assign a name to uniquely identify the destination.  
OAuth settings| Click **Create Account** > **Connect with LinkedIn Ads** and give RudderStack the necessary permissions to upload and manage your conversion tracking data.  
Hash and encode data| Encrypts your user email before sending it to LinkedIn Ads. Turn off this setting if your event data already contains hashed user email.  
  
> ![info](/docs/images/info.svg)
> 
> **Why do I see a request for Audience permissions while authorizing RudderStack?**
> 
> Since the LinkedIn Ads and [LinkedIn Audience](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/linkedin-audience/>) destination integrations share a common OAuth app in the backend, RudderStack requests all the necessary permissions needed for both integrations to work correctly.
> 
> RudderStack will **not** make any Audience-related API calls when sending data to your LinkedIn Ads destination.

### Advanced settings

Configure the below **optional** settings to receive your data correctly in LinkedIn Ads.

Setting| Description  
---|---  
LinkedIn Ad account ID| Choose your LinkedIn Ads account ID from the dropdown.  
Deduplication key| Specify the event property to be used for deduplicating your data in LinkedIn. By default, RudderStack maps `messageId` to LinkedIn’s `event_id` field for deduplication but you can specify any other field.  
  
**Make sure to specify the full path of the property**. For example, if you specify `properties.eventId`, then RudderStack maps `message.properties.eventId` to `event_id`.  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
### Events mapping

> ![warning](/docs/images/warning.svg)
> 
> You must create a conversion in your LinkedIn Campaign Manager **before** setting up the mappings.

To map RudderStack events to specific LinkedIn Ads conversion rules:

  1. Click **Set up mapping**.
  2. Specify the RudderStack event name and choose the LinkedIn conversion from the dropdown.

[![LinkedIn Ads event mappings](/docs/images/event-stream-destinations/linkedin-ads-event-mappings.webp)](</docs/images/event-stream-destinations/linkedin-ads-event-mappings.webp>)

## Next steps

  * [Send events in cloud mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/linkedin-ads/cloud-mode/>)


## FAQ

#### **How do I create a conversion in LinkedIn Campaign Manager?**

  1. Log in to [LinkedIn Campaign Manager](<https://www.linkedin.com/campaignmanager/>).
  2. From the left sidebar, click **Analyze** > **Conversion tracking**.
  3. Click **Create conversion** >**Conversions API or CSV conversion**.

[![LinkedIn Ads create conversion](/docs/images/event-stream-destinations/linkedin-ads-create-conversion.webp)](</docs/images/event-stream-destinations/linkedin-ads-create-conversion.webp>)

  4. Select **Direct API** and click **Next step**.

[![LinkedIn Ads direct API option](/docs/images/event-stream-destinations/linkedin-ads-direct-api.webp)](</docs/images/event-stream-destinations/linkedin-ads-direct-api.webp>)

  5. Define the conversion rules. Then, click **Next step**.

[![LinkedIn Ads conversion rules](/docs/images/event-stream-destinations/linkedin-ads-conversion-rules.webp)](</docs/images/event-stream-destinations/linkedin-ads-conversion-rules.webp>)

  6. Optionally, select the campaigns you want to track with the conversion. Then, click **Create**.

[![LinkedIn Ads select campaign](/docs/images/event-stream-destinations/linkedin-ads-campaign.webp)](</docs/images/event-stream-destinations/linkedin-ads-campaign.webp>)

See [Set up and create a conversion in Campaign Manager using Direct API](<https://www.linkedin.com/help/lms/answer/a1711116>) to fully complete the conversion setup.

#### **What permissions do I need to authenticate RudderStack successfully?**

You need one of the following permissions to successfully authenticate RudderStack to access and manage your conversions data:

  * `ACCOUNT_BILLING_ADMIN`
  * `ACCOUNT_MANAGER`
  * `CAMPAIGN_MANAGER`
  * `CREATIVE_MANAGER`