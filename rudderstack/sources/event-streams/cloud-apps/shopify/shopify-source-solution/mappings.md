# Shopify Event and Property Mappings

Event and property mapping details while ingesting data from Shopify.

* * *

  * __4 minute read

  * 


This page contains all the client-side pixel mappings and the webhook topic mappings.

## Event mappings

This section covers the event mappings from Shopify to RudderStack:

### Pixel events (client-side)

Shopify event| RudderStack event  
---|---  
[`cart_viewed`](<https://shopify.dev/docs/api/web-pixels-api/standard-events/cart_viewed>)| [`Cart Viewed`](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#cart-viewed>)  
[`checkout_address_info_submitted`](<https://shopify.dev/docs/api/web-pixels-api/standard-events/checkout_address_info_submitted>)| `Checkout Address Info Submitted`  
[`checkout_contact_info_submitted`](<https://shopify.dev/docs/api/web-pixels-api/standard-events/checkout_contact_info_submitted>)| `Checkout Contact Info Submitted`  
[`checkout_shipping_info_submitted`](<https://shopify.dev/docs/api/web-pixels-api/standard-events/checkout_shipping_info_submitted>)| `Checkout Shipping Info Submitted`  
[`payment_info_submitted`](<https://shopify.dev/docs/api/web-pixels-api/standard-events/payment_info_submitted>)| `Payment Info Submitted`  
[`checkout_started`](<https://shopify.dev/docs/api/web-pixels-api/standard-events/checkout_started>)| [`Checkout Started`](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#checkout-started>)  
[`collection_viewed`](<https://shopify.dev/docs/api/web-pixels-api/standard-events/collection_viewed>)| [`Product List Viewed`](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/browsing/#product-list-viewed>)  
[`page_viewed`](<https://shopify.dev/docs/api/web-pixels-api/standard-events/page_viewed>)| `page()`  
[`product_added_to_cart`](<https://shopify.dev/docs/api/web-pixels-api/standard-events/product_added_to_cart>)| [`Product Added`](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#product-added>)  
`product_removed_from_cart`| [`Product Removed`](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#product-removed>)  
`product_viewed`| [`Product Viewed`](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#product-viewed>)  
`search_submitted`| [`Products Searched`](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/browsing/#products-searched>)  
`checkout_completed`| [`Order Completed`](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#order-completed>)  
  
### Webhook events (server-side)

RudderStack automatically subscribes to the following Shopify webhook topics:

Shopify event| RudderStack event  
---|---  
`CHECKOUTS_CREATE`| [`Checkout Started`](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#checkout-started>)  
`CHECKOUTS_UPDATE`| `Checkout Updated`  
`CHECKOUTS_DELETE`| `Checkouts Delete`  
Custom track event  
`FULFILLMENTS_CREATE`| `Fulfillments Create`  
Custom track event  
`FULFILLMENTS_UPDATE`| `Fulfillments Update`  
Custom track event  
`FULFILLMENT_ORDERS_SPLIT`| `Fulfillment Orders Split`  
Custom track event  
`ORDERS_CREATE`| `Order Created`  
`ORDERS_UPDATED`| [`Order Updated`](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#order-updated>)  
`ORDERS_DELETE`| `Orders Delete`  
Custom track event  
`ORDERS_EDITED`| `Orders Edited`  
Custom track event  
`ORDERS_CANCELLED`| [`Order Cancelled`](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#order-cancelled>)  
`ORDERS_FULFILLED`| `Orders Fulfilled`  
`ORDERS_PAID`| `Orders Paid`  
`ORDERS_PARTIALLY_FULLFILLED`| `Orders Partially Fulfilled`  
`SHIPPING_ADDRESSES_CREATE`| `Shipping Addresses Create`  
Custom track event  
`SHIPPING_ADDRESSES_UPDATE`| `Shipping Addresses Update`  
Custom track event  
  
> ![warning](/docs/images/warning.svg)
> 
> Use Shopify webhook events (`Order Created`, `Orders Paid`, etc.) as the source of truth for order counts and conversions.
> 
> Frontend web pixel events (like `checkout_completed`) are not guaranteed to fire because adblockers can block them or they can be restricted due to user’s cookie consent preferences. As a result, web pixel events may undercount orders. Use them for behavioral analysis only, not for total conversions.
> 
> See the following references for more details:
> 
>   * [Pixel is blocked by ad blockers](<https://community.shopify.dev/t/pixel-is-blocked-by-ad-blockers/26771>)
>   * [Web pixels requesting consent](<https://shopify.dev/docs/apps/build/marketing-analytics/pixels#requesting-consent>)
> 


### How identify calls are triggered

In addition to the above events, RudderStack also triggers an `identify` call for each [Ecommerce Event](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>) to capture the user information from the event payload.

For example, for a `ORDERS_UPDATED` Shopify event, RudderStack triggers an [`Order Updated`](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#order-updated>) event along with an `identify` event containing the user information.

## Property mappings

This section covers the property mappings from Shopify events to the RudderStack events:

### Pixel events (client-side)

This section covers the property mappings for the client-side pixel events.

#### Checkout event mappings

RudderStack property| Shopify property  
---|---  
`order_id`| `inputEvent.data.checkout.order.id`  
`checkout_id`  
`value`| `inputEvent.data.checkout.token`  
`total`| `inputEvent.data.checkout.totalPrice.amount`  
`currency`| `inputEvent.data.checkout.currencyCode`  
`discount`| `inputEvent.data.checkout.discountsAmount.amount`  
`shipping`| `inputEvent.data.checkout.shippingLine.price.amount`  
`revenue`| `inputEvent.data.checkout.subtotalPrice.amount`  
`tax`| `inputEvent.data.checkout.totalTax.amount`  
  
##### Product-level mappings

RudderStack property| Shopify property  
---|---  
`quantity`| `product.quantity`  
`title`| `product.name`  
`image_url`| `variant.image.src`  
`price`| `variant.price.amount`  
`sku`| `variant.sku`  
`product_id`| `variant.product.id`  
`variant`| `variant.product.title`  
`category`| `variant.product.type`  
`url`| `variant.product.url`  
`brand`| `variant.product.vendor`  
  
#### `Product Viewed` event mappings

RudderStack property| Shopify property  
---|---  
`product_id`| `productVariant.product.id`  
`variant`| `productVariant.product.title`  
`brand`| `productVariant.product.vendor`  
`category`| `productVariant.product.type`  
`image_url`| `productVariant.product.image.src`  
`price`| `productVariant.price.amount`  
`currency`| `productVariant.price.currencyCode`  
`url`| `productVariant.product.url`  
`sku`| `productVariant.product.sku`  
`name`| `productVariant.product.title`  
`quantity`| `cartLine.quantity`  
  
#### `Product List Viewed` event mappings

RudderStack property| Shopify property  
---|---  
`image_url`| `image.src`  
`price`| `price.amount`  
`product_id`| `product.id`  
`variant`| `product.title`  
`category`| `product.type`  
`url`| `product.url`  
`brand`| `product.vendor`  
`sku`| `sku`  
`name`| `title`  
  
#### `Cart Viewed` event mappings

RudderStack property| Shopify property  
---|---  
`product_id`| `merchandise.product.id`  
`variant`| `merchandise.product.title`  
`image_url`| `merchandise.image.src`  
`price`| `merchandise.price.amount`  
`category`| `merchandise.product.type`  
`url`| `merchandise.product.url`  
`brand`| `merchandise.product.vendor`  
`sku`| `merchandise.sku`  
`name`| `merchandise.title`  
`quantity`| `quantity`  
  
### Webhook events (server-side)

This section covers the property mappings for the server-side webhook events.

#### Identify traits mapping

RudderStack automatically maps the [`identify` traits](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/#identify-traits>) from the [Standard Event Spec](<https://www.rudderstack.com/docs/event-spec/standard-events/>) to the corresponding Shopify fields.

For example, `userId` is mapped to Shopify’s `id` field, `traits.email` is mapped to `email`, `traits.phone` is mapped to `phone`, and so on.

#### Common mappings for the `products` array

RudderStack property| Shopify property| Notes  
---|---|---  
`product_id`| `product_id`| Automatically typecasted to String to conform with the [RudderStack Ecommerce Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).  
`sku`| `sku`| -  
`title`| `name`| -  
`price`| `price`| Automatically typecasted to Number to conform with the [RudderStack Ecommerce Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).  
`brand`| `vendor`| -  
`quantity`| `quantity`| -  
  
#### Common mappings for each product within the `products` array

RudderStack property| Shopify property| Notes  
---|---|---  
`order_id`| `id`| Automatically typecasted to String to conform with the [RudderStack Ecommerce Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).  
`value`| `total_price`| Automatically typecasted to Number to conform with the [RudderStack Ecommerce Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).  
`tax`| `total_tax`| Automatically typecasted to Number to conform with the [RudderStack Ecommerce Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).  
`currency`| `currency`| -  
  
## Warehouse destinations

While sending events from Shopify to [warehouse destinations](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>), RudderStack creates the columns based on the above property mappings along with a `shopifyDetails` column containing the entire untransformed event payload received received from Shopify.

> ![info](/docs/images/info.svg)
> 
> Shopify sends a lot more properties apart from the ones that RudderStack maps according to the property mappings. Hence, RudderStack sends the `shopifyDetails` to make sure that:
> 
>   * No data is lost.
>   * The warehouse is not bloated by creating a large number of columns corresponding to the additional properties.
> 


RudderStack sends the `shopifyDetails` object as a JSON path within the event’s `integrations` object, as shown:
    
    
    integrations: {
      SHOPIFY: true,
      DATA_WAREHOUSE: {
        options: {
          jsonPaths: [`${event.type}.context.shopifyDetails`],
        },
      },
    },
    

Note that `event.type` varies according to the type of event triggered, for example, `identify`, `track`, or `page`.