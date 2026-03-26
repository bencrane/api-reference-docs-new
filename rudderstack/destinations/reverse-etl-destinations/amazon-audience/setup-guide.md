# Setup Guide

Send your event data from RudderStack to Amazon Audience.

* * *

  * __3 minute read

  * 


This guide will help you set up Amazon Audience as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Amazon.

> ![info](/docs/images/info.svg)
> 
> Make sure you have already set up a [Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) in RudderStack before following the steps in this guide.

## Setup

In your [RudderStack dashboard](<https://app.rudderstack.com/>), go to **Directory** > **Destinations** > **Cloud Destinations** and search for **Amazon Audience**.

### Connection settings

Configure the following settings to set up Amazon Audience as a destination in RudderStack:

Setting| Description  
---|---  
Name| Specify a unique name to identify the destination in RudderStack.  
Account Settings| Click **Create Account** > **Connect with Amazon Audience** and give RudderStack the required permissions to access your Amazon account.  
Select your Account| Select the required Advertiser ID from the dropdown. This is populated from your Amazon Audience account.  
Authorization Servers| Select the authorization server from the dropdown. Currently, RudderStack supports only North America.  
  
## Send `record` event

The Amazon Audience destination supports only `record` events.

  1. Upload [record data](<https://advertising.amazon.com/API/docs/en-us/guides/dsp/data-provider#upload-your-hashed-data-to-a-record>) and provide an `externalId` of your choice to each record. It is used later to associate the record to a data provider audience. If not provided, RudderStack assigns `Rudderstack_${sha256(users)}` as the default `externalId`.

The following table lists the mappings between RudderStack and Amazon fields:

RudderStack field| Amazon Audience property/event Base: `records[0].hashedRecords.$.`| Data Type  
---|---|---  
`email`| `email`| String  
`phone`| `phone`| String  
`first_name`| `firstName`| String  
`last_name`| `lastName`| String  
`address`| `address`| String  
`city`| `city`| String  
`state`| `state`| String  
`country`| `country`| String  
`postalCode`| `postalCode`| String  


> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * You must [format](<https://advertising.amazon.com/help/GCCXMZYCK4RXWS6C>) and hash the above fields before sending them to Amazon.
>   * If you are passing the `phone` field, and:
>     * The country is `US`, you just need to send the hashed phone number.
>     * The country is not `US`, you must send the hashed phone number along with the country name in `country` property.
> 


  2. Create [data provider audience](<https://advertising.amazon.com/API/docs/en-us/guides/dsp/data-provider#create-a-new-data-provider-audience>).

The following table lists the mappings between RudderStack and Amazon fields:

RudderStack field| Amazon Audience property/event| Data Type  
---|---|---  
`name` (from RudderStack dashboard)  
Required| `name`| String  
`description` (from RudderStack dashboard)  
Required| `description`| String  
`config.advertiserId`  
Required| `advertiserID`| String  
`DATA_PROVIDER`| `metadata.type`| String  
`config.source_country`  
`US`| `metdadata.dataSourceCountry`| String  
`config.externalaudienceId`  
`Ruderstack Audience`| `externalAudienceId`| String  
`config.ttl`| `ttl`| String  


> ![info](/docs/images/info.svg)
> 
> You must hash the above fields before sending them to Amazon.

  3. [Associate record data with the data provider audience](<https://advertising.amazon.com/API/docs/en-us/guides/dsp/data-provider#associate-or-disassociate-your-records-with-your-data-provider-audience>).

The following table lists the mappings between RudderStack and Amazon fields:

RudderStack field| Amazon Audience property/event| Data Type  
---|---|---  
`externalId` (from step 1)  
Required| `externalId`| String  
`audienceId` (from step 2’s response)  
Required| `audienceId`| String  


## Next steps

  * [Connect Reverse ETL source to Amazon Audience](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/amazon-audience/connect-retl-source/>)


## FAQ

#### What might be the reason for below error while creating the data provider audience?
    
    
     {
        errorType: 'INVALID_INPUT',
        message: 'Existing name: string, New name: khfyuc',
        fieldName: 'name',
    },
    {
      errorType: 'INVALID_INPUT',
      message: 'Existing description: string, New description: strinogiycvg1',
      fieldName: 'description',
    },
    

You can try changing your `external_audience_id` which is unique for each audience. That should resolve the issue.