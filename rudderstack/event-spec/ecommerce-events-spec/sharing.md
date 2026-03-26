# Sharing

Understand how ecommerce sharing events work in RudderStack.

* * *

  * __2 minute read

  * 


Product sharing events allow customers to share interesting products to their friends or colleagues on various social media platforms.

## Product Shared

This event is triggered when a customer shares a product. The following properties are supported:

**Property Name**| **Type**| **Description of the Property**  
---|---|---  
`share_via`| String| Sharing method  
`share_message`| String| Message sent by the customer  
`recipient`| String| Sharing recipient  
`product_id`| String| Product ID of the product  
`sku`| String| SKU of the product  
`category`| String| Category of the product  
`name`| String| Name of the product  
`brand`| String| Product brand  
`variant`| String| Product variant  
`price`| Number| Price of the product (in USD)  
`url`| String| URL of the product’s page  
`image_url`| String| Image URL of the product  
  
Here is an example of the **Product Shared** event:
    
    
    rudderanalytics.track("Product Shared", {
      share_via: "email",
      share_message: "Check out this great game!",
      recipient: "buddy@example.com",
      product_id: "622c6f5d5cf86a4c77358033",
      sku: "8472-998-0112",
      category: "Games",
      name: "Cones of Dunshire",
      brand: "Wyatt Games",
      variant: "expansion pack",
      price: 49.99,
      url: "https://www.myecommercewebsite.com/product/prod",
      image_url: "https://www.myecommercewebsite.com/product/prod.jpg",
    })
    

## Cart Shared

This event is triggered when a customer shares a shopping cart. The following properties are supported:

**Property Name**| **Type**| **Description of the Property**  
---|---|---  
`share_via`| String| Sharing method  
`share_message`| String| Message sent by the customer  
`recipient`| String| Sharing recipient  
`cart_id`| String| Cart ID of the shopping cart being shared  
`products`| Array| List of products shared with the recipient  
`products.$.product_id`| String| Product ID displayed on the list  
  
An example of the **Cart Shared** event is as shown below:
    
    
    rudderanalytics.track("Cart Shared", {
      share_via: "email",
      share_message: "Hello, check out these items!",
      recipient: "buddy@example.com",
      cart_id: "6b2c6f5aecf86a4ae77358ae3",
      products: [{ product_id: "622c6f5d5cf86a4c77358033" }, { product_id: "577c6f5d5cf86a4c7735ba03" }],
    })