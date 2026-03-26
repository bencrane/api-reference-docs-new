# Iterable Web Device Mode Integration

Send events to Iterable using RudderStack web device mode.

* * *

  * __3 minute read

  * 


RudderStack lets you send your event data to Iterable via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) using the native web SDK.

> ![success](/docs/images/tick.svg)
> 
> You can use this connection mode to dynamically send web in-app messages to your customers along with customized push notifications.

Find the open source JavaScript SDK code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/Iterable>).

## Identify

For the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call, RudderStack uses either [Iterable’s `setEmail` or `setUserId` method](<https://github.com/Iterable/iterable-web-sdk#initialize>) to identify a given user. You can configure this using the [Identifier to identify a user over a session](<https://www.rudderstack.com/docs/destinations/streaming-destinations/iterable/setting-up-iterable/#web-sdk-settings>) setting in the RudderStack dashboard.

> ![info](/docs/images/info.svg)
> 
> Making an `identify` call is necessary to associate the `track` events and trigger the web push notifications for an identified user.

> ![info](/docs/images/info.svg)
> 
> By default, RudderStack prioritizes `email` over `userId`.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("", {
        "email": "alex@example.com"
    },{ "integrations": {
        "ITERABLE": {
            "jwt_token" : "<YOUR_JWT_TOKEN>"
        }
    }})
    

When you call `identify`, RudderStack initializes the SDK using the `email`/`userId` and the JWT token from the `integrations` object.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack **does not** generate JWT tokens automatically on the users’ behalf to initialize the Iterable web SDK for security reasons. You need to set a specific authorization logic within your web app to generate a JWT before you can start making requests using the SDK.
> 
> To generate the JWT token for initializing the Iterable web SDK, see the [Iterable support page](<https://support.iterable.com/hc/en-us/articles/360050801231-JWT-Enabled-API-Keys-#sample-python-code-for-jwt-generation>).

## Track

RudderStack supports the following three types of [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) events in web device mode:

### Purchase events

You can map certain `track` events to Iterable’s purchase events ([API reference](<https://api.iterable.com/api/docs#commerce_trackPurchase>)) by specifying them in the [Mapping to trigger the purchase events](<https://www.rudderstack.com/docs/destinations/streaming-destinations/iterable/setting-up-iterable/#web-sdk-settings>) setting of the RudderStack dashboard:

[![Iterable connection settings](/docs/images/event-stream-destinations/iterable-purchaseevents.webp)](</docs/images/event-stream-destinations/iterable-purchaseevents.webp>)

A sample `track` call for a purchase event is shown below:
    
    
    rudderanalytics.track("purchase event", {
      checkout_id: "12345",
      order_id: "1234",
      affiliation: "Apple Store",
      total: 20,
      revenue: 15.0,
      shipping: 22,
      tax: 1,
      discount: 1.5,
      coupon: "ImagePro",
      currency: "USD",
      products: [{
          product_id: "123",
          sku: "G-15",
          name: "Chess",
          price: 14,
          quantity: 1,
          category: "Games",
          url: "https://www.mywebsite.com/product/path",
          image_url: "https://www.mywebsite.com/product/path.jpg",
        }
      ],
    })
    

The following table lists the mappings between the RudderStack event properties and the Iterable properties in case of the purchase events:

RudderStack property| Iterable property  
---|---  
`properties.name`  
Required| `items[].name`  
`properties.order_id`  
`properties.checkout_id`  
Required| `id`  
`properties.total`  
Required| `total`  
`properties.product_id`| `items[].id`  
`properties.sku`| `items[].sku`  
`properties.price`| `items[].price`  
`properties.quantity`| `items[].quantity`  
`properties.image_url`| `items[].url`  
  
The above properties can be passed in any of the following ways:

  * `properties` object (for a single product), as shown in the above table.
  * `products` array as multiple objects (for multiple products), for example, `properties.products[0].name`. One example where you can have an array of products is the [Order Completed](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#order-completed>) event.


### `getInAppMessages` events

You can send this type of `track` events to track the users in-app activities and accordingly display pop-up messages and push notifications for them. The below image shows an example of a web push notification:

[![Iterable connection settings](/docs/images/event-stream-destinations/web-push-notifications-iterable.webp)](</docs/images/event-stream-destinations/web-push-notifications-iterable.webp>)

You can also customize the display configuration for the push notifications using the [In-app message settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/iterable/setting-up-iterable/#in-app-message-settings>) in the RudderStack dashboard.

> ![info](/docs/images/info.svg)
> 
> In case multiple `getInAppMessages` events are triggered, the SDK delivers all queued in-app notifications.

A sample `track` call mapped to Iterable’s `getInAppMessages` events is shown below:
    
    
    rudderanalytics.track("trigger event",{})
    

### Custom events

RudderStack sends all `track` events that are not mapped to Iterable’s purchase events or `getInAppMessages` events as custom events.

A sample custom `track` event is shown below:
    
    
    rudderanalytics.track(
      "custom event", {
        custom_id: "22222",
        name: "Some item",
        website_url: "http://www.exampledomain.com/products/some-item",
      })
    

The following table lists the mappings between the RudderStack event properties and the Iterable properties in case of the custom events:

RudderStack property| Iterable property  
---|---  
`event`  
Required| `eventName`  
`userId`  
Required, if email is not present.| `userId`  
`context.traits.email`  
Required, if userId is not present.| `email`  
`properties`| `dataFields`