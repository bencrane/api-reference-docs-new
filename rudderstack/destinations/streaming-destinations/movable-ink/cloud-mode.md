# Movable Ink Cloud Mode Integration Beta

Send events to Movable Ink using RudderStack cloud mode.

* * *

  * __8 minute read

  * 


After you have successfully instrumented Movable Ink as a destination in RudderStack, follow this guide to correctly send your events to Movable Ink in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/main/src/cdk/v2/destinations/movable_ink>).

## Create event mapping in Movable Ink

To send an event successfully to Movable Ink via RudderStack, you must set up its mapping in Movable Ink:

  1. Go to [Customer Data Endpoints](<https://app.movableink.com/behavioral/endpoints>) in the Movable Ink dashboard.
  2. Select the preferred endpoint and scroll to the **Event Mappings** section.
  3. Click **New event mapping** and fill the details:

[![Movable Ink public key](/docs/images/event-stream-destinations/identify-create.webp)](</docs/images/event-stream-destinations/identify-create.webp>)

> ![info](/docs/images/info.svg)
> 
> Refer to the `identify` and `track` sections to know about the **Match criteria** value.

  4. Click **Create** to create the event successfully.
  5. Click the created event, enter the JSON paths for the event properties (refer to the **RudderStack JSON Path** in the corresponding event’s mapping table in below sections) and click **Save Fields** :

[![Movable Ink public key](/docs/images/event-stream-destinations/identify-paths.webp)](</docs/images/event-stream-destinations/identify-paths.webp>)

  6. Turn the event status as **Activate**.


## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create or update a user in Movable Ink.

RudderStack maps the `identify` call to Movable Ink’s `Identify` event. You must set up the `identify` event mapping in Movable Ink with the match criteria as `.type == "identify"`. See Create event mapping in Movable Ink for more information.

A sample `identify` call is shown:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com",
      logins: 2
    })
    

> ![warning](/docs/images/warning.svg)
> 
> At least one of the `userId`, `email`, or `anonymousId` fields is required to send `identify` events to Movable Ink.

You can send up to 1000 events in a batch with the batch request size not exceeding 1 MB.

### Supported mappings

RudderStack maps the following `identify` event fields to the corresponding Movable Ink schema fields:

RudderStack property path| Movable Ink schema field| Data type  
---|---|---  
`userId`  
Required| `UserID`| String  
`anonymousId`  
Required| `AnonymousId`| String  
`timestamp`  
Required  
  
Automatically added by RudderStack in the final event payload.| `Timestamp`| Number (Unix timestamp)  
`context.timezone`| `Timezone`| String  
  
## Track

You can use a [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to send the [ecommerce](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>) and custom events to Movable Ink. The match criteria for any `track` event in the Movable Ink dashboard is `.event == "Event Name"`. See Create event mapping in Movable Ink for more information.

> ![warning](/docs/images/warning.svg)
> 
> At least one of the `userId`, `email`, or `anonymousId` fields is required to send `track` events to Movable Ink.

You can send up to 1000 events in a batch with the batch request size not exceeding 1MB.

### Supported event schemas

Movable Ink supports the following predefined [event schemas](<https://app.movableink.com/behavioral/schemas>) (mentioned with their corresponding match criterias):

  * Product (`Product Viewed`)
  * Category (`Category Viewed`)
  * CartAdd (`Product Added`)
  * Search (`Products Searched`)
  * Conversion (`Order Completed`)
  * CartRemove (`Product Removed`)


You can also create custom event schemas by clicking **New Schema** in the Movable Ink dashboard.

Movable Ink supports upto 20 custom properties for the **Product** , **CartAdd** , and **CartRemove** events. You must provide the custom property’s `name` and `JSON path` by clicking the event and adding the values in the schema fields.

### Product

The match criteria for **Product** event in Movable Ink is `.event == "Product Viewed"`.

A sample code is shown:
    
    
    rudderanalytics.track("Product Viewed", {
      product_id: "622123477358033",
      sku: "9472-998-0112",
      category: "Games",
      name: "Age of Empires",
      brand: "CEO Games",
      variant: "expansion pack",
      price: 49.99,
      quantity: 5,
      coupon: "PRE15",
      currency: "USD",
      position: 1,
      url: "https://www.example.com/product/path",
      image_url: "https://www.example.com/product/path.webp",
    })
    

RudderStack maps the following properties to Movable Ink schema fields for **Product** event:

RudderStack property path| Movable Ink schema field| Data type| Note  
---|---|---|---  
`properties.product_id`  
Required| `ID`| String| -  
`timestamp`  
Required| `Timestamp`| Number| Unix timestamp  
  
Automatically added by RudderStack in the final event payload.  
`properties.categories[]`| `Categories`| Array| You can pass the category URL and ID under categories. For example, `.url`, `.id`.  
`channel`| `Channel`| String| Automatically added by RudderStack in the final event payload.  
`properties.price`| `Price`| Number| -  
`context.timezone`| `Timezone`| Number| -  
`properties.name`| `Title`| String| -  
`properties.url`| `URL`| String| -  
  
### Category

RudderStack does not support any standard ecommerce event corresponding to the **Category** event but recommends to set the match criteria in Movable Ink as **Category Viewed**. However, you can configure any other event name and JSON path in the Movable Ink schema field and pass the same to RudderStack.

RudderStack maps the following properties to Movable Ink schema fields for **Category** event:

RudderStack property path| Movable Ink schema field| Data type  
---|---|---  
`properties.category_id`  
Required| `CategoryID`| String  
`timestamp`  
Required  
  
Automatically added by RudderStack in the final event payload.| `Timestamp`| Number (Unix timestamp)  
`channel`  
  
Automatically added by RudderStack in the final event payload.| `Channel`| String  
`context.timezone`| `Timezone`| Number  
`properties.name`| `Title`| String  
`properties.url`| `CategoryURL`| String  
  
### CartAdd

The match criteria for **CartAdd** event in Movable Ink is `.event == "Product Added"`.

A sample code is shown:
    
    
    rudderanalytics.track("Product Added", {
      product_id: "622113312385534c72358033",
      sku: "9472-998-0112",
      category: "Games",
      name: "Age of Empires",
      brand: "CEO Games",
      variant: "expansion pack",
      price: 29.99,
      quantity: 5,
      coupon: "PRE15",
      position: 1,
      url: "https://www.example.com/product/path",
      image_url: "https://www.example.com/product/path.webp",
    })
    

RudderStack maps the following properties to Movable Ink schema fields for **CartAdd** event:

RudderStack property path| Movable Ink schema field| Data type| Note  
---|---|---|---  
`properties.product_id`  
Required| `ID`| String| -  
`timestamp`  
Required| `Timestamp`| Number| Unix timestamp  
  
Automatically added by RudderStack in the final event payload.  
`properties.categories[]`| `Categories`| Array| You can pass the category URL and ID under categories. For example, `.url`, `.id`.  
`channel`| `Channel`| String| Automatically added by RudderStack in the final event payload.  
`properties.price`| `Price`| Number| -  
`context.timezone`| `Timezone`| Number| -  
`properties.name`| `Title`| String| -  
`properties.url`| `URL`| String| -  
  
### Search

The match criteria for **Search** event in Movable Ink is `.event == "Products Searched"`.

A sample code is shown:
    
    
    rudderanalytics.track("Products Searched", {
      query: "HDMI cable",
    })
    

RudderStack maps the following properties to Movable Ink schema fields for **Search** event:

RudderStack property path| Movable Ink schema field| Data type  
---|---|---  
`properties.query`  
Required| `Query`| String  
`timestamp`  
Required  
  
Automatically added by RudderStack in the final event payload.| `Timestamp`| Number (Unix timestamp)  
`userId`  
Required, if anonymousId is absent.| `UserID`| String  
`anonymousId`  
Required, if userId is absent.| `AnonymousID`| String  
`channel`  
  
Automatically added by RudderStack in the final event payload.| `Channel`| String  
`context.timezone`| `Timezone`| Number  
`properties.url`| `URL`| String  
  
### Conversion

The match criteria for **Conversion** event in Movable Ink is `.event == "Order Completed"`.

A sample code is shown:
    
    
    rudderanalytics.track("Order Completed", {
      checkout_id: "ea000000000000",
      order_id: "order1200000",
      affiliation: "CEO Games",
      total: 52.0,
      subtotal: 45.0,
      revenue: 50.0,
      shipping: 4.0,
      tax: 3.0,
      discount: 5.0,
      coupon: "freshorder5",
      currency: "USD",
      products: [
        {
          product_id: "622c6f5d5cf86a4c77358033",
          sku: "8472-998-0112",
          name: "Age of Empires",
          price: 40,
          quantity: 1,
          position: 1,
          category: "Games",
          url: "https://www.example.com/product/path",
          image_url: "https://www.example.com/product/path.jpg",
        },
        {
          product_id: "577c6f5d5cf86a4c7735ba03",
          sku: "3309-483-2201",
          name: "Monopoly",
          price: 5,
          quantity: 1,
          position: 2,
          category: "Games",
        },
      ],
    })
    

RudderStack maps the following properties to Movable Ink schema fields for **Conversion** event:

RudderStack property path| Movable Ink schema field| Data type| Note  
---|---|---|---  
`properties.products[]`  
Required| `Products`| Array| -  
`properties.products[n].product_id`  
Required| `Products.ID`| String| Path within the `products` array.  
`timestamp`  
Required| `Timestamp`| Number| Unix timestamp  
  
Automatically added by RudderStack in the final event payload.  
`properties.products[n].url`| `Products.URL`| String| Path within the `products` array.  
`properties.products[n].quantity`| `Products.Quantity`| Number| Path within the `products` array.  
`properties.products[n].price`| `Products.Price`| Number| Path within the `products` array.  
`properties.products[n].name`| `Products.Title`| String| Path within the `products` array.  
`channel`| `Channel`| String| Automatically added by RudderStack in the final event payload.  
`context.timezone`| `Timezone`| Number| -  
`properties.order_id`| `ID`| String| -  
`properties.revenue`| `Revenue`| Number| -  
  
### CartRemove

The match criteria for **CartRemove** event in Movable Ink is `.event == "Product Removed"`.

A sample code is shown:
    
    
    rudderanalytics.track("Product Removed", {
      product_id: "622c6f5d5cf86a4c77358033",
      sku: "8472-998-0112",
      category: "Games",
      name: "Age of Empires",
      brand: "CEO Games",
      variant: "expansion pack",
      price: 49.99,
      quantity: 5,
      coupon: "PRE15",
      position: 1,
      url: "https://www.example.com/product/path",
      image_url: "https://www.example.com/product/path.webp",
    })
    

RudderStack maps the following properties to Movable Ink schema fields for **CartRemove** event:

RudderStack property path| Movable Ink schema field| Data type| Note  
---|---|---|---  
`properties.product_id`  
Required| `ID`| String| -  
`timestamp`  
Required| `Timestamp`| Number| Unix timestamp  
  
Automatically added by RudderStack in the final event payload.  
`properties.categories[]`| `Categories`| Array| You can pass category URL and ID under categories. For example, `.url`, `.id`.  
`channel`| `Channel`| String| Automatically added by RudderStack in the final event payload.  
`properties.price`| `Price`| Number| -  
`context.timezone`| `Timezone`| Number| -  
`properties.name`| `Title`| String| -  
`properties.url`| `URL`| String| -  
  
### Custom events

For any custom event, you must configure the following bare minimum schema fields:

RudderStack property path| Movable Ink schema field| Data type  
---|---|---  
`timestamp`  
Required  
  
Automatically added by RudderStack in the final event payload.| `Timestamp`| Number (Unix timestamp)  
`context.timezone`| `Timezone`| String  
  
## Common field mappings

The following table lists the common mappings relevant for both the `identify` and `track` events:

RudderStack property| Movable Ink property  
---|---  
`traits.address`  
`context.traits.address`| `address`  
`traits.createdAt`  
`context.traits.createdAt`  
`timestamp`  
`originalTimestamp`| `createdAt`  
`traits.createdAt`  
`context.traits.createdAt`| `createdAtOnly`  
`traits.email`  
`context.traits.email`  
`properties.email`  
`context.externalId.0.id`| `email`  
`traits.email`  
`context.traits.email`  
`properties.email`| `emailOnly`  
`timestamp`  
`originalTimestamp`| `timestamp`  
`timestamp`  
`originalTimestamp`| `historicalTimestamp`  
`traits`  
`context.traits`| `traits`  
`groupId`  
`traits.groupId`| `groupId`  
`traits`  
`context.traits`| `groupTraits`  
`userId`  
`traits.userId`  
`traits.id`  
`context.traits.userId`  
`context.traits.id`  
`anonymousId`| `userId`  
`userId`  
`traits.userId`  
`traits.id`  
`context.traits.userId`  
`context.traits.id`| `userIdOnly`  
`traits.name`  
`context.traits.name`| `name`  
`traits.title`  
`context.traits.title`| `title`  
`traits.firstName`  
`traits.firstname`  
`traits.first_name`  
`context.traits.firstName`  
`context.traits.firstname`  
`context.traits.first_name`| `firstName`  
`traits.lastName`  
`traits.lastname`  
`traits.last_name`  
`context.traits.lastName`  
`context.traits.lastname`  
`context.traits.last_name`| `lastName`  
`traits.middleName`  
`traits.middleName`  
`traits.middle_name`  
`context.traits.middleName`  
`context.traits.middleName`  
`context.traits.middle_name`| `middleName`  
`traits.gender`  
`context.traits.gender`| `gender`  
`traits.phone`  
`context.traits.phone`  
`properties.phone`| `phone`  
`context.page.title`  
`properties.title`| `pageTitle`  
`context.page.url`  
`properties.url`| `pageUrl`  
`context.page.path`  
`properties.path`| `pagePath`  
`traits.website`  
`context.traits.website`  
`properties.website`| `website`  
`properties.url`  
`context.page.url`| `GApageUrl`  
`properties.referrer`  
`context.page.referrer`| `GApageRef`  
`properties.title`  
`context.page.title`| `GApageTitle`  
`properties.search`  
`context.page.search`| `GApageSearch`  
`traits.birthday`  
`context.traits.birthday`  
`traits.dateOfBirth`  
`context.traits.dateOfBirth`  
`traits.dateofbirth`  
`context.dateofbirth`  
`traits.dob`  
`context.traits.dob`  
`traits.DOB`  
`context.traits.DOB`| `birthday`  
`traits.state`  
`context.traits.state`| `state`  
`traits.country`  
`context.traits.country`| `country`  
`traits.region`  
`context.traits.region`| `region`  
`traits.address.city`  
`context.traits.address.city`| `city`  
`traits.street`  
`traits.address.street`  
`context.traits.street`  
`context.traits.address.street`| `street`  
`traits.avatar`  
`context.traits.avatar`  
`traits.avatarURL`  
`context.traits.avatarURL`  
`traits.avatar_URL`  
`context.traits.avatar_URL`| `avatar`  
`traits.zip`  
`traits.zipcode`  
`traits.zip_code`  
`traits.zipCode`  
`traits.postalcode`  
`traits.postal_code`  
`traits.postalCode`  
`traits.address.zipcode`  
`traits.address.zip_code`  
`traits.address.zip`  
`traits.address.zipCode`  
`traits.address.postalcode`  
`traits.address.postal_code`  
`traits.address.postalCode`  
`context.traits.zip`  
`context.traits.zipcode`  
`context.traits.zip_code`  
`context.traits.zipCode`  
`context.traits.postalcode`  
`context.traits.postal_code`  
`context.traits.postalCode`  
`context.traits.address.zip`  
`context.traits.address.zipcode`  
`context.traits.address.zip_code`  
`context.traits.address.zipCode`  
`context.traits.address.postalcode`  
`context.traits.address.postal_code`  
`context.traits.address.postalCode`| `zipcode`  
`session_id`  
`context.sessionId`| `sessionId`  
`traits.countryCode`  
`traits.address.countryCode`  
`context.traits.address.countryCode`  
`context.traits.countryCode`| `countryCode`