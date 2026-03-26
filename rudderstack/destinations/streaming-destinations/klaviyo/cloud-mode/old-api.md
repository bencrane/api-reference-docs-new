# Klaviyo Cloud Mode Integration (Old API) Deprecated

Send events to Klaviyo via RudderStack cloud mode using the old API (v2023-02-22).

* * *

  * __6 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> The Klaviyo API v2023-02-22 is deprecated.
> 
> RudderStack recommends using the [New API integration](<https://www.rudderstack.com/docs/destinations/streaming-destinations/klaviyo/cloud-mode/new-api/>) instead.

After you have successfully instrumented Klaviyo as a destination in RudderStack, follow this guide to correctly send your events to Klaviyo in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>) using the [old API (v2023-02-22)](<https://developers.klaviyo.com/en/v2023-02-22/reference/api_overview>).

## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call lets you identify a visiting user and associate them to their actions. It also lets you record the traits about them like their name, email address, etc.

> ![success](/docs/images/tick.svg)
> 
> You can send any number of key-value pairs as user traits and RudderStack updates them as [custom profile properties](<https://help.klaviyo.com/hc/en-us/articles/115005074627>) in Klaviyo.

To create a new user in Klaviyo, you must pass either the `userId`, `email`, or `phone` properties in the `identify` call. If a user already exists, RudderStack updates the user profile with the latest values.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4el9Z", {
      firstName: "Alex",
      lastName: "Keener",
      email: "alex@example.com",
      phone: "+12 345 678 900",
      title: "Owner",
      organization: "Company",
      city: "Tokyo",
      country: "JP",
      zip: "100-0001",
      Flagged: false,
      Residence: "Shibuya",
      properties: {
        listId: "XUepkK",
        subscribe: true,
        consent: "email",
        smsConsent: true,
      },
    })
    

Note that specifying `consent` and `smsConsent` in the event properties overrides the respective settings specified in the [RudderStack dashboard](<https://www.rudderstack.com/docs/destinations/streaming-destinations/klaviyo/setup-guide/#configuration-settings>).

### Add and subscribe user to list

You can add and subscribe a user to a Klaviyo list by specifying the **List ID** in the RudderStack dashboard and setting the `subscribe` option to `true`. Alternatively, you can add `listId` within the event properties - this will override the **List ID** specified in the dashboard for that particular event.

If you have enabled the **Double opt-in** setting for a list in Klaviyo, users will not be added to the list automatically without their consent. To add users to a list automatically without waiting for their consent, select the **Single opt-in** option in that list’s settings:

[![Destination Settings for Klaviyo](/docs/images/event-stream-destinations/Klaviyo-setting.webp)](</docs/images/event-stream-destinations/Klaviyo-setting.webp>)

## Track

> ![warning](/docs/images/warning.svg)
> 
> This destination does not strictly adhere to the [RudderStack Ecommerce Event Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you record the user actions along with any properties associated with them.

> ![warning](/docs/images/warning.svg)
> 
> When sending events to Klaviyo in [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>), you must first identify your users before sending any `track` events. Klaviyo **does not** record any anonymous user activity.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Checked Out", {
      Clicked_Rush_delivery_Button: true,
      total_value: 2000,
      Ordered: ["T-Shirt", "jacket"],
      revenue: 2000,
    })
    

In the above snippet, RudderStack captures the information related to the `Checked Out` event, along with the details of the event.

To associate a user with an event, you need to pass either their `userId`, `email`, or `phone` in the `track` call. A sample server-side `track` call along with the user information is as shown:
    
    
    client.track({
      userId: "user2",
      event: "Item Purchased",
      properties: {
        revenue: 97.5,
        products: [
          {
            productId: "pro1",
            price: 32.5,
            quantity: 3,
          },
        ],
      },
      context: {
        traits: {
          email: "user2@gmail.com",
        },
      },
    })
    

In the above snippet, RudderStack captures the information related to the `Item Purchased` event, along with its additional information in `properties`. Moreover, since this event is captured using a server-side SDK, RudderStack passes the user information in `context` along with a unique `userId`.

Note that:

  * Use `context.traits` to pass the information in your `track` or `screen` events in case you are using a server-side SDK that does not persist user context information.
  * To set a specific value to the `screen` or `track` type event, you need to pass the event-related property in the `properties` field. Also, you can send `revenue` property in the `track` event and RudderStack automatically maps it to Klaviyo’s special property `$value`.


### Ecommerce event mapping

RudderStack converts the following ecommerce events to the corresponding Klaviyo events:

**RudderStack event**| **Klaviyo event**  
---|---  
`Product Viewed`  
`Product Clicked`| `Viewed Product`  
`Product Added`| `Added to Cart`  
`Checkout Started`| `Started Checkout`  
  
In addition to the above, RudderStack sends the following:

  * **Customer properties** : Must contain either the `email` or `phone_number` (in E.164 format). RudderStack extracts these customer properties from `traits`/`context.traits` in the `track` call.


As mentioned above, you can send any number of key-value pairs as user traits and RudderStack updates them as [custom profile properties](<https://help.klaviyo.com/hc/en-us/articles/115005074627>) in Klaviyo.

  * **Token** : Public API key from the RudderStack dashboard.


Additionally, you can choose to send specific fields for each of the events covered in the following sections:

#### Product Viewed

RudderStack maps the `Product Viewed` event to `Viewed Product` and maps the following event properties:

**RudderStack property**| **Klaviyo property**  
---|---  
`name`| `ProductName`  
`product_id`| `ProductID`  
`sku`| `SKU`  
`image_url`| `ImageURL`  
`url`| `URL`  
`brand`| `Brand`  
`price`| `Price`  
`compare_at_price`| `CompareAtPrice`  
`categories`| `Categories`  
  
#### Product Added

RudderStack maps the `Product Added` event to `Added to Cart` and maps the following event properties:

**RudderStack property**| **Klaviyo property**  
---|---  
`value`| `$value`  
`name`| `AddedItemProductName`  
`product_id`| `AddedItemProductID`  
`sku`| `AddedItemSKU`  
`image_url`| `AddedItemImageURL`  
`url`| `AddedItemURL`  
`price`| `AddedItemPrice`  
`quantity`| `AddedItemQuantity`  
`categories`| `AddedItemCategories`  
`item_names`| `ItemNames`  
`checkout_url`| `CheckoutURL`  
`items` (deprecating soon)  
`products`| `Items`  
  
> ![warning](/docs/images/warning.svg)
> 
> `properties.items` will be deprecated soon.

Note that `products`/`items` can contain the following parameters:

**RudderStack parameters**| **Klaviyo parameters**  
---|---  
`product_id`| `ProductID`  
`sku`| `SKU`  
`name`| `ProductName`  
`quantity`| `Quantity`  
`price`| `Price`  
`total`| `RowTotal`  
`url`| `URL`  
`image_url`| `ImageURL`  
`categories`| `ProductCategories`  
  
#### Checkout Started

RudderStack maps the `Checkout Started` event name to `Started Checkout` and maps the following event properties:

**RudderStack Parameters**| **Klaviyo Parameters**  
---|---  
`order_id`| `$event_id`  
`value`| `$value`  
`categories`| `Categories`  
`item_names`| `ItemNames`  
`items` (deprecating soon)  
`products`| `Items`  
`checkout_url`| `CheckoutURL`  
  
> ![warning](/docs/images/warning.svg)
> 
> `properties.items` will be deprecated soon.

Note that `products` / `items` can contain the following parameters:

**RudderStack parameters**| **Klaviyo parameters**  
---|---  
`product_id`| `ProductID`  
`sku`| `SKU`  
`name`| `ProductName`  
`quantity`| `Quantity`  
`price`| `Price`  
`total`| `RowTotal`  
`url`| `URL`  
`image_url`| `ImageURL`  
`categories`| `ProductCategories`  
  
A sample `track` call containing the above ecommerce event parameters is shown below:
    
    
    rudderanalytics.track("Checkout Started ", {
      order_id: "1234",
      value: 12.34,
      categories: ["category1", "category2"],
      checkout_url: "http://www.testcall.com",
      item_names: ["item1", "item2"],
      products: [{
          product_id: "pId1",
          sku: "sku1",
          name: "item1",
          url: "https://www.item1URL.com",
          price: 1.0,
          quantity: 1,
          image_url: "https://www.item1Image.com,
          categories: ["category1", "category2"],
          row_total: 1.0
        },
        {
          product_id: "pId2",
          sku: "sku2",
          name: "item2",
          url: "https://www.item2URL.com",
          price: 2.0,
          quantity: 1,
          image_url: "https://www.item2Image.com,
          categories: ["category1", "category2"],
          row_total: 2.0
        },
      ],
    });
    

## Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) method lets you record whenever a user sees their mobile screen along with any optional properties about the viewed screen.

A sample `screen` call is shown below:
    
    
    [[RSClient sharedInstance] screen:@"Sample Screen Name" properties:@{@"prop_key" : @"prop_value"}];
    

In Klaviyo, the above `screen` call is shown as `Sample Screen Name` along with the associated properties.

## Group

The [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call lets you associate a particular identified user with a group, such as a company, organization, or an account.

To make a `group` call successfully, you must include either `email` or `phone` in it. A sample server-side `group` call is shown:
    
    
    client.group({
      userId: "userId",
      groupId: "listId",
      traits: {
        subscribe: true,
      },
      context: {
        traits: {
          email: "user.test@gmail.com",
          city: "city",
          country: "country",
          zip: "213456",
          age: 23,
          plan: "free",
          consent: "email",
          phone: "1-617-555-1333"
        },
      },
    })
    

In the above snippet, the user with the associated traits is added and subscribed to the list as it is set to `true`.

Note that specifying `consent` in the event properties overrides the **Consent** setting specified in the [RudderStack dashboard](<https://www.rudderstack.com/docs/destinations/streaming-destinations/klaviyo/setup-guide/#configuration-settings>).

## Troubleshooting

**Error**| **Reason**| **Solution**  
---|---|---  
"detail": "Duplicate email found: alex@example.com."| The identifiers in the event are possibly from different user profiles in Klaviyo.| Make sure that all the identifiers in the event payload belong to the same user profile.  
  
To update a profile, you can provide the user's email, phone, or user ID.  
"detail": "A profile already exists with one of these identifiers."