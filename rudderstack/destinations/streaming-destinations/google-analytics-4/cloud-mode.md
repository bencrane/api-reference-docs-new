# Google Analytics 4 Cloud Mode Integration

Send events to Google Analytics 4 using RudderStack cloud mode.

* * *

  * __15 minute read

  * 


RudderStack lets you send your event data to Google Analytics 4 via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>) by leveraging the [Google Analytics 4 Measurement Protocol](<https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference?client_type=gtag#payload>).

> ![warning](/docs/images/warning.svg)
> 
> Google Analytics 4 **does not officially support a complete server-to-server integration**. RudderStack utilizes the [GA4 Measurement Protocol API](<https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference?client_type=gtag#payload>) for **cloud mode** integration, which **does not currently allow ingestion of UTM parameters** for attribution reporting. This may significantly limit your ability to use certain GA4 reporting features. Refer to the [Google’s documentation](<https://developers.google.com/analytics/devguides/collection/protocol/ga4>) for more information on these limitations.
> 
> **For capturing a fuller, more robust set of attribution data while using Measurement Protocol, RudderStack suggests referencing and setting up a[hybrid mode connection](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-analytics-4/hybrid-mode/>).**

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/ga4>).

## Tagging methods

RudderStack supports both the `gtag` and `firebase` ways for tagging in websites in cloud mode. However, note that:

  * If you use `gtag`, passing the `client_id` parameter is mandatory.
  * If you use `firebase`, passing the `app_instance_id` parameter is mandatory.


Refer to the [Google Analytics 4 Measurement Protocol](<https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference?client_type=gtag#payload>) guide for more information.

The mappings for the above-mentioned mandatory parameters are listed in the following table:

Parameters| Mapping value  
---|---  
`client_id`| GA4 requires it to uniquely identify the user instance of a client. See Mapping `client_id`.  
`app_instance_id`| from `externalId` `ga4AppInstanceId`  
  
#### Mapping `client_id`

RudderStack maps `client_id` from the following fields in the same priority order as listed below:

  * From `externalID`: `ga4ClientId`
  * From `anonymousId`
  * From `rudderId`


#### `externalId`

You can use `externalID` to send a custom `client_id` that is external to RudderStack.

There are certain scenarios where you may want to send a custom `client_id`. For example, if you maintain a user with a certain identifier, then you may prefer to pass it as the custom `client_id` as a part of `externalId`:
    
    
    rudderanalytics.identify(
      "1hKOmRA4GRlm", {
        firstName: "Alex",
        city: "New Orleans",
        country: "Louisiana",
        phone: "+1-202-555-0146",
        email: "alex@example.com",
      } {
        externalId: [{
          id: "4718026.1683606287",
          type: "ga4ClientId",
        }, ],
      }
    );
    

### Supported mappings

The following table lists the mappings for the `gtag` and `firebase` parameters:

Parameters| Mapping| Description  
---|---|---  
`user_id`| `userId``traits.userId``traits.id``context.traits.userId``context.traits.id`| Unique identifier for a user which helps Google Analytics 4 know if two devices/browsers belong to the same user.  
`timestamp_micros`| `originalTimestamp``timestamp`| Timestamp in ISO 8601 format.  
`non_personalized_ads`| `context.device.adTrackingEnabled`| Indicates whether the events should be used for personalized ads. If `context.device.adTrackingEnabled` is set as `true`, `non_personalised_ads` will be set to `false`.  
  
> ![info](/docs/images/info.svg)
> 
> Google Analytics 4 Measurement Protocol only supports timestamps 72 hours into the past and 15 minutes into the future. RudderStack discards any event with a timestamp out of this range.

## Track

> ![warning](/docs/images/warning.svg)
> 
> This destination does not strictly adhere to the [RudderStack Ecommerce Event Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you capture user events along with the properties associated with them.

> ![info](/docs/images/info.svg)
> 
> You can use a `track` call to send any event to Google Analytics 4. However, RudderStack recommends using the `page` call to record page-related information for your website specifically.

You can send all the events mentioned in [GA4 documentation](<https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference/events>) as `track` events.

A sample `track` call using `gtag` is shown below:
    
    
    rudderanalytics.track('Product List Viewed', {
      list_id: "related_products",
      category: "Related_products",
      products: [{
        product_id: "507f1f77bcf86cd799439011",
        name: "Monopoly: 3rd Edition",
        coupon: "SUMMER_FUN",
        category: "Apparel",
        brand: "Google",
        variant: "green",
        price: "19",
        quantity: "2",
        position: "1",
        affiliation: "Google Merchandise Store",
        currency: "USD",
        discount: 2.22,
        item_category2: "Adult",
        item_category3: "Shirts",
        item_category4: "Crew",
        item_category5: "Short sleeve",
        item_list_id: "related_products",
        item_list_name: "Related Products",
        location_id: "L_12345"
      }]
    }, {
        externalId: [{
            type: "ga4ClientId",
            id: "client_id"
        }],
    });
    

A sample `track` call using `firebase` is shown below:
    
    
    rudderanalytics.track('Product List Viewed', {
      list_id: "related_products",
      category: "Related_products",
      products: [{
        product_id: "507f1f77bcf86cd799439011",
        name: "Monopoly: 3rd Edition",
        coupon: "SUMMER_FUN",
        category: "Apparel",
        brand: "Google",
        variant: "green",
        price: "19",
        quantity: "2",
        position: "1",
        affiliation: "Google Merchandise Store",
        currency: "USD",
        discount: 2.22,
        item_category2: "Adult",
        item_category3: "Shirts",
        item_category4: "Crew",
        item_category5: "Short sleeve",
        item_list_id: "related_products",
        item_list_name: "Related Products",
        location_id: "L_12345"
      }]
    }, {
      externalId: [{
        type: "ga4AppInstanceId",
        id: "f0dd99b6f979fb551ce583373900f937"
      }],
    });
    

### Supported mappings

The following table lists the property mappings between RudderStack and Google Analytics 4 for `login` and `sign_up` events:

RudderStack property| Google Analytics 4 property| Default value  
---|---|---  
`traits.method``properties.method`| `method`| -  
`traits.engagementTimeMsec``properties.engagementTimeMsec``context.traits.engagementTimeMsec``traits.engagement_time_msec``properties.engagement_time_msec``context.traits.engagement_time_msec`| `engagement_time_msec`| `1`  
  
The following table lists the property mappings between RudderStack and Google Analytics 4 for `generate_lead` event:

RudderStack property| Google Analytics 4 property| Default value  
---|---|---  
`properties.currency`| `currency`| USD  
`properties.total``properties.price``properties.value``properties.revenue`Required| `value`| -  
`traits.engagementTimeMsec``properties.engagementTimeMsec``context.traits.engagementTimeMsec``traits.engagement_time_msec``properties.engagement_time_msec``context.traits.engagement_time_msec`| `engagement_time_msec`| `1`  
  
## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record your website’s page views with any additional relevant information about the viewed page.

RudderStack maps the `page` call to a `page_view` event by default, and passes it to Google Analytics 4 as a custom event.

As mentioned in the `track` section, the RudderStack cloud mode supports both the `gtag` and `firebase` methods for tagging in websites.

A sample `page` call using `gtag` is shown below:
    
    
    rudderanalytics.page();
    

A sample `page` call using `firebase` is shown below:
    
    
    rudderanalytics.page({}, {
      externalId: [{
        type: "ga4AppInstanceId",
        id: "f0dd99b6f979fb551ce583373900f937"
      }],
    });
    

### Supported mappings

The following table lists the property mappings between RudderStack and Google Analytics 4:

RudderStack property| Google Analytics 4 property  
---|---  
`context.page.referrer`| `page_referrer`  
`context.page.title`| `page_title`  
`context.page.url`| `page_location`  
  
## Group

The [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call lets you link an identified user with a group such as a company, organization, or an account, and record any traits associated with that group, for example, company name, number of employees, etc.

RudderStack maps the `group` call to the `join_group` event by default.

A sample `group` call using `gtag` is shown below:
    
    
    rudderanalytics.group("1hKOmRA4", {
        "custom1": 1234,
        "custom2": "custom2"
    });
    

A sample `group` call using `firebase` is shown below:
    
    
    rudderanalytics.group("1hKOmRA4", {
        "custom1": 1234,
        "custom2": "custom2"
    }, {
        externalId: [{
            type: "ga4AppInstanceId",
            id: "f0dd99b6f979fb551ce583373900f937"
        }],
    });
    

## Ecommerce event tracking

RudderStack supports ecommerce tracking for Google Analytics 4. You can refer to the [Ecommerce Events Specification](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>) for sending events while instrumenting your site with the RudderStack SDK.

### Supported mappings

Event mappings  
RudderStack event| Google Analytics 4 event  
---|---  
Products Searched| `search`  
Product List Viewed| `view_item_list`  
Product Clicked| `select_item`  
Promotion Viewed| `view_promotion`  
Promotion Clicked| `select_promotion`  
Product Viewed| `view_item`  
Product Added| `add_to_cart`  
Product Removed| `remove_from_cart`  
Cart Viewed| `view_cart`  
Product Added to Wishlist| `add_to_wishlist`  
Checkout Started| `begin_checkout`  
Order Completed| `purchase`  
Order Refunded| `refund`  
Product Shared| `share`  
Cart Shared| `share`  
Payment Info Entered| `add_payment_info`  
Checkout Step Completed| `add_shipping_info`  
Property mappings based on specific RudderStack events  
RudderStack event| RudderStack property| Google Analytics 4 property  
---|---|---  
Products Searched| `properties.query`  
Required| `search_term`  
Product List Viewed  
Product Clicked| `properties.list_id`  
`properties.category`| `item_list_id`  
`item_list_name`  
Promotion Viewed  
Promotion Clicked| `properties.creative_name`  
`properties.creative`| `creative_name`  
`properties.creative_slot`  
`properties.position`| `creative_slot`  
`properties.promotion_name`  
`properties.name`| `promotion_name`  
`properties.promotion_id`| `promotion_id`  
Product Viewed  
Product Added to Wishlist| `properties.currency`| `currency`  
`properties.total`  
`properties.price`  
`properties.value`  
`properties.revenue`  
Required (one of the above)| `value`  
Product Added  
Product Removed| `properties.currency`| `currency`  
`properties.total`  
`properties.value`  
`properties.revenue`  
`(properties.price)` X `(properties.quantity)`  
Required (one of the above)| `value`  
Cart Viewed| `properties.currency`| `currency`  
`properties.total`  
`properties.value`  
`properties.revenue`  
Required (one of the above)| `value`  
Checkout Started| `properties.currency`  
`properties.coupon`| `currency`  
`coupon`  
`properties.total`  
`properties.value`  
`properties.revenue`  
Required (one of the above)| `value`  
Order Completed  
Order Refunded| `properties.currency`  
`properties.order_id` Required  
`properties.coupon`  
`properties.shipping`  
`properties.tax`| `currency`  
`transaction_id`  
`coupon`  
`shipping`  
`tax`  
  
**Note** : Make sure to pass `transaction_id` as an alphanumeric value. Otherwise, it may not reflect correctly in your reports.  
`properties.total`  
`properties.value`  
`properties.revenue`  
Required (one of the above)| `value`  
Product Shared| `properties.share_via`  
`properties.content_type`| `method`  
`content_type`  
`properties.item_id`  
`properties.product_id`  
`properties.sku`| `item_id`  
Cart Shared| `properties.share_via`  
`properties.content_type`| `method`  
`content_type`  
`properties.item_id`  
`properties.cart_id`| `item_id`  
Group| `groupId`| `group_id`  
Payment Info Entered| `properties.currency`  
`properties.coupon`  
`properties.payment_method`| `currency`  
`coupon`  
`payment_type`  
`properties.total`  
`properties.value`  
`properties.revenue`  
Required (one of the above)| `value`  
Checkout Step Completed| `properties.currency`| `currency`  
`properties.total`  
`properties.value`  
`properties.revenue`  
Required (one of the above)| `value`  
`properties.coupon`| `coupon`  
`properties.shipping_method`| `shipping_tier`  
  
> ![info](/docs/images/info.svg)
> 
> The default unit for `currency` property is USD.

`products` parameter for RudderStack events  


The following events include the `products` parameter (mapped to the [`items`](<https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference/events#view_item_list>) parameter) which accepts a `products` array:

RudderStack event| Presence of `products` parameter  
---|---  
Product List Viewed| Required  
Cart Viewed| Required  
Checkout Started| Required  
Payment Info entered| Required  
Order Completed| Required  
Order Refunded| Optional  
Checkout Step completed| Required  
View Search Results| Optional  
Promotion Viewed| Required  
Promotion Clicked| Optional  
`products` array mappings  
RudderStack| Google Analytics 4  
---|---  
properties.products.$.product_id  
Required, if name is not present.| `item_id`  
properties.products.$.name  
Required, if product_id is not present.| `item_name`  
properties.products.$.coupon| `coupon`  
properties.products.$.price| `price`  
properties.products.$.position| `index`  
properties.products.$.category| `item_category`  
properties.products.$.brand| `item_brand`  
properties.products.$.variant| `item_variant`  
properties.products.$.quantity| `quantity`  
properties.products.$.affiliation| `affiliation`  
properties.products.$.currency| `currency`  
properties.products.$.discount| `discount`  
properties.products.$.item_category2| `item_category2`  
properties.products.$.item_category3| `item_category3`  
properties.products.$.item_category4| `item_category4`  
properties.products.$.item_category5| `item_category5`  
properties.products.$.item_list_id| `item_list_id`  
properties.products.$.item_list_name| `item_list_name`  
properties.products.$.location_id| `location_id`  
`products` array mappings for **Promotion Viewed** and **Promotion Clicked** events  
RudderStack| Google Analytics 4  
---|---  
properties.products.$.creative_name| `creative_name`  
properties.products.$.creative_slot| `creative_slot`  
properties.products.$.promotion_id| `promotion_id`  
properties.products.$.promotion_name| `promotion_name`  
Root-level property mappings for ecommerce events  


The root-level properties of ecommerce events which do **not** include a `products` array are mapped to the following GA4 [`items`](<https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference/events#view_item_list_item>) array:

RudderStack| Google Analytics 4  
---|---  
`properties.product_id`  
Required, if name is not present.| `item_id`  
`properties.name`  
Required, if product_id is not present.| `item_name`  
`properties.coupon`| `coupon`  
`properties.category`| `item_category`  
`properties.brand`| `item_brand`  
`properties.variant`| `item_variant`  
`properties.price`| `price`  
`properties.quantity`| `quantity`  
`properties.position`| `index`  
`properties.affiliation`| `affiliation`  
`properties.currency`| `currency`  
`properties.discount`| `discount`  
`properties.item_category2`| `item_category2`  
`properties.item_category3`| `item_category3`  
`properties.item_category4`| `item_category4`  
`properties.item_category5`| `item_category5`  
`properties.item_list_id`| `item_list_id`  
`properties.item_list_name`| `item_list_name`  
`properties.location_id`| `location_id`  
  
### Payment Info Entered

The [Payment Info Entered](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#payment-info-entered>) event must include the `products` array apart from the common properties, as shown:
    
    
    rudderanalytics.track(
      "Payment Info Entered", {
        currency: "USD",
        value: "7.77",
        coupon: "SUMMER_FUN",
        payment_method: "Credit Card",
        products: [{
          product_id: "507f1f77bcf86cd799439011",
          name: "Monopoly: 3rd Edition",
          coupon: "SUMMER_FUN",
          category: "Apparel",
          brand: "Google",
          variant: "green",
          price: "19",
          quantity: "2",
          position: "1",
          affiliation: "Google Merchandise Store",
          currency: "USD",
          discount: 2.22,
          item_category2: "Adult",
          item_category3: "Shirts",
          item_category4: "Crew",
          item_category5: "Short sleeve",
          item_list_id: "related_products",
          item_list_name: "Related Products",
          location_id: "L_12345",
        }, ],
      }, {
        externalId: [{
          type: "ga4ClientId",
          id: "client_id",
        }, ],
      }
    );
    

### Promotion Viewed

The [Promotion Viewed](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/promotions/#promotion-viewed>) event must include the `products` array apart from the common properties, as shown:
    
    
    rudderanalytics.track(
      "Promotion Viewed", {
        creative: "Summer Banner",
        position: "featured_app_1",
        promotion_id: "P_12345",
        name: "Summer Sale",
        products: [{
          product_id: "507f1f77bcf86cd799439011",
          name: "Monopoly: 3rd Edition",
          coupon: "SUMMER_FUN",
          category: "Apparel",
          brand: "Google",
          variant: "green",
          price: "19",
          quantity: "2",
          position: "0",
          affiliation: "Google Merchandise Store",
          currency: "USD",
          discount: 2.22,
          item_category2: "Adult",
          item_category3: "Shirts",
          item_category4: "Crew",
          item_category5: "Short sleeve",
          item_list_id: "related_products",
          item_list_name: "Related Products",
          location_id: "L_12345",
          promotion_id: "P_12345",
          promotion_name: "Summer Sale",
          creative_name: "summer_banner2",
          creative_slot: "featured_app_1",
        }, ],
      }, {
        externalId: [{
          type: "ga4ClientId",
          id: "client_id",
        }, ],
      }
    );
    

### Promotion Clicked

The [Promotion Clicked](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/promotions/#promotion-clicked>) event can include the `products` array optionally, apart from the common properties, as shown:
    
    
    rudderanalytics.track(
      "Promotion Clicked", {
        creative: "Summer Banner",
        position: "featured_app_1",
        promotion_id: "P_12345",
        name: "Summer Sale",
        products: [{
          product_id: "507f1f77bcf86cd799439011",
          name: "Monopoly: 3rd Edition",
          coupon: "SUMMER_FUN",
          category: "Apparel",
          brand: "Google",
          variant: "green",
          price: "19",
          quantity: "2",
          position: "0",
          affiliation: "Google Merchandise Store",
          currency: "USD",
          discount: 2.22,
          item_category2: "Adult",
          item_category3: "Shirts",
          item_category4: "Crew",
          item_category5: "Short sleeve",
          item_list_id: "related_products",
          item_list_name: "Related Products",
          location_id: "L_12345",
          promotion_id: "P_12345",
          promotion_name: "Summer Sale",
          creative_name: "summer_banner2",
          creative_slot: "featured_app_1",
        }, ],
      }, {
        externalId: [{
          type: "ga4ClientId",
          id: "client_id",
        }, ],
      }
    );
    

### Checkout Step Completed

The [Checkout Step Completed](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#checkout-step-completed>) event must include the `products` array apart from the common properties, as shown:
    
    
    rudderanalytics.track(
      "Checkout Step Completed", {
        currency: "USD",
        value: "7.77",
        coupon: "SUMMER_FUN",
        shipping_method: "Ground",
        products: [{
          product_id: "507f1f77bcf86cd799439011",
          name: "Monopoly: 3rd Edition",
          coupon: "SUMMER_FUN",
          category: "Apparel",
          brand: "Google",
          variant: "green",
          price: "19",
          quantity: "2",
          position: "1",
          affiliation: "Google Merchandise Store",
          currency: "USD",
          discount: 2.22,
          item_category2: "Adult",
          item_category3: "Shirts",
          item_category4: "Crew",
          item_category5: "Short sleeve",
          item_list_id: "related_products",
          item_list_name: "Related Products",
          location_id: "L_12345",
        }, ],
      }, {
        externalId: [{
          type: "ga4ClientId",
          id: "client_id",
        }, ],
      }
    );
    

## Non ecommerce events tracking

The below table lists the mappings of the non ecommerce `track` events and properties that are passed to Google Analytics 4 events and properties:

Event Mapping| Property Mapping  
---|---  
RudderStack| Google Analytics 4| RudderStack| Google Analytics 4  
`generate_lead`| `generate_lead`| `properties.${currency}`  
`properties.${value}`| `currency`  
`value`  
`login`| `login`| `properties.${method}`| `method`  
`sign_up`| `sign_up`| `properties.${method}`| `method`  
`view_search_results`| `view_search_results`| `properties.search_term`| `search_term`  
`Campaign Details`  
`campaign_details`| `campaign_details`| `context.campaign.id`  
`properties.campaign.id`| `campaign_id`  
`context.campaign.name`  
`properties.campaign.name`| `campaign`  
`context.campaign.source`  
`properties.campaign.source`| `source`  
`context.campaign.medium`  
`properties.campaign.medium`| `medium`  
`context.campaign.term`  
`properties.campaign.term`| `term`  
`context.campaign.content`  
`properties.campaign.content`| `content`  
  
> ![info](/docs/images/info.svg)
> 
> You can pass the custom user properties to any of the events by passing them as `properties.user_properties` or `context.traits`. Refer to the [Google Analytics 4 documentation](<https://developers.google.com/analytics/devguides/collection/protocol/ga4/user-properties?client_type=gtag>) for more information.

## Custom events

You can use [custom events](<https://support.google.com/analytics/answer/12229021?hl=en>) to collect additional information that Google Analytics 4 does not collect automatically.

Follow the below rules while choosing a name for the custom events and parameters:

  * Event names are case-sensitive. For example, `my_event` and `My_Event` are two distinct events.
  * Event names must start with a letter. Only letters, numbers, and underscores are permitted. **Do not** use spaces.
  * Do not use [reserved prefixes and event names](<https://support.google.com/analytics/answer/13316687?sjid=15936425803368383083-AP#zippy=>). The list of such prefixes is mentioned below:
    * _ (underscore)
    * firebase_
    * ga_
    * google_
    * gtag.
  * **Do not** use spaces in event parameter names.


## Custom dimensions and metrics

Before sending events to Google Analytics 4, you must create [custom dimensions and metrics](<https://support.google.com/analytics/answer/10075209>) in your GA4 dashboard and link them to the event properties/parameters.

You can select a parameter from the list of already collected properties or specify the parameter you plan to collect in the future. RudderStack supports sending user properties via `properties.user_properties` and `context.traits`.

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * Custom dimensions can be either event-scoped or user-scoped. However, custom metrics **must** be event-scoped.
>   * Each user property should either be of a number, string, or Boolean data type. This is because GA4 accepts only flat key-value pairs as user properties.
>   * RudderStack drops any user property that is either an object or an array.
> 


## Track active users and sessions

As Google Analytics 4 only reports the users who engage with your website for a non-zero time, RudderStack sets the `engagement_time_msec` parameter to 1, by default. To track engagement time in your events, you can set the `engagement_time_msec` field to a different value.

RudderStack maps the following properties to GA4’s `engagement_time_msec` property:

RudderStack properties| Google Analytics 4 property  
---|---  
`traits.engagementTimeMsec`  
`context.traits.engagementTimeMsec`  
`traits.engagement_time_msec`  
`context.traits.engagement_time_msec`| `engagement_time_msec`  
  
You can use the Google Analytics 4 `session_id` parameter to identify the session associated with a particular event. To know more about sessions in Google Analytics 4, see [Google Analytics 4 help article](<https://support.google.com/analytics/answer/9191807?hl=en#zippy=>).

RudderStack maps the following session properties for the `group` call:

RudderStack properties| Google Analytics 4 property  
---|---  
`traits.sessionId`  
`context.traits.sessionId`  
`traits.session_id`  
`context.traits.session_id`  
`context.sessionId`| `session_id`  
  
RudderStack maps the following session properties for the `track` and `page` calls:

RudderStack properties| Google Analytics 4 property  
---|---  
`properties.sessionId`  
`properties.session_id`  
`context.sessionId`| `session_id`  
  
> ![warning](/docs/images/warning.svg)
> 
> RudderStack automatically collects `engagement_time_msec` and `session_id` when sending events via [device mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-analytics-4/device-mode/>). However, they must be manually passed while sending events via cloud mode.

> ![info](/docs/images/info.svg)
> 
> Server-side session tracking supports only a subset of user dimensions. Google’s Measurement Protocol API does not support the reserved fields like location, demographics, [predefined user dimensions](<https://support.google.com/analytics/answer/9268042?hl=en&ref_topic=11151952>), and device-specific information.

See [Google Analytics 4 documentation](<https://developers.google.com/analytics/devguides/collection/protocol/ga4/sending-events?client_type=firebase#optional_parameters_for_reports>) for more information on the optional reporting parameters.

## Send consent information

RudderStack supports sending consent information to Google Analytics 4 using the Measurement Protocol’s [`consent` object](<https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference?client_type=firebase#payload_consent>). This lets you specify user consent for leveraging their data for advertisements and personalization.

You can specify consent by using the `integrations` object in your event payloads. RudderStack maps the consent values to the GA4 Measurement Protocol consent object as follows:

A sample `track` call with consent information is shown below:
    
    
    rudderanalytics.track('Product List Viewed', {
      list_id: "related_products",
      category: "Related_products",
      products: [{
        product_id: "507f1f77bcf86cd799439011",
        name: "Monopoly: 3rd Edition",
        price: "19",
        quantity: "2"
      }]
    }, {
      integrations: {
        GA4: {
          consents: {
            ad_user_data: "GRANTED",
            ad_personalization: "GRANTED"
          }
        }
      }
    });
    

Note that:

  * The permissible values for `ad_user_data` and `ad_personalization` are `GRANTED` and `DENIED`.
  * If you don’t set the `consents` field in the event payload, RudderStack doesn’t include the consent object in the Measurement Protocol request. In this case, GA4 uses the consent mode settings from other interactions for the client or app instance, provided valid `client_id` and `session_id` values are included.


## View events in GA4

To verify if your events are sent to GA4 successfully, go to **Reports** > **Realtime** in your Google Analytics dashboard or check [Debug View](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-analytics-4/device-mode/#debug-mode>) (only available in device mode). For more information, see [GA4 documentation](<https://support.google.com/analytics/answer/9333790>) for more information.

> ![warning](/docs/images/warning.svg)
> 
> It can take **up to 24 hours** for the data to be processed in GA4 and appear in the other reports.

#### Events not showing in GA4

If your events do not show up in GA4’s **Realtime** view, there could be issues with your implementation. See [GA4 documentation](<https://developers.google.com/analytics/devguides/collection/protocol/ga4/verify-implementation?client_type=gtag#realtime>) for more information on verifying your implementation or checking the realtime view.

You can also see the GA4 [Troubleshooting guide](<https://developers.google.com/analytics/devguides/collection/protocol/ga4/troubleshooting?client_type=gtag>) for steps on identifying and fixing any possible implementation issues.

Also, make sure you are not using a reserved name for your events. This is a common reason for events not showing up in GA4. See FAQ for more information on reserved event names.

> ![warning](/docs/images/warning.svg)
> 
> Not all types of data flow through to GA4’s **Realtime** dashboard. For example, the Measurement Protocol does not support geolocation data and it does not show up in the Realtime dashboard (except for `page` calls sent via hybrid mode).

## FAQ

#### What does the (not set) value mean in reports?

If you see (not set) value in your reports, see [GA4 documentation](<https://support.google.com/analytics/answer/13504892?hl=en#zippy=%2Cin-this-article>) to diagnose the cause first.

RudderStack utilizes the GA4 Measurement Protocol API for cloud mode integration. It does not support ingestion of UTM parameters for attribution reporting currently.

Some other probable reasons could be:

**Reserved event, parameter, and user property names in Google Analytics 4**  
Google Analytics 4 has some reserved event, parameter, and user property names that cannot be used. If passed, they are dropped silently. See [Measurement Protocol (Google Analytics 4)](<https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference?client_type=gtag#reserved_names>) for a complete list of reserved names. Also, note that Google does not accept any event/user property names that include spaces or fields that include null values.

**DebugView**  
[DebugView](<https://support.google.com/analytics/answer/7201382?hl=en>) is only supported in the device mode and is enabled automatically when you set up a device mode GA4 connection. For cloud mode connections, RudderStack sends the events to the [validation server](<https://developers.google.com/analytics/devguides/collection/protocol/ga4/validating-events?client_type=gtag>) and they do not show up in reports.

**Validating events**  
The Google Analytics Measurement Protocol for Google Analytics 4 does not return `HTTP` error codes, even if an event is malformed or missing required parameters. To ensure your events are valid, you should test them against the Measurement Protocol Validation Server before deploying them to production. See [Validating events](<https://developers.google.com/analytics/devguides/collection/protocol/ga4/validating-events?client_type=gtag>) for more information.

#### Why am I seeing inaccurate `transaction_id` values in my Google Analytics reports?

Make sure to pass `transaction_id` as an alphanumeric value. Otherwise, it may not reflect accurately in your reports.

See the [Google Analytics documentation](<https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference/events#purchase>) for more information on the `transaction_id` parameter.

#### How do I obtain `app_instance_id`?

You can retrieve `app_instance_id` through the Firebase SDK depending on the platform where the SDK is installed:

  * [Android: `getAppInstanceId()`](<https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#public-taskstring-getappinstanceid>)
  * [Kotlin: `getAppInstanceId()`](<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#getappinstanceid>)
  * [Swift: `appInstanceID()`](<https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Classes/Analytics#appinstanceid>)
  * [Objective-C: `appInstanceID`](<https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Classes/FIRAnalytics#+appinstanceid>)
  * [C++: `GetAnalyticsInstanceId()`](<https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#getanalyticsinstanceid>)
  * [Unity: `GetAnalyticsInstanceIdAsync()`](<https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#getanalyticsinstanceidasync>)


See [GA4 documentation](<https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference?client_type=firebase#payload_post_body>) for more information.