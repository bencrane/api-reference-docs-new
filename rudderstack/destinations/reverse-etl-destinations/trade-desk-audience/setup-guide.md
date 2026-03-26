# Setup Guide Beta

Send your event data from RudderStack to The Trade Desk Audience.

* * *

  * __3 minute read

  * 


This guide will help you set up The Trade Desk Audience as a destination in RudderStack when connecting to a [Reverse ETL source](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/trade-desk-audience/connect-retl-source/>).

> ![info](/docs/images/info.svg)
> 
> This guide assumes you have already set up a [Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) in RudderStack.

## Setup

In your [RudderStack dashboard](<https://app.rudderstack.com/>), go to **Directory** > **Destinations** > **Cloud Destinations** and search for **The Trade Desk Audience**.

### Connection settings

Configure the following settings to set up The Trade Desk Audience as a destination in RudderStack:

  * **Name** : Specify a unique name to identify the destination in RudderStack.
  * **Advertiser ID** : Enter the advertiser ID from the **Advertiser Preferences** page in the The Trade Desk dashboard.
  * **Advertiser Secret Key** : Enter the advertiser secret key from The Trade Desk dashboard under **Advertiser Preferences** > **Seat Identifiers & Keys**. For more information, refer to the [The Trade Desk documentation](<https://partner.thetradedesk.com/v3/portal/data/doc/DataAuthentication#secret-keys>).
  * **Data Server** : Select the preferred data server from dropdown. For more information, refer to the [The Trade Desk documentation](<https://partner.thetradedesk.com/v3/portal/data/doc/DataEnvironments#1pd-servers>).


### Configuration settings

Configure the following settings in the **Configuration** tab of the The Trade Desk Audience destination:

  * **TTL (in days)** : Enter the Time-to-Live (TTL) indicating the duration for which a user must remain active in the segment. The default TTL is set to 30 days and the maximum allowable TTL value is 180 days.


> ![warning](/docs/images/warning.svg)
> 
> Once the TTL expires, the user data gets removed from the data segments. You need to trigger a full sync to repopulate the data by going to the **Syncs** tab of your Reverse ETL source in the dashboard.

## Sync first-party data

RudderStack supports adding/deleting the IDs from the data segments in The Trade Desk Audience by using the [`POST /data/advertiser`](<https://partner.thetradedesk.com/v3/portal/data/doc/post-data-advertiser-external>) endpoint of The Trade Desk Audience API. It uploads the first-party data for the specified advertiser ID to perform audience targeting.

RudderStack supports all the ID types mentioned in this [The Trade Desk API reference](<https://partner.thetradedesk.com/v3/portal/data/doc/post-data-advertiser-external#supported-ids>). Refer to the documentation to know more about these ID types, their data type, and usage.

Refer to the following request example with an external provider and different IDs:
    
    
    {
      "DataProviderId": "test-dataProviderId",
      "AdvertiserId": "test-advertiserId",
      "Items": [{
          "TDID": "123e4567-e89b-12d3-a456-426652340000", // {ID_TYPE}
          "Data": [{
            "Name": "1210", // The name of the segment to which this ID will be added               
            "TimestampUtc": "2023-11-11T10:11:30+5000",
            "TTLInMinutes": 43200
          }]
        },
        {
          "DAID": "234e4567-e89b-12d3-a456-426652340000", // {ID_TYPE}
          "Data": [{
            "Name": "1210", // The name of the segment to which this ID will be added
            "TimestampUtc": "2023-11-11T10:11:30+5000",
            "TTLInMinutes": 43200
          }]
        }
      ]
    }
    

> ![info](/docs/images/info.svg)
> 
> RudderStack internally splits the request into multiple batches to adhere to the batch limit of 2.5MB imposed by The Trade Desk Audience.

### Upload UIDs using Snowflake source

While using the [Snowflake source](<https://www.rudderstack.com/docs/sources/reverse-etl/snowflake/>) with The Trade Desk, you can use the [Unified ID 2.0 (UID2)](<https://app.snowflake.com/marketplace/listing/GZT0ZRYXTMV/unified-id-2-0-unified-id-2-0-advertiser-identity-solution?originTab=provider&providerName=Unified%20ID%202.0>) for advertising without exposing any sensitive directly identifying information.

To do this, [set up the UID2 Snowflake account](<https://unifiedid.com/docs/guides/snowflake_integration>) and interact with Snowflake’s UID2 function to convert the emails and phone numbers into UIDs. Once these UIDs are available in the Snowflake warehouse, RudderStack will upload them to The Trade Desk using its [First Party Data Endpoint](<https://partner.thetradedesk.com/v3/portal/data/doc/post-data-advertiser-external>).