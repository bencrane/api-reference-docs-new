# Facebook Offline Conversions Deprecated

Send your event data from RudderStack to Facebook Offline Conversions.

* * *

  * __7 minute read

  * 


[Facebook Offline Conversions](<https://www.facebook.com/business/help/1142103235885551?id=565900110447546>) lets you measure your sales in the offline world, resulting through your online Facebook ads. It helps you leverage the offline events data by tracking the in-store purchases, phone orders, bookings, etc.

> ![danger](/docs/images/danger.svg)
> 
> **This destination is deprecated**.
> 
> To send events from RudderStack to Facebook by leveraging the Conversions API, use the [Facebook Conversions](<https://www.rudderstack.com/docs/destinations/streaming-destinations/fb-conversions/>) destination integration instead.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **Facebook Offline Conversions** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
  
## Get started

Once you have confirmed that the source platform supports sending events to Facebook Offline Conversions, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Facebook Offline Conversions**.
  2. Assign a name to your destination and click **Continue**.


## Connection settings

To successfully configure Facebook Offline Conversions as a destination, you will need to configure the following settings:

  * **System User Access Token** : Enter your system user access token from the Facebook Business account. Refer to the FAQ section for more information on obtaining the access token.
  * **Map your events with Facebook Standard Events** : Use this setting to map the standard Facebook events with custom event names. You can map one or more custom events to a standard Facebook event but **not** vice-versa.
  * **Map Facebook Standard Events With Event Set IDs** : Use this setting to map the standard Facebook events (specified in the above setting) to Facebook event set ID’s. You can map one or more standard Facebook events to event set ID’s and vice-versa. Refer to the FAQ section for more information on obtaining the event set ID’s.


> ![info](/docs/images/info.svg)
> 
> If a Facebook standard event is mapped to more than one event set ID, RudderStack will send an event for every event set ID.

  * **Map Categories to Facebook Content Types** : Enter the category value and the corresponding Facebook [`content_type`](<https://developers.facebook.com/docs/meta-pixel/get-started/advantage-catalog-ads#content-type>) which should be mapped to each other. This `content_type` is sent to Facebook every time you send the specified category value via RudderStack. Refer to the Sending custom `content_type` section for more information on sending the customized `content_type` to Facebook.
  * **Value Field Identifier** : Enter the identifier you want to assign to the `value` field in Facebook’s event payload. The default value is set to `properties.value`.
  * **Limited Data Usage** : Enable this setting to let RudderStack take the data processing information from the payload and send it to Facebook.
  * **Enable Hashing** : This setting is enabled by default and hash encodes the user data using `SHA256`. Facebook expects the user data to be hash encoded.


## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to capture user events along with the properties associated with them.

> ![info](/docs/images/info.svg)
> 
> Facebook’s [conversion attribution window](<https://developers.facebook.com/docs/marketing-api/insights#sample>) is 28 days. Hence, it is recommended to send your server-side `track` conversions within 62 days of the occurrence of offline conversions.

The event name sent in the `track` call must be mapped in the **Map Facebook Standard Events With Event Set IDs** RudderStack dashboard setting otherwise, an error is thrown.

A sample `track` call is shown below:
    
    
    rudderanalytics.track({
      userId: 'user@1',
      event: 'Product Added',
      properties: {
        products: [{
          id: 1,
          category: 'Games',
          brand: 'Hasbro',
          price: 18.99,
          quantity: 1,
        }],
        order_id: 'cart1234',
        price: 18.99,
        currency: "USD"
      },
      traits: {
        email: 'alex@example.com',
        phone: '+1-202-555-0146',
        gender: 'male',
        firstName: 'Alex',
        lastName: "Keener",
        address: {
          city: 'New Orleans',
          state: 'Louisiana',
          postalCode: '90009',
          country: 'USA'
        }
      },
      context: {
        "dataProcessingOptions": [
          [
            "LDU"
          ],
          1,
          1000
        ],
      }
    });
    

If your server has access to Facebook’s `leadId` from their [Lead Ads](<https://developers.facebook.com/docs/marketing-api/guides/lead-ads/>) product, you can choose to send it using the integration specific options. The `leadId` is mapped via `externalId`:
    
    
    "externalId": [
      {
      "id": "leadId-value",
      "type": "LeadId"
      }, ]
    

### Property mappings

The following table lists the event property mappings between RudderStack and Facebook Offline Conversions:

RudderStack property| Facebook Offline Conversions property| Notes  
---|---|---  
`userId`  
`traits.userId`  
`traits.id`  
`context.traits.userId`  
`context.traits.id`  
`anonymousId`  
Required| `extern_id`| -  
`originalTimestamp`  
`timestamp`  
Required| `event_time`| Unix timestamp. The default value is the current timestamp.  
`event`  
Required| `event_name`| -  
`properties.currency`  
Required| `currency`| If not provided, the default value is set to `USD`.  
`properties.total`  
`properties.price`  
`properties.value`  
`properties.revenue`  
Required| `value` (currency value)| If not provided, the default value is set to `0`.  
`properties.upload_tag`| `upload_tag`| The default value is set to `RudderStack`.  
`properties.item_number`| `item_number`| -  
`properties.order_id`  
`properties.orderId`| `order_id`| -  
`properties`| `custom_data`| -  
`properties.products`| `contents`| -  
`traits.email`  
`context.traits.email`  
`properties.email`  
`context.externalId.0.id`| `email`| -  
`traits.phone`  
`context.traits.phone`  
`properties.phone`| `phone`| -  
`traits.gender`  
`context.traits.gender`| `gen`| -  
`traits.birthday`  
`context.traits.birthday`  
`traits.dateOfBirth`  
`context.traits.dateOfBirth`  
`traits.dateofbirth`  
`context.dateofbirth`  
`traits.dob`  
`context.traits.dob`  
`traits.DOB`  
`context.traits.DOB`| `doby`| The expected format is `DD, MM, YYYY`. RudderStack extracts the year, month, and day before sending it to Facebook Offline Conversions.  
`traits.firstName`  
`traits.firstname`  
`traits.first_name`  
`context.traits.firstName`  
`context.traits.firstname`  
`context.traits.first_name`| `fn`| -  
`traits.lastName`  
`traits.lastname`  
`traits.last_name`  
`context.traits.lastName`  
`context.traits.lastname`  
`context.traits.last_name`| `ln`| -  
`traits.address.city`  
`context.traits.address.city`| `ct`| -  
`traits.state`  
`context.traits.state`| `st`| -  
`traits.zip`  
`traits.zipcode`  
`traits.zip_code`  
`traits.zipCode`  
`traits.postalcode`  
`traits.postal_code`  
`traits.postalCode`  
`traits.address.zipcode`  
`traits.address.zip_code`| `zip`| -  
`traits.country`  
`context.traits.country`| `country`| -  
`context.device.advertisingId`| `madid`| -  
`context.userAgent`| `client_user_agent`| -  
`traits.action_source`  
`context.traits.action_source`  
`properties.action_source`| `action_source`| -  
`context.page.url`  
`properties.url`| `event_source_url`| -  
`context.fbc`| `fbc`| -  
`context.fbp`| `fbp`| -  
  
Note the following important points while sending event data to Facebook Offline Conversions:

  * At least one [`match_key`](<https://developers.facebook.com/docs/marketing-api/offline-conversions/#:~:text=one%20API%20call.-,Match%20Keys,-match_keys%20is%20a>) is required to send an event successfully. RudderStack uses SHA256 encoding to hash all `match_keys` that include personally identifiable data in compliance with Facebook’s privacy requirements.
  * If you send a `products` array using the `properties` object, RudderStack sends only the `id`, `quantity`, `brand`, `category`, and `price` properties for each product. The reason is that Facebook throws an error on encountering any property apart from these.
  * If you send an event name as **Product List Viewed** , the value of [`content_type`](<https://developers.facebook.com/docs/meta-pixel/get-started/advantage-catalog-ads#content-type>) key is set as `product_group` otherwise, it is set as `product`.
  * RudderStack sends a conversion event as long as it contains a `userId`. However, it is recommended to send as much user data through `context.traits` for better attribution results.
  * You can send either the `firstName` and `lastName` separately or just the `name` property. RudderStack maps it to `fn` and `ln` on its own.


## Sending custom `content_type`

You can either send the custom [`content_type`](<https://developers.facebook.com/docs/meta-pixel/get-started/advantage-catalog-ads#content-type>) by specifying it in the **Map Categories to Facebook Content Types** dashboard setting or via the `integrations` object:
    
    
    "integrations": {
      "FacebookOfflineConversions": {
        "contentType": "sending dedicated content type for this particular payload"
      }
    }
    

The priority order of setting the `content_type` value is as follows:

  1. `content_type` provided in the `integrations` object is given the highest priority.
  2. `content_type` provided in the RudderStack dashboard is given the second highest priority.
  3. If none of the above is provided, the `content_type` is set to `product` by default, except in the following cases:


  * If **Product List Viewed** event is sent:
    * with `products` array, then the `content_type` is set to `product`.
    * without the `products` array, then the `content_type` is set to `product_group`.
  * If **Product Viewed** event is mapped in the RudderStack dashboard, then the `content_type` is set to `product`.
  * If **Product Viewed** event is not mapped in RudderStack dashboard (default mapping is set to **View Content** event) and is sent:
    * with `products` array, then the `content_type` is set to `product`.
    * without the `products` array, then the `content_type` is set to `product_group`.
  * If any other event is mapped to the Facebook standard event **View Content** in the RudderStack dashboard and is sent:
    * with `products` array, then the `content_type` is set to `product`.
    * without the `products` array, then the `content_type` is set to `product_group`.


## FAQ

#### Where can I find the System User Access Token?

  1. Log in to the [Facebook Business](<https://business.facebook.com/>) account.
  2. Go to **Business Settings** > **Users** > **System users**.
  3. Click **Generate New Token** , select your app from the dropdown, and **ads_management** permission.
  4. Click **Generate Token** as shown:

[![Facebook settings](/docs/images/event-stream-destinations/fb-generate-token.webp)](</docs/images/event-stream-destinations/fb-generate-token.webp>)

#### Where can I find the event set ID in Facebook dashboard?

  1. Log in to the [Facebook Business](<https://business.facebook.com/>) account.
  2. Go to **Business Settings** > **Data Sources** > **Offline event sets** and select **Open in Events Manager**. You can see the event set ID as shown:

[![Facebook settings](/docs/images/event-stream-destinations/fb-event-set-id.webp)](</docs/images/event-stream-destinations/fb-event-set-id.webp>)

#### Which permissions are required to upload the offline event data?

Refer to the [Facebook dcoumentation](<https://www.facebook.com/business/help/629677790575687?id=565900110447546>) to know about the detailed permissions required to upload offline event data.