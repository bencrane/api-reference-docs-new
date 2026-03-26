# Cursor Column Support

Use cursor columns for efficient incremental upsert syncs.

* * *

  * __4 minute read

  * 


RudderStack’s **Cursor Column Support** feature offers a more efficient way of syncing incremental data using the [Reverse ETL sources](<https://www.rudderstack.com/docs/sources/reverse-etl/>) in [Upsert mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/>). With this feature, you can run cost-effective SQL queries to infer the changes to be synced by leveraging cursor columns.

This guide walks you through the cursor column feature in detail.

## How the cursor column feature works

Previously, RudderStack identified the incremental data in [Upsert mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/#upsert-mode>) by comparing each column and row to detect changes. This led to longer sync times and increased warehouse costs, especially in case of large table size.

In the **cursor column** mode, RudderStack leverages a cursor column specified by the user to track and identify the changes. It then syncs only those records with a cursor value greater than the last checkpoint (recorded internally by RudderStack), avoiding the need to compare all columns.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack does not support migrating existing Reverse ETL connections from **upsert** mode to **cursor column** mode. You must create a new Reverse ETL connection to use this feature.

Note that:

  * For a full sync, all the records are synced. Generally, a full sync is triggered in the below cases:

    * First sync for a connection.
    * The data mapping is changed.
    * There is a change in the source schema, for example, the data type for one of the mapped columns is changed.
  * For the incremental syncs, RudderStack syncs all the rows whose cursor column value is **greater than** the last saved checkpoint from the cursor column.

  * RudderStack retries syncing any retryable records that failed to sync previously in the next sync - irrespective of their cursor column value. This includes failures due to errors with `429`, `5xx`, etc. status codes. See the Example for more information.


## Use the cursor column feature

> ![warning](/docs/images/warning.svg)
> 
> Make sure to see Limitations before using this feature.

  1. Create a new Reverse ETL source and connect it to a destination.
  2. In the **Data Mapping** settings, set **Sync mode** to **Upsert**.
  3. Toggle on the **Use cursor column** setting.
  4. Specify the cursor column from the dropdown.


> ![info](/docs/images/info.svg)
> 
> RudderStack recommends choosing a cursor column that is comparable, that is, it supports operators like `<`, `>`, `ORDER BY`, etc.

[![Cursor column settings in RudderStack](/docs/images/data-pipelines/cursor-column.webp)](</docs/images/data-pipelines/cursor-column.webp>)

## Example

The following example illustrates how the cursor column feature works works:

**Source table for first sync**

email| score| updated_at  
---|---|---  
`alex@example.com`| 10| 2024-10-03T05:36:30  
`alice@example.com`| 20| 2024-10-03T05:37:30  
`john@example.com`| 30| 2024-10-03T05:38:30  
  
**Cursor column selection**

Suppose the user selects `updated_at` as the cursor column in the RudderStack dashboard. RudderStack uses this column to note the checkpoints.

**First sync**

Now, let’s assume two of the above records failed and one succeeds in the first sync:

email| score| updated_at| status  
---|---|---|---  
`alex@example.com`| 10| 2024-10-03T05:36:30| Success  
`alice@example.com`| 20| 2024-10-03T05:37:30| Failed  
`john@example.com`| 30| 2024-10-03T05:38:30| Failed  
  
**Last checkpoint**

In this case, RudderStack records the last checkpoint (`2024-10-03T05:38:30`) for the next incremental sync.

**Source table for incremental sync**

Next, suppose the source table is updated with new and updated records, as shown:

email| score| updated_at| Notes  
---|---|---|---  
`alex@example.com`| 10| 2024-10-03T05:36:30| Unchanged record  
`john@example.com`| 30| 2024-10-03T05:38:30| Unchanged record, previously failed  
`alice@example.com`| 50| 2024-10-03T05:39:30| Changed record, previously failed  
  
**Next sync (incremental)**

In this case, RudderStack leverages the previous checkpoint (`2024-10-03T05:38:30`) from the cursor column to sync the following records:

email| score| updated_at| status| Notes  
---|---|---|---|---  
`alice@example.com`| 50| 2024-10-03T05:39:30| Success| `updated_at` value is greater than the previous checkpoint.  
  
RudderStack does not sync the previously failed record for this email.  
`john@example.com`| 30| 2024-10-03T05:38:30| Success| RudderStack retries and syncs this record because it failed in the previous sync.  
  
As seen above, RudderStack only syncs the records that are:

  * Updated after the previous checkpoint, or
  * Retryable records that failed in the previous sync


> ![warning](/docs/images/warning.svg)
> 
> RudderStack does not sync records that come in as a result of late arrival of data, that is, it will not sync the records even if they were updated but their cursor column value is less than the previous checkpoint.

## Limitations

  * This feature **does not** support deletes. Since no diffing is involved, the sync does not track deleted records to perform any action on the deleted rows.
  * The feature **only works** for Reverse ETL sources of [Table and SQL Model type](<https://www.rudderstack.com/docs/sources/reverse-etl/amazon-redshift/#specify-name-and-source-type>) \- it does not support the Audience type.
  * This feature **does not** support the [Amazon S3 source](<https://www.rudderstack.com/docs/sources/reverse-etl/amazon-s3/>).
  * Users are responsible for selecting an appropriate cursor column. RudderStack relies on the provided cursor column value to determine the incremental changes.