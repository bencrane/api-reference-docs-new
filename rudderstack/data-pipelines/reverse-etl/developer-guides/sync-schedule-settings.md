# Sync Schedule

Options to sync data from your Reverse ETL sources.

* * *

  * __3 minute read

  * 


RudderStack lets you set a schedule for importing data from your Reverse ETL sources while setting them up in your dashboard. It lets you specify the schedule type that defines how and when the syncs will run.

RudderStack supports the following three schedule types:

Schedule type| Description  
---|---  
Basic| Run syncs at a given time interval and specified time.  
CRON| Run syncs based on a CRON expression defined by the user.  
Manual| Run syncs manually.  
  
## Basic

This schedule type lets you run the data syncs at a set interval. You can specify the sync frequency as well as the time(in UTC) when you want the sync to start.

[![Basic sync schedule](/docs/images/warehouse-actions-sources/sync-schedule-basic.webp)](</docs/images/warehouse-actions-sources/sync-schedule-basic.webp>)

  * **Frequency** \- You can choose the data sync frequency from the following options:

    * 5 minutes
    * 10 minutes
    * 15 minutes
    * 30 minutes
    * 1 hour
    * 3 hours
    * 6 hours
    * 12 hours
    * 24 hours
  * **Sync Starting At** \- Specify the time at which the data sync should start.


## CRON

This schedule type lets you define a custom CRON expression and runs the data syncs based on this setting.

> ![info](/docs/images/info.svg)
> 
> You can use the [CRON scheduler utility](<https://crontab.guru/>) to specify your sync schedule.

[![CRON schedule](/docs/images/warehouse-actions-sources/sync-schedule-cron.webp)](</docs/images/warehouse-actions-sources/sync-schedule-cron.webp>)

Note that the sync frequency specified under **Run Settings** needs to be greater than or equal to 5 minutes. Otherwise, you will encounter an error as shown below:

[![CRON schedule error](/docs/images/retl-sources/cron-error.webp)](</docs/images/retl-sources/cron-error.webp>)

## Manual

This schedule type lets you run your data syncs manually. RudderStack won’t sync the data until you explicitly trigger it.

To trigger a sync manually, go to the **Syncs** tab in your Reverse ETL connections page and click **Sync Now** :

[![Trigger manual syncs](/docs/images/retl-sources/trigger-manual-sync.webp)](</docs/images/retl-sources/trigger-manual-sync.webp>)

> ![info](/docs/images/info.svg)
> 
> To programmatically schedule and trigger a sync from outside RudderStack, see the [RudderStack Airflow Provider](<https://www.rudderstack.com/docs/data-pipelines/orchestration/airflow/>) documentation.

## Sync modes behavior

The following sections explain the behavior of the two sync modes(Upsert and Mirror) when a sync schedule is set in RudderStack.

### Upsert mode

For [upsert mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/#upsert>), you can trigger a new sync anytime by pressing the **Sync Now** button. Multiple syncs can run simultaneously.

### Mirror mode

For [mirror mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/#mirror-mode>), you can run only one sync at any given point of time. A new sync starts only after the previous one is completed.

Suppose you have a sync scheduled for every 30 minutes. If there is a sync running for more than 30 minutes, then the next scheduled sync will be skipped when using the mirror mode.

## FAQ

#### Can I change my sync schedule type?

Yes, you can.

  1. Go to the **Settings** tab of your Reverse ETL connection details page and click the edit icon next to **Schedule** :

[![Change sync schedule](/docs/images/retl-sources/schedule-type.webp)](</docs/images/retl-sources/schedule-type.webp>)

  2. Then, select your new sync schedule type.


#### What happens if I don’t set the Sync Starting At time?

RudderStack considers strict time windows to schedule syncs if you do not explicitly set the time under **Sync Starting At**.

Suppose you create a source at 12:30 hrs UTC, specify the **Frequency** as 3 hours, and do not specify any time under **Sync Starting At**. In this case, as the time falls in the 12:00-13:00 time window, RudderStack will run the next sync at 15:00 hrs UTC (12:00 + 03:00 = 15:00 hrs).