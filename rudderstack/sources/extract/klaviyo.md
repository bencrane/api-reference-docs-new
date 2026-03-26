# Klaviyo Cloud Extract Source Deprecated

Sync data from Klaviyo to your warehouse destination via RudderStack.

* * *

  * __4 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> This source is deprecated and no longer supported as of **January 10, 2026**.

[Klaviyo](<https://www.klaviyo.com/>) is a powerful ecommerce platform that lets you boost your business revenue. It offers features like trend reports, cohort analysis, and various options for boosting customer engagement.

This document guides you in setting up Klaviyo as a source in RudderStack. Once configured, RudderStack automatically ingests your Klaviyo data and routes it to your specified data warehouse destination.

> ![danger](/docs/images/danger.svg)
> 
> **This source uses the legacy Klaviyo v1 API which is[scheduled to retire](<https://developers.klaviyo.com/en/v1-2/reference/api-overview>) on June 30, 2024.**
> 
> Using the [Klaviyo v2](<https://www.rudderstack.com/docs/sources/extract/klaviyo-v2/>) source that leverages the latest and most stable version of the Klaviyo API is strongly recommended.

## Getting started

To set up Klaviyo as a source in RudderStack, follow these steps:

  1. Log into your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Sources** > **New source** > **Cloud Extract** and select **Klaviyo** from the list of sources.
  3. Assign a name to your source and click **Next**.


### Connection settings

Enter the following connection settings to set up the Klaviyo source:

[![Klaviyo connection settings](/docs/images/cloud-extract-sources/klaviyo-connection-settings.webp)](</docs/images/cloud-extract-sources/klaviyo-connection-settings.webp>)

The connection settings are described below:

  * **API Key** : Enter your Klaviyo Private API key. You can find it in your Klaviyo dashboard by clicking your organization name and going to **Account & billing** > **Settings** > **API Keys**.


> ![info](/docs/images/info.svg)
> 
> For more information on obtaining the Klaviyo private API key, refer to the [Klaviyo support guide](<https://help.klaviyo.com/hc/en-us/articles/115005062267-How-to-Manage-Your-Account-s-API-Keys#your-private-api-keys3>).

  * **Start Date** : Select the date from when RudderStack ingests your Klaviyo data.


> ![warning](/docs/images/warning.svg)
> 
> RudderStack will **not replicate** any data before this date.

### Destination settings

The following settings specify how RudderStack sends the data ingested from Klaviyo to the connected warehouse destination:

  * **Table prefix** : RudderStack uses this prefix to create a table in your data warehouse and loads all your Klaviyo data into it.


> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add special characters like `-` or `_` to the prefix by default. Hence, you need to specify it while setting the prefix.

  * **Schedule Settings** : RudderStack gives you three options to ingest the data from Klaviyo:
    * **Basic** : Runs the syncs at the specified time interval.
    * **CRON** : Runs the syncs based on the user-defined CRON expression.
    * **Manual** : You are required to run the syncs manually.


> ![info](/docs/images/info.svg)
> 
> For more information on the schedule types, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/>) guide.

### Selecting the data to import

You can choose the Klaviyo data you want to ingest by selecting the required resources:

[![Selecting the data to import](/docs/images/cloud-extract-sources/klaviyo-connection-settings-2.webp)](</docs/images/cloud-extract-sources/klaviyo-connection-settings-2.webp>)

The below table mentions the syncs and API endpoints supported by these resources from Klaviyo to your warehouse destination:

Resource| Full Refresh sync| Incremental sync| Primary key| Klaviyo API endpoint  
---|---|---|---|---  
`campaigns`| Yes| No| `id`| `/campaigns`  
`events`| Yes| Yes| `id`| `/metrics/timeline`  
`flows`| Yes| Yes| `id`| `/flows`  
`global_exclusions`| Yes| No| `email`| `/people/exclusions`  
`lists`| Yes| No| `id`| `/lists`  
`metrics`| Yes| No| `id`| `/metrics`  
  
> ![info](/docs/images/info.svg)
> 
> For more information on the **Full Refresh** and **Incremental** sync modes, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/#sync-modes>) guide.

Klaviyo is now configured as a source. RudderStack will start ingesting data from Klaviyo as per your specified schedule and frequency.

You can further connect this source to your data warehouse by clicking on **Add Destination** :

[![Adding a destination](/docs/images/cloud-extract-sources/add-destination.webp)](</docs/images/cloud-extract-sources/add-destination.webp>)

> ![success](/docs/images/tick.svg)
> 
> Use the **Use Existing Destination** option if you have an already-configured data warehouse destination in RudderStack. To configure a data warehouse destination from scratch, select the **Create New Destination** button.

## FAQ

#### Can I connect my Klaviyo source to multiple data warehouse destinations?

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