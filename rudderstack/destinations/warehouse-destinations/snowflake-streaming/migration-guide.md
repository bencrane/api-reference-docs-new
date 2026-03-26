# Snowflake Streaming Migration Guide

Learn how to migrate from RudderStack’s Snowflake batch destination to the low-latency Snowflake Streaming destination.

Available Plans

  * starter
  * growth
  * enterprise


* * *

  *  __19 minute read

  * 


This guide walks you through migrating from RudderStackʼs [Snowflake batch destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/>) to the newer, low-latency [Snowflake Streaming destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake-streaming/>).

> ![warning](/docs/images/warning.svg)
> 
> Review the Important considerations before you start the migration.

## Overview

This guide contains the steps to migrate to the Snowflake Streaming destination in the below two scenarios:

  * Assisted migration: Seamless migration using the assisted migration feature within your Snowflake batch destination

  * Manual migration: Manual migration in the following two scenarios — in both cases, there may be duplicate events which you can handle post-migration:

    * Namespace is configured in Snowflake batch destination
    * Namespace is empty in Snowflake batch destination


## Important considerations

Before you start the migration process, make sure to go through the limitations and post-migration considerations explained in this section.

### Limitations

This section covers the limitations of the Snowflake Streaming destination integration.

#### Merge mode support

The Snowflake Streaming destination **does not support** merge mode. The Snowpipe Streaming API only supports **inserts** and writes rows directly into tables to reduce latency.

See the [Snowpipe Streaming documentation](<https://docs.snowflake.com/en/user-guide/snowpipe-streaming/data-load-snowpipe-streaming-overview#insert-only-operations>) for more information.

#### `users` table support

The Snowflake Streaming destination **does not support** the [`users`](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#table-users>) table.

> ![info](/docs/images/info.svg)
> 
> RudderStack maintains the `users` table by merging user traits. Since the Snowpipe Streaming API only supports inserts (no merge operations), the `users` table cannot be maintained.

For **Identity Stitching** , see RudderStack’s [Profiles](<https://www.rudderstack.com/docs/profiles/overview/>) product where you can create a more comprehensive identity graph around users.

#### JSON column support

If you have enabled the [JSON Column Support](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/json-column-support/>) feature at the [event level](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/json-column-support/#1-at-the-event-level>), then you will need to change your warehouse integration configuration from `SNOWFLAKE` to `ALL`.
    
    
    "integrations": {
      "SNOWFLAKE": {
        "options": {
          "jsonPaths": ["track.properties.testMap.nestedMap", "track.context.ctestMap.cnestedMap"]
        }
      }
    }
    
    
    
    "integrations": {
      "ALL": {
        "options": {
          "jsonPaths": ["track.properties.testMap.nestedMap", "track.context.ctestMap.cnestedMap"]
        }
      }
    }
    

### Compute costs after migration

As a best practice, RudderStack recommends running deduplication queries on the target tables after you migrate to Snowflake Streaming. Therefore, the compute cost of migrating will be affected by:

  * The number of target tables
  * The total duration of time it took to migrate
  * Total record count across your deduplication queries


## Assisted migration

> ![info](/docs/images/info.svg)
> 
> The assisted migration feature is only supported for Snowflake batch destinations that have key-pair authentication enabled.

If you’re currently using RudderStack’s traditional Snowflake batch destination and want to upgrade to real-time streaming, the new assisted migration feature makes the transition seamless and safe with step-by-step guidance.

### How assisted migration works

> ![success](/docs/images/tick.svg)
> 
> With the assisted migration feature, you maintain control throughout the migration process with the ability to rollback changes with no data loss if there are any validation or event delivery errors in the newly created Snowflake Streaming destination(s).

The assisted migration process guides you through each step to ensure a smooth transition:

  1. **Initiate migration** : You will see a banner at the top of your existing batch destination. Within the banner, click **Proceed** and the process will be initiated.

[![Snowflake Batch Migration Banner](/docs/images/dw-integrations/snowflake_migration_banner.webp)](</docs/images/dw-integrations/snowflake_migration_banner.webp>)

  2. **Automatic destination setup** : RudderStack creates and configures your new Snowflake Streaming destination(s) using your existing batch destination credentials and configuration, preserving your schema and table mappings.
  3. **Verify streaming** : The wizard will prompt you to review and validate that your new Snowflake Streaming destination is receiving data correctly
  4. **Trigger final sync** : The wizard will then trigger a final sync from the Snowflake batch destination. You can open a new tab to verify that the final sync succeeds with no errors.
  5. **Complete migration** : Run deduplication queries on demand when you’re ready to finalize the process. RudderStack will expose the start and end timestamps of the migration process within the wizard so that you can use them for the deduplication queries.


> ![info](/docs/images/info.svg)
> 
> Deduplication queries are necessary to run only on the duration of time it took to start and complete the migration. RudderStack provides the timestamps to use for the deduplication queries if you used the assisted migration feature.

After the migration is complete, you can safely delete your old Snowflake batch destination if desired.

### Get started

To upgrade, visit your existing Snowflake destination in the RudderStack dashboard and look for the **Migrate to Snowflake Streaming** banner to begin the assisted migration process.

For manual migration instructions, see the rest of the sections below.

## Manual migration

The following sections cover the details of manually migrating from your Snowflake batch destination to a new Snowflake Streaming destination.

### Case 1: Namespace configured in Snowflake destination

If you defined the [Namespace](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/#connection-settings:~:text=User%20setting%20above.-,Namespace,-%3A%20Enter%20the%20schema>) setting while creating your Snowflake destination, you will need to migrate it to use Snowflake Streaming.

RudderStack provides the following two options for this migration process:

  1. Ingest data to the same schema and then disable the Snowflake batch destination (**Recommended**)
  2. Ingest data to a new schema and backfill


#### 1: Ingest data to same schema and disable Snowflake destination

> ![info](/docs/images/info.svg)
> 
> RudderStack recommends using the same schema for the Snowflake Streaming destination as Snowflake allows concurrent writes on tables — this way, your downstream reporting and modeling will be unaffected.

In this option, you will need to:

  1. Set up and pre-validate a new connection using Snowflake Streaming.
  2. Migrate all sources connected to the Snowflake batch destination to the new Snowflake Streaming destination.


> ![warning](/docs/images/warning.svg)
> 
> For the duration of migration, **both** the Snowflake batch destination and Snowflake Streaming destination will ingest data to same tables.

  3. Turn off the Snowflake batch destination.
  4. Clean up the duplicate entries.


##### **Pre-validation**

The pre-validation steps ensure that switching sources from Snowflake batch to Snowflake Streaming does not cause any issues. It is similar to setting up a demo Snowflake Streaming destination and validating the syncs, table schema, and data type.

Follow these steps for pre-validation:

  1. Set up a Snowflake Streaming destination with a **new temporary schema** (configured using the [Namespace setting](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake-streaming/#connection-settings>)). For example, if your Snowflake batch destination namespace is `MY_PROD_DATA`, you can choose `MY_PROD_DATA_TEST_STREAMING` as the new schema name.


> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * A new temporary schema is only used for validation — you will need to delete it after the validation is complete.
>   * Make sure to consider all relevant [advanced settings](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/#advanced-settings>) configured in the Snowflake batch destination like **JSON columns** , **Skip Tracks Table** , etc.
>   * The [**Skip Users Table**](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/#advanced-settings>) setting available in the Snowflake batch destination is not supported for Snowflake Streaming.
> 


  2. To maintain data types for tables created in the Snowflake destination, RudderStack recommends creating all tables in the new schema beforehand. This ensures validation of the Snowflake Streaming ingestion once you direct the data ingestion from the existing schema of the Snowflake batch destination.


    
    
    CREATE SCHEMA IF NOT EXISTS MY_PROD_DATA_TEST_STREAMING;
    
    DECLARE
      t_name STRING;
      records RESULTSET;
    BEGIN
        records := (SELECT table_name FROM <DB>.INFORMATION_SCHEMA.TABLES WHERE table_type = 'BASE TABLE' AND table_schema = 'MY_PROD_DATA');
        FOR record IN records DO
            t_name := record.table_name;
            EXECUTE IMMEDIATE 
                'CREATE TABLE MY_PROD_DATA_TEST_STREAMING."' || t_name || 
                '" LIKE MY_PROD_DATA."' || t_name || '";';
        END FOR;
    END;
    

In the above query, replace `<DB>` with your database name.

  3. Follow these steps for **all** sources connected to the Snowflake batch destination that you want to migrate to Snowflake Streaming:

     * Connect the source to the Snowflake Streaming destination. **Do not disconnect** this source from the Snowflake batch destination.
     * Validate successful event delivery from the **Events** tab in the Snowflake Streaming destination page.
  4. After successful validation, disconnect **all** sources from the Snowflake Streaming destination and then delete this test destination.


##### **Migration**

After testing the Snowflake Streaming destination with a similar setup as the Snowflake batch destination, follow these steps for migration:

  1. Set up a Snowflake Streaming destination with same configuration as the Snowflake batch destination, including [Namespace](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/#connection-settings:~:text=User%20setting%20above.-,Namespace,-%3A%20Enter%20the%20schema>), [advanced settings](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/#advanced-settings>), etc.

  2. Connect all sources connected to the Snowflake batch destination to the new Snowflake Streaming destination. Note the time `T_start` (in UTC) you started this action — this will come in handy in running the deduplication queries later.

  3. Validate that data ingestion for all sources is working as expected for the Snowflake Streaming destination.


> ![info](/docs/images/info.svg)
> 
> This process can take a few hours — during this time, both the Snowflake batch destination and Snowflake Streaming destination will ingest the same data.

  4. Go to your Snowflake batch destination and change the [Sync Frequency](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/#connection-settings:~:text=the%20namespace%20later.-,Sync%20Frequency,-%3A%20Specify%20how%20often>) to **1 day**.
  5. Go to the **Syncs** tab of the Snowflake batch destination and click **Sync Now**. Wait for any syncs in progress to complete. Then, take a note of the time `T_end` (in UTC) — this will come in handy while running the deduplication queries later.

[![Sync now button for Snowflake destination](/docs/images/dw-integrations/snowflake-sync-now.webp)](</docs/images/dw-integrations/snowflake-sync-now.webp>)

  6. Disconnect all sources from the Snowflake destination now that they are already connected to the Snowflake Streaming destination (as in Step 2).
  7. Run the following deduplication script for **each table** :


    
    
    -- Set your timestamp range
    SET T_start = '2024-01-01 00:00:00';
    SET T_end = '2024-12-31 23:59:59';
    
    -- Start transaction
    BEGIN;
    
    -- Step 1: Create temp table with latest row for each duplicate ID in range
    CREATE OR REPLACE TEMP TABLE TEMP_<TABLE_NAME> AS
    SELECT *
    FROM <TABLE_NAME>
    WHERE TIMESTAMP BETWEEN $T_start AND $T_end
    QUALIFY ROW_NUMBER() OVER (PARTITION BY ID ORDER BY TIMESTAMP DESC) = 1
    AND ID IN (
      SELECT ID
      FROM <TABLE_NAME>
      WHERE TIMESTAMP BETWEEN $T_start AND $T_end
      GROUP BY ID
      HAVING COUNT(*) > 1
    );
    
    -- Step 2: Delete all rows for those duplicate IDs in the range from source table.
    DELETE FROM <TABLE_NAME>
    WHERE ID IN (
      SELECT ID FROM TEMP_<TABLE_NAME>
    )
    AND TIMESTAMP BETWEEN $T_start AND $T_end;
    
    -- Step 3: Insert back the unique rows into source table
    INSERT INTO <TABLE_NAME>
    SELECT * FROM TEMP_<TABLE_NAME>;
    
    -- Commit transaction
    COMMIT;
    

In the above query, replace `<TABLE_NAME>` with the name of the table for which you want to deduplicate data. Note that `DB.SCHEMA` has not been added in the above SQL, considering you can set it while executing the query from the Snowflake console.

#### 2\. Ingest data to new schema and backfill

This method lets you safely set up a new Snowflake Streaming connection with a new namespace **without impacting** the existing Snowflake connection.

After the validations, you can disable the old Snowflake batch destination and backfill the corresponding table data while handling duplicates.

> ![warning](/docs/images/warning.svg)
> 
> **Impact on downstream reporting and modeling**
> 
> If you are using this approach for migration (implementing a new schema where your data lands), downstream modeling and reporting will be impacted — you will need to update them to point to the new schema.

  1. Set up a Snowflake Streaming destination with a **new schema** (configured using the [Namespace setting](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake-streaming/#connection-settings>)). For example, if your Snowflake batch destination namespace is `MY_PROD_DATA`, you can choose `MY_PROD_DATA_TEST_STREAMING` as the new schema name.


> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * Make sure to consider all relevant [advanced settings](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/#advanced-settings>) configured in the Snowflake batch destination like **JSON columns** , **Skip Tracks Table** , etc.
>   * The [**Skip Users Table**](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/#advanced-settings>) setting available in the Snowflake batch destination is not supported for Snowflake Streaming.
> 


  2. Follow these steps for **all** sources connected to the Snowflake batch destination that you want to migrate to Snowflake Streaming.

     * Connect the source to the Snowflake Streaming destination. **Do not disconnect** this source from the Snowflake batch destination.
     * Validate successful event delivery from the **Events** tab in the Snowflake Streaming destination page.
     * Note that there are chances of a change in the data type of some columns — this is because the column’s data type is inferred from the first event and it evolves if you changed the data type manually in the tables created from the Snowflake batch destination. If the old data types were correct, you can update them accordingly for the new tables in your new schema.


> ![info](/docs/images/info.svg)
> 
> RudderStack recommends connecting **all** sources to the Snowflake Streaming destination. This is because multiple sources might ingest data to the same table. Also, there is a chance that multiple sources might generate the same event name.
> 
> Migrating all sources will make the backfilling process easier by considering all tables.

  3. Once you connect all sources to the new Snowflake Streaming destination and validate schemas of all tables, go to the **Syncs** tab of the Snowflake batch destination and click **Sync Now** to flush any data to be synced.

[![Sync now button for Snowflake destination](/docs/images/dw-integrations/snowflake-sync-now.webp)](</docs/images/dw-integrations/snowflake-sync-now.webp>)

  4. After the sync completes, disconnect all the sources and disable the Snowflake batch destination.


##### **Backfilling process**

You can backfill the data by following these steps:

  1. Insert all data from the Snowflake batch destination schema to the respective tables in the Snowflake Streaming destination schema.
  2. Remove duplicates by running the following query for **each table** :


    
    
    -- Set your timestamp range
    SET T_start = '2024-01-01 00:00:00';
    SET T_end = '2024-12-31 23:59:59';
    
    -- Start transaction
    BEGIN;
    
    -- Step 1: Create temp table with latest row for each duplicate ID in range
    CREATE OR REPLACE TEMP TABLE TEMP_<TABLE_NAME> AS
    SELECT *
    FROM <TABLE_NAME>
    WHERE TIMESTAMP BETWEEN $T_start AND $T_end
    QUALIFY ROW_NUMBER() OVER (PARTITION BY ID ORDER BY TIMESTAMP DESC) = 1
    AND ID IN (
      SELECT ID
      FROM <TABLE_NAME>
      WHERE TIMESTAMP BETWEEN $T_start AND $T_end
      GROUP BY ID
      HAVING COUNT(*) > 1
    );
    
    -- Step 2: Delete all rows for those duplicate IDs in the range from source table.
    DELETE FROM <TABLE_NAME>
    WHERE ID IN (
      SELECT ID FROM TEMP_<TABLE_NAME>
    )
    AND TIMESTAMP BETWEEN $T_start AND $T_end;
    
    -- Step 3: Insert back the unique rows into source table
    INSERT INTO <TABLE_NAME>
    SELECT * FROM TEMP_<TABLE_NAME>;
    
    -- Commit transaction
    COMMIT;
    

Replace `<TABLE_NAME>` in the above query with the name of the table for which you want to deduplicate data.

### Case 2: Namespace empty in Snowflake destination

If the [Namespace](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/#connection-settings:~:text=User%20setting%20above.-,Namespace,-%3A%20Enter%20the%20schema>) setting is not configured in the Snowflake batch destination, then each source connected to the destination creates its own schema using the source name.

> ![warning](/docs/images/warning.svg)
> 
> In this scenario, you will need to create a new Snowflake Streaming destination with the expected schema name (Namespace) for **each source** connected to the Snowflake batch destination.
> 
> You can get the schema name from the warehouse directly or from the **Syncs** tab of your Snowflake batch destination.

RudderStack provides the following two options for this migration process:

  1. Ingest data to the same schema and then disable the Snowflake batch destination (**Recommended**)
  2. Ingest data to a new schema and backfill


#### 1: Ingest data to same schema and disable Snowflake destination

> ![info](/docs/images/info.svg)
> 
> RudderStack recommends using the same schema for the Snowflake Streaming destination as Snowflake allows concurrent writes on tables — this way, your downstream reporting and modeling will be unaffected.

In this option, you will need to:

  1. Pre-validate a new connection using Snowflake Streaming.
  2. Migrate all sources connected to the Snowflake batch destination to the new Snowflake Streaming destination.


> ![warning](/docs/images/warning.svg)
> 
> For some time, **both** the Snowflake batch destination and Snowflake Streaming destination will ingest data to same tables.

  3. Turn off the Snowflake batch destination.
  4. Clean up the duplicate entries.


##### **Pre-validation**

  1. Set up a Snowflake Streaming destination with the **same temporary schema** (configured using the [Namespace setting](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake-streaming/#connection-settings>)) as the schema for the old connection (derived from the source name). You can add a `_test_streaming` suffix to the schema name as a pre-validation step.


> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * A new temporary schema is only used for validation — you will need to delete it after the validation is complete.
>   * Make sure to consider all relevant [advanced settings](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/#advanced-settings>) configured in the Snowflake batch destination like **JSON columns** , **Skip Tracks Table** , etc.
>   * The [**Skip Users Table**](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/#advanced-settings>) setting available in the Snowflake batch destination is not supported for Snowflake Streaming.
> 


  2. Verify that the data ingestion is working correctly and data is populated in the new tables in the schema corresponding to source name.


> ![info](/docs/images/info.svg)
> 
> As some data types can be different, RudderStack recommends comparing the columns and data types for all tables in the Snowflake Streaming schema with the Snowflake batch destination schema.

  3. Disconnect the source and delete the test Snowflake Streaming destination.
  4. Delete the new schema and tables created in the warehouse.


##### **Migration**

After testing the Snowflake Streaming destination with a similar setup as the Snowflake batch destination, follow these steps for migration:

  1. Set up a Snowflake Streaming destination with the **exact configuration** as the Snowflake batch destination, including the [advanced settings](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/#advanced-settings>). Make sure to set the [Namespace](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake-streaming/#connection-settings>) setting as the schema for the old connection (derived from the source name).
  2. Connect the source to Snowflake Streaming destination. Note the time `T_start` (in UTC) when you started this action — this will come in handy while running the deduplication queries later.
  3. Validate that data ingestion for all sources is working as expected for the Snowflake Streaming destination.


> ![info](/docs/images/info.svg)
> 
> This process can take a few hours — during this time, both the Snowflake batch destination and Snowflake Streaming destination will ingest the same data.

  4. Go to your Snowflake batch destination and change the [Sync Frequency](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/#connection-settings:~:text=the%20namespace%20later.-,Sync%20Frequency,-%3A%20Specify%20how%20often>) to **1 day**.
  5. Go to the **Syncs** tab of the Snowflake batch destination and click **Sync Now**. Wait for any syncs in progress to complete. Then, take a note of the time `T_end` (in UTC) — this will come in handy while running the deduplication queries later.

[![Sync now button for Snowflake destination](/docs/images/dw-integrations/snowflake-sync-now.webp)](</docs/images/dw-integrations/snowflake-sync-now.webp>)

  6. Run the following deduplication script for **each table** :


    
    
    -- Set your timestamp range
    SET T_start = '2024-01-01 00:00:00';
    SET T_end = '2024-12-31 23:59:59';
    
    -- Start transaction
    BEGIN;
    
    -- Step 1: Create temp table with latest row for each duplicate ID in range
    CREATE OR REPLACE TEMP TABLE TEMP_<TABLE_NAME> AS
    SELECT *
    FROM <TABLE_NAME>
    WHERE TIMESTAMP BETWEEN $T_start AND $T_end
    QUALIFY ROW_NUMBER() OVER (PARTITION BY ID ORDER BY TIMESTAMP DESC) = 1
    AND ID IN (
      SELECT ID
      FROM <TABLE_NAME>
      WHERE TIMESTAMP BETWEEN $T_start AND $T_end
      GROUP BY ID
      HAVING COUNT(*) > 1
    );
    
    -- Step 2: Delete all rows for those duplicate IDs in the range from source table.
    DELETE FROM <TABLE_NAME>
    WHERE ID IN (
      SELECT ID FROM TEMP_<TABLE_NAME>
    )
    AND TIMESTAMP BETWEEN $T_start AND $T_end;
    
    -- Step 3: Insert back the unique rows into source table
    INSERT INTO <TABLE_NAME>
    SELECT * FROM TEMP_<TABLE_NAME>;
    
    -- Commit transaction
    COMMIT;
    

In the above query, replace `<TABLE_NAME>` with the name of the table for which you want to deduplicate data. Note that `DB.SCHEMA` has not been added in the above SQL, considering you can set it while executing the query from the Snowflake console.

#### 2\. Ingest data to new schema and backfill

This method lets you safely set up a new Snowflake Streaming connection for a source to start writing data to tables in new schema. You can do this by setting a different namespace in the Snowflake Streaming streaming destination.

> ![warning](/docs/images/warning.svg)
> 
> **Impact on downstream reporting and modeling**
> 
> If you are using this approach for migration (implementing a new schema where your data lands), downstream modeling and reporting will be impacted — you will need to update them to point to the new schema.

  1. Set up a Snowflake Streaming destination with a **new schema** (configured using the [Namespace setting](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake-streaming/#connection-settings>)). For example, if the schema derived from the source name is `MY_PROD_DATA`, then you can choose `MY_PROD_DATA_STREAMING` as the new schema name.


> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * Make sure to consider all relevant [advanced settings](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/#advanced-settings>) configured in the Snowflake batch destination like **JSON columns** , **Skip Tracks Table** , etc.
>   * The [**Skip Users Table**](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/#advanced-settings>) setting available in the Snowflake batch destination is not supported for Snowflake Streaming.
> 


  2. Follow these steps for **all** sources connected to the Snowflake batch destination that you want to migrate to Snowflake Streaming:

     * Connect the source to the Snowflake Streaming destination. **Do not disconnect** this source from the Snowflake batch destination.
     * Validate successful event delivery from the **Events** tab in the Snowflake Streaming destination page.
     * Verify the columns and data types for all tables with the tables created from the Snowflake batch destination.


> ![info](/docs/images/info.svg)
> 
> RudderStack recommends connecting **all** sources to the Snowflake Streaming destination. This is because multiple sources might ingest data to the same table. Also, there is a chance that multiple sources might generate the same event name.
> 
> Migrating all sources will make the backfilling process easier by considering all tables.

  3. Once you connect all sources to the new Snowflake Streaming destination and validate schemas of all tables, go to your Snowflake batch destination and change the [Sync Frequency](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/#connection-settings:~:text=the%20namespace%20later.-,Sync%20Frequency,-%3A%20Specify%20how%20often>) to **1 day**.

  4. Go to the **Syncs** tab of the Snowflake batch destination and click **Sync Now** to flush any data to be synced.


[![Sync now button for Snowflake destination](/docs/images/dw-integrations/snowflake-sync-now.webp)](</docs/images/dw-integrations/snowflake-sync-now.webp>)

  5. After the sync completes, disconnect all the sources and disable the Snowflake batch destination.


##### **Backfilling process**

You can backfill the data by following these steps:

  1. Insert all data from the Snowflake batch destination schema to the respective tables in the Snowflake Streaming destination schema.
  2. Remove duplicates by running the following query for **each table** :


    
    
    -- Set your timestamp range
    SET T_start = '2024-01-01 00:00:00';
    SET T_end = '2024-12-31 23:59:59';
    
    -- Start transaction
    BEGIN;
    
    -- Step 1: Create temp table with latest row for each duplicate ID in range
    CREATE OR REPLACE TEMP TABLE TEMP_<TABLE_NAME> AS
    SELECT *
    FROM <TABLE_NAME>
    WHERE TIMESTAMP BETWEEN $T_start AND $T_end
    QUALIFY ROW_NUMBER() OVER (PARTITION BY ID ORDER BY TIMESTAMP DESC) = 1
    AND ID IN (
      SELECT ID
      FROM <TABLE_NAME>
      WHERE TIMESTAMP BETWEEN $T_start AND $T_end
      GROUP BY ID
      HAVING COUNT(*) > 1
    );
    
    -- Step 2: Delete all rows for those duplicate IDs in the range from source table.
    DELETE FROM <TABLE_NAME>
    WHERE ID IN (
      SELECT ID FROM TEMP_<TABLE_NAME>
    )
    AND TIMESTAMP BETWEEN $T_start AND $T_end;
    
    -- Step 3: Insert back the unique rows into source table
    INSERT INTO <TABLE_NAME>
    SELECT * FROM TEMP_<TABLE_NAME>;
    
    -- Commit transaction
    COMMIT;
    

Replace `<TABLE_NAME>` in the above query with the name of the table for which you want to deduplicate data.

## Choose the best migration strategy

RudderStack provides the following approaches for both the manual migration scenarios discussed above and the best approach depends on your use case:

  * **Ingest data to the same schema and deduplicate** : This approach is ideal if you want to avoid schema changes and minimize disruptions to the existing workflows and downstream modeling.
  * **Ingest data to a new schema and backfill** : This approach is ideal for customers planning for schema optimizations or prioritizing data freshness and clean separation.


## FAQ

#### How does RudderStack configure the schema name before loading the data in the warehouse?

RudderStack configures the schema name based on the values mentioned in the below table. The table columns are defined as follows:

  * **Sync** : Indicates whether RudderStack performs the first data sync after the source is set up or the subsequent syncs.
  * **Namespace** : The **Namespace** field set by the user while configuring the warehouse destination in the RudderStack dashboard.
  * **Warehouse. <destType>.customDataset Prefix**: The `RSERVER_WAREHOUSE_(DEST_TYPE)_CUSTOM_DATA_SET_PREFIX` parameter in the `config.yaml` file, in case the user has a RudderStack deployment locally/in their own environment.
  * **Source name** : Name of the source connected to the warehouse destination.

Sync| Namespace| `customDataset` Prefix| Source name| Schema name| Notes  
---|---|---|---|---|---  
First sync| AB| XY| S| AB| The namespace is given priority over all the other values.  
First sync| Not set| XY| S| XY_S| RudderStack combines the `customDataset` prefix and the source name to set the schema name, if the namespace is absent.  
First sync| Not set| Not set| S| S| RudderStack sets the source name as the schema name if the namespace and `customDataset` prefix are absent.  
First sync| AB| Not set| S| AB| The namespace is given priority over the other values.  
Second sync onwards| ABC| XYZ| SS| ABC| The namespace, source name and the `customDataset` prefix have all been modified. The new namespace is given priority and set as the schema name.  
  
All the data from the second sync will now be stored in the new schema (ABC) and the original schema (AB) will be left as is.  
Second sync onwards| Not set| XYZ| S| XYZ_S| The `customDataset` prefix name has been modified.  
  
RudderStack combines the `customDataset` prefix and the source name to set the schema name.  
Second sync onwards| Not set| XYZ| SS| XYZ_SS| The source name and `customDataset` prefix have been modified.  
  
RudderStack combines them together to set the schema name.  
Second sync onwards| ABC| Not set| SS| ABC| The namespace and source names have been modified.  
  
The namespace is given priority and set as the schema name.  
Second sync onwards| Not set| Not set| SS| S| The source name has been modified. However, it does not impact the schema name and it remains the same as in the first sync.  
  
> ![info](/docs/images/info.svg)
> 
> **Key takeaways**
> 
>   * The namespace set in the RudderStack dashboard always takes precedence when setting the schema name in the warehouse.
>   * If the `RSERVER_WAREHOUSE_(DEST_TYPE)_CUSTOM_DATA_SET_PREFIX` parameter is set in the `config.yaml` file of your RudderStack deployment, RudderStack sets the schema name in the `customDataset_sourcename` format, as noted in this FAQ.
>   * If the namespace and `RSERVER_WAREHOUSE_(DEST_TYPE)_CUSTOM_DATA_SET_PREFIX` parameter, both are absent, RudderStack sets the source name as the schema name.
>