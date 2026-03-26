# Wishlist

Understand how ecommerce wishlist events work in RudderStack.

* * *

  * __3 minute read

  * 


Product wishlist events are a customer adding a product to their shopping wishlist. This is useful if your website/app supports a wishlisting feature.

## Product Added to Wishlist

This event is triggered when a customer adds a product to their shopping wishlist. The following properties are supported:

**Property Name**| **Type**| **Description of the Property**  
---|---|---  
`wishlist_id`| String| Wishlist ID  
`wishlist_name`| String| Name of the wishlist the product was added to  
`product_id`| String| Product ID of the product being viewed  
`sku`| String| SKU of the product  
`category`| String| Category of the product  
`name`| String| Name of the product  
`brand`| String| Name of the brand associated with the product  
`variant`| String| Name of the variant associated with the product  
`price`| Number| Price of the product (in USD)  
`quantity`| Number| Quantity of the product  
`coupon`| String| Coupon code associated with the product  
`position`| Number| Position of the product in the product list  
`url`| String| URL of the product page  
`image_url`| String| Image URL of the product  
  
Here is an example of the **Product Added to Wishlist** event:
    
    
    rudderanalytics.track("Product Added to Wishlist", {
      wishlist_id: "74fkdjfl0jfdkdj29j030",
      wishlist_name: "New Games",
      product_id: "622c6f5d5cf86a4c77358033",
      sku: "8472-998-0112",
      category: "Games",
      name: "Cones of Dunshire",
      brand: "Wyatt Games",
      variant: "expansion pack",
      price: 49.99,
      quantity: 1,
      coupon: "PREORDER15",
      position: 1,
      url: "https://www.site.com/product/path",
      image_url: "https://www.site.com/product/path.jpg",
    })
    

## Product Removed from Wishlist

This event is triggered when a customer removes a product from their shopping wishlist. The following properties are supported:

**Property**| **Type**| **Description**  
---|---|---  
`wishlist_id`| String| Wishlist ID  
`wishlist_name`| String| Name of the wishlist the product was added to  
`product_id`| String| Product ID of the product being viewed  
`sku`| String| SKU of the product  
`category`| String| Category of the product being viewed  
`name`| String| Name of the product  
`brand`| String| Name of the brand associated with the product  
`variant`| String| Name of the variant associated with the product  
`price`| Number| Price of the product (in USD)  
`quantity`| Number| Quantity of the product  
`coupon`| String| Coupon code associated with the product  
`position`| Number| Position of the product in the product list  
`url`| String| URL of the product page  
`image_url`| String| Image URL of the product  
  
Here is an example of the **Product Removed from Wishlist** event:
    
    
    rudderanalytics.track("Product Removed from Wishlist", {
      wishlist_id: "74fkdjfl0jfdkdj29j030",
      wishlist_name: "New Games",
      product_id: "622c6f5d5cf86a4c77358033",
      sku: "8472-998-0112",
      category: "Games",
      name: "Cones of Dunshire",
      brand: "Wyatt Games",
      variant: "expansion pack",
      price: 49.99,
      quantity: 1,
      coupon: "PREORDER15",
      position: 1,
      url: "https://www.site.com/product/path",
      image_url: "https://www.site.com/product/path.jpg",
    })
    

## Wishlist Product Added to Cart

This event is triggered whenever a wishlisted product is added to the shopping cart by the customer. The following properties are supported by this event:

**Property**| **Type**| **Description**  
---|---|---  
`wishlist_id`| String| Wishlist ID  
`wishlist_name`| String| Name of the wishlist the product was added to  
`product_id`| String| Product ID of the product being viewed  
`sku`| String| SKU of the product  
`category`| String| Category of the product being viewed  
`name`| String| Name of the product  
`brand`| String| Name of the brand associated with the product  
`variant`| String| Name of the variant associated with the product  
`price`| Number| Price of the product (in USD)  
`quantity`| Number| Quantity of the product  
`coupon`| String| Coupon code associated with the product  
`position`| Number| Position of the product in the product list  
`url`| String| URL of the product page  
`image_url`| String| Image URL of the product  
  
An example of the **Wishlist Product Added to Cart** event is as shown:
    
    
    rudderanalytics.track("Wishlist Product Added to Cart", {
      wishlist_id: "74fkdjfl0jfdkdj29j030",
      wishlist_name: "New Games",
      product_id: "622c6f5d5cf86a4c77358033",
      sku: "8472-998-0112",
      category: "Games",
      name: "Cones of Dunshire",
      brand: "Wyatt Games",
      variant: "expansion pack",
      price: 49.99,
      quantity: 1,
      coupon: "PREORDER15",
      position: 1,
      url: "https://www.site.com/product/path",
      image_url: "https://www.site.com/product/path.jpg",
    })