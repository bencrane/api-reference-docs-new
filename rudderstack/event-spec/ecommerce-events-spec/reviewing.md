# Reviewing

Understand how ecommerce product review events work in RudderStack.

* * *

  * __less than a minute

  * 


Product review lifecycle events are a customer adding a product review on your app or website.

## Product Reviewed

This event is triggered whenever a customer reviews a product. The following properties are supported:

**Property Name**| **Type**| **Description of the Property**  
---|---|---  
`product_id`| String| Product ID of the product being reviewed  
`review_id`| String| Review ID of the review being posted by the customer  
`review_body`| String| Review text posted by the customer  
`rating`| String| Customer rating of the product  
  
Here is an example of the **Product Reviewed** event:
    
    
    rudderanalytics.track("Product Reviewed", {
      product_id: "0a4f1f33deb86cd799439092",
      review_id: "9ec72f55ace900e0bb51a066",
      review_body: "Good product, delivered in excellent condition",
      rating: "5",
    })