# How to Migrate from Standard Snowflake Streaming to Iceberg

Migrate an existing Snowflake Streaming destination to Snowflake-managed Iceberg tables and optionally backfill historical data.

Available Plans

  * starter
  * growth
  * enterprise


* * *

  *  __5 minute read

  * 


If you already use the Snowflake Streaming destination **without** Iceberg, you can migrate to Snowflake-managed Iceberg tables by creating a new destination and, optionally, backfilling historical data.

This guide will help you:

  * Create a new Snowflake Streaming destination with Iceberg enabled
  * Route the same sources to the new destination
  * Optionally copy historical data from your existing tables into the new Iceberg tables
  * Decommission the old destination once you complete the migration


> ![info](/docs/images/info.svg)
> 
> **There is no automatic migration from standard Snowflake Streaming to Iceberg.**
> 
> Your existing destination continues to work unchanged until you disable or remove it.

## Understand the migration model

Migration from standard Snowflake Streaming to Iceberg works as follows:

  * You create a new Snowflake Streaming destination with [Create Iceberg Tables](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake-streaming/iceberg-tables/configuration/#4-enable-iceberg-and-specify-the-external-volume>) setting toggled on
  * New events flow into Iceberg tables stored as Parquet files in your external volume
  * **Optional** : You can backfill historical data from your existing Snowflake Streaming tables into the new Iceberg tables
  * You keep both destinations active during a cutover period and then decommission the old Snowflake Streaming destination


> ![warning](/docs/images/warning.svg)
> 
> Because the **Create Iceberg Tables** and **External Volume Name** settings are immutable, you cannot convert an existing Snowflake Streaming destination with no Iceberg support into an Iceberg destination.

## 1\. Prepare Snowflake and cloud storage for Iceberg

Before you create the new destination, complete the Snowflake and cloud storage setup described in [How to Configure Snowflake Streaming to Iceberg Tables](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake-streaming/iceberg-tables/configuration/>), including:

  * Enabling Iceberg support in your Snowflake account
  * Creating and verifying an **external volume** that points to your cloud storage
  * Configuring **RSA key-pair authentication** for the Snowflake user that RudderStack uses


> ![info](/docs/images/info.svg)
> 
> You can reuse the warehouse, database, role, and user from your current Snowflake Streaming destination if they meet the Iceberg requirements.

## 2\. Create a new Iceberg-enabled Snowflake Streaming destination

  1. Create a new Snowflake Streaming destination by following the steps outlined in the [Snowflake Streaming Destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake-streaming/>) guide.
  2. Connect the **same sources** that you currently route to your standard Snowflake Streaming destination.
  3. Give the new destination a name that clearly indicates it uses Iceberg, for example, **Snowflake Streaming (Iceberg)**.
  4. Enable Iceberg for the new destination by configuring the following settings:

Setting| Description  
---|---  
Create Iceberg Tables| Turn on the toggle to enable Snowflake-managed Iceberg tables for this destination  
External Volume Name| Specify the name of the external volume you created by following the steps [here](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake-streaming/iceberg-tables/configuration/#1-create-an-external-volume-for-iceberg-data>)  
  
> ![warning](/docs/images/warning.svg)
> 
> The **Create Iceberg Tables** and **External Volume Name** settings are immutable — you cannot change them after you create the destination.
> 
> To use a different external volume or to disable Iceberg, you will need to create a new Snowflake Streaming destination.

  5. Save the destination configuration.


#### What happens when Iceberg is enabled

  * RudderStack sends events to Snowflake through the **Snowpipe Streaming API**
  * Snowflake buffers incoming rows and periodically flushes them as **Parquet files** into your external volume
  * Snowflake maintains the **Iceberg metadata** and catalog, exposing the tables as standard Snowflake-managed Iceberg tables


> ![info](/docs/images/info.svg)
> 
> You should expect approximately **30 seconds of end-to-end latency** from when RudderStack receives an event to when you can query it in Snowflake.
> 
> Snowflake uses a default flush interval (for example, through `MAX_CLIENT_LAG`) to balance file size and latency.

## 3\. Verify new events in Iceberg tables

After you enable and activate the new destination in RudderStack:

  1. Send events from your connected sources.
  2. In Snowflake, check that Iceberg tables appear in the new schema:


    
    
    SHOW ICEBERG TABLES IN SCHEMA <ICEBERG_DATABASE>.<ICEBERG_SCHEMA>;
    

  3. Query one of the event tables, such as `TRACKS`, to confirm that new events are present:
         
         SELECT *
         FROM <YOUR_DATABASE>.<YOUR_SCHEMA>.<YOUR_TABLE>
         ORDER BY received_at DESC
         LIMIT 10;
         

  4. In your cloud storage bucket, confirm that Parquet files are being written under the external volume path.


> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Keep both destinations active until you are comfortable that the new Iceberg destination is working as expected.

## 4\. Optional: Backfill historical data

Copy historical data from your existing Snowflake Streaming tables into the new Iceberg tables so that you maintain continuity in your analytics.

The exact SQL depends on your database names, schemas, and tables. The example below shows how to backfill the `TRACKS` table:
    
    
    INSERT INTO <ICEBERG_DATABASE>.<ICEBERG_SCHEMA>.<ICEBERG_TABLE>
    SELECT *
    FROM <YOUR_DATABASE>.<YOUR_SCHEMA>.<YOUR_TABLE>
    WHERE received_at < '2026-03-01';  -- Replace with your cutover date
    

#### Considerations for backfilling

  * Choose a **cutover date** so that you do not duplicate rows that the new destination already ingested
  * Consider backfilling in **batches** (for example, by date range) if your historical tables are large
  * Monitor Snowflake compute usage and adjust warehouse size if needed


Repeat this pattern for other tables (like `PAGES`, `SCREENS`, `IDENTIFIES`, `GROUPS`, and `ALIASES`) if you want historical data for those event types in your Iceberg tables.

> ![warning](/docs/images/warning.svg)
> 
> **Do not plan to backfill the`USERS` table for this destination**
> 
> The Snowflake Streaming destination that uses Iceberg does not create a `USERS` table as the integration is append-only.

## 5\. Cut over and decommission the old destination

After you verify the new destination and complete any backfill:

  1. Choose a cutover time when new events should only go to the Iceberg destination.
  2. Disconnect your sources from the **old** Snowflake Streaming destination or disable the destination entirely.
  3. Optionally, remove the old destination from the RudderStack dashboard after you confirm that you no longer need it.


> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Update any downstream queries, dashboards, or data consumers to read from the Iceberg-backed tables if they previously read from the original tables.

## Troubleshooting

Issue| Solution  
---|---  
Backfill queries are slow or fail| If your backfill queries take too long or fail:  
  


  * Reduce the size of each batch by narrowing the `WHERE` clause (for example, backfill one month at a time)
  * Make sure the source and target tables have compatible schemas. If you added columns in the new destination, you may need to specify column lists in the `INSERT` statement

  
New events appear only in the old destination| If you still see new events only in the standard Streaming tables:  
  


  * Confirm that your sources are connected to the **new** Iceberg-enabled destination
  * Check that the Iceberg destination is enabled and does not show connection errors

  
  
If the issue persists, contact [RudderStack Support](<mailto:support@rudderstack.com>) with your destination configuration and the queries you are using for verification.