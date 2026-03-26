# Reddit Destination

Send your event data from RudderStack to Reddit.

* * *

  * __4 minute read

  * 


Reddit’s [Conversions API](<https://reddit.my.site.com/helpcenter/s/article/Conversions-API>) is a server-to-server solution for tracking and sharing your web conversion data with Reddit.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/main/src/cdk/v2/destinations/reddit>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Reddit** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), set up a source.
  2. Go to the **Overview** tab of your source and select **Add Destination** > **Create new destination**.

[![Add new destination in RudderStack dashboard](/docs/images/event-stream-destinations/add-new-destination.webp)](</docs/images/event-stream-destinations/add-new-destination.webp>)

  3. Select **Reddit** from the list of destinations. Then, click **Continue**.


### Connection settings

Setting| Description  
---|---  
Name| Assign a name to uniquely identify the destination.  
Event delivery account| Click **Create Account** > **Connect with Reddit**. Then, give RudderStack the necessary permissions to access your Reddit account.  
API Version| Select the Reddit API version from the dropdown.  
  


> ![warning](/docs/images/warning.svg)API v2 is deprecated but not yet sunset.  
>   
> For existing connections that leverage API v2, see [Reddit Destination v3 Migration Guide](<https://www.rudderstack.com/docs/destinations/streaming-destinations/reddit/v3-migration/>) for more information on how to migrate to API v3.  
  
Pixel ID| Enter the Pixel ID of your Reddit Ads account associated with the conversion events.  
Hash Data| This setting is turned on by default. RudderStack hash encrypts the event properties (for example, `email`, `userId`, `ip`, etc.) before sending them to Reddit.  
  


> ![warning](/docs/images/warning.svg)If you are already hashing this data before sending it to RudderStack, make sure to turn off this setting.  
  
### Configuration settings

Setting| Description  
---|---  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs.  
  
See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
### Event mapping settings

Click **Set up mapping** to map your RudderStack events to specific Reddit events. You can also use the JSON mapper to set these mappings.

[![Reddit event mapping setting](/docs/images/event-stream-destinations/reddit-event-mapping.webp)](</docs/images/event-stream-destinations/reddit-event-mapping.webp>)

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to record and send conversion events along with any associated properties to Reddit for processing.

A sample `track` event sent to Reddit:
    
    
    rudderanalytics.track("Order Completed", {
      revenue: 500,
      currency: "INR",
      conversionId: "G53B1A44XQ",
      clickId: "4583752045291814500",
      products: [{
        product_id: "item1",
        sku: "9472-775-0112",
        name: "Sample Item",
        price: 30,
        position: 1,
        category: "Sample Items"
        url: "https://www.website.com/sample-product/",
        image_url: "https://www.website.com/product/path.jpg",
      }]
    }, {
      traits: {
        email: "alex@example.com",
        userId: "1hKOmRA4GRlm",
        firstName: "Alex",
        lastName: "Keener"
      }
    });
    

### Standard event mappings

You can use the Event mapping settings in the dashboard to map your events to the below Reddit standard events:

  * `AddToCart`
  * `AddToWishlist`
  * `Lead`
  * `PageVisit`
  * `Purchase`
  * `Search`
  * `SignUp`
  * `ViewContent`


Note that RudderStack automatically maps the following standard [ecommerce events](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>) to Reddit’s standard `tracking_type` events:

RudderStack event| Reddit standard event  
---|---  
`Order Completed`| `Purchase`  
`Product Viewed`  
`Product List Viewed`| `ViewContent`  
`Product Added`| `AddToCart`  
`Product Added to Wishlist`| `AddToWishlist`  
`Products Searched`| `Search`  
  
> ![warning](/docs/images/warning.svg)
> 
> If you do not map your events in the RudderStack dashboard and they do not match the above standard ecommerce events, then RudderStack automatically sends them as custom events and maps them to Reddit’s `Custom` tracking type.

### Supported mappings

RudderStack maps the following event properties in the `track` events to the corresponding Reddit fields:

RudderStack property| Reddit property (API v2)| Reddit property (API v3)  
---|---|---  
`event`  
Required| `tracking_type` as set in the dashboard or as per the above standard mapping.| Same as API v2  
`event`  
Required| `custom_event_name` with `tracking_type` set to `Custom`| Same as API v2  
`originalTimestamp`  
Required| `event_at`| Same as API v2  
`context.ip`  
`request_ip`| `user.ip_address`| Same as API v2  
`context.userAgent`| `user.user_agent`| Same as API v2  
`context.traits.userId`| `user.external_id`| Same as API v2  
`properties.uuid`| `user.uuid`| Same as API v2  
`context.screen.height`| `user.screen_dimensions.height`| Same as API v2  
`context.screen.width`| `user.screen_dimensions.width`| Same as API v2  
`context.device.advertisingId`| `user.idfa` / `user.aaid`| Same as API v2  
`traits.email`  
`context.traits.email`| `user.email`| Same as API v2  
`traits.phone`  
`context.traits.phone`  
`properties.phone`| Not available| `user.phone_number`  
`traits.region`  
`context.traits.region`| Not available| `user.data_processing_options.region`  
`traits.country`  
`context.traits.country`| Not available| `user.data_processing_options.country`  
`properties.clickId`| `click_id`| Same as API v2  
`properties.conversionId`  
`messageId`| `event_metadata.conversion_id`| `metadata.conversion_id`  
`properties.currency`| `event_metadata.currency`| `metadata.currency`  
`properties.modes`| Not available| `user.data_processing_options.modes`  
`properties.optOut`| `opt_out`| Deprecated  
`properties.products.$.quantity`  
`properties.quantity`  
`properties.item_count`| `event_metadata.item_count`| `metadata.item_count`  
`properties.products.$.category`| `event_metadata.products.$.category`| `metadata.products.$.category`  
`properties.products.$.product_id`| `event_metadata.products.$.id`| `metadata.products.$.id`  
`properties.products.$.name`| `event_metadata.products.$.name`| `metadata.products.$.name`  
`properties.revenue`| `event_metadata.value`| `metadata.value`  
`properties.test_Id`| Not available| `test_id`  
  
## FAQ

#### Where can I find the Pixel ID?

  1. Log in to the [Reddit Ads Manager account](<https://accounts.reddit.com/adsregister>).
  2. Select **Events Manager** from the drop-down menu in the top-left corner.

[![](/docs/images/event-stream-destinations/reddit-pixel-id-1.webp)](</docs/images/event-stream-destinations/reddit-pixel-id-1.webp>)

  3. Select **Set Up Reddit Pixel** and choose from one of the below options according to your requirement:

[![](/docs/images/event-stream-destinations/reddit-pixel-id.webp)](</docs/images/event-stream-destinations/reddit-pixel-id.webp>)

Based on the selected option, you will find your Pixel ID on the next screen.

See [Reddit Pixel documentation](<https://business.reddithelp.com/helpcenter/s/article/Install-the-Reddit-Pixel-on-your-website>) for more information on setting up the Reddit Pixel.