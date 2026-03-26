# Reverse ETL Sync Modes

Learn about different sync modes to send data from reverse ETL sources to your destinations.

* * *

  * __4 minute read

  * 


The Reverse ETL sources support three sync modes that define how RudderStack syncs data to the destinations.

  * Upsert mode
  * Mirror mode
  * Full sync mode


## Specify sync mode

You can configure the sync mode in the **Data Mapping** settings while connecting your Reverse ETL source to a destination.

[![Sync mode setting in RudderStack dashboard](/docs/images/data-pipelines/specify-sync-mode.webp)](</docs/images/data-pipelines/specify-sync-mode.webp>)

## Supported sources

The following Reverse ETL sources support the sync modes listed above:

  * [BigQuery](<https://www.rudderstack.com/docs/sources/reverse-etl/google-bigquery/>)
  * [Databricks](<https://www.rudderstack.com/docs/sources/reverse-etl/databricks/>)
  * [MySQL](<https://www.rudderstack.com/docs/sources/reverse-etl/mysql/>)
  * [PostgreSQL](<https://www.rudderstack.com/docs/sources/reverse-etl/postgresql/>)
  * [Redshift](<https://www.rudderstack.com/docs/sources/reverse-etl/amazon-redshift/>)
  * [Snowflake](<https://www.rudderstack.com/docs/sources/reverse-etl/snowflake/>)
  * [Trino](<https://www.rudderstack.com/docs/sources/reverse-etl/trino/>)


## Upsert mode

In this mode, RudderStack inserts only the new records and updates to the existing records while syncing data to the destination.

RudderStack supports upsert mode for **all** destinations except the destinations that only support mirror mode.

See Sync behavior for more information on how RudderStack syncs records after you update the source-destination mappings.

## Mirror mode

In this mode, RudderStack ‘mirrors’ the source by keeping the destination data the same as the source data. It performs insertion, updates, and deletion of records while syncing data to the destination.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack does not support `track` event type for this mode.

RudderStack supports mirror mode for the following destinations:

[![Bloomreach Catalog logo](/docs/images/logos/destinations/bloomreach.svg)Bloomreach Catalog](</docs/destinations/reverse-etl-destinations/bloomreach-catalog/>)[![Amazon Audience logo](/docs/images/logos/destinations/amazon.svg)Amazon Audience](</docs/destinations/reverse-etl-destinations/amazon-audience/>)[![Bing Ads Audience logo](/docs/images/logos/destinations/bing-ads.svg)Bing Ads Audience](</docs/destinations/reverse-etl-destinations/bing-ads-audience/>)[![Bing Ads Offline Conversions logo](/docs/images/logos/destinations/bing-ads.svg)Bing Ads Offline Conversions](</docs/destinations/reverse-etl-destinations/bing-ads-offline-conversions/>)[![Bloomreach Catalog logo](/docs/images/logos/destinations/bloomreach.svg)Bloomreach Catalog](</docs/destinations/reverse-etl-destinations/bloomreach-catalog/>)[![Criteo Audience logo](/docs/images/logos/destinations/criteo.svg)Criteo Audience](</docs/destinations/reverse-etl-destinations/criteo-audience/>)[![Customer.io Audience logo](/docs/images/logos/destinations/customerio.svg)Customer.io Audience](</docs/destinations/reverse-etl-destinations/customerio-audience/>)[![Facebook Custom Audience logo](/docs/images/logos/destinations/facebook.svg)Facebook Custom Audience](</docs/destinations/reverse-etl-destinations/facebook-custom-audience/>)[![Google Ads Remarketing Lists \(Customer Match\) logo](/docs/images/logos/destinations/googleads.svg)Google Ads Remarketing Lists (Customer Match)](</docs/destinations/reverse-etl-destinations/google-ads-remarketing-lists/>)[![LaunchDarkly Segments logo](/docs/images/logos/destinations/launchdarkly.svg)LaunchDarkly Segments](</docs/destinations/reverse-etl-destinations/launchdarkly-segments/>)[![Linkedin Audience logo](/docs/images/logos/destinations/linkedin.svg)Linkedin Audience](</docs/destinations/reverse-etl-destinations/linkedin-audience/>)[![Marketo Static Lists logo](/docs/images/logos/destinations/marketo.svg)Marketo Static Lists](</docs/destinations/reverse-etl-destinations/marketo-static-lists/>)[![SFTP logo](/docs/images/logos/destinations/sftp.svg)SFTP](</docs/destinations/reverse-etl-destinations/sftp/>)[![Snapchat Custom Audience logo](/docs/images/logos/destinations/snapchat.svg)Snapchat Custom Audience](</docs/destinations/reverse-etl-destinations/snapchat-custom-audience/>)[![The Trade Desk Audience logo](/docs/images/logos/destinations/the-trade-desk.svg)The Trade Desk Audience](</docs/destinations/reverse-etl-destinations/trade-desk-audience/>)[![TikTok Audiences logo](/docs/images/logos/destinations/tiktok-ads.svg)TikTok Audiences](</docs/destinations/reverse-etl-destinations/tiktok-audiences/>)[![X Audience logo](/docs/images/logos/destinations/twitter.svg)X Audience](</docs/destinations/reverse-etl-destinations/x-audience/>)

  


See Sync behavior for more information on how RudderStack syncs records after you update the source-destination mappings.

## Full sync mode

In this mode, RudderStack syncs **all** the records to the destination irrespective of whether they were updated or not. For example, if you have 10,000 records and only 2000 records were updated, RudderStack will still sync all the 10,000 records to the destination.

> ![warning](/docs/images/warning.svg)
> 
> Using the full sync mode will lead to a higher event usage as all the source records are sent to the destination in each sync.

Note that RudderStack supports the full sync mode for **all** destinations except the destinations that only support mirror mode.

## Sync behavior

This section describes how RudderStack syncs data to the destinations in the below scenarios:

### First sync

When you sync data from the Reverse ETL sources for the first time, RudderStack performs a full sync by default, **irrespective of the sync mode**.

For the subsequent syncs, RudderStack will:

  * Incrementally sync any new records since the last sync, in case of Upsert and Mirror modes.
  * Continue to sync all the records to the destination in case of Full sync mode.


You can also force a full data sync at any point using the [Reset History and Full Sync](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/start-stop-syncs/#start-and-stop-syncs>) functionality.

[![Reset History and Full Sync option](/docs/images/retl-sources/reset-history-full-sync.webp)](</docs/images/retl-sources/reset-history-full-sync.webp>)

### After updating mappings

> ![info](/docs/images/info.svg)
> 
> This section is applicable only for Upsert and Mirror modes, as RudderStack syncs all the data to the destination in Full sync mode regardless of whether mappings are updated or not.

RudderStack determines whether to run a full sync depending on whether a source-destination field mapping is added/updated or removed.

  * **If a mapping is removed** : RudderStack does not run a full sync. It continues to sync records incrementally as per the specified sync mode.
  * **If a mapping is added or updated** : RudderStack runs a full sync.


#### Example

Consider the following source-destination mappings:

Warehouse column| Destination field  
---|---  
`email`| `email_id`  
`first_name`| `fn`  
`last_name`| `ln`  
  
If you remove the mapping for `last_name` (mapped to `ln` field in the destination), then RudderStack continues to sync the source records to the destination as per the specified sync mode. It ignores the records for the `last_name` column as the mapping was removed.

Now if you add a new mapping (highlighted in bold) as follows:

Warehouse column| Destination field  
---|---  
`email`| `email_id`  
`first_name`| `fn`  
`last_name`| `ln`  
**`address`**| **`address`**  
  
In this case, RudderStack runs a full sync as it has to update all the records as per the new mapping.

## FAQ

#### What happens to the records that have not been successfully sent to the destination in the previous sync?

In case of an unsuccessful delivery, RudderStack retries sending the events in the next sync.