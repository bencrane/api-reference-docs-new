# FAQ

Answers to some of the commonly asked questions on the Reverse ETL feature.

* * *

  * __4 minute read

  * 


## Reverse ETL feature

#### How do I use the Reverse ETL feature?

RudderStack’s Reverse ETL feature lets you set up your data warehouse as a source in RudderStack and route the data residing in it to your preferred destination.

To use this feature, follow these steps:

  1. Set up a Reverse ETL source in RudderStack.
  2. Connect it to a new or existing destination.
  3. Specify the warehouse data you want to sync to that destination.


#### What is the difference between the Table, Model, and Audience options when creating a Reverse ETL source?

When creating a new Reverse ETL source, you are presented with the following three options from which RudderStack syncs the source data:

[![](/docs/images/warehouse-actions-sources/table-model-audience-options.webp)](</docs/images/warehouse-actions-sources/table-model-audience-options.webp>)

  * When you choose **Table** , RudderStack imports all data associated with the specified warehouse table during the sync.
  * When you choose **Model** , RudderStack imports the data by running the query specified in the connected [model](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/models/>) during the sync.
  * When you choose **Audience** , RudderStack syncs the [audience](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/audiences/>) you created in the RudderStack dashboard.


> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * [MySQL](<https://www.rudderstack.com/docs/sources/reverse-etl/mysql/>) and [PostgreSQL](<https://www.rudderstack.com/docs/sources/reverse-etl/postgresql/>) sources support syncing data only from a warehouse table and model. Hence, you will not see the **Audience** option while setting up this source.
>   * [S3](<https://www.rudderstack.com/docs/sources/reverse-etl/amazon-s3/>) supports syncing data only from your S3 bucket.
> 


#### Can I use Reverse ETL to ingest streaming data from the warehouse?

Reverse ETL does not support ingesting streaming data. It is not built to handle the rapidly changing data in the warehouse.

#### Can I connect a Reverse ETL source to multiple destinations?

Yes — RudderStack supports connecting a Reverse ETL source to multiple destinations.

> ![info](/docs/images/info.svg)
> 
> **Event usage/billing in 1:many connections**
> 
> When sending data from a Reverse ETL source to multiple destinations, RudderStack sends the record to each destination separately — this means you will be charged on a **per connection basis**.

See [Set Up Reverse ETL Connection](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/retl-connection-setup/>) for more information on connecting your Reverse ETL sources to destinations in RudderStack.

#### Can I connect multiple Reverse ETL sources to a single destination?

RudderStack supports connecting **multiple** Reverse ETL sources to a single downstream destination. However, this feature is available only for the below destinations currently — support for more integrations is coming soon.

[![Facebook Custom Audience logo](/docs/images/logos/destinations/facebook.svg)Facebook Custom Audience](</docs/destinations/reverse-etl-destinations/facebook-custom-audience/>)[![Google Ads Remarketing Lists \(Customer Match\) logo](/docs/images/logos/destinations/googleads.svg)Google Ads Remarketing Lists (Customer Match)](</docs/destinations/reverse-etl-destinations/google-ads-remarketing-lists/>)

  


#### Can I connect a warehouse source to a warehouse destination in RudderStack?

No - RudderStack does not support connecting a Reverse ETL (warehouse) source to a warehouse destination.

#### Why can’t I add a Reverse ETL source to an already configured destination?

The Reverse ETL feature supports only source-driven configuration of your pipeline. So, you need to configure a new or existing Reverse ETL source in RudderStack and then connect it to a new or existing destination.

## Data syncs

#### What is the `_RUDDERSTACK` schema used for?

RudderStack uses the `_RUDDERSTACK` schema (`rudderstack_` for [BigQuery](<https://www.rudderstack.com/docs/sources/reverse-etl/google-bigquery/#creating-the-rudderstack-schema-and-granting-permissions>)) created in your warehouse to store the state of each data sync. Hence, you should not change this name.

> ![info](/docs/images/info.svg)
> 
> You are required to create this schema in your warehouse (for example, [Snowflake](<https://www.rudderstack.com/docs/sources/reverse-etl/snowflake/#creating-the-rudderstack-schema-and-granting-permissions>)) before setting up the [Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) in RudderStack.

#### How much time does it take for the synced data to appear in the destination?

RudderStack sends the records to the destination pretty quickly. It takes around a couple of minutes in most cases but it may take longer depending on the destination type. However, the sync metrics may take some more time (around 10 minutes) to reflect in the RudderStack dashboard.

If you see a prompt on the sync stating “Records sent to destination, finalizing sync stats”, it indicates that the records have successfully reached the destination.

## Event replay

#### Can I replay data from a Reverse ETL source in case of failure?

RudderStack does not support [replaying data](<https://www.rudderstack.com/docs/user-guides/administrators-guide/event-replay/>) from Reverse ETL sources.

## Sync modes and schedule settings

#### What is the difference between Basic, CRON, and Manual schedule settings?

When creating a new Reverse ETL source, RudderStack lets you [schedule](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-schedule-settings/>) your data imports and define how and when the data syncs will run.

RudderStack defines the following three sync schedule types:

Schedule type| Description  
---|---  
Basic| Runs syncs at a user-specified time and interval.  
CRON| Runs syncs based on a user-defined CRON expression.  
Manual| User triggers the data syncs manually.  
  
#### What is the difference between Upsert and Mirror mode when syncing data?

RudderStack supports two [sync modes](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/>) (available based on the source and the chosen destination) that let you define how you want to sync your data. These are **Upsert** and **Mirror** mode.

  * In the **Upsert** mode, RudderStack supports insertion of new records and updates to the existing records, while syncing data to the destination.
  * In the **Mirror** mode, RudderStack ‘mirrors’ the source by keeping the destination data the same as the source data. It performs insertion, updates, and deletion of records while syncing data to the destination.


#### What is the difference between the Full and Incremental sync types?

The sync type determines the scope of the sync. It can be one of the following:

  * **Incremental** : RudderStack syncs only the newly added data in the warehouse since the last sync.
  * **Full** : RudderStack syncs all the data present in the warehouse, irrespective of whether it was synced to the destination previously.