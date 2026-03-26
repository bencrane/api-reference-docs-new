# Ometria

Send your event data from RudderStack to Ometria.

* * *

  * __7 minute read

  * 


[Ometria](<https://ometria.com/>) is a customer data and marketing platform. It leverages AI-powered insights and cross-channel marketing to help you create personalized experiences for your customers throughout their product journey.

RudderStack supports Ometria as a destination to which you can seamlessly send your customer data.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **Ometria** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
  
## Get started

Once you have confirmed that your source platform supports sending events to Ometria, follow these steps:

  * From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. From the list of destinations, select **Ometria**.
  * Assign a name to the destination and click **Next**. You should then see the following screen:


[![Ometria](/docs/images/Ometria.webp)](</docs/images/Ometria.webp>)Ometria

### Connection Settings

This section details the connection settings required to configure Ometria as a destination in RudderStack.

  * Enter your Ometria **API Token**.


> ![info](/docs/images/info.svg)
> 
> To get the Ometria API token, go to your your Ometria dashboard and navigate to **Settings** \- **API Keys**. Then, click **New API Key**.

  * Under **Contact Settings** , you can choose the **Marketing Optin** status from the dropdown list. By default, it is set to **Explicitly Opted Out**. The different options are:
    * **Explicitly Opted In** : The customer is eligible for marketing
    * **Explicitly Opted Out** : The customer is not eligible for marketing
    * **Not Specified** : No option is specified


> ![info](/docs/images/info.svg)
> 
> You can also pass this value in the `identify` call - refer to the **Identify** section below for more details. Note that the value set via the `identify` call will have a higher precedence.

  * Under **SMS Channel Settings** , you can enable **Allow Marketing**. This setting determines whether the contact is opted in or out for SMS marketing. By default, it is **disabled**.
  * **Allow Transactional** : Enabling or disabling this setting determines if the contact is opted in or out for transactional SMSes. By default, it is **disabled**.


> ![info](/docs/images/info.svg)
> 
> You can additionally set the values for **Allow Marketing** and **Allow Transactional** via the `identify` call - refer to the **Identify** section below for more details. Note that the value set via the `identify` call will have a higher precedence.

  * Finally, click **Next**. Ometria will now be enabled as a destination in RudderStack.


## Identify

The `identify` call lets you add a new contact or update an already existing contact in Ometria.

> ![warning](/docs/images/warning.svg)
> 
> Note that `listingId` and `email` fields are the mandatory fields for the `identify` call.

You can set the values for the **Marketing Optin** , **Allow Marketing** , and **Allow Transactional** fields from RudderStack dashboard. You can also send these values using an `integrations` object in the `identify` event payload, **which will have higher precedence**. The SMS channel fields `dt_updated_marketing` and `dt_updated_transactional` can also be passed using this object.

The `listingId` is the ID specific to a contact in a particular Ometria collection. Note that the `listingId` specified in the `integrations` object will have a higher precedence than the one present in the traits.

A sample `identify` call is as shown:
    
    
    rudderanalytics.identify(
      "userId",
      {
        listingId: "listingId123",
        email: "sampleuser@testmail.com",
        firstName: "Demo",
        lastName: "Example",
        phoneNumber: "+123451212260",
        custom_fields: {
          field1: "val1",
        }
      },
      {
        integrations: {
          Ometria: {
            marketingOptin: "EXPLICITLY_OPTEDIN",
            allow_marketing: true,
            allow_transactional: true,
          }
        }
      }
    );
    

A few things to keep in mind while making the `identify` call:

  * The `phoneNumber` field must follow the [E.164](<https://en.wikipedia.org/wiki/E.164>) format. Otherwise, it will be set to `null`.
  * The `custom_fields` are mapped to the `properties` and will be the used in the `track` call too.
  * If `custom_fields` is not provided, then RudderStack will create that object with extra fields. Note that these fields must be different from the ones mentioned in the mapping list mentioned in the **Identify Mapping** section below, i.e, the non-default fields.
  * Inside the `integrations` object, you can additionally send two timestamps - `dt_updated_marketing` and `dt_updated_transactional`. These timestamps must follow the [ISO-8601](<https://en.wikipedia.org/wiki/ISO_8601>) format.


### Identify Mapping

The following table includes all `identify` fields with their relative mapping to the Ometria fields:

**RudderStack Field**| **Ometria Field**  
---|---  
`userId` / `anonymousId`| `customer_id`  
`email`| `email`  
`listingId`| `id`  
`firstName`/`first_name`/`firstname`| `firstname`  
`middleName`/ `middle_name` / `middlename`| `middlename`  
`lastName`/`last_name`/`lastname`| `lastname`  
`phoneNumber`| `phone_number`  
`collection`| `@collection`  
`prefix`| `prefix`  
`dateOfBirth`| `date_of_birth`  
`countryId`| `country_id`  
`timezone`| `timezone`  
`timestampAcquired`| `timestamp_acquired`  
`timestampSubscribed`| `timestamp_subscribed`  
`timestampUnsubscribed`| `timestamp_unsubscribed`  
`storeIds`| `store_ids`  
`gender`| `gender`  
`removeFromLists`| `@remove_from_lists`  
`addToLists`| `@add_to_lists`  
`custom_fields`| `properties`  
`forceOptin`| `@force_optin`  
`merge`| `@merge`  
  
> ![info](/docs/images/info.svg)
> 
> In addition to the above fields, the customer name can also be sent using the `name` field. If the name consists of two words, then `firstname` and `lastname` will be automatically set.

## Track

The `track` call lets you send custom events to Ometria. Note that `track` also supports ecommerce events and sends them using the **Ometria Order Object**.

> ![warning](/docs/images/warning.svg)
> 
> Note that `userId` and `email` are the mandatory fields for the `track` call. `event_id` is required for custom events. If not provided, RudderStack will populate the field with `messageId`.

A sample `track` call for a custom event is as shown:
    
    
    rudderanalytics.track("Sample Event", {
      event_id: "sample123",
      timestamp: "2017-05-01T14:00:00Z",
      profile_id: "sample",
      custom_fields: {
        field1: "val1",
      },
    });
    

A few things to note:

  * The event name must be provided in the `track` call.
  * The `custom_fields` property is mapped to the `properties` object in Ometria. If it is not provided, the non-default Ometria fields will be taken as custom fields.
  * The `timestamp` field follows the [ISO-8601](<https://en.wikipedia.org/wiki/ISO_8601>) format. If it is not specified in the correct format, the call will be dropped - i.e., not be sent to Ometria.


### Ometria Custom Event

The following table includes all RudderStack fields set as custom events in the `track` call, with their relative mapping to the Ometria fields:

**RudderStack Field**| **Ometria Field**  
---|---  
`event_id`| `id`  
`timestamp`| `timestamp`  
`custom_fields`| `properties`  
`profile_id`| `profile_id`  
`email`| `identity_email`  
`userId / anonymousId`| `identity_account_id`  
  
### Ecommerce Events

> ![warning](/docs/images/warning.svg)
> 
> This destination does not strictly adhere to the [RudderStack Ecommerce Event Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).

The `track` call also lets you record order-related information like `order_id`, `grandtotal`, `timestamp`, `currency`, etc.

RudderStack will create a `customer` object with `userId`, `email`, `firstname` and `lastname` from `context.traits`.

> ![warning](/docs/images/warning.svg)
> 
> Note that `order_id`, `timestamp`, `grand_total` and `currency` are the mandatory fields for the `orders` event, while `userId` and `email` are required for `customer` object. You can pass `email` either via the `identify` call or the `track` call’s properties.

The supported `order` ecommerce events are as listed below:

  * `order completed` / `complete`/ `order complete`
  * `order shipped` / `shipped`
  * `order pending` / `pending`


A sample `track` call for an ecommerce order event is as shown:
    
    
    rudderanalytics.track("order completed", {
      order_id: "order1",
      timestamp: "2017-05-01T14:00:00Z",
      currency: "usd",
      grand_total: 1,
      field1: "val1",
      products: [
        {
          product_id: "prod123",
          quantity: 4,
          subtotal: 10,
          variant_options:[
            {
              type: "size",
              id: "newid",
              label: "5"
            }
          ]
        }
      ]
    });
    

A few things to note:

  * Ometria requires the `currency` field to follow the [ISO 4217](<https://en.wikipedia.org/wiki/ISO_4217>) format. If it is invalid, the event will be **dropped**.
  * If `custom_fields` is not provided, the non-default fields are taken as custom fields. In the above example, `field1` will be mapped as a `custom_fields`.
  * The `products` field is **not mandatory**. However, if provided, each object should contain `product_id`, `quantity`, and either `subtotal` or `unit_price`. If either of these fields are absent, then that object will be dropped and the `track` call will be made.
  * RudderStack will set the `status` field according to the event name. For instance, if event name is `order pending` status will be set to `pending`.
  * The field `is_valid` is always set to `true`. For more information on how to use this field, refer to this [example](<https://docs.ometria.com/recipes/how-to-process-a-full-refund>).


### Track Orders Mapping

The following table includes all fields in `track` call for ecommerce orders, with their relative mapping to the Ometria fields:

**RudderStack Field**| **Ometria Field**  
---|---  
`order_id`| `id`  
`timestamp`| `timestamp`  
`grand_total`| `grand_total`  
`subtotal`| `subtotal`  
`discount`| `discount`  
`shipping`| `shipping`  
`tax`| `tax`  
`currency`| `currency`  
`web_id`| `web_id`  
`ip_address`| `ip_address`  
`channel`| `channel`  
`store`| `store`  
`payment_method`| `payment_method`  
`shipping_method`| `shipping_method`  
`shipping_address`| `shipping_address`  
`billing_address`| `billing_address`  
`coupon_code`| `coupon_code`  
`custom_fields`| `properties`  
**`products`**| `lineitems`  
  
> ![info](/docs/images/info.svg)
> 
> `shipping_address` and `billing_address` should be an object.

Note that **`products`** is an array of objects. Every object in this array can contain the following fields:

**RudderStack Field**| **Ometria Field**  
---|---  
`product_id`| `product_id`  
`variant_id`| `variant_id`  
`quantity`| `quantity`  
`sku`| `sku`  
`unit_price`| `unit_price`  
`quantity_refunded`| `quantity_refunded`  
`refunded`| `refunded`  
`subtotal`| `subtotal`  
`tax`| `tax`  
`total`| `total`  
`discount`| `discount`  
`is_on_sale`| `is_on_sale`  
`totals`| `totals`  
`properties`| `properties`  
**`variant_options`**| **`variant_options`**  
  
Note that **`variant_options`** listed above is an array of objects. It is not a mandatory field. However, if provided, each object in this array **must** contain the following fields:

**RudderStack Field**| **Ometria Field**  
---|---  
`id`| `id`  
`type`| `type`  
`label`| `label`  
  
## FAQ

#### How do I get the Ometria API Key?

To get the Ometria API token, go to your your Ometria dashboard and navigate to **Settings** \- **API Keys**. Then, click **New API Key**.