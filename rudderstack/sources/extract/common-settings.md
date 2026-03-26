# Common settings Deprecated

Table prefix, schedule settings, and sync modes for configuring Extract sources.

* * *

  * __4 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> As of **January 10, 2026** , all ETL connections are turned off. You will not be able to activate new connections or toggle on existing connections.
> 
> See this [Release Note](<https://www.rudderstack.com/docs/releases/etl-sunset/>) for more details.

This guide covers the common destination-specific settings to be configured while setting up your Cloud Extract sources. Common settings include: table prefix, schedule settings, and sync modes.

[![Sendgrid destination settings](/docs/images/cloud-extract-sources/sendgrid-connection-settings-2.webp)](</docs/images/cloud-extract-sources/sendgrid-connection-settings-2.webp>)

## Table prefix

RudderStack uses your specified table prefix to create a table named `prefix_table_name` in your data warehouse and load all imported source data into it.

> ![info](/docs/images/info.svg)
> 
> If you do not specify a prefix, RudderStack creates a table in your warehouse as `table_name`, where `table_name` refers to the resource you are importing.

For example, if you set the prefix to `rs_` and the resource you are importing is named `valid_emails`, then RudderStack creates the table `rs_valid_emails` in the warehouse.

## Schedule settings

RudderStack lets you set a schedule for importing data from your Cloud Extract sources while setting them up in your dashboard. It lets you specify the schedule type that defines how and when the syncs will run.

RudderStack supports the following three schedule types:

Schedule type| Description  
---|---  
Basic| Run syncs at a given time interval and specified time.  
CRON| Run syncs based on a CRON expression defined by the user.  
Manual| Run syncs manually.  
  
### Basic

This schedule type lets you run the data syncs at a set interval. You can specify the sync frequency as well as the time(in UTC) when you want the sync to start.

[![Basic sync schedule](/docs/images/warehouse-actions-sources/sync-schedule-basic.webp)](</docs/images/warehouse-actions-sources/sync-schedule-basic.webp>)

  * **Frequency** : You can choose the data sync frequency from the following options:

    * 15 minutes
    * 30 minutes
    * 1 hour
    * 3 hours
    * 6 hours
    * 12 hours
    * 24 hours
  * **Sync Starting At** : Specify the time at which the data sync should start.


### CRON

This schedule type lets you define a custom CRON expression and runs the data syncs based on this setting.

> ![info](/docs/images/info.svg)
> 
> You can use the [CRON scheduler utility](<https://crontab.guru/>) to specify your sync schedule.

[![CRON schedule](/docs/images/warehouse-actions-sources/sync-schedule-cron.webp)](</docs/images/warehouse-actions-sources/sync-schedule-cron.webp>)

> ![warning](/docs/images/warning.svg)
> 
> The sync frequency specified under **Run Settings** needs to be greater than or equal to 15 minutes. Otherwise, you will encounter an error as shown below:

[![CRON schedule error](/docs/images/warehouse-actions-sources/sync-schedule-cron-error.webp)](</docs/images/warehouse-actions-sources/sync-schedule-cron-error.webp>)

### Manual

This schedule type lets you run your data syncs manually. RudderStack won’t sync the data until you explicitly trigger it.

To trigger a sync manually, go to the **Syncs** tab in your Cloud Extract source details page and click **Sync Now** :

[![Manual sync schedule](/docs/images/cloud-extract-sources/sync-schedule-manual.webp)](</docs/images/cloud-extract-sources/sync-schedule-manual.webp>)

## Sync modes

A sync mode determines how RudderStack reads the data from a source and writes to a warehouse destination. RudderStack supports the following sync modes:

### Full Refresh

In this mode, RudderStack retrieves **all** the available information from the source, **regardless** of whether it has been synced previously.

> ![info](/docs/images/info.svg)
> 
> In this mode, RudderStack replaces all existing data with the new data.

### Incremental

In this mode, RudderStack syncs or replicates only the new or modified data starting from the date specified in the **Start date** RudderStack dashboard setting. It does not replicate the data that has been already synced before.

During the incremental syncs, RudderStack only updates the the existing rows that have been modified as opposed to adding a new version of the row with the updated data.

> ![info](/docs/images/info.svg)
> 
> Any resource that supports the **Incremental** sync mode also supports **Full Refresh** , by default.
> 
>   * If you want to do a Full Refresh sync only for particular Incremental resources, then [contact the RudderStack team](<mailto:support@rudderstack.com>). This is helpful in cases where your destination’s data gets corrupted or you want to sync your data all over again.
>   * If you want to do a Full Refresh sync for all the resources associated with an Extract source, then change the **Start date** setting in your existing source configuration. Refer to the FAQ section for more information.
> 


### Semi-Incremental

This sync mode is a combination of **Full Refresh** and **Incremental** sync modes. RudderStack reads all data from the source and filters it to sync only the new or modified data starting from the date specified in the **Start Date** RudderStack dashboard setting.

> ![info](/docs/images/info.svg)
> 
> The data synced in the **Semi-Incremental** mode is exactly the same as in the **Incremental mode**. The only difference is that in the **Semi-Incremental** mode, RudderStack internally filters the data to be synced instead of the source API.

## FAQ

#### Can I change my sync schedule type?

Yes, you can.

  1. Go to the **Settings** tab in your Cloud Extract source details page and click **Edit sync schedule** option:

[![Syncs schedule settings change](/docs/images/cloud-extract-sources/sync-schedule-settings-change.webp)](</docs/images/cloud-extract-sources/sync-schedule-settings-change.webp>)

  2. Then, select your new sync schedule type.


#### What happens if I don’t set the Sync Starting At time?

RudderStack considers strict time windows to schedule syncs if you do not explicitly set the time under **Sync Starting At**.

Suppose you create a source at 12:30 hrs UTC, specify the **Frequency** as 3 hours, and do not specify any time under **Sync Starting At**. In this case, as the time falls in the 12:00-13:00 time window, RudderStack will run the next sync at 15:00 hrs UTC (12:00 + 03:00 = 15:00 hrs).

#### How do I force a Full Refresh sync for all the resources?

To force a Full Refresh sync for **all** the resources supported by the Extract source, change the **Start date** setting in your existing source configuration.

[![Update Extract source configuration](/docs/images/cloud-extract-sources/extract-update-configuration.webp)](</docs/images/cloud-extract-sources/extract-update-configuration.webp>)

> ![warning](/docs/images/warning.svg)
> 
> Disconnecting and reconnecting an Extract source to a warehouse destination does not force a full sync.