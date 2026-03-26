# Reverse ETL Quickstart Guide

Set up a Reverse ETL pipeline and sync your warehouse data to downstream destinations in no time.

* * *

  * __6 minute read

  * 


The easiest way to set up a Reverse ETL pipeline is to configure your warehouse source, connect it to a downstream destination, and specify the data mappings and sync settings.

> ![info](/docs/images/info.svg)
> 
> You can set up to 10 connections in the RudderStack Cloud [Free and Starter](<https://rudderstack.com/pricing/>) plans and unlimited connections in the [Growth and Enterprise](<https://rudderstack.com/pricing/>) plans.

For most use cases, you can set up and activate your Reverse ETL pipeline by following these steps:

  1. Add a source
  2. Add destination
  3. Define mappings
  4. Schedule syncs
  5. Activate connection


## Step 1: Add source

> ![info](/docs/images/info.svg)
> 
> RudderStack lets you set up a Reverse ETL source from a warehouse table, [Model](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/models/>), or [Audience](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/audiences/>).

  1. Sign in to your [RudderStack dashboard](<https://app.rudderstack.com/>) and click **\+ Add source** in the default **Connections** view.

[![Add source](/docs/images/get-started/quickstart/add-source.webp)](</docs/images/get-started/quickstart/add-source.webp>)

  2. Under **Sources** , click **Reverse ETL** and select your warehouse source.
  3. Configure your source. See the [source-specific documentation](<https://www.rudderstack.com/docs/sources/reverse-etl/#supported-reverse-etl-sources>) for configuration details.


> ![warning](/docs/images/warning.svg)
> 
> RudderStack requires some warehouse-specific permissions to sync data from it. These permissions are listed in the source documentation, for example, see [BigQuery permissions](<https://www.rudderstack.com/docs/sources/reverse-etl/google-bigquery/#granting-permissions>).
> 
> Make sure to grant these permissions **before** you set up the source.

## Step 2: Connect destination

Once you have set up the Reverse ETL source, the next step is to connect it to a downstream destination.

> ![success](/docs/images/tick.svg)
> 
> RudderStack supports syncing data to over 200 [Event Stream](<https://www.rudderstack.com/docs/destinations/streaming-destinations/>) and [Reverse ETL-only](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/>) destinations.

You can connect the Reverse ETL source to an existing or new [destination](<https://www.rudderstack.com/docs/destinations/overview/>) to start using it. To connect to a destination later, click **Done** on the top right.

[![Next steps](/docs/images/retl-sources/created-source.webp)](</docs/images/retl-sources/created-source.webp>)

You will then be redirected to the **Overview** page of the source where you get the option of connecting it to an existing or new destination.

[![Add destination](/docs/images/retl-sources/add-destination.webp)](</docs/images/retl-sources/add-destination.webp>)

See [Set up Reverse ETL Connections](<>) section for more information.

## Step 3: Create mappings

RudderStack provides two options to map your warehouse columns to specific destination fields before syncing your data:

  * [Map with Visualizer](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/visual-data-mapper/>)
  * [Map with JSON](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/json-data-mapping/>)


> ![info](/docs/images/info.svg)
> 
> RudderStack supports the **Map with Visualizer** option only for [selected destinations](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/visual-data-mapper/#supported-destinations>).
> 
> Other destinations that do not support Visual Data Mapper have the **Map with JSON** option by default, with the **Map with Visualizer** option greyed out.

The steps to set the data mappings (using JSON) are listed below:

  1. Select the **Sync mode** to specify how RudderStack syncs each record to the destination. RudderStack supports two [sync modes](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/>):

Sync mode| Description  
---|---  
Upsert| In this mode, RudderStack inserts new records and updates the existing records in the destination while syncing the data.  
Mirror| In this mode, RudderStack ‘mirrors’ the source by keeping the destination data the same as the source data. It performs insertion, deletion, and updates to the records while syncing the data.  
  
Note that:

  * Only [select destinations](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/#mirror-mode>) support this mode.
  * RudderStack does not support `track` event type for this mode.

  
  
  2. If you have set the sync mode to **Upsert** , you can also use the **Use cursor column** setting for managing incremental syncs. See [Cursor Column Support](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/cursor-column-support/>) guide for more information on this setting.

  3. Select the **Event Type** \- RudderStack supports sending the synced data to your downstream destinations as `identify` or `track` events.

     * If you select `track` as the **Event Type** , you also need to set the event name that is sent to the downstream destination. This is because every `track` event requires a name.
     * You can also set the column name as the event name by turning on the **Lookup event name by column** toggle and selecting the column from the dropdown:

[![Schema tab options in RudderStack](/docs/images/warehouse-actions-sources/event-name-table-track.webp)](</docs/images/warehouse-actions-sources/event-name-table-track.webp>)

  3. Set at least one user identifier from `user_id` or `anonymous_id` in the **Choose user identifier** setting.

[![Map with JSON feature](/docs/images/data-pipelines/map-with-json.webp)](</docs/images/data-pipelines/map-with-json.webp>)

  4. Preview the resulting data and make the necessary changes before proceeding.


## Step 4: Schedule syncs

RudderStack determines how and when to run a sync based on the [sync schedule](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-schedule-settings/>) you set for your Reverse ETL connection.

Schedule type| Description  
---|---  
Basic| Run syncs at a given time interval and specified time (in UTC).  
CRON| Run syncs based on a specified CRON expression (in UTC).  
Manual| Run syncs manually.  
  
## Step 5: Activate connection

Once your source and destination are set up, activate the connection by clicking **Turn on the connection**.

[![Turn on Reverse ETL connection](/docs/images/data-pipelines/turn-on-connection.webp)](</docs/images/data-pipelines/turn-on-connection.webp>)

Once you activate the connection, RudderStack automatically triggers the syncs as per the sync schedule.

> ![info](/docs/images/info.svg)
> 
> When you sync data from the source for the first time, RudderStack performs a full sync by default, irrespective of the sync mode you specified while setting the mappings. It then incrementally syncs any new data since the last sync.

### Trigger syncs

Go to the **Syncs** tab of your Reverse ETL source and click the **Sync Now** button to trigger a new sync. To force a full data sync, choose the **Reset History and Full Sync** option.

[![Trigger new syncs](/docs/images/data-pipelines/trigger-full-sync.webp)](</docs/images/data-pipelines/trigger-full-sync.webp>)

To stop a running sync, click the **Stop Now** button.

[![Stop syncs](/docs/images/data-pipelines/stop-sync.webp)](</docs/images/data-pipelines/stop-sync.webp>)

> ![warning](/docs/images/warning.svg)
> 
> Note the following before stopping a sync:
> 
>   * Once you stop a sync, any data that RudderStack reads from the warehouse and is on the fly may not be stopped or dropped from being delivered to the destination. It will only stop reading and sending any new data from the warehouse to the destination and stop the sync from progressing.
>   * For a very low number of deltas (new data since the last attempted sync), you may sometimes see a “0 deltas succeeded” after you stop the sync.
>   * Once you cancel a sync, the behavior of the next sync depends on the type of the previously cancelled sync. For example, if a cancelled sync is an incremental sync, then the next sync will be incremental too. Similarly, if the cancelled is a full sync, then the next sync will be a full sync.
> 


### Update your mappings

In cases where your warehouse schema has changed, RudderStack lets you update the mappings to ensure the data is synced to the destination correctly.

Go to the **Schema** tab of your connection page and click **Update** to update your mappings. Make sure to save the updated mappings.

> ![warning](/docs/images/warning.svg)
> 
> You cannot update the mappings while a sync is in progress.

[![Update connection mappings](/docs/images/data-pipelines/update-mappings.webp)](</docs/images/data-pipelines/update-mappings.webp>)

## Sync data from SQL models

RudderStack’s [Models](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/models/>) feature lets you create models by defining custom SQL queries. You can then run these queries on your warehouse and send the resulting data to specific destinations.

Follow these steps to set up a Reverse ETL pipeline using a model:

  1. [Create a new model](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/models/#create-model>)
  2. [Connect the model to a destination](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/models/#connect-model-to-destination>)
  3. [Set up the data mappings](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/json-data-mapping/>)


## Sync data from Audiences

RudderStack’s [Audiences](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/audiences/>) feature lets you create customer lists or a subset of users satisfying specific criteria with easy-to-use filters on your warehouse tables. Once created, you can connect and activate them in your downstream destinations.

Follow these steps to set up a Reverse ETL pipeline using an audience:

  1. [Set up a new audience](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/audiences/#create-audience>)
  2. [Connect the audience source to a destination](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/audiences/#connect-audience>)
  3. [Set up the data mappings](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/json-data-mapping/>)