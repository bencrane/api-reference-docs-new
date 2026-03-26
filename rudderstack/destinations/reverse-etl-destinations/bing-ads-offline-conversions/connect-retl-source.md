# Connect Reverse ETL Source to Bing Ads Offline Conversions Beta

Configure a Reverse ETL source with your Bing Ads Offline Conversions destination.

* * *

  * __3 minute read

  * 


This guide takes you through the steps to connect a Reverse ETL source to the Bing Ads Offline Conversions destination.

## Set up connection

> ![warning](/docs/images/warning.svg)
> 
> **The Reverse ETL feature supports only source-driven pipeline configuration.**
> 
> Make sure you have [set up a RETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) and connected it to your Bing Ads Offline Conversions destination before following the below steps.

  1. [Confirm the connection settings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/bing-ads-offline-conversions/setup-guide/#connection-settings>) for Bing Ads Offline Conversions destination and click **Continue**.
  2. In the [Data Mapping](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/visual-data-mapper/>) section, select the **Object**.
  3. Specify the [Sync mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/>) to specify how RudderStack should sync the data to Bing Ads.
  4. In **Choose identifier** , specify the warehouse column that RudderStack uses to identify your records.


> ![info](/docs/images/info.svg)
> 
> You can map this warehouse column to any of the following Bing Ads fields:
> 
>   * `EMAIL`
>   * `MICROSOFT_CLICK_ID`
>   * `PHONE`
> 


  5. Map the other warehouse columns to specific Bing Ads fields using the **Map fields** setting.

[![](/docs/images/event-stream-destinations/bingads-offlineconversions-map-fields.webp)](</docs/images/event-stream-destinations/bingads-offlineconversions-map-fields.webp>)

## Supported mappings

RudderStack automatically maps the following schema fields to the corresponding Bing Ads properties depending on the type of operation:

### Create

For any field `x` of type `record`:

RudderStack property| Bing Ads property  
---|---  
`x.conversionCurrencyCode`| [Conversion Currency Code](<https://learn.microsoft.com/en-us/advertising/bulk-service/offline-conversion?view=bingads-13#conversioncurrencycode>)  
`x.conversionName`| [Conversion Name](<https://learn.microsoft.com/en-us/advertising/bulk-service/offline-conversion?view=bingads-13#conversionname>)  
`x.conversionTime`  
Should be in ISO 8601 or Bing Ads-supported format  
Examples:  


  * `2006-01-02T15:04:05Z` (ISO 8601)
  * `02/01/2006 3:04:05 PM` (Bing Ads format)

| [Conversion Time](<https://learn.microsoft.com/en-us/advertising/bulk-service/offline-conversion?view=bingads-13#conversiontime>)  
`x.conversionValue`| [Conversion Value](<https://learn.microsoft.com/en-us/advertising/bulk-service/offline-conversion?view=bingads-13#conversionvalue>)  
`x.clickId`| [Microsoft Click ID](<https://learn.microsoft.com/en-us/advertising/bulk-service/offline-conversion?view=bingads-13#microsoftclickid>)  
`x.userId` or `x.customerId`| Client ID  
`x.externalAttributionCredit`| [External Attribution Credit](<https://learn.microsoft.com/en-us/advertising/bulk-service/offline-conversion?view=bingads-13#externalattributioncredit>)  
`x.externalAttributionModel`| [External Attribution Model](<https://learn.microsoft.com/en-us/advertising/bulk-service/offline-conversion?view=bingads-13#externalattributionmodel>)  
SHA256(`x.email`)  
Required for enhanced conversions.| [Hashed Email Address](<https://learn.microsoft.com/en-us/advertising/bulk-service/offline-conversion?view=bingads-13#hashedemailaddress>)  
SHA256(`x.phone`)  
Required for enhanced conversions.| [Hashed Phone Number](<https://learn.microsoft.com/en-us/advertising/bulk-service/offline-conversion?view=bingads-13#hashedphonenumber>)  
  
### Update

For any field `x` of type `record`:

RudderStack property| Bing Ads property  
---|---  
`restate`| [Adjustment Type](<https://learn.microsoft.com/en-us/advertising/bulk-service/offline-conversion?view=bingads-13#adjustmenttype>)  
`x.conversionCurrencyCode`| [Adjustment Currency Code](<https://learn.microsoft.com/en-us/advertising/bulk-service/offline-conversion?view=bingads-13#adjustmentcurrencycode>)  
`x.conversionName`| [Conversion Name](<https://learn.microsoft.com/en-us/advertising/bulk-service/offline-conversion?view=bingads-13#conversionname>)  
`x.conversionTime`  
Should be in ISO 8601 or Bing Ads-supported format  
Examples:  


  * `2006-01-02T15:04:05Z` (ISO 8601)
  * `02/01/2006 3:04:05 PM` (Bing Ads format)

| [Conversion Time](<https://learn.microsoft.com/en-us/advertising/bulk-service/offline-conversion?view=bingads-13#conversiontime>)  
`x.adjustmentTime`  
Should be in ISO 8601 or Bing Ads-supported format  
Examples:  


  * `2006-01-02T15:04:05Z` (ISO 8601)
  * `02/01/2006 3:04:05 PM` (Bing Ads format)

| [Adjustment Time](<https://learn.microsoft.com/en-us/advertising/bulk-service/offline-conversion?view=bingads-13#adjustmenttime>)  
`x.conversionValue`| [Adjustment Value](<https://learn.microsoft.com/en-us/advertising/bulk-service/offline-conversion?view=bingads-13#adjustmentvalue>)  
`x.clickId`| [Microsoft Click ID](<https://learn.microsoft.com/en-us/advertising/bulk-service/offline-conversion?view=bingads-13#microsoftclickid>)  
SHA256(`x.email`)  
Required for enhanced conversions.| [Hashed Email Address](<https://learn.microsoft.com/en-us/advertising/bulk-service/offline-conversion?view=bingads-13#hashedemailaddress>)  
SHA256(`x.phone`)  
Required for enhanced conversions.| [Hashed Phone Number](<https://learn.microsoft.com/en-us/advertising/bulk-service/offline-conversion?view=bingads-13#hashedphonenumber>)  
  
### Delete

For any field `x` of type `record`:

RudderStack property| Bing Ads property  
---|---  
`retract`| [Adjustment Type](<https://learn.microsoft.com/en-us/advertising/bulk-service/offline-conversion?view=bingads-13#adjustmenttype>)  
`x.conversionName`| [Conversion Name](<https://learn.microsoft.com/en-us/advertising/bulk-service/offline-conversion?view=bingads-13#conversionname>)  
`x.conversionTime`| [Conversion Time](<https://learn.microsoft.com/en-us/advertising/bulk-service/offline-conversion?view=bingads-13#conversiontime>)  
`x.clickId`| [Microsoft Click ID](<https://learn.microsoft.com/en-us/advertising/bulk-service/offline-conversion?view=bingads-13#microsoftclickid>)  
  
## `record` event structure

The Bing Ads Offline Conversions destination supports only `record` events.

A sample `record` event that RudderStack sends to Bing Ads Offline Conversions is shown:
    
    
    {
      "action": "insert",
      "context": {
        "sources": {
          "job_run_id": "<job_run_id>",
          "task_run_id": "<task_run_id>",
          "job_id": "<job_id>",
          "version": "<version>"
        }
      },
      "recordId": "2",
      "rudderId": "2",
      "fields": {
        "microsoftClickId": "<microsoft_clickid>",
        "conversionTime": "2006-01-02T15:04:05Z",
        "conversionName": "<conversion_name>",
        "conversionValue": 100,
        "externalAttributionCredit": "0.5",
        "externalAttributionModel": "<goal_name>",
        "email": "<email>",
        "phone": "<phone>"
      },
      "identifiers": {
        "Email": "alex@example.com"
      },
      "type": "record"
    }
    

## FAQ

#### Why can’t I add a Reverse ETL source from the destination page?

The Reverse ETL feature supports only source-driven pipeline configuration. It means that you must configure a Reverse ETL source in RudderStack and then connect it to a new or existing destination. Note that this destination should not be connected to any other source.

See [Reverse ETL FAQ](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/faq/>) for more information.