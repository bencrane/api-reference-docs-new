# Bing Ads Destination

Send your event data from RudderStack to Bing Ads.

* * *

  * __5 minute read

  * 


[Bing Ads](<https://ads.microsoft.com/>) is an advertising platform that lets you track and monitor ad campaigns, clicks, CTRs, etc. You can also implement efficient ad retargeting for your customers.

Find the open source JavaScript SDK code for this destination in our [Github repository](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/BingAds>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **Bing Ads** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> RudderStack loads the Bing Ads native SDK from the `https://bat.bing.com/` domain in the web device mode integration. Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Bing Ads SDK successfully.

## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), set up a source.
  2. Go to the **Overview** tab of your source and select **Add Destination** > **Create new destination**.

[![Add new destination in RudderStack dashboard](/docs/images/event-stream-destinations/add-new-destination.webp)](</docs/images/event-stream-destinations/add-new-destination.webp>)

  3. Select **Bing Ads** from the list of destinations. Then, click **Continue**.


### Connection settings

Setting| Description  
---|---  
Tag ID| Enter the UET tag ID associated with your Bing Ads account.  
  
You can create a UET tag by logging in to your [Bing Ads account](<https://ads.microsoft.com/>) and navigating to **Tools** > **Conversion Tracking** > **UET tag** > **Create UET tag**. See [Bing Ads documentation](<https://about.ads.microsoft.com/en/tools/performance/conversion-tracking>) for detailed instructions.  
Enable enhanced conversions| Turn on this toggle to send enhanced conversions to Bing Ads.  
  
### Other settings

Setting| Description  
---|---  
Client-side Events Filtering| This setting lets you specify which events should be blocked or allowed to flow through to Bing Ads.  
  
See [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) for more information on this setting.  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs.  
  
See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
Use device mode to send events| This setting is enabled by default as Bing Ads is a [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>)-only destination.  
  
## Page

You can make a [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call to Bing Ads to record a page view. The web SDK will send this data to Bing Ads with the event type as `pageLoad`.

The following snippet highlights a sample `page` call:
    
    
    rudderanalytics.page("Cart", "Cart Viewed", {
      path: "/cart",
      referrer: "test.com",
      search: "term",
      title: "test_item",
      url: "http://test.in",
    })
    

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to capture user events and their associated properties.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Item Purchased", {
      category: "MyCategory",
      currency: "INR",
      total: 5,
      revenue: 125,
      value: 100,
    })
    

### Supported mappings

The following table details the mappings between RudderStack and Bing Ads properties:

RudderStack property| Bing Ads property| Description  
---|---|---  
`properties.event_action`  
`message.type`| `event`| Event action.  
`properties.ecomm_pagetype`  
`properties.pagetype`| `ecomm_pagetype`| Viewed page type.  
`properties.products.$.product_id`  
`properties.products.$.sku`  
  
If `products` array is absent, then:  
  
`properties.product_id`  
`properties.sku`| `ecomm_prodid`| Product identifier.  
`properties.query`| `search_term`  
`ecomm_query`| Search query.  
`properties.ecomm_category`  
`properties.category_id`| `ecomm_category`| Category ID for the category browse page.  
`properties.total`  
`properties.value`| `ecomm_totalvalue`| Total value of all items in the transaction.  
`properties.transaction_id`  
`properties.order_id`  
`properties.checkout_id`| `transaction_id`| Unique ID for the transaction.  
`properties.products.$.product_id`  
`properties.products.$.sku`  
`properties.products.$.quantity`  
`properties.products.$.price`  
  
If `products` array is absent, then:  
  
`properties.product_id`  
`properties.sku`  
`properties.quantity`  
`properties.price`| `items`  
  
(id, quantity, price)| Product details like product ID, quantity, price.  
  
Note that:

  * RudderStack prioritizes `properties.total` over `properties.revenue` followed by `properties.value`, before mapping it to the Bing Ads `revenue` property.

  * Bing Ads accepts the following values for `properties.ecomm_pagetype`/`properties.pagetype` (mapped to `ecomm_pagetype`):

    * `other` (default value)
    * `home`
    * `category`
    * `searchresults`
    * `product`
    * `cart`
    * `purchase`
  * Bing Ads allows a maximum of 50 characters for the `product_id`/`sku` properties (mapped to `ecomm_prodid`).

  * You can override the default RudderStack mappings with the Bing Ads UET parameters by passing them directly in the event payload. For example, passing `ecomm_totalvalue` in the payload overrides the RudderStack properties `properties.total`/`properties.value` (mapped to `ecomm_totalvalue`). However, note that this functionality is **not applicable** for the `items` parameter.


See the [Bing Ads documentation](<https://help.ads.microsoft.com/#apex/ads/en/60123/-1>) for more information on the UET parameters.

### Send enhanced conversions

With [enhanced conversions](<https://help.ads.microsoft.com/apex/index/3/en/60178>), you can safely use first-party information like email address or phone number instead of using a third-party cookie. RudderStack includes this information in a `pid` object and sends it to Bing Ads.

To use this feature while sending events via RudderStack, make sure to toggle on the Enable enhanced conversions dashboard setting. Then, include the `email` and `phone` properties in your events.

RudderStack maps the `email` and `phone` properties in your event to the below enhanced conversions parameters by default:

  * `em` for email address
  * `ph` for phone


> ![warning](/docs/images/warning.svg)
> 
> If you have configured different parameters for email and phone, make sure to provide them in your `pid` object.

## Consent management

If you configure the consent settings for the Bing Ads destination in the RudderStack dashboard, then:

  * The core SDK prevents the Bing integration from loading unless the user grants the required consent.
  * If the user changes the consent status mid-session, then a page reload is required for the changes to take effect. This ensures that the SDK re-evaluates the consent settings and does not load the Bing Ads integration if the consent is revoked.


#### When consent is not configured

If you do not configure the consent settings in the RudderStack dashboard, then the Bing Ads SDK is already loaded and active. In this case, you must inform the Bing SDK explicitly if the user revokes or updates consent mid-session.

An example of a mid-session consent update is shown below:
    
    
    window.uetq = window.uetq || []; 
    window.uetq.push('consent', 'update', { 'ad_storage': 'denied' });
    

The above snippet instructs the Bing SDK to stop any data collection. In this scenario:

  * No page reload is required
  * Any new requests made by the Bing SDK will include the updated consent values.