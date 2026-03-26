# Mixpanel Cloud Extract Source Deprecated

Sync data from Mixpanel to your warehouse destination via RudderStack.

* * *

  * __5 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> This source is deprecated and no longer supported as of **January 10, 2026**.

[Mixpanel](<https://mixpanel.com/>) is an analytics platform that provides specific tools for targeted business communication and customer engagement, in-app A/B testing, user survey forms, and custom reports to measure customer retention.

This document guides you in setting up Mixpanel as a source in RudderStack. Once configured, RudderStack automatically ingests your Mixpanel data and routes it to your specified data warehouse destination.

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * All Cloud Extract sources support sending data only to a [data warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).
>   * This source works only with the [Mixpanel Growth and Enterprise](<https://mixpanel.com/pricing/>) versions. It **does not support** the Free plan.
> 


## Getting started

To set up Mixpanel as a source in RudderStack, follow these steps:

  1. Log into your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Sources** > **New source** > **Cloud Extract** and select **Mixpanel** from the list of sources.
  3. Assign a name to your source and click **Continue**.


### Connection settings

Enter the following connection settings to set up the Mixpanel source:

  * **Authentication** : Select either **Service Account** or **Project Secret** from the dropdown to give RudderStack the required permissions to access your Mixpanel account. Refer to the [Service Accounts](<https://developer.mixpanel.com/reference/service-accounts>) and [Project Secret](<https://developer.mixpanel.com/reference/project-secret>) documentation for more information on obtaining these details.
  * **Project ID** : Enter your Mixpanel project ID by going to **Project Settings** > **Overview** in your Mixpanel dashboard. Refer to the [Mixpanel support guide](<https://help.mixpanel.com/hc/en-us/articles/115004490503-Project-Settings#project-id>) for more information.
  * **Attribution Window** : Specify the time period for attributing results to the ads and the lookback period during which the ads results are counted. By default, this value is set to **5 days**.
  * **Project Timezone** : Specify your Mixpanel project timezone by going to **Project Settings** > **Project Details** in your Mixpanel dashboard. For more information on getting your Mixpanel project timezone, refer to the [Mixpanel support guide](<https://help.mixpanel.com/hc/en-us/articles/115004547203-Manage-Timezones-for-Projects-in-Mixpanel>).
  * **Select Properties By Default** : Enable this setting to capture new event properties and engage records. If disabled, these properties will be ignored.
  * **Start Date** : Select the date from when RudderStack ingests your Mixpanel data.


> ![warning](/docs/images/warning.svg)
> 
> RudderStack will **not replicate** any data before this date. If you do not set this option, RudderStack will replicate the Mixpanel data up to one year from the current date by default.

  * **End Date** : Specify the end date for the replication window.


> ![warning](/docs/images/warning.svg)
> 
> RudderStack will not replicate any data **after** this date. Do not set this field if you want RudderStack to sync the most recent Mixpanel data.

  * **Region** : Specify your Mixpanel domain instance from either **US** or **EU**.
  * **Date Slicing Window** : Define the window size used to slice through the Mixpanel data. By default, RudderStack sets this field to **30 days**.


> ![info](/docs/images/info.svg)
> 
> Reduce the value of this field if the amount of data in the slicing window is too large for your environment.

### Destination settings

The following settings specify how RudderStack sends the data ingested from Mixpanel to the connected warehouse destination:

  * **Table prefix** : RudderStack uses this prefix to create a table in your data warehouse and loads all your Mixpanel data into it.


> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add special characters like `-` or `_` to the prefix by default. Hence, you need to specify it while setting the prefix.

  * **Schedule Settings** : RudderStack gives you three options to ingest the data from Mixpanel:
    * **Basic** : Runs the syncs at the specified time interval.
    * **CRON** : Runs the syncs based on the user-defined CRON expression.
    * **Manual** : You are required to run the syncs manually.


> ![info](/docs/images/info.svg)
> 
> If you have configured **End Date** in the connection settings, setting the schedule setting to **Manual** is highly recommended.
> 
> For this source, RudderStack allows the end date to be less than or equal to the current date. **Basic** /**CRON** scheduling is useful when you want to keep syncing updates for some time in the future as well. By setting the sync schedule to **Manual** , only one sync is required to sync all your Mixpanel data.

For more information on the schedule types, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/>) guide.

### Selecting the data to import

You can choose the Mixpanel data you want to ingest by selecting the required resources:

[![Selecting the data to import](/docs/images/cloud-extract-sources/mixpanel-connection-settings-2.webp)](</docs/images/cloud-extract-sources/mixpanel-connection-settings-2.webp>)

The below table mentions the syncs and API endpoints supported by these resources from Mixpanel to your warehouse destination:

Resource| Sync type| Mixpanel API endpoint  
---|---|---  
`revenue`| Incremental| `/engage`  
`funnels`| Incremental| `/funnels`  
`export`| Incremental| `/export`  
`engage`| Incremental| `/engage`  
`cohorts`| Incremental| `/cohorts/list`  
`cohort_members`| Incremental| `/engage`  
`annotations`| Full Refresh| `/annotations`  
  
> ![info](/docs/images/info.svg)
> 
> For more information on the **Full Refresh** and **Incremental** sync modes, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/#sync-modes>) guide.

Mixpanel is now configured as a source. RudderStack will start ingesting data from Mixpanel as per your specified schedule and frequency.

You can further connect this source to your data warehouse by clicking on **Add Destination** :

[![Adding a destination](/docs/images/cloud-extract-sources/add-destination.webp)](</docs/images/cloud-extract-sources/add-destination.webp>)

> ![success](/docs/images/tick.svg)
> 
> Use the **Use Existing Destination** option if you have an already-configured data warehouse destination in RudderStack. To configure a data warehouse destination from scratch, select the **Create New Destination** button.

## FAQ

#### Can I connect my Mixpanel source to multiple data warehouse destinations?

You can connect **only one data warehouse destination** per Cloud Extract source. If you wish to send data to multiple warehouses, you can configure multiple Cloud Extract sources with the same settings and connect them to each data warehouse.

#### Is it possible to have multiple Cloud Extract sources writing to the same schema?

Yes, it is.

RudderStack associates a table prefix for every Cloud Extract source writing to a warehouse schema. This way, multiple Cloud Extract sources can write to the same schema with different table prefixes.

#### How does RudderStack count the events for Cloud Extract sources?

RudderStack counts the number of records returned by the source APIs when queried during each sync. It considers each record as an event.

#### How does RudderStack set the table name for the data sent via Cloud Extract sources?

RudderStack sets the table name for the resource you are syncing to the warehouse by adding `rudder_` to the **Table prefix** you set while configuring your Cloud Extract source in the dashboard.

[![Cloud Extract table prefix](/docs/images/cloud-extract-sources/etl-table-prefix.webp)](</docs/images/cloud-extract-sources/etl-table-prefix.webp>)

For example, if you set `test_` as the **Table prefix** in the dashboard, RudderStack sets the table name as `test_rudder_<resource_name>`, where `<resource_name>` is the name of the resource you are syncing (for example, `contacts`, `messages`, etc.).

> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add the character `_` to the prefix by default. Hence, you need to specify it while setting the prefix.