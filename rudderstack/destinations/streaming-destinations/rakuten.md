# Rakuten Beta

Send your event data from RudderStack to Rakuten.

* * *

  * __8 minute read

  * 


[Rakuten](<https://rakutenadvertising.com/affiliate/>) provides a robust affiliate marketing ecosystem to expand your reach by connecting with a vast and engaged audience across multiple channels.

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/main/src/cdk/v2/destinations/rakuten>).

## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), go to **Directory** > **Destinations** > **Cloud Destinations** and search for **Rakuten**.
  2. Connect your source and click **Continue**.


### Connection settings

Configure the following settings to set up Rakuten as a destination in RudderStack:

  * **Name** : Assign a name to uniquely identify the destination.
  * **Merchant ID** : Enter the numeric merchant ID that uniquely identifies you in the Rakuten marketing system.


### Connection mode

Destination Information  
---  
  
  * **Status:** Beta
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Unity, AMP , Web, Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Rakuten** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
  
## Track

You can use the RudderStack [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) event to track events along with any associated properties and send this information to Rakuten.

A sample `track` event is shown below:
    
    
    rudderananlytics.track('event', {
      orderId: "OR122441",
      land: 1234,
      ranSiteId: "823421983a3-231824ft12-e12-gh1208b12-14"
      products: [{
          sku: 'sku1',
          amount: '8' // instead of 10 for 20% discount
          quantity: 1,
          name: 'Product1'
        },
        {
          sku: 'sku2',
          amount: 81 // instead of 90 for 10% discount
          quantity: 2,
          name: 'Product2'
        }
      ]
    })
    

### Property mappings

RudderStack maps the following properties to the Rakuten fields:

RudderStack property| Rakuten property| Limitations  
---|---|---  
`properties.order_id`  
`properties.orderId`  
  
Required| `ord`| <40 non-blank characters  
`properties.land`  
`properties.land_time`  
`properties.landTime`  
  
Required| `land`| Should be present as `YYYYMMDD_HHMM` in the GMT 24-hour format.  
  
**Note** : This is the datetime value set in the cookie of your Rakuten Marketing-specific gateway page when a customer arrives at your website.  
`properties.date`  
`properties.order_completed_time`  
`properties.orderCompletedTime`| date| Should be present as `YYYYMMDD_HHMM` in the GMT 24-hour format.  
  
**Note** : Represents the date and time of the online completion (Thank You) page.  
`properties.altord`  
`properties.alt_ord`  
`properties.alter_order_id`  
`properties.alterOrderId`| `altord`| <40 characters  
  
**Note** : Alternative version of the reported order ID like a backend version, customer-facing version, etc.  
`properties.currency`| `cur`| 3 alphanumeric characters matching the currency used by the customer in the transaction. For example, `USD`, `CAD`, `GBP`, `JPY`, `BRL`, `EUR`, `AUD`.  
`properties.creditCardType`  
`properties.credit_card_type`| `cc`| <16 characters  
`properties.commreason`  
`properties.comm_reason`| `commreason`| <255 characters  
  
**Note** : Used for reporting only and should be used to show the reason for the commission (`iscomm`) flag.  
`properties.iscomm`  
`properties.is_comm`| `iscomm`| -  
  
**Note** : Specifies if a commission is applicable for an order.  
`properties.consumed`| `consumed`| <13 characters  
Should be formatted as `YYYYMMDD_HHMM` in the GMT 24-hour format.  
**Note** : Expected date when a travel event is consumed.  
`properties.coupon`| `coupon`| <128 characters  
`properties.customerId`  
`properties.customer_id`  
`properties.cust_id`  
`properties.custId`  
`properties.userId`| `custid`| <128 characters  
  
**Note** : Identifier representing the customer like ID, hashed email, etc. Make sure to not pass any PII. Any special characters should be URL-encoded into the hex format.  
`properties.cust_score`  
`properties.customer_score`  
`properties.customerScore`  
`properties.custScore`| `custscore`| <16 characters  
  
**Note** : Represents a score assigned to the customer by the system. It can alphabetical, numeric, or alphanumeric.  
`properties.customerStatus`  
`properties.custStatus`  
`properties.customer_status`  
`properties.cust_status`| `custstatus`| <32 characters  
  
**Note** : Represents the status of the customer like new, existing, guest, etc.  
`properties.dId`  
`properties.advertisingId`  
`properties.advertising_id`| `did`| <42 characters  
  
**Note** : Used for the advertising ID of the mobile device.  
`properties.discountAmount`  
`properties.disAmt`  
`properties.discount_amount`| `disamt`| <9 characters  
`properties.orderStatus`  
`properties.ordStatus`  
`properties.order_status`  
`properties.ord_status`| `ordstatus`| <32 characters  
  
**Note** : Represents the order status assigned by the system.  
`properties.tr`  
`properties.ran_site_id`  
`properties.ranSiteID`| `tr`| <34 characters  
  
**Note** : Set in a cookie of your Rakuten Marketing-specific gateway page. Can include mixed-case letters, numbers, and special characters like `-`, `.`, `_`, `/`, and `*`.  
`properties.segment`| `segment`| <32 characters  
  
**Note** : Represents the customer segment.  
`properties.shipcountry`  
`properties.ship_country`| `shipcountry`| <3 characters  
  
**Note** : The country where the order is to be shipped. Must follow the ISO 3-character country code.  
`properties.shipped`| `shipped`| Should be present as `YYYYMMDD_HHMM` in the GMT 24-hour format.  
  
**Note** : Expected date when the order will be shipped.  
`properties.sitename`  
`properties.site_name`  
`properties.url`  
`context.page.url`| `sitename`| <128 characters  
  
**Note** : Identifier representing where the conversion took place like domain name of the site. Any special characters should be URL-encoded in the hex format.  
`properties.storeId`  
`properties.store_id`| `storeid`| <255 characters  
  
**Note** : Represents the category of the store where the conversion occurred.  
`properties.storecat`  
`properties.store_cat`  
`properties.storeCategory`  
`properties.store_category`| `storecat`| -  
  
**Note** : Represents the category name for the store where the conversion occurred.  
  
### Item-level mappings

RudderStack maps the following item-level properties to the Rakuten properties:

RudderStack property| Rakuten property| Limitations  
---|---|---  
`product.$.sku`  
  
Required| `skulist.$`| -  
`product.$.amount`  
`product.$.(price*quantity)`  
  
Required| `amtlist.$`| -  
`product.$.quantity`  
  
Required| `qlist.$`| -  
`product.$.name`  
  
Required| `namelist.$`| -  
`product.$.brand`| `brandlist.$`| <255 characters.  
`product.$.coupon`| `couponlist.$`| -  
  
**Note** : Holds a pipe-delimited list of item-level coupons applied to the order. Order of values in this list must match the order of values in `skulist`. Multiple item-level coupon codes are not allowed.  
`product.$.categoryId`| `catidlist.$`| <128 characters  
  
**Note** : You can specify up to 5 category IDs per item separated by `>`. For example, `(1001>2001>3001)`  
`product.$.category`| `catlist.$`| <255 characters  
  
**Note** : You can specify up to 5 category IDs per item separated by `>`. For example, `(ParentCat>ChildCat1>ChildCat2)`  
`product.$.discountAmount`| `disamtlist.$`| <9 characters  
  
**Note** : Pipe delimited list of item-specific discount amounts formatted as a number. Values must match the order of values in `skulist`.  
`product.$.discountType`| `distypelist.$`| <256 characters  
  
**Note** : Pipe delimited list of item-level discount types. Order of values must match of values in `skulist`. Special characters should be URL-encoded in hex format.  
`product.$.isClearance`| `isclearancelist.$`| Acceptable values are `Y` or `N`  
  
**Note** : Pipe delimited list of flags indicating if the item is on clearance. Values must match the order of values in `skulist`.  
`product.$.isMarketPlace`| `ismarketplacelist.$`| Acceptable values are `Y` or `N`  
  
**Note** : Pipe delimited list of flags indicating if the item is from a marketplace. Values must match the order of values in `skulist`.  
`product.$.isSale`| `issalelist.$`| Acceptable values are `Y` or `N`  
  
**Note** : Pipe delimited list of flags indicating if the item is on sale. Values must match the order of values in `skulist`.  
`product.$.itmStatus`| `itmstatuslist.$`| <32 characters  
  
**Note** : Pipe delimited list of item-level statuses. Order of values in this list must match the order of values in `skulist`. Possible values are `In-Stock`, `Back-Ordered`, etc. Special characters must be URL-encoded in hex format.  
`product.$.margin`| `marginlist.$`| <3 characters  
  
**Note** : Pipe delimited list representing profit margin of the products. Order of values in this list must match the order of values in `skulist`.  
`product.$.markdown`| `markdownlist.$`| <6 characters  
  
**Note** : Pipe delimited list representing markdown rate of an item. Order of values in this list must match the order of values in `skulist`.  
`product.$.sequence`| `sequencelist.$`| <4 characters.  
  
**Note** : Identifies the sequence of items included in a shipment or return.  
`product.$.shipby`| `shipbylist.$`| <32 characters  
  
**Note** : Pipe delimited list of strings identifying who shipped the item. Possible values are `Store` if the item is shipped from a physical store, `Fulfullment Vendor X` if shipped by a fulfillment partner, etc. Special characters must be URL-encoded in hex format.  
`product.$.shipID`| `shipidlist.$`| <32 characters  
  
**Note** : Identifies a collection of items that are shipped or returned together.  
`product.$.taxexempt`| `taxexemptlist.$`| Acceptable values are `Y` or `N`  
  
**Note** : Pipe delimited list of flags indicating if the item is tax-exempt. Rakuten then reduces the transaction amount by a defined tax rate.  
  
## Discount reporting

For accurate discount reporting, make sure to report only product discounts or discounts that reduce a product subtotal. Do not include free shipping in the discount amount.

Suppose a customer purchases 1 item of SKU A for $10.00 and 2 items of SKU B for $45.00 each and then redeems a 10% order-level discount. In that case, Rakuten provides two options for reporting discounts:

  * Reduced item reporting (preferred)
  * Discounts as SKU


### Reduced item reporting

> ![info](/docs/images/info.svg)
> 
> Rakuten prescribes this reporting method for selected goods commissioning, that is, if you want to commission by product type.

In this case, you can adjust the reported amount value to reflect the applied discounts. In the above example, you can send the amounts in a `product` array as $9.00 and $81.00 respectively for the two SKUs.

For multiple item purchases, disperse the discounts accordingly among each value in the total amount value.

### Discounts as SKU

> ![info](/docs/images/info.svg)
> 
> Rakuten prescribes this method if you intend to set the same commission on all goods.

For this reporting model, add an extra value to the `sku`, `quantity`, `amount`, and the product `name` fields that depict the discount.

  * For `sku`, and `name`, use the string `Discount`.
  * For `quantity`, use `0`.
  * For `amount`, use the negative dollar value of the discount.


A sample `track` event highlighting this method is shown:
    
    
    rudderananlytics.track('event', {
      products: [{
          sku: 'sku1',
          amount: '100'
          quantity: 1
        },
        {
          sku: 'Discount',
          name: 'Discount',
          amount: -10 // Total discount of 10
          quantity: 0
        }
      ]
    })
    

## FAQ

#### Why are products commissionable even if `iscomm` is set to `N` (no)?

Note that `iscomm` is applicable for the entire order.

Even if you have `iscomm=N` in the postback, the transaction is still commissionable in Rakuten. You need to explicitly set the dynamic commissioning rules (for example, if `iscomm` equals `N`, pay $0 commission) in the Rakuten dashboard to avoid paying commission for a particular order.

#### How can I report a returned item in `Order Cancelled` or `Partially Cancelled` events?

Suppose a customer returns two items of SKU A and one item of SKU B, the cancellation records would look like below:
    
    
    rudderananlytics.track('event', {
      orderId: "ord123",
      land: 1133,
      ranSiteId: "846t21983y3-231824et12-e12-ey1208e12-14",
      cur: 'USD',
      products: [{
          sku: 'A',
          amount: '-200'
          quantity: 2,
          name: 'name_1'
        },
        {
          sku: 'B',
          amount: -10
          quantity: 1,
          name: 'name_2'
        }
      ]
    })
    

Note that the quantity shows the number of returned items and price is negative, reflecting the return. Quantity is not a negative number for returns unless the price in the original order was zero.

You must also account for any discounts applied during the order cancellation. For reduced item discount reporting, note that:

  * If you are using discount as a SKU option, send a cancellation record for the discount SKU item **in addition** to the regular SKUs of the order for cancellation.