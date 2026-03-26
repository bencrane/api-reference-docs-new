# Bluecore Beta

Send your event data from RudderStack to Bluecore.

* * *

  * __5 minute read

  * 


[Bluecore](<https://www.bluecore.com/>) is an AI-powered retail marketing platform that helps brands personalize their campaigns by analyzing customer data. It enables targeted email and messaging campaigns, aiming to enhance engagement, boost sales, and improve marketing efficiency.

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/main/src/cdk/v2/destinations/bluecore>).

## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), go to **Directory** > **Destinations** > **Cloud Destinations** and search for **Bluecore**.
  2. Connect your source and click **Continue**.


### Connection settings

Configure the following settings to set up Bluecore as a destination in RudderStack:

  * **Name** : Assign a name to uniquely identify the destination.
  * **Bluecore namespace** : Enter your Bluecore token from the Bluecore dashboard.


### Connection mode

Destination Information  
---  
  
  * **Status:** Beta
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Unity, AMP , React Native , Flutter, Cordova, Web, Cloud, Shopify, Warehouse
  * Refer to it as **Bluecore** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
  
### Configuration settings

After completing the initial setup, configure the following settings to receive your data in Bluecore correctly:

  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


### Mappings

**Event mappings** : Click **Set-up mapping** to map the RudderStack events to [Bluecore standard ecommerce events](<https://help.bluecore.com/en/articles/6786828-events-service#h_ead2fa8c16>). RudderStack also provides the JSON mapper to set these mappings.

[![Bluecore event mapping](/docs/images/event-stream-destinations/bluecore-event-mapping.webp)](</docs/images/event-stream-destinations/bluecore-event-mapping.webp>)

RudderStack maps the following events to the Bluecore standard ecommerce events by default:

RudderStack event| Bluecore event  
---|---  
Product Viewed| `viewed_product`  
Products Searched| `search`  
Product Added| `add_to_cart`  
Product Removed| `remove_from_cart`  
Product Added to WIshlist| `wishlist`  
Order Completed| `purchase`  
  
## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create a new customer or link an email ID to an existing customer in Bluecore.

RudderStack sends this information to Bluecore by leveraging their [REST API endpoint](<https://help.bluecore.com/en/articles/6786828-events-service#h_188a59bb5b>).

A sample `identify` call to create a new customer in Bluecore:
    
    
    rudderanalytics.identify("27340af5c8819", {
      firstName: "Alex Keener",
      logins: 2
    })
    

You can [link an email ID with an existing customer](<https://help.bluecore.com/en/articles/6786828-events-service#h_b4ed19062c>) by sending the following attributes for the customer’s `distinct_id` (unique identifier for the customer):

  * `email`
  * custom field `message.traits.action` with `identify` value


    
    
    rudderanalytics.identify("27340af5c8819", {
      firstName: "Alex Keener",
      logins: 2,
      action: 'identify',
      email: 'alex@example.com'
    })
    

You can also send the `distinct_id` for a customer in the `externalId` object as shown:
    
    
    context: {
      externalId: [{
        type: 'bluecoreExternalId',
        id: '54321'
      }],
    }
    

> ![info](/docs/images/info.svg)
> 
> Note that any customer attributes or product properties you send in the RudderStack `identify` or `track` calls (for example, `first_name`) are permanently created in Bluecore if they do not exist already. To avoid excess or redundant attributes, only send the attributes critical to your campaigns and ensure their syntax remains the same throughout.

### Property mappings

RudderStack maps the following properties to the Bluecore properties:

RudderStack property| Bluecore property  
---|---  
`externalId`  
`email`  
`userId`  
`anonymousId`  
Required| `distinct_id`  
`name`| `customer.name`  
`age`| `customer.age`  
`sex`| `customer.sex`  
`address`| `customer.address`  
`email`| `customer.email`  
`context.app.version`| `client`  
`context.device.model`| `device`  
`destination.Config.token`| `token`  
  
## Track

You can use the RudderStack [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to track the user behavior along with any associated properties.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Product Viewed", {
      product_id: "622c6f5d5cf86a4c77358033",
      sku: "8472-998-0112",
      category: "Games",
      name: "Cones of Dunshire",
      brand: "Wyatt Games",
      variant: "exapansion pack",
      price: 49.99,
      quantity: 5,
      coupon: "PREORDER15",
      currency: "USD",
      position: 1,
      url: "https://www.website.com/product/path",
      image_url: "https://www.website.com/product/path.webp",
    })
    

> ![info](/docs/images/info.svg)
> 
> Note that any customer attributes or product properties you send in the RudderStack `identify` or `track` calls (for example, `first_name`) are permanently created in Bluecore if they do not exist already. To avoid excess or redundant attributes, only send the attributes critical to your campaigns and ensure their syntax remains the same throughout.

### Opt-in and unsubscribe users

You can also send `track` events to [opt-in or unsubscribe users](<https://help.bluecore.com/en/articles/6786828-events-service#h_66485dc4cd>) in Bluecore.

  * For opting-in a customer email, send a `subscription_event` event with the `channelConsents` object, where `email` is set to `true`:


    
    
    rudderanalytics.track("subscription_event", {
      channelConsents: {
        email: true
      }
    })
    

  * For unsubscribing a customer email, set the `email` field to `false`:


> ![info](/docs/images/info.svg)
> 
> It may take up to 24 hours for the user to be included in the unsubscribe list. See the [Bluecore documentation](<https://help.bluecore.com/en/articles/3550418-unsubscribes>) for more information.
    
    
    rudderanalytics.track("subscription_event", {
      channelConsents: {
        email: false
      }
    })
    

### Other custom events

If you have created any custom events in the Bluecore dashboard, you can send them as `track` calls via RudderStack without mapping them in the RudderStack dashboard. RudderStack sends the custom events as is.

### Property mappings

RudderStack maps the following properties to the Bluecore fields:

RudderStack property| Bluecore property  
---|---  
`userId`  
`anonymousId`  
`email`| `distinct_id`  
`name`| `customer.name`  
`age`| `customer.age`  
`sex`| `customer.sex`  
`address`| `customer.address`  
`email`| `customer.email`  
`properties.query`  
Required for Search events.| `search_term`  
`properties.order_id`  
Required for Purchase events.| `order_id`  
`properties.total`  
Required for Purchase events.| `total`  
`context.app.version`| `client`  
`context.device.model`| `device`  
`properties.products[#idx].id`/`product_id`/`sku`| `products[#idx].id`  
`properties.products[#idx].name`| `products[#idx].name`  
`properties.products[#idx].price`| `products[#idx].price`  
  
The following property mappings are applicable for the `subscription_event` event:

RudderStack property| Bluecore property  
---|---  
`userId`  
`anonymousId`  
`email`| `distinct_id`  
`email`| `email`  
`context.app.version`| `client`  
`context.device.model`| `device`  
  
Note that:

  * All the standard [RudderStack Ecommerce Events](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>) **require** `products` array except the [Products Searched](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/browsing/#products-searched>) event or any custom event mapped to Bluecore’s standard `search` ecommerce event.
  * Any custom event mapped to Bluecore’s standard `purchase` ecommerce event also **requires** `products` array, along with the `order_id`, `total`, and customer information (which RudderStack maps from the `traits` or `context.traits` object).
  * RudderStack maps the `id` for the `products` array either from the `product_id`, `sku`, or `id`. Further, RudderStack eliminates the `product_id`, `sku`, or `id` fields after computing the `id` of the `products` object before sending it to Bluecore.


## FAQ

#### Where can I find the Bluecore namespace?

  1. Log in to the [Bluecore dashboard](<https://app.bluecore.com/login>).
  2. From the left sidebar, go to **Account** > **Integration Guide**.

[![Bluecore namespace](/docs/images/event-stream-destinations/account-bluecore.webp)](</docs/images/event-stream-destinations/account-bluecore.webp>)

You can find the Bluecore namespace in the JavaScript code snippet:

[![Bluecore namespace](/docs/images/event-stream-destinations/bluecore-namespace.webp)](</docs/images/event-stream-destinations/bluecore-namespace.webp>)