# Promotions

Understand how ecommerce promotion events work in RudderStack.

* * *

  * __less than a minute

  * 


Promotion view or click events collect useful information tracking and analyzing internal offers on your website or mobile app.

## Promotion Viewed

This event is triggered when a user views a website promotion or offer. The following properties are supported:

**Property Name**| **Type**| **Description of the Property**  
---|---|---  
`promotion_id`| String| Promotion ID  
`creative`| String| Creative details of the promotion  
`name`| String| Name of the promotion  
`position`| String| Promotion’s position on the website/app  
  
Here is an example of the **Promotion Viewed** event:
    
    
    rudderanalytics.track("Promotion Viewed", {
      promotion_id: "promo1",
      creative: "top_banner1",
      name: "15% off flash sale",
      position: "home_top_banner",
    })
    

> ![warning](/docs/images/warning.svg)
> 
> For the Google Analytics 4 destination, you must include the `products` parameter in the [Promotion Viewed](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-analytics-4/cloud-mode/#promotion-viewed>) event to send it successfully.

## Promotion Clicked

This event is triggered when a visitor clicks on a promotional offer on the website or mobile app. The following properties are supported:

**Property**| **Type**| **Description of the Property**  
---|---|---  
`promotion_id`| String| Promotion ID  
`creative`| String| Creative details of the promotion  
`name`| String| Name of the promotion  
`position`| String| Promotion’s position on the website/app  
  
Here is an example of the **Promotion Clicked** event:
    
    
    rudderanalytics.track("Promotion Clicked", {
      promotion_id: "promo1",
      creative: "top_banner1",
      name: "15% off flash sale",
      position: "home_top_banner",
    })
    

> ![warning](/docs/images/warning.svg)
> 
> For the Google Analytics 4 destination, you can include the `products` parameter in the [Promotion Clicked](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-analytics-4/cloud-mode/#promotion-clicked>) event.