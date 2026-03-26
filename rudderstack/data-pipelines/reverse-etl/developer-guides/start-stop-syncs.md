# Start and Stop Reverse ETL Syncs

Start, stop, and trigger a Reverse ETL sync manually.

* * *

  * __3 minute read

  * 


When you [set up a Reverse ETL connection](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/retl-connection-setup/>), RudderStack performs a full sync the first time, that is, it syncs all the data from the source. Subsequently, it incrementally syncs any new data since the last sync according to the [sync schedule](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/retl-connection-setup/#schedule-syncs>), or whenever you press the **Sync Now** button.

RudderStack also lets you force a full data resync or stop an ongoing sync.

## Start and stop syncs

Go to the **Syncs** tab of your Reverse ETL connection and click **Sync Now** to start a new sync. As mentioned above, this new sync will be incremental in nature, that is, it syncs only the new data available in the warehouse since the last sync.

[![Sync now option](/docs/images/retl-sources/sync-now.webp)](</docs/images/retl-sources/sync-now.webp>)

Choose the **Reset History and Full Sync** option to reset the sync history and force a full data sync.

[![Reset History and Full Sync option](/docs/images/retl-sources/reset-history-full-sync.webp)](</docs/images/retl-sources/reset-history-full-sync.webp>)

Click the **Stop Now** button to stop an ongoing sync.

[![Stop sync option](/docs/images/retl-sources/stop-sync.webp)](</docs/images/retl-sources/stop-sync.webp>)

In the confirmation pop up, click **Stop Sync** to cancel and stop the sync.

[![Stop sync confirmation](/docs/images/retl-sources/stop-sync-confirmation.webp)](</docs/images/retl-sources/stop-sync-confirmation.webp>)

> ![info](/docs/images/info.svg)
> 
> Note the following when stopping a sync:
> 
>   * Once you stop a sync, any data that RudderStack reads from the warehouse and is on the fly may not be stopped or dropped from being delivered to the destination. RudderStack only stops reading and sending any new data from the warehouse to the destination and prevents the sync from progressing.
>   * For a very low number of deltas (new data since the last attempted sync), you may sometimes see a “0 deltas succeeded” after you stop the sync.
>   * Once you cancel a sync, the behavior of the next sync depends on the [type](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/faq/#what-is-the-difference-between-the-full-and-incremental-sync-types>) of the cancelled sync. For example, if a cancelled sync is an incremental sync, then the next sync will be incremental too. Similarly, if the cancelled is a full sync, then the next sync will be a full sync.
>   * RudderStack makes sure there is no data loss in the next sync as a result of the previous cancelled sync irrespective of the sync type (full/incremental) or [sync mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/>)(upsert/mirror).
> 


## Drain behavior on sync cancellation

> ![info](/docs/images/info.svg)
> 
> This process is also applicable for scenarios where a Reverse ETL source is disabled or disconnected from a destination.

Whenever you stop a Reverse ETL sync, there might be some events that are in the process of being delivered and need to be drained from the pipeline.

This is important to make sure the next sync is not affected and you don’t have to wait for the events already in pipeline to be delivered or failed.

After you stop a sync, RudderStack automatically triggers this draining process in the background. The time taken for this process to complete depends on the amount of data. Hence, waiting for some time before triggering next sync is recommended.