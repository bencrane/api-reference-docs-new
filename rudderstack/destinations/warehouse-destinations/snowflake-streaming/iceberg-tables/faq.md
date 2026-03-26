# Snowflake Streaming to Iceberg Tables FAQ

Frequently asked questions about Snowflake Streaming to Iceberg tables, including costs, compatibility, and data handling.

Available Plans

  * starter
  * growth
  * enterprise


* * *

  *  __3 minute read

  * 


This guide answers common questions about the Snowflake Streaming to Iceberg tables integration.

## Pricing and billing

#### Does Snowflake Streaming to Iceberg tables cost extra?

On the RudderStack side, Iceberg table support is included with Snowflake Streaming.

On the Snowflake side, compute costs are similar to standard tables and storage costs are billed by your cloud provider (S3, GCS, or Azure Blob) because data lives in your external volume rather than in Snowflake’s internal storage.

## Engine interoperability and compatibility

#### Can I query my Iceberg data from engines other than Snowflake?

Yes — your data is stored as standard Parquet files in your cloud storage. You can configure Snowflake’s catalog integration so that engines such as Spark, Trino, Athena, or Databricks can read the same tables.

These engines treat the tables as read-only — Snowflake remains the single writer.

#### Can I use Snowflake-managed Iceberg tables as a Reverse ETL source in RudderStack?

Yes – given your preconfigured warehouse credentials have read and write access.

If you use the same warehouse account with the same role, you will be able to query the data and use it as a table, [Model](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/models/>), or [Audience](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/audiences/>) source in RudderStack.

## Schema evolution and migration

#### What happens if I add a new event property?

When you add a new property to your events, RudderStack automatically:

  * Evolves the schema
  * Adds the corresponding column to the relevant Iceberg table


You do not need to manually alter the table in Snowflake.

#### Can I switch an existing Snowflake Streaming destination to Iceberg?

No — you cannot convert an existing non-Iceberg Snowflake Streaming destination into an Iceberg destination. You must:

  1. Create a new Snowflake Streaming destination with [**Create Iceberg Tables** setting](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake-streaming/iceberg-tables/configuration/#4-enable-iceberg-and-specify-the-external-volume>) turned on.
  2. Connect your sources to the new destination.
  3. Optionally backfill historical data from your original tables into the new Iceberg tables.


See [How to Migrate from Standard Snowflake Streaming to Iceberg](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake-streaming/iceberg-tables/migration-from-standard-streaming/>) for a step-by-step guide.

## Data model and storage behavior

#### Why is my JSON data stored as a string instead of a nested object?

Snowflake-managed Iceberg tables do not currently support the `VARIANT` data type.

RudderStack stores JSON as `VARCHAR` so that it can be ingested into Iceberg tables. Use `PARSE_JSON` in your Snowflake queries to work with nested fields.

#### Why is there no `USERS` table?

The `USERS` table depends on MERGE operations for deduplication. The Snowflake Streaming to Iceberg integration uses an append-only model that does not support this pattern. Instead, you should read identity information from the `IDENTIFIES` table and other event tables.

## Performance and infrastructure

#### What latency should I expect?

You should expect **approximately 30 seconds** of latency between when RudderStack receives an event and when you can query it in Snowflake. This latency comes from Snowflake’s buffering and flush settings for streaming workloads.

#### Which cloud providers can I use for the external volume?

You can use any of the following providers for the external volume that backs your Iceberg tables:

  * AWS S3
  * Google Cloud Storage
  * Azure Blob Storage


Follow the provider-specific examples presented in [How to Configure Snowflake Streaming to Iceberg Tables](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake-streaming/iceberg-tables/configuration/#1-create-an-external-volume-for-iceberg-data>) when you create and verify the external volume.