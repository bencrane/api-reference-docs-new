# Quora Pixel

Send your event data from RudderStack to Quora Pixel.

* * *

  * __5 minute read

  * 


[Quora Conversion Pixel](<https://quoraadsupport.zendesk.com/hc/en-us/articles/115010303387-About-the-Quora-Pixel>) is a popular advertising and marketing tool to track your website traffic and conversions. If you are running ad campaigns on [Quora](<https://quora.com/>), you can attribute the downstream user actions on your website to your Quora impressions.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **Quora Pixel** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Web| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Quora Pixel native SDK from the`https://a.quora.com/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Quora Pixel SDK successfully.

## Get started

Once you have confirmed that the source platform supports sending events to Quora Pixel, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Quora Pixel**.
  2. Assign a name to your destination and click **Continue**.


### Connection settings

To successfully configure Quora Pixel as a destination, you need to configure the following settings:

  * **Pixel ID** : Enter the Pixel ID from your Quora Ads Manager Account. For more information on getting your Pixel ID, refer to the FAQ section below.
  * **Map RudderStack events to Quora Pixel events** : Use this setting to map your events to specific Quora Pixel events.


> ![info](/docs/images/info.svg)
> 
> You can map multiple Quora Pixel events to a single RudderStack event and vice versa. If you do not specify a mapping for a particular event, RudderStack maps it to Quora’s **Generic** event.

  * **Client-side Events Filtering** : This setting lets you specify which events should be blocked or allowed to flow through to Quora Pixel. For more information on this setting, refer to the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide.
  * **Use device mode to send events** : As this is a [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>)-only destination, this setting is enabled by default and cannot be disabled.
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


## Supported calls

Quora Pixel does not accept the standard RudderStack events, that is, [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>), [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>), etc. directly. You need to first map these event names to the corresponding Quora events in the RudderStack dashboard.

Suppose you specify the following mapping in the RudderStack dashboard:

[![Quora Pixel event mapping use-case](/docs/images/event-stream-destinations/quora-pixel-usecase.webp)](</docs/images/event-stream-destinations/quora-pixel-usecase.webp>)

RudderStack then takes the event name `Product Viewed` and maps it to Quora’s `Search` event.

A sample `Product Viewed` event is shown below:
    
    
    rudderanalytics.track("Product Viewed");
    

> ![warning](/docs/images/warning.svg)
> 
> You can only pass the event name to Quora Pixel. It does not accept any event properties.

RudderStack sends any event for which the mapping is not specified in the dashboard as a `Generic` event.

## Event mapping

Quora Ads supports two types of events, [Standard](<https://quoraadsupport.zendesk.com/hc/en-us/articles/360029101832-Standard-Events>) and [Custom](<https://quoraadsupport.zendesk.com/hc/en-us/articles/360029101852>).

### Standard events

Quora Pixel **natively supports** the following standard events:

Standard event| Description  
---|---  
Generic| Used to track generic actions that are not accounted for in the other categories.  
Purchase| Used to track purchases of digital or physical goods.  
Generate Lead| Used to track the lead generation process.  
Complete Registration| Used to track user signups for a newsletter or service.  
Add Payment Info| Used to track the linking of payment information to a user’s account.  
Add to Cart| Used to track the addition of items to a cart.  
Add to Wishlist| Used to track the addition of items to a wishlist.  
Initiate Checkout| Used to track the checkout process initialization.  
Search| Used to track different types of searches.  
  
You can map these events to the RudderStack events via the **Map RudderStack events to Quora Pixel events** dashboard setting.

### Custom events

Before you map your RudderStack events to Quora’s [custom events](<https://quoraadsupport.zendesk.com/hc/en-us/articles/360029101852>), make sure you have first configured the custom event in your Quora Ads Manager account.

To add a new custom event in Quora Ads Manager, follow these steps:

  1. Log into your [Quora Ads Manager Account](<https://www.quora.com/ads/account>).
  2. Navigate to the **Pixel & events** tab in your Quora Dashboard.
  3. Click the **Create event** button to open the **Create custom event** modal.
  4. Custom events require a name and description, and category. They also require **at least** one URL rule in the **URL Event** setting:

[![Custom Event](/docs/images/event-stream-destinations/quora-pixel-custom-event.webp)](</docs/images/event-stream-destinations/quora-pixel-custom-event.webp>)

  5. Click **Create event** to add a new custom event.


By default, Quora Pixel automatically tracks the custom events based on the **URL Event** setting. You need to include the specific web page URL keywords from which requests will be sent to Quora.

You can also send a specific RudderStack event as a Quora custom event by choosing the **Custom** event option from the dropdown:

[![Custom Event](/docs/images/event-stream-destinations/quora-pixel-custom-events-example.webp)](</docs/images/event-stream-destinations/quora-pixel-custom-events-example.webp>)

> ![warning](/docs/images/warning.svg)
> 
> If you send a standard event from a URL that is included in the **URL Event** property of your custom event configured in Quora Pixel, the event will be recorded in Quora as **both** a standard and custom event.

## FAQ

#### How do I retrieve the Quora Pixel ID?

To retrieve your Pixel ID from the Quora Ads dashboard, follow these steps:

  1. Log into your [Quora Ads Manager Account](<https://www.quora.com/ads/account>).
  2. Navigate to the **Pixel & events** tab in your Quora Ads dashboard.
  3. Click the **Setup Pixel** button to open the **Install the Quora Pixel** modal.
  4. Select **Install manually** and click the **Next** button.
  5. In the **Step 1: Install the base Pixel** modal, copy the installation JavaScript snippet and paste it somewhere safe.
  6. Search for `init` in the snippet. The string corresponding to `init` is your Pixel ID. For example, if your snippet contains the following code:


    
    
    qp('init', 'd2bnp3ubi9x6zq1p89h5hyx2hf5q1k3v');
    

In this case, `d2bnp3ubi9x6zq1p89h5hyx2hf5q1k3v` is your Pixel ID.

#### Can I use the client-side events filtering feature for the custom events?

The [client-side events filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) feature is not applicable for custom events. This is because Quora tracks custom events based on the **URL Event** property.