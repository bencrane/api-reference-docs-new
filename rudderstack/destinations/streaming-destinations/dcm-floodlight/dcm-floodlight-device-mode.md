# DCM Floodlight Web Device Mode Integration

Send events to DCM Floodlight using RudderStack device mode.

* * *

  * __4 minute read

  * 


RudderStack lets you send your event data to DCM Floodlight destination via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) using the native web SDK. RudderStack uses global site tagging in device mode.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/DCMFloodlight/>).

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you capture user events along with the properties associated with them.

A sample `track` call is as shown below:
    
    
    rudderanalytics.track('tshirt', {
      countingMethod: "transactions",
      revenue: "2605846",
      orderId: "2605847"
    });
    

> ![info](/docs/images/info.svg)
> 
> `countingMethod` is a required property that specifies how to count the conversions for a Floodlight activity. The methods to count conversions depend on whether you are creating or editing a [counter](<https://support.google.com/campaignmanager/answer/7554821#zippy=%2Cfields-in-event-snippets-for-counter-tags>) or [sales](<https://support.google.com/campaignmanager/answer/7554821#zippy=%2Cfields-in-event-snippets-for-sales-tags>) tag activity.
> 
> Refer to the FAQ section for more information on counting methods for these tags.

Note that if `countingMethod` is absent in your event properties, RudderStack uses the method specified in the **Floodlight Counting Method** [dashboard setting](<https://www.rudderstack.com/docs/destinations/streaming-destinations/dcm-floodlight/setting-up-dcm-floodlight-in-rudderstack/#conversion-events>) as a fallback value. If you do not specify both these fields, RudderStack gives a “not found” error for the counting method.

The following table details the `integrations` object mapping for DCM Floodlight:

**RudderStack property**| **DCM Floodlight property**| **Description**  
---|---|---  
`COPPA`| `tag_for_child_directed_treatment`| Imposes requirements on the websites/online services operators directed to children under 13 years of age. [Reference](<https://www.ftc.gov/tips-advice/business-center/privacy-and-security/children%27s-privacy>).  
`GDPR`| `tfua`| The EU law on general data protection and privacy. [Reference](<http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679>).  
`npa`| `npa`| The law catering to users who wish to opt out of remarketing.  
  
The following table details the mapping between the optional RudderStack and DCM Floodlight properties:

RudderStack property| DCM Floodlight property| Tag  
---|---|---  
`properties.ord`| `ord`| Counter  
`properties.sessionId`| `ord`| Counter - per_session  
`properties.sessionId`| `session_id`| Counter - per_session  
`properties.num`| `num`| Counter - unique  
`context.device.adTrackingEnabled`| `dc_lat`| Counter/Sales  
`properties.matchId`| `match_id`| Counter/Sales  
`properties.orderId`| `ord`| Sales  
`properties.orderId`| `transaction_id`| Sales  
`properties.revenue`| `value`| Sales  
`properties.quantity`| `quantity`| Sales - items_sold  
  
There are some slight variations in terms of the mapped DCM Floodlight parameters when you use the Iframe tag, as opposed to the global site tag. However, RudderStack handles this variation internally.

The following table details the mapping between the optional RudderStack and DCM Floodlight properties when using the Iframe tag:

RudderStack property| DCM Floodlight property| Tag  
---|---|---  
`properties.ord`| `ord`| Counter - standard  
`properties.sessionId`| `ord`| Counter - per_session  
`properties.num`| `num`| Counter - unique  
`context.device.adTrackingEnabled`| `dc_lat`| Counter/Sales  
`properties.matchId`| `match_id`| Counter/Sales  
`properties.orderId`| `ord`| Sales  
`properties.orderId`| `transaction_id`| Sales  
`properties.revenue`| `cost`| Sales  
`properties.quantity`| `qty`| Sales - items_sold  
  
> ![info](/docs/images/info.svg)
> 
> When using the Iframe tag, RudderStack sends `ord=1` for the Counter - unique tag and `qty=1` for the Sales - transactions tag.

The following table provides a brief description of the above DCM Floodlight properties:

DCM Floodlight property| Description  
---|---  
`dc_lat`| Indicates if the user has enabled the **Limited Ad Tracking** option for IDFA/Android Advertising ID.  
`ord`| Makes the Floodlight tag unique and prevents browser caching.  
`quantity`| RudderStack adds the quantity of all products in the `products` array or refers to the top-level `quantity` property.  
`value`| RudderStack sends the `revenue` parameter to DCM Floodlight.  
`matchId`| Identifier created by the advertiser to attribute offline conversions.  
`num`| Controls cache busting manually.  
`session_id`| Inserts a unique session ID while using counter tags with a per session counting methodology.  
`transaction_id`| Sets a unique identifier for a transaction.  
  
## Custom parameters

You can also send data to DCM Floodlight using the below-mentioned custom fields:

RudderStack custom field| DCM Floodlight property| [Counting method](<https://support.google.com/campaignmanager/answer/2823400?hl=en>)  
---|---|---  
`properties.ord`/`properties.orderId`/`properties.sessionId`/| `ord`| All  
`context.device.adTrackingEnabled`| `dc_lat`| All  
`COPPA`| `tag_for_child_directed_treatment`| All  
`GDPR`| `tfua`| All  
`npa`| `npa`| All  
`properties.matchId`| `match_id`| All  
`properties.num`| `num`| Counter - unique  
  
> ![info](/docs/images/info.svg)
> 
> For more information on the counting methods, refer to this [DCM Floodlight documentation](<https://support.google.com/campaignmanager/answer/2823400?hl=en>).

## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record your website’s page views with any additional relevant information about the viewed page.

Based on the presence of `name` and `category` fields in the `page` call, RudderStack transforms the event in the following format:

`name` field| `category` field| Transformed event  
---|---|---  
 __| __| Viewed Page  
 __| __| Viewed`PAGE NAME` Page  
 __| __| Viewed`CATEGORY NAME` `PAGE NAME` Page  
  
A sample `page` call is as shown below:
    
    
    rudderanalytics.page('landing', {
      countingMethod: "standard"
    });
    

## FAQ

#### What are the counting methods for sales and counter tag?

For the Sales tag, the counting methods are as shown:

[![DCM Floodlight report builder](/docs/images/event-stream-destinations/sales-tag.webp)](</docs/images/event-stream-destinations/sales-tag.webp>)

For the Counter tag, the counting methods are shown below:[![DCM Floodlight report builder](/docs/images/event-stream-destinations/counter-tag.webp)](</docs/images/event-stream-destinations/counter-tag.webp>)