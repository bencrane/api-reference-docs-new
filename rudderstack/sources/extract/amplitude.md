# Amplitude Cloud Extract Source Deprecated

Sync data from Amplitude to your warehouse destination via RudderStack.

* * *

  * __4 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> This source is deprecated and no longer supported as of **January 10, 2026**.

[Amplitude](<https://amplitude.com/>) is a comprehensive product analytics platform for the web as well as mobile platforms. It helps you get useful marketing insights that drive product strategy, customer conversion, and retention.

This document guides you in setting up Amplitude as a source in RudderStack. Once configured, RudderStack automatically ingests your Amplitude data and routes it to your specified data warehouse destination.

> ![info](/docs/images/info.svg)
> 
> All Cloud Extract sources support sending data only to a [data warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).

## Getting started

To set up Amplitude as a source in RudderStack, follow these steps:

  1. Log into your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Sources** > **New source** > **Cloud Extract** and select **Amplitude** from the list of sources.
  3. Assign a name to your source and click **Next**.


### Connection settings

Enter the following connection settings to set up the Amplitude source:

[![Amplitude connection settings](/docs/images/cloud-extract-sources/amplitude-connection-settings.webp)](</docs/images/cloud-extract-sources/amplitude-connection-settings.webp>)

The settings are described below:

  * **API Key** : Enter your Amplitude project’s API key. You can find it in your Amplitude dashboard by going to **Settings** > **Projects** > Your project name > **General**.
  * **Secret Key** : Enter your project’s secret key.


> ![info](/docs/images/info.svg)
> 
> For more information on the Amplitude API key and secret key, refer to the [Amplitude support guide](<https://help.amplitude.com/hc/en-us/articles/360058073772-Create-and-manage-organizations-and-projects#view-and-edit-your-project-information>).

  * **Replication Start Date** : Select the date from when RudderStack ingests your Amplitude data.


> ![warning](/docs/images/warning.svg)
> 
> RudderStack will **not replicate** any data before this date.

### Destination settings

The following settings specify how RudderStack sends the data ingested from Amplitude to the connected warehouse destination:

  * **Table prefix** : RudderStack uses this prefix to create a table in your data warehouse and loads all your Amplitude data into it.


> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add special characters like `-` or `_` to the prefix by default. Hence, you need to specify it while setting the prefix.

  * **Schedule Settings** : RudderStack gives you three options to ingest the data from Amplitude:
    * **Basic** : Runs the syncs at the specified time interval.
    * **CRON** : Runs the syncs based on the user-defined CRON expression.
    * **Manual** : You are required to run the syncs manually.


> ![info](/docs/images/info.svg)
> 
> For more information on the schedule types, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/>) guide.

### Selecting the data to import

You can choose the Amplitude data you want to ingest by selecting the required resources:

[![Selecting the data to import](/docs/images/cloud-extract-sources/amplitude-connection-settings-2.webp)](</docs/images/cloud-extract-sources/amplitude-connection-settings-2.webp>)

The below table mentions the syncs and API endpoints supported by these resources from Amplitude to your warehouse destination:

Resource| Full Refresh sync| Incremental sync| Primary key| Amplitude API endpoint  
---|---|---|---|---  
`events`| Yes| Yes| `uuid`| `/export`  
`cohorts`| Yes| No| `id`| `/cohorts`  
`average_session_length`| No| Yes| `date`| `/dashboard`  
`annotations`| Yes| No| `id`| `/annotations`  
`active_users`| No| Yes| `date`| `/dashboard`  
  
For more information on the **Full Refresh** and **Incremental** sync modes, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/#sync-modes>) guide.

Amplitude is now configured as a source. RudderStack will start ingesting data from Amplitude as per your specified schedule and frequency.

You can further connect this source to your data warehouse by clicking on **Add Destination** :

[![Adding a destination](/docs/images/cloud-extract-sources/add-destination.webp)](</docs/images/cloud-extract-sources/add-destination.webp>)

> ![success](/docs/images/tick.svg)
> 
> Use the **Use Existing Destination** option if you have an already-configured data warehouse destination in RudderStack. To configure a data warehouse destination from scratch, select the **Create New Destination** button.

## FAQ

#### Can I connect my Amplitude source to multiple data warehouse destinations?

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