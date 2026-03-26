# Shopify Source (Legacy RudderStack App)

Ingest your event data from Shopify into RudderStack.

* * *

  * __10 minute read

  * 


[Shopify](<https://www.shopify.com/>) is a popular ecommerce platform that gives you all tools to start, run, and grow your business effectively. It offers online retailers a variety of services around digital payments, marketing, product shipping, customer engagement and retention, and more.

This guide will help you set up Shopify as a source in RudderStack.

## Setup overview

Setting up the Shopify source involves two steps:

  1. Configuring a new Shopify source in RudderStack
  2. Configuring the RudderStack app in your Shopify store


See the below video tutorial for more information:

## Configure Shopify source in RudderStack

  1. Log in to your [RudderStack dashboard](<https://app.rudderstack.com/>) and click **Add Source**.
  2. From the list of **Event Streams** sources, select **Shopify**.
  3. Assign a name to your source and click **Continue**.


### Connection settings

Setting| Description  
---|---  
Disable client-side identifier| If you turn on this setting, RudderStack **does not** track the client-side `identify` events automatically.

> ![info](/docs/images/info.svg)Enable this setting to set your own `userId` in the client-side events using RudderStack’s [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call.  
>   
> For example, when you enable this flag and call `rudderanalytics.identify('custom_userId')`, RudderStack sets `custom_userId` as the client-side user ID instead of the `userId` set by the RudderStack Shopify tracker.  
  
Your Shopify source is now configured. Go to the **Setup** tab and note the source **Write key**. This is required later while configuring the RudderStack app in your Shopify store.

[![Shopify source write key](/docs/images/event-stream-sources/shopify-source-write-key.webp)](</docs/images/event-stream-sources/shopify-source-write-key.webp>)

## Configure the RudderStack app in your Shopify store

Follow these steps to add and configure the RudderStack app in your Shopify store and complete the setup:

  1. Go to your Shopify store’s [admin dashboard](<https://accounts.shopify.com/store-login>).
  2. In the left sidebar, go to **Apps** > **Customize your store** :

[![Customizing Shopify store](/docs/images/event-stream-sources/shopify-3.webp)](</docs/images/event-stream-sources/shopify-3.webp>)

  3. Search for RudderStack.

[![RudderStack app search](/docs/images/event-stream-sources/shopify-4.webp)](</docs/images/event-stream-sources/shopify-4.webp>)

  4. In the search results, select the RudderStack app and click **Add app**.

[![Add RudderStack app](/docs/images/event-stream-sources/RS-Shopify-app.webp)](</docs/images/event-stream-sources/RS-Shopify-app.webp>)

  5. After installation, you should be able to see the app in the **Installed apps** section:

[![Installed RudderStack app](/docs/images/event-stream-sources/shopify-5.webp)](</docs/images/event-stream-sources/shopify-5.webp>)

  6. Select the installed RudderStack app.
  7. Enter the **Source Write Key** that you copied above and your [RudderStack data plane URL](<https://www.rudderstack.com/docs/dashboard-guides/overview/#connections>):

[![Data plane URL and source write key](/docs/images/event-stream-sources/shopify-6.webp)](</docs/images/event-stream-sources/shopify-6.webp>)

  8. Click **Submit**.


> ![success](/docs/images/tick.svg)
> 
> You can update these fields later with a different write key and data plane URL.

## Event tracking and transformation

You can track user events using server-side and client-side tracking supported by Shopify.

> ![info](/docs/images/info.svg)
> 
> **Identity stitching enhancement for client-side and server-side tracking**
> 
> RudderStack internally performs identity stitching and sets the same `anonymousId` and [`sessionId`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/>) (generated automatically) for the same user in client-side and server-side events. You don’t need to take any action (like updating or reinstalling your RudderStack Shopify app) to use this feature.

### Track server-side events

RudderStack uses the Shopify-provided webhooks for tracking events on the server-side.

The following table details the supported Shopify events and their corresponding [topic](<https://shopify.dev/api/admin-rest/2022-01/resources/webhook#:~:text=a%20custom%20storefront.-,Mandatory%20webhooks,-You%20don%27t%20create>) mapping for `identify` calls:

Identify event name| Description| Subscribed Shopify topic  
---|---|---  
`customers_create`| Customer was created.| `customers/create`  
`customers_update`| Customer was updated.| `customers/update`  
`customers_disabled`| Customer was disabled.| `customers/disable`  
`customers_enable`| Customer was enabled.| `customers/enable`  
  
The following table details the supported Shopify events and their corresponding [topic](<https://shopify.dev/api/admin-rest/2022-01/resources/webhook#:~:text=a%20custom%20storefront.-,Mandatory%20webhooks,-You%20don%27t%20create>) mapping for `track` calls:

Track event name| Description| Subscribed Shopify topic  
---|---|---  
`checkout_delete`| Checkout was deleted.| `checkouts/delete`  
`checkout_update`| Checkout was updated.| `checkouts/update`  
`carts_update`| Cart was updated.| `cart/update`  
`fulfillments_create`| Fulfillment was created.| `fulfillments/create`  
`fulfillments_update`| Fulfillment was updated.| `fulfillments/update`  
`orders_create`| Order was created.| `orders/create`  
`orders_delete`| Order was deleted.| `orders/delete`  
`orders_cancelled`| Order was cancelled.| `orders/cancelled`  
`orders_fulfilled`| Order was fulfilled.| `orders/fulfilled`  
`orders_paid`| Order was paid.| `orders/paid`  
`orders_partially_fullfilled`| Order was partly fulfilled.| `orders/partially_fulfilled`  
  
> ![warning](/docs/images/warning.svg)
> 
> As of May 23, 2023, the `carts_create` event is deprecated. Instead, you can use the `carts_update` event that is fired whenever an update is made to a cart.

RudderStack also supports the following [ecommerce events](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>):

Ecommerce event name| Description| Subscribed Shopify topic  
---|---|---  
`Checkout Started`| A new checkout was created.| `checkouts/create`  
`Order Updated`| Order was updated.| `orders/updated`  
  
> ![warning](/docs/images/warning.svg)
> 
> Any other events flowing through RudderStack except the `track`, `identify`, and the above-mentioned ecommerce events are **discarded**.

> ![info](/docs/images/info.svg)
> 
> RudderStack captures user-related information from the `traits` object of the event payload. The product-specific information present in the above resources in `line_items` is mapped to the `products` array in the payload. For more information on the RudderStack event payload nomenclature, see [Event Specification](<https://www.rudderstack.com/docs/event-spec/standard-events/>) and [Common Fields](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/>).

#### Required scopes

The RudderStack app requires the following [scopes](<https://shopify.dev/api/usage/access-scopes>) for tracking user events in the Shopify store:
    
    
    read_checkouts, read_orders, read_customers, read_fulfillments, write_script_tags
    

The below is an example of server-side event transformed by RudderStack:
    
    
    {
      "anonymousId": "bb35ad42-d59b-405c-b311-2daf98671c9c",
      "type": "identify",
      "context": {
        "integration": {
          "name": "SHOPIFY"
        },
        "ip": "[::1]",
        "sessionId": "57470820",
        "library": {
          "name": "unknown",
          "version": "unknown"
        }
      },
      "integrations": {
        "SHOPIFY": true
      },
      "messageId": "7cbc1a8c-597d-42f7-8a1e-a659700da011",
      "originalTimestamp": "2022-01-03T12:34:08.876+05:30",
      "receivedAt": "2022-01-03T12:34:04.763+05:30",
      "request_ip": "[::1]",
      "rudderId": "f31e31dd-00c2-4f77-96b5-0dd46839bc9c",
      "sentAt": "2022-01-03T12:34:08.876+05:30",
      "timestamp": "2021-12-29T09:45:20.000Z",
      "traits": {
        "acceptsMarketing": false,
        "acceptsMarketingUpdatedAt": "2021-12-29T15:15:20+05:30",
        "address": {
          "address1": "6649 N",
          "address2": "Blue Gum Street",
          "city": "New Orleans",
          "company": "Example Organization",
          "country": "USA",
          "country_code": "US",
          "country_name": "USA",
          "customer_id": 5747017285820,
          "default": true,
          "first_name": "Alex",
          "id": 6947581821116,
          "last_name": "Keener",
          "name": "Alex Keener",
          "phone": "8005550100",
          "province": "Louisiana",
          "province_code": "LA",
          "zip": "00000"
        },
        "addressList": [{
          "address1": "6649 N",
          "address2": "Blue Gum Street",
          "city": "New Orleans",
          "company": "Example Organization",
          "country": "USA",
          "country_code": "US",
          "country_name": "USA",
          "customer_id": 5747017285820,
          "default": true,
          "first_name": "Alex",
          "id": 6947581821116,
          "last_name": "Keener",
          "name": "Alex Keener",
          "phone": "8005550100",
          "province": "Louisiana",
          "province_code": "LA",
          "zip": "00000"
        }],
        "adminGraphqlApiId": "gid://shopify/Customer/5747017285820",
        "currency": "USD",
        "email": "alex@example.com",
        "firstName": "Alex",
        "lastName": "Keener",
        "note": "",
        "orderCount": 0,
        "phone": "8005550100",
        "smsMarketingConsent": {
          "consent_collected_from": "SHOPIFY",
          "consent_updated_at": null,
          "opt_in_level": "single_opt_in",
          "state": "not_subscribed"
        },
        "state": "disabled",
        "tags": "",
        "taxExempt": false,
        "taxExemptions": [],
        "totalSpent": "0.00",
        "verifiedEmail": true
      },
      "userId": "5747017285820"
    }
    

### Track client-side events

For tracking the client-side events, RudderStack inserts a JavaScript tracking code into every page of the respective Shopify store.

Note that:

  * RudderStack supports the [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) event for every page visited on the Shopify store.
  * It also supports `Registration Viewed` as a generic [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) event whenever the user views their account or registration page.
  * RudderStack tracks the `Login Viewed` event **only** on the `account/login` page. It triggers the event if only if the user accesses this path.


> ![warning](/docs/images/warning.svg)
> 
> You can trigger the `Registration Viewed` and `Login Viewed` events only if you have configured the **Legacy** customer accounts version for your Shopify store setup.
> 
> ![Legacy customer accounts version](/docs/images/event-stream-sources/shopify-tracker-legacy-customer-account-version.webp)

  * RudderStack also supports the following [ecommerce events](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>) on client-side:

Event name| Description  
---|---  
`Cart Viewed`| User viewed the cart page.  
`Checkout Started`| User clicked on the buy button.  
`Product Added`| User added the product to the cart.  
`Product Clicked`| User clicked on a product.  
`Product List Viewed`| User viewed the product collections page.  
`Product Viewed`| User viewed a product page.  
  
A sample client-side event transformed by RudderStack is shown:
    
    
    {
      "channel": "web",
      "context": {
        "app": {
          "build": "1.0.0",
          "name": "RudderLabs JavaScript SDK",
          "namespace": "com.rudderlabs.javascript",
          "version": "2.2.4"
        },
        "traits": {},
        "sessionId": "23342112",
        "library": {
          "name": "RudderLabs JavaScript SDK",
          "version": "2.2.4"
        },
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36",
        "os": {
          "name": "",
          "version": ""
        },
        "locale": "en-GB",
        "screen": {
          "density": 2,
          "width": 1440,
          "height": 900,
          "innerWidth": 1440,
          "innerHeight": 185
        },
        "campaign": {},
        "page": {
          "path": "/",
          "referrer": "$direct",
          "referring_domain": "",
          "search": "",
          "title": "rudderstack-store-final",
          "url": "https://rudderstack-store-final.myshopify.com/",
          "tab_url": "https://rudderstack-store-final.myshopify.com/",
          "initial_referrer": "$direct",
          "initial_referring_domain": ""
        }
      },
      "type": "page",
      "messageId": "0cd68548-8e0a-42d0-9745-c2a0b38092f2",
      "originalTimestamp": "2022-02-22T05:08:51.357Z",
      "anonymousId": "f4a8e9c1-b757-4565-a12c-0dd80619316d",
      "userId": "",
      "properties": {
        "path": "/",
        "referrer": "",
        "search": "",
        "title": "rudderstack-store-final",
        "url": "https://rudderstack-store-final.myshopify.com/",
        "category": "t",
        "referring_domain": "",
        "tab_url": "https://rudderstack-store-final.myshopify.com/",
        "initial_referrer": "$direct",
        "initial_referring_domain": ""
      },
      "integrations": {
        "All": true
      },
      "category": "t",
      "sentAt": "2022-02-22T05:08:51.357Z"
    }
    

## Best practices

This section highlights some best practices for using the Shopify source efficiently.

### Provide login functionality

Shopify provides the store owners the capability to either make user login compulsory or allow guest checkout in their stores. However, it is a best practice to prompt users to log in onto your platform. That way, RudderStack can fetch the user details and provide you with meaningful event data corresponding to the user’s journey on your platform.

### Support for client-side calls

It is highly recommended **not** to make any drastic changes to your store structure to preserve data integrity. If you do so, RudderStack may track incorrect calls or miss them entirely, owing to the disparity between URL and triggered event.

Note the following additional details for ecommerce events tracked by RudderStack:

  * **Cart Viewed** : It is recommended to keep the URL in `[store-url]/cart` format.
  * **Checkout Started** : This event can be triggered in any of the following ways:
    * When **Checkout** button is clicked on the `[store-url]/cart` page.
    * When **Buy it Now** button is clicked on the product description page.
    * Using the pop-ups when adding a product.
  * **Product Added** : This event is triggered when the **Add to Cart** button is clicked on a product description page with `[store-url]/products/product_name` format.
  * **Product Clicked** : This event is triggered when you click a product entry on any page in the store.
  * **Product List Viewed** : This event is triggered when user sees a product on a page.
  * **Product Viewed** : This event is triggered when a product’s description page in `[store-url]/products/product_name` format is opened. It is an indicative of the product listing page being viewed.


### Event listener conditions for Shopify tracker

Event| Code| Example  
---|---|---  
Product Added| `form[action="/cart/add"] [type="submit"]`  
  
`form` element with `action="/cart/add"` and `type = "submit"`| `<form action= "/cart/add" class=”shopify-form”>`  
`<button type = "submit" class = “shopify-addToCart”>Add To Cart </button>`  
`</form>`  
Product Clicked| `$("a").filter((a, b) => b.href.indexOf("/products") > -1)`  
  
Above code runs through the whole HTML looking for anchor tags with `href` having `/products`.| `<a href="/products/product1">Product 1</a>`  
Product List Viewed| [Code](<https://github.com/rudderlabs/rudder-shopify-tracker/blob/6d6dafc9c6bf255613cc9697f7ab645e83315937/deviceModeInit.js#L202>)  
  
Above code checks the whole HTML for anchor tags with `href` having `/products` and an `img` tag either at the parent or their sibling level.| -  
Checkout Started| `form[action="/cart/add"] [type="button"]` and check for `checkout` or `buy` keywords in the button.  
  
`form` element with `action="/cart/add"` and `type = "button"`  
| `<form action= "/cart/add" class=”shopify-form”>`  
`<button type = "button" class = “shopify-addToCart”>Buy Now</button>`  
`</form>`  
  
## FAQ

#### I’m getting a Registration Failed/Updated Failed error when I enter the data plane URL and the write key. What should I do?

When configuring the RudderStack app in your Shopify store, enter your RudderStack data plane URL and the source write key obtained while setting up the Shopify source in RudderStack.

[![Data plane URL and source write key](/docs/images/event-stream-sources/shopify-6.webp)](</docs/images/event-stream-sources/shopify-6.webp>)

If you get a **Registrated Failed** or **Update Failed** error after entering the credentials, uninstall and reinstall the RudderStack app in your Shopify store and try again.

#### Where can I find the RudderStack data plane URL?

You can find the data plane URL in the home page of your [RudderStack dashboard](<https://app.rudderstack.com>):

[![Data Plane URL](/docs/images/rs-cloud/data-plane-url.webp)](</docs/images/rs-cloud/data-plane-url.webp>)

#### My app is behaving unexpectedly and no event is flowing. What should I do?

You can try deleting and reinstalling the app. If that does not work, you can [contact](<mailto:docs@rudderstack.com>) the RudderStack team.

#### How to track events from multiple stores?

You need to have the app installed and configured properly in each of the stores.

#### Why does RudderStack not load the client-side SDK on all the Shopify store pages?

If you customize the page paths for a standard Shopify store, RudderStack will not be able to track user activity on them. This is a limitation of RudderStack’s client-side tracking capabilities. Hence, it is highly recommended **not** to make any drastic changes to your store structure.

#### What is the difference between `browser_ip` and `requestIP`?

The `requestIP` is the IP address of the Shopify backend server which pushes data to RudderStack, while `browser_ip` is the user’s IP address.

#### Is it possible to collect additional/custom fields from Shopify?

Yes, it is possible to collect additional/custom fields from Shopify by using `identify` and `track` calls.

Note that the `rudderanalytics` object of JS SDK (for example, `rudderanalytics.track()` or `rudderanalytics.identify()`) is already loaded on the `window` object of the store where the app is installed. Hence, the `rudderanalytics` object should not be loaded separately to collect additional/custom fields from Shopify.

#### How does RudderStack set the `userId`?

RudderStack fetches Shopify’s `customerId` and uses it as `userId`.

#### Does RudderStack persist `anonymousId` for future calls?

RudderStack persists `anonymousId` throughout a user’s journey (from visiting the store to placing an order). After the user places the order, a new journey starts; RudderStack then sets a new `anonymousId` and persists it throughout that journey.

After placing an order, the user/admin may sometimes need to update it. Hence, RudderStack persists the `anonymousId` for any post-order updates for up to 1 hour (tracked as server-side events).

#### How can I differentiate between the data collected from Shopify Cloud (Webhooks) and Shopify Device (web device mode)?

You can differentiate between the data collected in cloud and device mode by looking at the signature in payload:

  * In the [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>), RudderStack subscribes to the Shopify webhooks to consume data from Shopify. The data collected from Shopify cloud has the following signature in the payload:


    
    
    context ": {....
    "library": {
      "name": "RudderStack Shopify Cloud",
      "version": "1.0.0"
      }
    }
    

  * In [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>), RudderStack loads its JavaScript SDK on every Shopify store page for web tracking. The data collected from the Shopify device mode has the following signature in the payload:


    
    
    "context": {
      ....
      "library": {
        "name": "RudderLabs JavaScript SDK",
        "version": "2.4.2"
      }
    }
    

#### Do I need to update or reinstall the RudderStack app in Shopify to use the identity stitching feature?

No, you do not need to take any action to use the identity stitching or Skip `identify` call enhancements.