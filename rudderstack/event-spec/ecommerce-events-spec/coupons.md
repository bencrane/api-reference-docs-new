# Coupons

Understand how ecommerce coupon events work in RudderStack.

* * *

  * __2 minute read

  * 


The following events are associated with the key interactions that a customer has with the app or website while using discount coupons:

## Coupon Entered

This event is triggered when a coupon is entered by the customer, either on a cart or during the order/transaction. The following properties are supported:

**Property Name**| **Type**| **Description of the Property**  
---|---|---  
`order_id`| String| Order ID or transaction ID, if applicable  
`cart_id`| String| Cart ID, if applicable  
`coupon_id`| String| Coupon ID  
  
Here is an example of the **Coupon Entered** event:
    
    
    rudderanalytics.track("Coupon Entered", {
      order_id: "26988d4c2ead000000000000",
      cart_id: "349349349da27da72ad7d73bc4",
      coupon_id: "earlybird10",
    })
    

## Coupon Applied

This event is triggered when a coupon is applied to a cart or a transaction successfully. The following properties are supported:

**Property Name**| **Type**| **Description of the Property**  
---|---|---  
`order_id`| String| Order ID or transaction ID, if applicable  
`cart_id`| String| Cart ID, if applicable  
`coupon_id`| String| Coupon ID  
`coupon_name`| String| Name of the coupon  
`discount`| Number| Discount amount applied from the coupon  
  
Here is an example of the **Coupon Entered** event:
    
    
    rudderanalytics.track("Coupon Applied", {
          order_id: "26988d4c2ead000000000000",
          cart_id: "349349349da27da72ad7d73bc4",
          coupon_id: "earlybird10",
          coupon_name: "Early Bird $10 Discount",
          discount: 10.00
        });
    

## Coupon Denied

This event is triggered when an invalid coupon code is applied to a cart or a transaction. The following properties are supported:

**Property Name**| **Type**| **Description of the Property**  
---|---|---  
`order_id`| String| Order ID or transaction ID, if applicable  
`cart_id`| String| Cart ID, if applicable  
`coupon_id`| String| Coupon ID  
`coupon_name`| String| Name of the coupon  
`reason`| String| Reason why the coupon was declined  
  
Here is an example of the **Coupon Denied** event:
    
    
    rudderanalytics.track("Coupon Denied", {
          order_id: "26988d4c2ead000000000000",
          cart_id: "349349349da27da72ad7d73bc4",
          coupon_id: "earlybird10",
          reason: "Coupon expired"
        });
    

## Coupon Removed

This event is triggered when a customer removes an already applied coupon from a cart or transaction. The following properties are supported:

**Property Name**| **Type**| **Description of the Property**  
---|---|---  
`order_id`| String| Order ID or transaction ID, if applicable  
`cart_id`| String| Cart ID, if applicable  
`coupon_id`| String| Coupon ID  
`coupon_name`| String| Name of the coupon  
`discount`| Number| Discount amount applied from the coupon  
  
Here is an example of the **Coupon Removed** event:
    
    
    rudderanalytics.track("Coupon Removed", {
      order_id: "26988d4c2ead000000000000",
      cart_id: "349349349da27da72ad7d73bc4",
      coupon_id: "earlybird10",
      coupon_name: "Early Bird $10 Discount",
      discount: 10.00
    });