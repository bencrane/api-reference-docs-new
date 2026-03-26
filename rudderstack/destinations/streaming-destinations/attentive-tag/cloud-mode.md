# Attentive Tag Cloud Mode Integration

Send events to Attentive Tag using RudderStack cloud mode.

* * *

  * __6 minute read

  * 


After you have successfully [set up Attentive Tag as a destination](<https://www.rudderstack.com/docs/destinations/streaming-destinations/attentive-tag/setup-guide/>) in RudderStack, follow this guide to correctly send your events to Attentive Tag in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/attentive_tag>).

## Identify

You can subscribe or unsubscribe a user from an Attentive list using the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call.

> ![info](/docs/images/info.svg)
> 
> The default behavior of `identify` call is to subscribe a user. To unsubscribe, you can pass `identifyOperation` as `unsubscribe` in the `integrations` object.

### Subscribe users

RudderStack maps the following traits to the Attentive properties while subscribing a user:

RudderStack trait| Attentive property  
---|---  
`traits.email`/`context.traits.email`/`properties.email`  
Required, if `phone` is not provided.| `user.email`  
`traits.phone`/`context.traits.phone`/`properties.phone`  
Required, if `email` is not provided.| `user.phone`  
`integrations.attentive_tag.signUpsourceId`  
Required, if not specified in the RudderStack dashboard.| `signUpSourceId`  
`externalId`| `externalIdentifiers`  
`context.traits.customIdentifiers`/`traits.customIdentifiers`| `externalIdentifiers.customIdentifiers`  
  
> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * The `externalIdentifiers` property can be an array of objects containing identifiers like `clientUserId`, `shopifyId`, `klaviyoId`.
>   * RudderStack prioritizes the `signUpSourceId` property in the `integrations` object over the value specified in the **Sign Up Source ID** dashboard setting.
> 


A sample `identify` call to subscribe a user is as follows:
    
    
    rudderanalytics.identify("jbu3471", {
      "email": "alex@example.com",
      "phone": "+1-202-555-0146",
      "customIdentifiers": [{
        "name": "string",
        "value": "string"
      }]
    }, {
      "externalId": [{
          "type": "clientUserId",
          "id": "144"
        },
        {
          "type": "shopifyId",
          "id": "224"
        },
        {
          "type": "klaviyoId",
          "id": "132"
        }
      ],
      "integrations": {
        "signUpSourceId": "347393"
      }
    });
    

> ![warning](/docs/images/warning.svg)
> 
> The `externalId` fields are case-sensitive. Also, RudderStack expects them to be in the above format for mapping them correctly.

### Unsubscribe users

You can set `identifyOperation` to `unsubscribe` in the `integrations` object to unsubscribe a user:
    
    
    rudderanalytics.identify("jbu3471", {
      "email": "alex@example.com",
      "phone": "+1-202-555-0146",
    }, {
      "integrations": {
        "attentive_tag": {
          "identifyOperation": "unsubscribe",
        },
        "subscriptions": [{
          "type": "MARKETING",
          "channel": "TEXT"
        }],
        "notification": {
          "language": "en-US"
        }
      }
    });
    

RudderStack maps the following traits to the Attentive properties while unsubscribing a user:

RudderStack trait| Attentive property  
---|---  
`traits.email`/`context.traits.email`/`properties.email`  
Required, if `phone` is not provided.| `email`  
`traits.phone`/`context.traits.phone`/`properties.phone`  
Required, if `email` is not provided.| `phone`  
`integrations.attentive_tag.subscriptions`| `subscriptions`  
`integrations.attentive_tag.notification`| `notification`  
  
> ![warning](/docs/images/warning.svg)
> 
> Passing an `email` attribute does not locate or unsubscribe a user from SMS subscription. Similarly, passing the `phone` attribute does not locate or unsubscribe a user from email subscription.

You can also unsubscribe a user from a channel by specifying it in `subscriptions` within the `integrations` object. The supported values for `subscriptions` are:
    
    
    "subscriptions": [{
        "type": "MARKETING" || "TRANSACTIONAL" || "CHECKOUT_ABANDONED"
        "channel": "TEXT" || "EMAIL"
      }]
    

> ![info](/docs/images/info.svg)
> 
> You can also provide the `language` in the `notification` inside the `integrations` object to change the notification language. Currently, RudderStack supports only `en-US` and `fr-CA` as the notification languages, which are case-sensitive.

### Use new Identify flow

> ![info](/docs/images/info.svg)
> 
> This feature is currently in beta.

The new Identify flow leverages the following Attentive APIs:

  * [Identity API](<https://docs.attentivemobile.com/openapi/reference/tag/Identity/>): To associate a client user identifier or custom identifier(s) with other identifiers.
  * [Custom Attributes API](<https://docs.attentivemobile.com/openapi/reference/tag/Custom-Attributes/#tag/Custom-Attributes>): For updating the user attributes or properties.


To use the new Identify flow, turn on the [**Enable new Identify flow** setting](<https://www.rudderstack.com/docs/destinations/streaming-destinations/attentive-tag/setup-guide/#advanced-settings>) during the destination setup.

> ![warning](/docs/images/warning.svg)
> 
> Your API key must have the necessary permissions to use the new Identify flow. Contact your Attentive representative for steps on enabling these permissions.

Note that:

  * If you toggle off this setting, RudderStack uses the default [subscription](<https://www.rudderstack.com/docs/destinations/streaming-destinations/attentive-tag/cloud-mode/#subscribing-users>) / [unsubscription](<https://www.rudderstack.com/docs/destinations/streaming-destinations/attentive-tag/cloud-mode/#unsubscribing-users>) flows instead.
  * In this flow, RudderStack **does not make** any user subscription or unsubscription API calls — to do so, you will need to use the `subscription_event` `track` call.


#### Identity API mappings

RudderStack trait| Attentive property  
---|---  
`traits.email`/`context.traits.email`/`properties.email`| `email`  
`traits.phone`/`context.traits.phone`/`properties.phone`| `phone`  
`context.externalId.[].shopifyId`| `shopifyId`  
`context.externalId.[].klaviyoId`| `klaviyoId`  
`context.externalId.[].clientUserId`| `clientUserId`  
`context.traits.customIdentifiers` / `traits.customIdentifiers`| `customIdentifiers`  
  
#### Custom Attributes API mappings

> ![info](/docs/images/info.svg)
> 
> RudderStack uses this API to send any traits in the `identify` call within the `properties` object of the request.

RudderStack trait| Attentive property  
---|---  
`traits.email`/`context.traits.email`/`properties.email`| `user.email`  
`traits.phone` / `context.traits.phone` / `properties.phone`| `user.phone`  
`context.externalId`| `user.externalIdentifiers`  
  
## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you capture the user actions along with the associated properties.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack does not trigger an event if the timestamp is older than 12 hours.

### Property mapping

RudderStack maps the following `track` call properties to the Attentive properties:

RudderStack property| Attentive property  
---|---  
`event`  
Required| `type`  
`traits.email`/`context.traits.email`/`properties.email`| `user.email`  
`traits.phone`/`context.traits.phone`/`properties.phone`| `user.phone`  
`externalId`| `user.externalIdentifiers`  
`properties`| `properties`  
`originalTimestamp`/`timestamp`| `occuredAt`  
`properties.eventId`| `externalEventId`  
`context.traits.customIdentifiers`/`traits.customIdentifiers`| `user.externalIdentifiers.customIdentifiers`  
  
> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * You must specify the timestamp in the ISO 8601 format.
>   * The event type is case-sensitive. For example, Attentive considers `Order shipped` and `Order Shipped` as different events.
>   * The keys of the `properties` object should not contain characters, like [`'`, `"`, `{`, `}`, `[`, `]`, \ , `,`]
> 


### Subscription events

You can perform user subscription and unsubscription operations using the `subscription_event` `track` call.

A sample `subscription_event` is shown below:
    
    
    rudderanalytics.track("subscription_event", {
      "context": {
        "traits": {
          "email": "alex@example.com",
          "phone": "+1-202-555-0146"
        }
      },
      "channelConsents": [{
          "channel": "email",
          "consented": true
        },
        {
          "channel": "sms",
          "consented": false,
          // "type": "MARKETING" (Unsubscribes the user from this subscription type)
        }
      ],
      // To specify the Signup Source ID in the track event instead of destination setting
      // "signUpSourceId": 123456
      
      // For unsubscribe case:
      // Optional notification properties to override
      "notification": {
        "language": "en-US",
        "disable": true
      }
    });
    

The above event results in the following `POST` calls:

  * The `/subscriptions` endpoint is used for subscribing the user’s `email` to the `email` channel.
  * The `/subscriptions/unsubscribe` is used for unsubscribing `phone` from the `sms` channel.


For subscribing to both `email` and `sms` channels, you can send the channel consents as shown below:
    
    
    "channelConsents": [{
          "channel": "email",
          "consented": true
        },
        {
          "channel": "sms",
          "consented": true,
        }
     ]
    

#### Considerations

This section highlights some key considerations for the subscription and unsubscription operations.

##### **For subscription**

  * [**Signup Source ID**](<https://www.rudderstack.com/docs/destinations/streaming-destinations/attentive-tag/setup-guide/#connection-settings>) is required for the subscription operation. You can also provide the `signUpSourceId` in the `track` event, as shown.


    
    
    rudderanalytics.track("subscription_event", {
      "context": {
        "traits": {
          "email": "alex@example.com",
          "phone": "+1-202-555-0146"
        }
      },
      "channelConsents": [{
        "channel": "email",
        "consented": true
      }],
      "signUpSourceId": 123456
    });
    

> ![info](/docs/images/info.svg)
> 
> The `signUpSourceId` field in the event payload overrides the **Signup Source ID** specified in the [destination settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/attentive-tag/setup-guide/#connection-settings>).

##### **For unsubscription**

  * The user is removed from **all subscriptions** if subscription `type` is not present in the event.
  * If `type` is provided, the user is removed from the specified subscription type or channel combination. An example is shown below:


    
    
    rudderanalytics.track("subscription_event", {
      "context": {
        "traits": {
          "email": "alex@example.com",
          "phone": "+1-202-555-0146"
        }
      },
      "channelConsents": [{
        "channel": "sms",
        "consented": false,
        "type": "MARKETING" // Unsubscribes the user from this subscription type
      }]
    });
    

### Ecommerce events

RudderStack converts the following ecommerce events to the corresponding Attentive events:

RudderStack event| Attentive event  
---|---  
Product List Viewed  
Product Viewed| `product-view`  
Product Added| `add-to-cart`  
Order Completed| `purchase`  
  
#### Product List Viewed

RudderStack maps the `Product List Viewed` event properties to the following Attentive properties:

RudderStack property| Attentive Tag property  
---|---  
`properties.products.$.product_id`  
Required| `items.productId`  
`properties.products.$.price`  
Required| `items.price.$.value`  
`properties.products.$.variant`  
Required| `items.productVariantId`  
`traits.email`/`context.traits.email`/`properties.email`| `user.email`  
`traits.phone`/`context.traits.phone`/`properties.phone`| `user.phone`  
`externalId`| `user.externalIdentifiers`  
`properties.products.$.currency`| `items.price.$.currency`  
`properties.products.$.name`| `items.name`  
`properties.products.$.url`| `items.productUrl`  
`properties.products.$.image_url`| `items.productImage`  
`context.traits.customIdentifiers`/`traits.customIdentifiers`| `user.externalIdentifiers.customIdentifiers`  
  
#### Product Viewed/Product Added

RudderStack maps the `Product Viewed` and `Product Added` event properties to the following Attentive properties:

RudderStack property| Attentive property  
---|---  
`properties.product_id`  
Required| `items.productId`  
`properties.price`  
Required| `items.price.$.value`  
`properties.variant`  
Required| `items.productVariant.Id`  
`properties.currency`| `items.price.$.currency`  
`properties.name`| `items.name`  
`properties.url`| `items.productUrl`  
`properties.image_url`| `items.productImage`  
`traits.email`/`context.traits.email`/`properties.email`| `user.email`  
`traits.phone`/`context.traits.phone`/`properties.phone`| `user.phone`  
`externalId`| `user.externalIdentifiers`  
`context.traits.customIdentifiers`/`traits.customIdentifiers`| `user.externalIdentifiers.customIdentifiers`  
  
#### Order Completed

RudderStack maps the `Order Completed` event properties to the following Attentive properties:

RudderStack property| Attentive property  
---|---  
`properties.products.$.variant`  
Required| `items.productVariantId`  
`properties.products.$.product_id`  
Required| `items.productId`  
`properties.products.$.price`  
Required| `items.price.$.value`  
`properties.products.$.currency`| `items.price.$.currency`  
`properties.products.$.name`| `items.name`  
`properties.products.$.url`| `items.productUrl`  
`properties.products.$.image_url`| `items.productImage`  
`traits.email`/`context.traits.email`/`properties.email`| `user.email`  
`traits.phone`/`context.traits.phone`/`properties.phone`| `user.phone`  
`externalId`| `user.externalIdentifiers`  
`context.traits.customIdentifiers`/`traits.customIdentifiers`| `user.externalIdentifiers.customIdentifiers`  
  
The following snippet highlights a sample `track` call for the above ecommerce event parameters:
    
    
    rudderanalytics.track("Order Completed", {
      "products": [{
        "product_id": "507f1f77bcf86cd799439011",
        "name": "MOBILE",
        "variant": "green",
        "price": "19",
        "image_url": "image.com",
        "url": "url.com",
        "quantity": "2",
        "currency": "USD"
      }]
    }, {
      "traits": {
        "email": "alex@example.com",
        "phone": "+1-202-555-0146"
      },
      "externalId": [{
          "type": "clientUserId",
          "id": "144"
        },
        {
          "type": "shopifyId",
          "id": "224"
        },
        {
          "type": "klaviyoId",
          "id": "132"
        }
      ]
    });