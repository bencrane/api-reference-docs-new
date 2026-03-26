# Podsights (Spotify Ad Analytics)

Send your event data from RudderStack to Podsights.

* * *

  * __8 minute read

  * 


> ![info](/docs/images/info.svg)
> 
> Podsights has now been rebranded to [Spotify Ad Analytics](<https://help.adanalytics.spotify.com/spotify-ad-analytics-faq>).

[Podsights](<https://podsights.com/>) is a podcast advertising and attribution platform. It lets you plan your advertising campaigns and measure the effectiveness of your podcasts through audience insights and real-time impression reporting.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **Podsights** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Podsights, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Podsights**.
  2. Assign a name to your destination and click **Continue**.


## Connection settings

To successfully configure Podsights as a destination, you will need to configure the following settings:

  * **Pixel ID** : Enter your Podsights Pixel ID. For more information on obtaining your Podsights Pixel ID, refer to the FAQ section below.
  * **Map Rudder events to Podsights Pixel events** : Use this setting to map your RudderStack events with standard Podsights Pixel events selected from the dropdown. You can map multiple Podsights Pixel events to a single RudderStack event and vice versa.
  * **Pass Internal ID** : Enable this setting to pass a hashed internal ID in case of `alias` events. For more information on obtaining the internal ID, refer to the FAQ section below.
  * **Client-side Events Filtering** : This setting lets you specify which events should be blocked or allowed to flow through to Podsights. For more information on this setting, refer to the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide.
  * **Use device mode to send events** : As this is a [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>)-only destination, this setting is enabled by default and cannot be disabled.
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


## Track

> ![warning](/docs/images/warning.svg)
> 
> This destination does not strictly adhere to the [RudderStack Ecommerce Event Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).

You can use the [Ecommerce Events Specification](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>) for sending the events while instrumenting your site with the RudderStack SDK.

You can use the RudderStack [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) event to track user events along with any associated properties and send this information to Podsights.

RudderStack supports the following standard [Podsights Pixel events](<https://help.adanalytics.spotify.com/technical-pixel-docs>):

Podsights Pixel event| Event name| Description  
---|---|---  
Lead| `lead`| User completed an action like form submission, free trial signup, button click, etc.  
Product| `product`| User viewed a product.  
Add to cart| `addtocart`| User added a product to cart.  
Check out| `checkout`| User initiated a checkout.  
Purchase| `purchase`| User purchased a product.  
  
You can map your RudderStack events to the above Podsights events in the RudderStack dashboard using the **Map Rudder events to Podsights Pixel Events** setting:

[![RudderStack event mapping with Podsights](/docs/images/event-stream-destinations/rudderstack-podsights-event-mapping.webp)](</docs/images/event-stream-destinations/rudderstack-podsights-event-mapping.webp>)

In the above example, RudderStack maps the event `Order Completed` with the Podsights `checkout` Pixel event.

By default, RudderStack maps the following events to the Podsights Pixel events:

RudderStack event| Podsights Pixel event name  
---|---  
`Signed Up`| `lead`  
`Product Viewed`| `product`  
`Product Added`| `addtocart`  
`Checkout Started`| `checkout`  
`Order Completed`| `purchase`  
  
RudderStack prioritizes the custom event mappings you set in the dashboard over the above standard mappings.

### Lead

A sample `track` call mapped to a Podsights `lead` event is shown below:
    
    
    rudderanalytics.track("Signed Up", {
      price: 500,
      currency: "USD",
      type: "paper",
      category: "Clothes"
    });
    

The following table lists the mapping between the **optional** RudderStack event properties and the Podsight attributes:

RudderStack property| Podsights property  
---|---  
`properties.price`| `value`  
`properties.currency`| `currency`  
`properties.type`| `type`  
`properties.category`| `category`  
  
### Product

A sample `track` call mapped to a Podsights `product` event is shown below:
    
    
    rudderanalytics.track("product", {
      price: 1300,
      currency: "USD",
      product_id: "1234000",
      name: "goldenTest",
      product_type: "Card",
      brand: "testVendor"
    });
    

The following table lists the mapping between the **optional** RudderStack event properties and the Podsight attributes:

RudderStack property| Podsights property  
---|---  
`properties.price`| `value`  
`properties.currency`| `currency`  
`properties.product_id`| `product_id`  
`properties.name`| `product_name`  
`properties.product_type`| `product_type`  
`properties.brand`| `product_vendor`  
  
#### Sending multiple product details

If you send the product details as an array in the `track` event, RudderStack fetches the details from each product item and calls the Podsights `product` event for each item. For example, consider the following `track` event:
    
    
    rudderanalytics.track("Product", {
      price: 10.0,
      currency: "INR",
      quantity: 2,
      products: [
        {
          product_id: "S1100",
          name: "Product 1",
          product_type: "Card",
          brand: "Some Vendor"
        },
        {
          product_id: "S1200",
          name: "Product 2",
          product_type: "Card",
          brand: "Some Vendor 2"
        }
      ]
    });
    

In this case, RudderStack makes two `track` calls to Podsights with the individual product details:
    
    
    // Call 1
    
    rudderanalytics.track("Product", {
      price: 10.0,
      quantity: 2,
      currency: "INR",
      product_id: "S1100",
      name: "Product 1",
      product_type: "Card",
      brand: "Some Vendor"
    });
    
    // Call 2
    
    rudderanalytics.track("Product", {
      price: 10.0,
      quantity: 2,
      currency: "INR",
      product_id: "S1200",
      name: "Product 2",
      product_type: "Card",
      brand: "Some Vendor 2"
    });
    

### Add to Cart

A sample `track` call mapped to a Podsights `addtocart` event is shown below:
    
    
    rudderanalytics.track("Add to Cart", {
      price: 23.2,
      currency: "USD",
      product_id: "1234000",
      name: "goldenTest",
      product_type: "Card",
      brand: "testVendor"
    });
    

The following table lists the mapping between the **optional** RudderStack event properties and the Podsight attributes:

RudderStack property| Podsights property  
---|---  
`properties.price`| `value`  
`properties.currency`| `currency`  
`properties.product_id`| `product_id`  
`properties.name`| `product_name`  
`properties.product_type`| `product_type`  
`properties.brand`| `product_vendor`  
`properties.quantity`| `quantity`  
`properties.variant_id`| `variant_id`  
`properties.variant_name`| `variant_name`  
  
Similar to the Product event, if you send the product details as an array in the `track` event, RudderStack fetches the details from each product item and calls the Podsights `addtocart` event for each item.

### Check out

A sample `track` call mapped to a Podsights `checkout` event is shown below:
    
    
    rudderanalytics.track("checkout", {
      price: 30.0,
      currency: "USD",
      discount_code: "PODCAST_CODE_TEST",
      quantity: 3,
      line_items: [
        {
          price: 21.2,
          quantity: 1,
          product_id: "1234000",
          product_name: "goldenTest",
          product_type: "Card",
          product_vendor: "testVendor",
          variant_id: "11112",
          variant_name: "Test"
        }
      ]
    });
    

The following table lists the mapping between the **optional** RudderStack event properties and the Podsight attributes:

RudderStack property| Podsights property  
---|---  
`properties.price`| `value`  
`properties.currency`| `currency`  
`properties.quantity`| `quantity`  
`properties.variant_id`| `variant_id`  
`properties.discount_code`| `discount_code`  
`properties.line_items`| `line_items`  
  
> ![info](/docs/images/info.svg)
> 
> If you do not pass the `line_items` object, then RudderStack fetches the `line_items` from the event’s properties and maps them to Podsight’s `line_items` field.

#### Passing multiple product items

If you pass multiple product items as an array, then RudderStack fetches the individual product details and internally builds the `line_items` object before passing it on to Podsights via the `checkout` event, as demonstrated in the following example:

Consider the following `track` event:
    
    
    rudderanalytics.track("Checkout", {
      price: 10.0,
      currency: "USD",
      quantity: 2,
      discountCode: "POD_CODE",
      products: [
        {
          price: 21.6,
          quantity: 12,
          product_id: "SKU123",
          name: "Card Game",
          product_type: "Card",
          brand: "Some Vendor",
          variant_id: "test123",
          variant_name: "Test 123"
        },
        {
          price: 42.4,
          quantity: 2,
          product_id: "SKU124",
          name: "Floppy Disk",
          product_type: "Card123",
          brand: "Some Vendor",
          variant_id: "test124",
          variant_name: "Test 124"
        }
      ]
    });
    

RudderStack internally collates all product information and builds the `line_items` array before sending it to Podsights:
    
    
    pdst("checkout", {
      price: 10.0,
      currency: "USD",
      discount_code: "POD_CODE",
      quantity: 2,
      line_items: [
        {
          price: 21.6,
          quantity: 12,
          product_id: "SKU123",
          product_name: "Card Game",
          product_type: "Card",
          product_vendor: "Some Vendor",
          variant_id: "test123",
          variant_name: "Test 123"
        },
        {
          price: 42.4,
          quantity: 2,
          product_id: "SKU124",
          product_name: "Floppy Disk",
          product_type: "Card123",
          product_vendor: "Some Vendor",
          variant_id: "test124",
          variant_name: "Test 124"
        }
      ]
    });
    

### Purchase

A sample `track` call mapped to a [`purchase`](<https://podsights.com/docs#purchase>) event is shown below:
    
    
    rudderanalytics.track("purchase", {
      price: 1000,
      currency: "rupee",
      discountCode: "PODCAST_CODE",
      orderId: "12322323232",
      is_new_customer: true,
      quantity: 3,
      line_items: [
        {
          price: 21.2,
          quantity: 1,
          product_id: "1234000",
          product_name: "goldenTest",
          product_type: "Card",
          product_vendor: "testVendor",
          variant_id: "11112222",
          variant_name: "testTest"
        }
      ]
    });
    

The following table lists the mapping between the **optional** RudderStack event properties and the Podsight attributes:

RudderStack property| Podsights property  
---|---  
`properties.price`| `value`  
`properties.currency`| `currency`  
`properties.discountCode`| `discount_code`  
`properties.line_items`| `line_items`  
`properties.orderId`| `order_id`  
`properties.is_new_customer`| `is_new_customer`  
`properties.quantity`| `quantity`  
  
Similar to the Check out event, if you pass multiple product items as an array, then RudderStack fetches the individual product details and internally builds the `line_items` object before passing it on to Podsights via the `purchase` event.

### Passing hashed internal ID to Podsights

If you turn on **Pass Internal ID** setting in the RudderStack dashboard and **Alias** events are enabled for your Podsight Pixel, then RudderStack triggers a Podsights `alias` event capturing the hashed internal user ID along with every conversion event.

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * The Podsights `alias` event matches the Podsights internal cookie ID with your hashed internal user IDs.
>   * RudderStack uses SHA-256 encryption for hashing your `userId`.
> 


To enable this feature, follow these steps:

  1. Activate **Alias Events** for your Podsights Pixel from your dashboard:

[![Podsights alias event setting](/docs/images/event-stream-destinations/pixel-alias-event.webp)](</docs/images/event-stream-destinations/pixel-alias-event.webp>)

  2. Enable the **Pass Internal ID** setting in the RudderStack dashboard.


RudderStack automatically calls the Podsights `alias` event by mapping the following internal RudderStack IDs to Podsights:

RudderStack attribute| Podsights attribute  
---|---  
`userId`  
`context.traits.userId`  
`context.traits.id`| `id`  
  
Suppose you send the following `track` call named `testEvent` mapped to Podsights’ `lead` event with the **Pass Internal ID** enabled:
    
    
    rudderanalytics.track("testEvent", {
      price: 100,
      currency: "euro",
      type: "paper"
    });
    

RudderStack then makes the following two calls to Podsights:

[![Alias calls made to Podsights](/docs/images/event-stream-destinations/spotify-alias-calls.webp)](</docs/images/event-stream-destinations/spotify-alias-calls.webp>)

## Page

You can use the [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call to record your website’s page views with any additional information about the viewed page.

> ![info](/docs/images/info.svg)
> 
> You can also set custom attributes inside the `page` event properties.

RudderStack sends the `page` calls to Podsights as a `view` event.

A sample `page` call is as shown:
    
    
    rudderanalytics.page("Home", "Clothes", {
      path: "/best-seller/1",
      referrer: "https://www.google.com/search?q=estore+bestseller",
      url: "https://www.estore.com/best-seller/1"
    });
    

### Supported property mappings

RudderStack maps the following **optional** properties with the Podsights properties:

RudderStack property| Podsights property  
---|---  
`context.page.referrer`| `referrer`  
`context.page.url`| `url`  
  
## FAQ

#### Where can I find the Podsights Pixel ID?

To get your Podsights Pixel ID, follow these steps:

  1. Log in to your [Podsights dashboard](<https://dash.podsights.com/>).
  2. From the left sidebar, go to **Manage** > **Your Pixels**. You can find your Podsights Pixel ID under **Your Pixels**.


#### Where can I find the Podsights alias ID for `alias` events?

  1. Log in to your [Podsights dashboard](<https://dash.podsights.com/>).
  2. From the left sidebar, go to **Manage** > **Your Pixels**. Then, click the edit button next to your pixel.

[![Podsights alias ID](/docs/images/event-stream-destinations/pixel-manage-option.webp)](</docs/images/event-stream-destinations/pixel-manage-option.webp>)

  3. The **Alias ID** is listed under **Alias Events** :

[![Podsights alias ID](/docs/images/event-stream-destinations/pixel-alias-id.webp)](</docs/images/event-stream-destinations/pixel-alias-id.webp>)

#### Where can I view the events sent to Podsights?

To view the events sent to Podsights, follow these steps:

  1. Log into your [Podsights dashboard](<https://dash.podsights.com/>).
  2. From the left sidebar, go to **Manage** > **Your Pixels**.
  3. Click your pixel and go to the **Debugger** tab.

[![Alias calls made to Podsights](/docs/images/event-stream-destinations/spotify-alias-calls.webp)](</docs/images/event-stream-destinations/spotify-alias-calls.webp>)

> ![info](/docs/images/info.svg)
> 
> You can filter the events by name or platform, as per your requirement.