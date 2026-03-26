# Awin

Send your event data from RudderStack to Awin.

* * *

  * __3 minute read

  * 


[Awin](<https://www.awin.com/>) is an affiliate marketing program that connects advertisers and affiliates of all sizes. It provides a network of affiliate partners, click tracing and tracking, advertiser directory, reports and analytics, and more.

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/awin>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **Awin** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Awin, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Awin**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully set up Awin as a destination, you will need to configure the following settings:

  * **Advertiser ID** : Enter your Awin advertiser ID.
  * **Events to Track** : Enter the event names for which you want to track the conversions.


> ![warning](/docs/images/warning.svg)
> 
> You must enter all event names for which you want to make a `track` call.

  * **Map Rudder payload property to custom Awin field** : Enter the RudderStack property and the corresponding Awin custom field you want to map together. These custom properties get associated to a specific transaction and sent to Awin for `track` calls. The Awin field names must follow the `p<int>` format (like `p1`, `p2`, etc.). RudderStack picks the field values from `message.properties` and sends them as query parameters.


> ![warning](/docs/images/warning.svg)
> 
> Duplicate mapping can cause errors.

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to [send the conversion data directly to Awin’s servers](<https://wiki.awin.com/index.php/Advertiser_Tracking_Guide/Conversion_Pixel_Only_Tracking#Server_To_Server_.28S2S.29>).

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Product Purchased New", {
      revenue: 4.99,
      currency: "USD",
      commissionGroup: "CD",
      name: "Shirt",
      voucherCode: "FIRSTSALE",
      order_id: "ORD123",
    });
    

### Supported mappings

The following table lists the mappings between the RudderStack and Awin properties:

#### **Product-level tracking**

RudderStack property| Awin property  
---|---  
`properties.order_id`  
`properties.orderId`  
`properties.orderReference`  
`properties.order_reference`  
Required| `orderReference`  
`product[i].product_id`  
`product[i].productId`  
Required| `productId`  
`properties.products[i].name`  
Required| `productName`  
`properties.products[i].price`  
Required| `productItemPrice`  
`properties.products[i].quantity`  
Required| `productQuantity`  
`properties.commissionGroup`  
`properties.commission_group`  
Required. Default value is `DEFAULT`| `commissionGroupCode`  
`properties.products[i].sku`  
Optional. If not present, RudderStack sends an empty value instead.| `productSku`  
`properties.products[i].category`  
Optional. If not present, RudderStack sends an empty value instead.| `productCategory`  
  
#### **Other mappings**

RudderStack property| Awin property  
---|---  
`properties.revenue`  
`properties.totalAmount`  
`properties.amount`  
`properties.total_amount`| `totalAmount`  
`properties.voucherCode`  
`properties.voucher_code`| `voucher_code`  
`properties.currency`  
`properties.currencyCode`  
`properties.currency_code`| `currencyCode`  
`properties.cks`  
`properties.awc`| `awc`  
`properties.testMode`  
`properties.test_mode`  
`properties.isTest`  
`properties.is_test`  
Default value is `0`.| `isTest`  
  
## FAQ

#### Where can I find the Awin advertiser ID?

To obtain your Awin advertiser ID, log in to your [Awin dashboard](<https://ui.awin.com/idp/en/awin/login>) to see the advertiser ID in the top right corner as well as in the URL:

[![Awin advertiser ID](/docs/images/event-stream-destinations/advertiser-id-awin.webp)](</docs/images/event-stream-destinations/advertiser-id-awin.webp>)