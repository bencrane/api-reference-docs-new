# Browsing

Understand how ecommerce browsing events work in RudderStack.

* * *

  * __3 minute read

  * 


The browsing lifecycle events are associated with key activities that a customer might perform while browsing through your website or mobile app.

## Products Searched

This event is triggered when a visitor searches for a product on your app/website. The following properties are supported:

**Property Name**| **Type**| **Description of the Property**  
---|---|---  
`query`| String / Object| Query searched by the user  
  
Here is an example of the **Products Searched** event:
    
    
    rudderanalytics.track("Products Searched", {
      query: "HDMI cable",
    })
    

## Product List Viewed

This event is triggered when a visitor views a list or category of products on your website or app. The following properties are supported:

**Property Name**| **Type**| **Description of the Property**  
---|---|---  
`list_id`| String| Name of the product list being viewed  
`category`| String| Category of the product being viewed  
`products`| Array| Array of products displayed in the product list  
`products.$.product_id`| String| Product ID displayed on the list  
`products.$.sku`| String| SKU (Stock Keeping Unit) of the product being viewed  
`products.$.category`| String| Category of the product being viewed  
`products.$.name`| String| Name of the product being viewed  
`products.$.brand`| String| Name of the brand associated with the product  
`products.$.variant`| String| Name of the variant of the product  
`products.$.price`| Number| Price of the product being viewed (in USD)  
`products.$.quantity`| Number| Quantity of the product  
`products.$.coupon`| String| Coupon code associated with a product  
`products.$.position`| Number| Position of the product in the product list  
`products.$.url`| String| URL of the product page  
`products.$.image_url`| String| Image URL of the product  
  
Here is an example of the **Product List Viewed** event:
    
    
    rudderanalytics.track("Product List Viewed", {
      list_id: "list1",
      category: "What's New",
      products: [
        {
          product_id: "017c6f5d5cf86a4b22432066",
          sku: "8732-98",
          name: "Just Another Game",
          price: 22,
          position: 2,
          category: "Games and Entertainment",
          url: "https://www.myecommercewebsite.com/product",
          image_url: "https://www.myecommercewebsite.com/product/path.jpg"
        },
        {
          product_id: "89ac6f5d5cf86a4b64eac145",
          sku: "1267-01",
          name: "Wrestling Trump Cards",
          price: 4,
          position: 21,
          category: "Card Games"
        }
      ]
    });
    

## Product List Filtered

This event is triggered when a visitor filters a list or category of products on your website or app. The following properties are supported:

**Property Name**| **Type**| **Description of the Property**  
---|---|---  
`list_id`| String| Name of the product list being viewed  
`category`| String| Name of the product category being viewed  
`filters`| Array| Product filters that the customer has applied  
`filters.$.type`| String| ID of the filter type that the customer is using  
`filters.$.value`| String| ID of the selection chosen by the customer  
`sorts`| Array| Product sorting used by the customer  
`sorts.$.type`| String| ID of the sort type used by the customer  
`sorts.$.value`| String| ID of the selection-type the customer is using  
`products`| Array| Products displayed in the product list  
`products.$.product_id`| String| Product ID displayed in the product list  
`products.$.sku`| String| SKU of the viewed product  
`products.$.category`| String| Product category viewed by the customer  
`products.$.name`| String| Name of the product being viewed by the user  
`products.$.brand`| String| Brand name associated with the product  
`products.$.variant`| String| Name of the product variant  
`products.$.price`| Number| Price of the product being viewed (in USD)  
`products.$.quantity`| Number| Quantity of a product  
`products.$.coupon`| String| Coupon code associated with a product  
`products.$.position`| Number| Position of the product in the product list  
`products.$.url`| String| URL of the product page  
`products.$.image_url`| String| Image URL of the product  
  
An example of the **Product List Filtered** event is as shown:
    
    
    rudderanalytics.track("Product List Filtered", {
      list_id: "dealoftheday",
      filters: [
        {
          type: "department",
          value: "health",
        },
        {
          type: "price",
          value: "under-$75",
        },
      ],
      sorts: [
        {
          type: "price",
          value: "asc",
        },
      ],
      products: [
        {
          product_id: "5556ed1b1cf49eb378a32009",
          sku: "4594-58",
          name: "Whey Protein",
          price: 55.45,
          position: 1,
          category: "health",
          url: "https://www.myecommercewebsite.com/product/product1123",
          image_url: "https://www.example.com/product/1123.jpg",
        },
        {
          product_id: "9281bb1e0af05af308a32009",
          sku: "0966-22",
          name: "Boost",
          price: 47.85,
          position: 12,
          category: "health",
        },
      ],
    })