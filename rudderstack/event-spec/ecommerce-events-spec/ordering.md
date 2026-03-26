# Ordering

Understand how ecommerce product order events work in RudderStack.

* * *

  * __12 minute read

  * 


These lifecycle events are associated with the key interactions that a customer has with the app or website while placing an order for a product.

## Product Clicked

This event is triggered when a visitor clicks on a product. The following properties are:

**Property Name**| **Type**| **Description**  
---|---|---  
`product_id`| String| Product ID of the product being viewed  
`sku`| String| SKU of the product  
`category`| String| Category of the product  
`name`| String| Name of the product being viewed  
`brand`| String| Name of the brand associated with the product  
`variant`| String| Variant associated with the product  
`price`| Number| Price of the product being viewed  
`quantity`| Number| Quantity of the product  
`coupon`| String| Coupon code associated with a product  
`position`| Number| Position of the product in the product list  
`url`| String| URL of the product page  
`image_url`| String| Image URL of the product  
  
Here is an example of the **Product Clicked** event:
    
    
    rudderanalytics.track("Product Clicked", {
      product_id: "622c6f5d5cf86a4c77358033",
      sku: "8472-998-0112",
      category: "Games",
      name: "Cones of Dunshire",
      brand: "Wyatt Games",
      variant: "expansion pack",
      price: 49.99,
      quantity: 5,
      coupon: "PREORDER15",
      position: 1,
      url: "https://www.website.com/product/path",
      image_url: "https://www.website.com/product/path.webp",
    })
    

## Product Viewed

This event is triggered when a visitor views a product. The following properties are supported:

**Property Name**| **Type**| **Description**  
---|---|---  
`product_id`| String| Product ID of the product being viewed  
`sku`| String| SKU of the product  
`category`| String| Category of the product  
`name`| String| Name of the product being viewed  
`brand`| String| Name of the brand associated with the product  
`variant`| String| Variant associated with the product  
`price`| Number| Price of the product being viewed  
`quantity`| Number| Quantity of the product  
`coupon`| String| Coupon code associated with a product  
`currency`| String| Currency of the transaction  
`position`| Number| Position of the product in the product list  
`url`| String| URL of the product page  
`image_url`| String| Image URL of the product  
  
Here is an example of the **Product Viewed** event:
    
    
    rudderanalytics.track("Product Viewed", {
      product_id: "622c6f5d5cf86a4c77358033",
      sku: "8472-998-0112",
      category: "Games",
      name: "Cones of Dunshire",
      brand: "Wyatt Games",
      variant: "expansion pack",
      price: 49.99,
      quantity: 5,
      coupon: "PREORDER15",
      currency: "USD",
      position: 1,
      url: "https://www.website.com/product/path",
      image_url: "https://www.website.com/product/path.webp",
    })
    

## Product Added

This event is triggered when a visitor/customer adds a product to their shopping cart. The following properties are supported by this event:

**Property Name**| **Type**| **Description**  
---|---|---  
`cart_id`| String| Cart ID  
`product_id`| String| ID of the product being viewed  
`sku`| String| SKU of the product being viewed  
`category`| String| Category of the product being viewed  
`name`| String| Name of the product being viewed  
`brand`| String| Name of the brand associated with the product  
`variant`| String| Variant associated with the product  
`price`| Number| Price of the product being viewed  
`quantity`| Number| Quantity of the product  
`coupon`| String| Coupon code associated with the product  
`position`| Number| Position of the product in the product list  
`url`| String| URL of the product page  
`image_url`| String| Image URL of the product  
  
An example of the **Product Added** event is as shown:
    
    
    rudderanalytics.track("Product Added", {
      product_id: "622c6f5d5cf86a4c77358033",
      sku: "8472-998-0112",
      category: "Games",
      name: "Cones of Dunshire",
      brand: "Wyatt Games",
      variant: "expansion pack",
      price: 49.99,
      quantity: 5,
      coupon: "PREORDER15",
      position: 1,
      url: "https://www.website.com/product/path",
      image_url: "https://www.website.com/product/path.webp",
    })
    

## Product Removed

This event is triggered when a product is removed from the shopping cart by the customer. The following properties are supported:

**Property Name**| **Type**| **Description**  
---|---|---  
`cart_id`| String| Cart ID  
`product_id`| String| Product ID of the product being viewed  
`sku`| String| SKU of the product being viewed  
`category`| String| Category of the product being viewed  
`name`| String| Name of the product being viewed  
`brand`| String| Name of the brand associated with the product  
`variant`| String| Variant associated with the product  
`price`| Number| Price of the product being viewed  
`quantity`| Number| Quantity of the product  
`coupon`| String| Coupon code associated with a product  
`position`| Number| Position of the product in the product list  
`url`| String| URL of the product page  
`image_url`| String| Image URL of the product  
  
Here is an example of the **Product Removed** event:
    
    
    rudderanalytics.track("Product Removed", {
      product_id: "622c6f5d5cf86a4c77358033",
      sku: "8472-998-0112",
      category: "Games",
      name: "Cones of Dunshire",
      brand: "Wyatt Games",
      variant: "expansion pack",
      price: 49.99,
      quantity: 5,
      coupon: "PREORDER15",
      position: 1,
      url: "https://www.website.com/product/path",
      image_url: "https://www.website.com/product/path.webp",
    })
    

## Cart Viewed

This event is triggered whenever a visitor or customer views their shopping cart. The following properties are supported by this event:

**Property Name**| **Type**| **Description**  
---|---|---  
`cart_id`| String| Cart ID  
`products`| Array| List of products displayed in the product list  
`products.$.product_id`| String| Product ID displayed on the list  
`products.$.sku`| String| SKU of the product being viewed  
`products.$.category`| String| Category of the product being viewed  
`products.$.name`| String| Name of the product being viewed  
`products.$.brand`| String| Name of the brand associated with the product  
`products.$.variant`| String| Variant associated with the product  
`products.$.price`| Number| Price of the product being viewed  
`products.$.quantity`| Number| Quantity of the product  
`products.$.coupon`| String| Coupon code associated with a product  
`products.$.position`| Number| Position of the product in the product list  
`products.$.url`| String| URL of the product page  
`products.$.image_url`| String| Image URL of the product  
  
Here is an example of the **Cart Viewed** event:
    
    
    rudderanalytics.track("Cart Viewed", {
      cart_id: "6b2c6f5aecf86a4ae77358ae3",
      products: [
        {
          product_id: "622c6f5d5cf86a4c77358033",
          sku: "8472-998-0112",
          name: "Cones of Dunshire",
          price: 49.99,
          position: 5,
          category: "Games",
          url: "https://www.website.com/product/path",
          image_url: "https://www.website.com/product/path.jpg",
        },
        {
          product_id: "577c6f5d5cf86a4c7735ba03",
          sku: "3309-483-2201",
          name: "Five Crowns",
          price: 5.99,
          position: 2,
          category: "Games",
        },
      ],
    })
    

## Checkout Started

This event is triggered when an order or transaction is initiated. The following properties are supported:

**Property Name**| **Type**| **Description**  
---|---|---  
`order_id`| String| Order ID or transaction ID, whichever is applicable  
`affiliation`| String| Store or affiliation details from where the transaction occured  
`value`| Number| Revenue with discount and coupons factored in  
`revenue`| Number| Revenue associated with the transaction, excluding the shipping and tax details  
`shipping`| Number| Shipping cost associated with the order or transaction  
`tax`| Number| Total tax associated with the order or the transaction  
`discount`| Number| Total discount associated with the transaction  
`coupon`| String| Coupon redeemed with the transaction  
`currency`| String| Currency code associated with an order or transaction  
`products`| Array| List of products in the order or transaction  
`products.$.product_id`| String| Product ID  
`products.$.sku`| String| SKU of the product being viewed  
`products.$.category`| String| Category of the product being viewed  
`products.$.name`| String| Mame of the product being viewed  
`products.$.brand`| String| Name of the brand associated with the product  
`products.$.variant`| String| Variant associated with the product  
`products.$.price`| Number| Price of the product being viewed  
`products.$.quantity`| Number| Quantity of the product  
`products.$.coupon`| String| Coupon code associated with a product  
`products.$.position`| Number| Position of the product in the product list  
`products.$.url`| String| URL of the product page  
`products.$.image_url`| String| Image URL of the product  
  
> ![warning](/docs/images/warning.svg)
> 
> RudderStack’s SDKs do not calculate the value for any of the supported properties (e.g., `revenue`, `value`, `total`, `subtotal`). You must provide these values when triggering the `track` call. Also, RudderStack maps the values associated with these fields to the destination fields where send the data. Therefore, it is helpful to understand how these fields are defined in a specific destination.

Here is an example of the **Checkout Started** event:
    
    
    rudderanalytics.track("Checkout Started", {
      order_id: "40684e8f0eaf000000000000",
      affiliation: "Vandelay Games",
      value: 52,
      revenue: 50.0,
      shipping: 4,
      tax: 3,
      discount: 5,
      coupon: "NEWCUST5",
      currency: "USD",
      products: [
        {
          product_id: "622c6f5d5cf86a4c77358033",
          sku: "8472-998-0112",
          name: "Cones of Dunshire",
          price: 40,
          position: 1,
          category: "Games",
          url: "https://www.website.com/product/path",
          image_url: "https://www.website.com/product/path.jpg",
        },
        {
          product_id: "577c6f5d5cf86a4c7735ba03",
          sku: "3309-483-2201",
          name: "Five Crowns",
          price: 5,
          position: 2,
          category: "Games",
        },
      ],
    })
    

## Checkout Step Viewed

This event is triggered when a checkout step is viewed. The following properties are supported:

**Property Name**| **Type**| **Description**  
---|---|---  
`checkout_id`| String| Checkout transaction ID  
`step`| Number| Checkout process step number  
`shipping_method`| String| Chosen shipping method  
`payment_method`| String| Payment method  
  
Here is an example of the **Checkout Step Viewed** event:
    
    
    rudderanalytics.track("Checkout Step Viewed", {
      checkout_id: "70324a1f0eaf000000000000",
      step: 1,
      shipping_method: "UPS",
      payment_method: "Mastercard",
    })
    

## Checkout Step Completed

This event is triggered when a checkout step is completed. The following properties are supported:

**Property Name**| **Type**| **Description**  
---|---|---  
`checkout_id`| String| Checkout transaction ID  
`step`| Number| Checkout process step number  
`shipping_method`| String| Chosen shipping method  
`payment_method`| String| Payment method  
  
An example of the **Checkout Step Completed** event is as shown:
    
    
    rudderanalytics.track("Checkout Step Completed", {
      checkout_id: "70324a1f0eaf000000000000",
      step: 1,
      shipping_method: "UPS",
      payment_method: "Mastercard",
    })
    

> ![warning](/docs/images/warning.svg)
> 
> For the Google Analytics 4 destination, you must include the `products` parameter in the [Checkout Step Completed](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-analytics-4/cloud-mode/#checkout-step-completed>) event to send it successfully.

## Payment Info Entered

This event is triggered when payment information is successfully entered. The following properties are supported:

**Property Name**| **Type**| **Description**  
---|---|---  
`checkout_id`| String| Checkout transaction ID  
`order_id`| String| Order ID, optionsal  
`step`| Number| Checkout process step number  
`shipping_method`| String| Chosen shipping method  
`payment_method`| String| Payment method  
  
Here is an example of the **Payment Info Entered** event:
    
    
    rudderanalytics.track("Payment Info Entered", {
      checkout_id: "70324a1f0eaf000000000000",
      order_id: "40684e8f0eaf000000000000",
    })
    

> ![warning](/docs/images/warning.svg)
> 
> For the Google Analytics 4 destination, you must include the `products` parameter in the [Payment Info Entered](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-analytics-4/cloud-mode/#payment-info-entered>) event to send it successfully.

## Order Updated

This event is triggered when an order or transaction is updated. The following properties are supported:

**Property Name**| **Type**| **Description**  
---|---|---  
`order_id`| String| Order ID or transaction ID, whichever is applicable  
`affiliation`| String| Store or affiliation details from where the transaction was started  
`total`| Number| Revenue with the discount and coupons factored in  
`revenue`| Number| Revenue associated with the transaction, excluding the shipping and tax details  
`shipping`| Number| Shipping cost associated with the order or transaction  
`tax`| Number| Total tax associated with the order or the transaction  
`discount`| Number| Total discount associated with the transaction  
`coupon`| String| Coupon redeemed with the transaction  
`currency`| String| Currency code associated with an order or transaction  
`products`| Array| List of products in the order or transaction  
`products.$.product_id`| String| Product ID displayed on the list  
`products.$.sku`| String| SKU of the product being viewed  
`products.$.category`| String| Category of the product being viewed  
`products.$.name`| String| Name of the product being viewed  
`products.$.brand`| String| Name of the brand associated with the product  
`products.$.variant`| String| Variant associated with the product  
`products.$.price`| Number| Price of the product being viewed  
`products.$.quantity`| Number| Quantity of the product  
`products.$.coupon`| String| Coupon code associated with a product  
`products.$.position`| Number| position of the product in the product list  
`products.$.url`| String| URL of the product page  
`products.$.image_url`| String| Image URL of the product  
  
An example of the **Order Updated** event is as shown:
    
    
    rudderanalytics.track("Order Updated", {
      order_id: "40684e8f0eaf000000000000",
      affiliation: "Vandelay Games",
      total: 52,
      revenue: 50.0,
      shipping: 4,
      tax: 3,
      discount: 5,
      coupon: "NEWCUST5",
      currency: "USD",
      products: [
        {
          product_id: "622c6f5d5cf86a4c77358033",
          sku: "8472-998-0112",
          name: "Cones of Dunshire",
          price: 40,
          position: 1,
          category: "Games",
          url: "https://www.website.com/product/path",
          image_url: "https://www.website.com/product/path.jpg",
        },
        {
          product_id: "577c6f5d5cf86a4c7735ba03",
          sku: "3309-483-2201",
          name: "Five Crowns",
          price: 5,
          position: 2,
          category: "Games",
        },
      ],
    })
    

## Order Completed

This event is triggered when an order is completed successfully. The following properties are supported:

**Property Name**| **Type**| **Description**  
---|---|---  
`checkout_id`| String| Checkout ID  
`order_id`| String| Order ID or transaction ID, whichever is applicable  
`affiliation`| String| Store or affiliation details from where the transaction was started  
`subtotal`| Number| Order total after discounts but not including the taxes and shipping charges  
`total`| Number| Revenue with the discount and coupons factored in  
`revenue`| Number| Revenue associated with the transaction, excluding the shipping and tax details  
`shipping`| Number| Shipping cost associated with the order or transaction  
`tax`| Number| Total tax associated with the order or the transaction  
`discount`| Number| Total discount associated with the transaction  
`coupon`| String| Coupon redeemed with the transaction  
`currency`| String| Currency code associated with an order or transaction  
`products`| Array| List of products in the order or transaction  
`products.$.product_id`| String| Product ID displayed on the list  
`products.$.sku`| String| SKU of the product being viewed  
`products.$.category`| String| Category of the product being viewed  
`products.$.name`| String| Name of the product being viewed  
`products.$.brand`| String| Name of the brand associated with the product  
`products.$.variant`| String| Variant associated with the product  
`products.$.price`| Number| Price of the product being viewed  
`products.$.quantity`| Number| Quantity of the product  
`products.$.coupon`| String| Coupon code associated with a product  
`products.$.position`| Number| Position of the product in the product list  
`products.$.url`| String| URL of the product page  
`products.$.image_url`| String| Image URL of the product  
  
> ![warning](/docs/images/warning.svg)
> 
> RudderStack’s SDKs do not calculate the value for any of the properties (e.g., `revenue`, `value`, `total`, `subtotal`). You must provide these values when triggering the `track` call. Also, RudderStack maps the values associated with these fields to the destination fields where you want to send the data. Therefore, it is helpful to understand how these fields are defined in a specific destination.

Here is an example of the **Order Completed** event:
    
    
    rudderanalytics.track("Order Completed", {
      checkout_id: "70324a1f0eaf000000000000",
      order_id: "40684e8f0eaf000000000000",
      affiliation: "Vandelay Games",
      total: 52.0,
      subtotal: 45.0,
      revenue: 50.0,
      shipping: 4.0,
      tax: 3.0,
      discount: 5.0,
      coupon: "NEWCUST5",
      currency: "USD",
      products: [
        {
          product_id: "622c6f5d5cf86a4c77358033",
          sku: "8472-998-0112",
          name: "Cones of Dunshire",
          price: 40,
          position: 1,
          category: "Games",
          url: "https://www.website.com/product/path",
          image_url: "https://www.website.com/product/path.jpg",
        },
        {
          product_id: "577c6f5d5cf86a4c7735ba03",
          sku: "3309-483-2201",
          name: "Five Crowns",
          price: 5,
          position: 2,
          category: "Games",
        },
      ],
    })
    

## Order Refunded

This event is triggered when an order is refunded. You must include all items in the cart as **Order Refunded** event properties, with the same properties as the **Order Completed** event.

The following properties are supported:

**Property Name**| **Type**| **Description**  
---|---|---  
`order_id`| String| Order or transaction ID  
  
Here is an example of the **Order Refunded** event:
    
    
    rudderanalytics.track("Order Refunded", {
      order_id: "40684e8f0eaf000000000000",
      total: 52,
      currency: "USD",
      products: [
        {
          product_id: "622c6f5d5cf86a4c77358033",
          sku: "8472-998-0112",
          name: "Cones of Dunshire",
          price: 40,
          position: 1,
          category: "Games",
          url: "https://www.website.com/product/path",
          image_url: "https://www.website.com/product/path.jpg",
        },
        {
          product_id: "577c6f5d5cf86a4c7735ba03",
          sku: "3309-483-2201",
          name: "Five Crowns",
          price: 5,
          position: 2,
          category: "Games",
        },
      ],
    })
    

## Order Cancelled

This event is triggered when an order is canceled. The following properties are supported:

**Property Name**| **Type**| **Description**  
---|---|---  
`order_id`| String| Order ID or transaction ID, whichever is applicable  
`affiliation`| String| Store or affiliation details from where the transaction was started  
`total`| Number| Revenue with the discount and coupons factored in  
`revenue`| Number| Revenue associated with the transaction, excluding the shipping and tax details  
`shipping`| Number| Shipping cost associated with the order or transaction  
`tax`| Number| Total tax associated with the order or the transaction  
`discount`| Number| Total discount associated with the transaction  
`coupon`| String| Coupon which can be redeemed with the transaction  
`currency`| String| Currency code associated with an order or transaction  
`products`| Array| List of products in the order or transaction  
`products.$.product_id`| String| Product ID displayed on the list  
`products.$.sku`| String| SKU of the product being viewed  
`products.$.category`| String| Category of the product being viewed  
`products.$.name`| String| Name of the product being viewed  
`products.$.brand`| String| Name of the brand associated with the product  
`products.$.variant`| String| Variant associated with the product  
`products.$.price`| Number| Price of the product being viewed  
`products.$.quantity`| Number| Quantity of the product  
`products.$.coupon`| String| Coupon code associated with a product  
`products.$.position`| Number| Position of the product in the product list  
`products.$.url`| String| URL of the product page  
`products.$.image_url`| String| Image URL of the product  
  
> ![warning](/docs/images/warning.svg)
> 
> RudderStack’s SDKs do not calculate the value for any of the properties (e.g., `revenue`, `value`, `total`, `subtotal`). You must provide these values when triggering the `track` call. Also, RudderStack maps the values associated with these fields to the destination fields where you want to send the data. Therefore, it is helpful to understand how these fields are defined in a specific destination.

Here is an example of the **Order Cancelled** event:
    
    
    rudderanalytics.track("Order Cancelled", {
      order_id: "40684e8f0eaf000000000000",
      affiliation: "Vandelay Games",
      total: 52,
      revenue: 50.0,
      shipping: 4,
      tax: 3,
      discount: 5,
      coupon: "NEWCUST5",
      currency: "USD",
      products: [
        {
          product_id: "622c6f5d5cf86a4c77358033",
          sku: "8472-998-0112",
          name: "Cones of Dunshire",
          price: 40,
          position: 1,
          category: "Games",
          url: "https://www.website.com/product/path",
          image_url: "https://www.website.com/product/path.jpg",
        },
        {
          product_id: "577c6f5d5cf86a4c7735ba03",
          sku: "3309-483-2201",
          name: "Five Crowns",
          price: 5,
          position: 2,
          category: "Games",
        },
      ],
    })