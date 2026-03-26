# Snap Pixel

Send your event data from RudderStack to Snap Pixel.

* * *

  * __5 minute read

  * 


[Snap Pixel](<https://ads.snapchat.com/>) is a piece of JavaScript code that lets you measure the cross-device impact of your advertising campaigns. It enables you to understand how many Snapchat users interact with your website after seeing the ads.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **Snap Pixel** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Snap Pixel native SDK from the `https://sc-static.net/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Snap Pixel SDK successfully.

## Get started

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. From the list of destinations, select **Snap Pixel**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

Setting| Description  
---|---  
Pixel ID| Enter your Snap Pixel ID. See FAQ for more information on obtaining this ID.  
Hashing Method| Snap Pixel lets you pass a user parameter (`email` or `phone`) in both hashed and non-hashed format during the snippet’s initialization.  
  
If you choose **SHA-256** , RudderStack hash-encodes the parameter before passing it to Snap Pixel.  
Mapping to trigger the Snap Pixel events for the respective events| Use this setting to map custom event names to the standard Snap Pixel events.  
Client-side Events Filtering| This setting lets you specify which events should be blocked or allowed to flow through to Snap Pixel.  
  
See the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide for more information on this setting.  
Customize Client Deduplication Key| Toggle on this setting to set a custom client deduplication ID in Snap Pixel.  
  
See Setting custom client deduplication key for more information on this setting.  
Use device mode to send events| As this is a web device mode-only destination, this setting is on by default and cannot be toggled off.  
  
## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to initialize the Snap Pixel code.

RudderStack checks the cookies for the user parameter (`email` or `phone`) before loading the Snap Pixel snippet. If the parameter is present, RudderStack loads the snippet. Otherwise, it loads the snippet **without passing** the user parameter.

> ![info](/docs/images/info.svg)
> 
> Snapchat strongly recommends passing a user parameter (either `email` or `phone`) through the Snap Pixel, as it lets you get better insights into your tracked conversions and creates more robust Pixel Custom Audiences. For more information, refer to the [Snap Pixel FAQ](<https://businesshelp.snapchat.com/s/article/pixel-website-install?language=en_US>).

A sample `identify` call is as shown:
    
    
    rudderanalytics.identify({
      email: "alex@example.com",
      phone: "+1-202-555-0146"
    });   
    

The following table lists the user parameters along with the corresponding mapping to the Snap Pixel parameters:

RudderStack user parameter| Snap Pixel user parameter  
---|---  
`email`| `user_email`  
`phone`| `user_phone_number`  
  
## Page

When you make a [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call, RudderStack sends the following call to Snap Pixel:
    
    
    snaptr("track", "PAGE_VIEW")
    

> ![info](/docs/images/info.svg)
> 
> You can make a `page` call with or without the event payload.

A sample `page` call is as shown:
    
    
    rudderanalytics.page();
    

## Track

> ![warning](/docs/images/warning.svg)
> 
> This destination does not strictly adhere to the [RudderStack Ecommerce Event Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to send Snap Pixel events. Refer to the [Snapchat documentation](<https://businesshelp.snapchat.com/s/article/pixel-website-install?language=en_US>) for more information on the Snap Pixel events.

A sample `track` call is as shown below:
    
    
    rudderanalytics.track('Order Completed', {
      'currency': 'USD',
      'price': 333.33,
      'order_id': '11111111'
    });
    

You can also send the following [RudderStack ecommerce events](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>):

**RudderStack event**| **Snap Pixel event**  
---|---  
`Order Completed`| `PURCHASE`  
`Checkout Started`| `START_CHECKOUT`  
`Product Added`| `ADD_CART`  
`Payment Info Entered`| `ADD_BILLING`  
`Promotion Clicked`| `AD_CLICK`  
`Promotion Viewed`| `AD_VIEW`  
`Product Added To Wishlist`| `ADD_TO_WISHLIST`  
`Product Viewed`| `VIEW_CONTENT`  
`Product List Viewed`| `VIEW_CONTENT`  
`Products Searched`| `SEARCH`  
  
> ![warning](/docs/images/warning.svg)
> 
> RudderStack maps `order_id` to Snap Pixel’s `transaction_id` only in case of the `Order Completed` event.

Snap Pixel supports up to 5 custom events, listed below:

  * `CUSTOM_EVENT_1`
  * `CUSTOM_EVENT_2`
  * `CUSTOM_EVENT_3`
  * `CUSTOM_EVENT_4`
  * `CUSTOM_EVENT_5`


## Set custom client deduplication key

RudderStack lets you define the client deduplication key for event deduplication. Turn on the **Customize Client Deduplication Key** setting in the dashboard to use this feature.

The following scenarios describe the different ways RudderStack sets the custom deduplication key:

### Scenario 1: Pass the key in event properties

Suppose you turn on the **Customize Client Deduplication Key** setting and set the **Client Deduplication Field** to `properties.dedup`. RudderStack then sets the client deduplication ID with the value associated with `properties.dedup`, as shown in the following snippet:
    
    
    rudderanalytics.track(
      "SHARE", {
        dedup: "mydedupid",
        checkout_id: "12345",
        product_name: "Red T-shirt",
        product_url: "http://www.sampledomain.com/products/myred-t-shirt",
      }, {
        integrations: {},
      }
    );
    

In this case, RudderStack sets `mydedupid` as the client deduplication ID.

### Scenario 2: Pass `messageId` as the deduplication key

Suppose you turn on **Customize Client Deduplication Key** and leave the **Client Deduplication Field** empty. In this case, RudderStack sets the event’s `messageId` as the client deduplication ID.

### Scenario 3: Wrong/missing field in the dashboard settings

Suppose you turn on **Customize Client Deduplication Key** and set the **Client Deduplication Field** , but the field is either missing or has a different name in the event. In this case, RudderStack **does not set** the client deduplication ID.

For example, if you set **Client Deduplication Field** to `properties.dedup` and the event contains `properties.deduplication` instead, then RudderStack sends the event to Snap Pixel **without setting** the client deduplication ID.

## FAQ

#### Where can I find the Snap Pixel ID?

To get your Snap Pixel ID, follow these steps:

  1. Go to your [Snap Ads Manager](<https://ads.snapchat.com/>) account.
  2. Under **Events Manager** , go to **View Pixel Details** > **Setup Pixel**. You can find the Pixel ID under **Set Up Your Snap Pixel** :

[![Snap Pixel ID](/docs/images/event-stream-destinations/snap-pixel-id.webp)](</docs/images/event-stream-destinations/snap-pixel-id.webp>)