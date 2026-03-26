# Sync Observability Settings

Options to store connection level sync logs and retry sending failed records.

* * *

  * __3 minute read

  * 


This guide explains the different observability settings that let you specify:

  * How RudderStack retains the sync log and snapshot tables for your [Reverse ETL connection](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/retl-connection-setup/>).
  * Whether RudderStack should continually retry sending the failed records in the future syncs.


## Sync settings

You can access the following sync settings in the **Settings** tab of your Reverse ETL connection:

Setting| Description  
---|---  
Retain sync logs| This setting is toggled on by default and instructs RudderStack to store the sync logs in your warehouse. You can also configure the below settings:  
  
| Setting| Description  
---|---  
Sync log retention| Specify the retention period of the [sync logs](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-observability/#sync-logs>) in your warehouse.  
  
If you set it to 1, then RudderStack deletes any sync log older than a day (in UTC time).  
Snapshot table retention| Specify the number of [snapshot tables](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-observability/#snapshot-table-schema>) to retain.  
Retry failed records| This setting is toggled on by default and causes RudderStack to continually [retry sending the failed records](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-observability/#retry-failed-records>).  
  
> ![warning](/docs/images/warning.svg)
> 
> Storing sync logs and snapshot tables may incur additional warehouse costs.

## Sync logs

RudderStack supports storing Reverse ETL sync logs in your warehouse. These logs are stored in a certain format in the [RudderStack schema](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/faq/#rudderstack-schema>) (used for storing the state of each sync). You can explore these logs using SQL or any BI tool to debug any issues or failures during syncs.

> ![warning](/docs/images/warning.svg)
> 
> Storing the sync logs in your warehouse will incur additional costs.

### Sync log table schema

The sync log table schema is as follows:

Column| Description  
---|---  
`connection_id`| Connection ID for the sync run.  
`sync_run_id`| Unique identifier for the sync run.  
`primary_key`| Value of the primary key column selected for the sync.  
`operation`| Nature of the operation performed on the row. It can be either `insert`, `update`, or `delete`.  
`status`| Result of the operation. It can be either `succeeded` or `failed`.  
`error_reason`| Reason for failure in case `status` is `failed`.  
`sync_started_at`| Sync start time in UTC.  
`sync_finished_at`| Sync finish time in UTC.  
  
### Snapshot table schema

RudderStack generates a snapshot table in the [RudderStack schema](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/faq/#rudderstack-schema>) for each sync. It contains rows (barring invalid rows like duplicate primary keys and null primary keys) from the data source like a warehouse table, view, SQL model, or audience. It also includes the details of the changes that happened in each row during the sync.

> ![warning](/docs/images/warning.svg)
> 
> Storing the snapshot tables in your warehouse will incur additional costs.

The snapshot tables are stored in the `snapshot_<connection_id>_<sync_run_id>` format, where:

  * `<connection_id>` is the Reverse ETL [connection ID](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/retl-connection-setup/#update-mapping-configuration>).
  * `<sync_run_id>` is the unique identifier for the sync run.

[![RETL connection sync run ID](/docs/images/retl-sources/sync-run-id.webp)](</docs/images/retl-sources/sync-run-id.webp>)

The snapshot table schema is as follows:

Column| Description  
---|---  
`rudder_operation_type`| Type of operation performed on the row when compared with the last synced data. It can be either `insert`, `update`, or `delete`.  
`<column_name>`| Name of the columns selected in the mappings for the sync.  
  
### Debug issues with sync logs

This section lists some queries you can run on your sync logs for debugging issues in your Reverse ETL syncs.

  * Check how a particular primary key has changed over time for a Reverse ETL connection:


    
    
    select * from _rudderstack.sync_log where primary_key='<primary_key>' and connection_id='<connection_id>';
    

  * Check the data for failures in the sync run:


    
    
    SELECT *
    FROM   _rudderstack.sync_log sl
           LEFT JOIN
           _rudderstack.snapshot_<connection_id>_<sync_run_id>
           sn
                  ON sl.primary_key = sn.<primary_key>
    WHERE  sl.sync_run_id = '<sync_run_id>'
           AND sl.status = 'failed'; 
    

> ![warning](/docs/images/warning.svg)
> 
> Make sure to replace the placeholders in the above queries with the actual values.

## Retry failed records

The **Retry failed records** toggle in the sync settings lets you determine whether RudderStack should continually retry sending the failed records in the previous syncs to the downstream destination.

> ![info](/docs/images/info.svg)
> 
> If a failed record has undergone any changes, RudderStack retries syncing the updated record instead.