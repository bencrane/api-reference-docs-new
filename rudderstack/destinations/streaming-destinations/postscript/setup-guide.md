# PostScript Destination Setup Guide Beta

Set up PostScript as a destination in RudderStack.

* * *

  * __3 minute read

  * 


This guide will help you set up PostScript as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to PostScript.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Beta
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Postscript** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), set up a source.
  2. Go to the **Overview** tab of your source and select **Add Destination** > **Create new destination**.

[![Add new destination in RudderStack dashboard](/docs/images/event-stream-destinations/add-new-destination.webp)](</docs/images/event-stream-destinations/add-new-destination.webp>)

  3. Select **PostScript** from the list of destinations. Then, click **Continue**.


## Connection settings

Setting| Description  
---|---  
Name| Assign a name to uniquely identify the destination in RudderStack.  
API key  
Required| Your PostScript API key used for authentication.  
  
> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * Your PostScript API key must have the following permissions:
> 
>     * **Subscriber management** : Create and update subscriber profiles
>     * **Custom events** : Send behavioral events for automation triggers
>   * Make sure to secure your API key — anyone with access to this key can modify your PostScript subscribers and send events.
> 
> 


## Configuration settings

Setting| Description  
---|---  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs.  
  
See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
> ![info](/docs/images/info.svg)
> 
> When consent management is enabled, RudderStack only sends events to PostScript when the user has provided appropriate consent.

## Next steps

After setting up your PostScript destination:

  * See the [PostScript Cloud Mode Integration](<https://www.rudderstack.com/docs/destinations/streaming-destinations/postscript/cloud-mode/>) guide to understand how RudderStack maps and sends events to PostScript.
  * Send test events to verify your setup is working correctly
  * Create SMS flows in PostScript that trigger based on the events you’re sending


## FAQ

#### Can I use PostScript with mobile SDKs?

Yes, PostScript works with all RudderStack SDKs through cloud mode. Events from mobile, web, and server sources are sent server-to-server to PostScript.

#### How do I handle subscriber consent?

Use RudderStack’s consent management features with OneTrust or Ketch to ensure you only send events for users who have provided appropriate consent.

#### Where can I find my PostScript API key?

  1. Log in to your PostScript dashboard.
  2. In your project, navigate to **API**.
  3. Click **Show** under **Private Key** to get your API key.

[![](/docs/images/event-stream-destinations/postscript-api-key.webp)](</docs/images/event-stream-destinations/postscript-api-key.webp>)

#### What permissions are required for my PostScript API key?

Your PostScript API key needs permissions for:

  * Subscriber management (create/update subscribers)
  * Custom events (send behavioral events)