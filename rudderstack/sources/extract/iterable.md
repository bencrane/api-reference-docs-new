# Iterable Cloud Extract Source Deprecated

Sync data from Iterable to your warehouse destination via RudderStack.

* * *

  * __4 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> This source is deprecated and no longer supported as of **January 10, 2026**.

[Iterable](<https://www.Iterable.com/>) is a popular growth marketing platform that lets you maximize customer interaction and improve your customers’ overall LTV (Life Time Value).

This document guides you in setting up Iterable as a source in RudderStack. Once configured, RudderStack automatically ingests your Iterable data and routes it to your specified data warehouse destination.

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * For sending real-time events from Iterable to RudderStack via webhook, see the [Iterable Webhook](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/iterable/>) documentation.
>   * All Cloud Extract sources support sending data only to a [data warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).
> 


## Getting started

To set up Iterable as a source in RudderStack, follow these steps:

  1. Log into your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Sources** > **New source** > **Cloud Extract** and select **Iterable** from the list of sources.
  3. Assign a name to your source and click **Next**.


### Connection settings

Next, configure the following dashboard settings:

[![Configuring Iterable](/docs/images/cloud-extract-sources/iterable-connection-settings.webp)](</docs/images/cloud-extract-sources/iterable-connection-settings.webp>)

  * **Start Date** : Enter the date from which RudderStack should ingest the Iterable data. RudderStack will not replicate any data before this date.
  * **API Key** : Enter your Iterable project’s API key by going to **Integrations** > **API Keys**.


### Destination settings

The following settings specify how RudderStack sends the data ingested from Iterable to the connected warehouse destination:

  * **Table prefix** : RudderStack uses this prefix to create a table in your data warehouse and loads all your Iterable data into it.


> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add special characters like `-` or `_` to the prefix by default. Hence, you need to specify it while setting the prefix.

  * **Schedule Settings** : RudderStack gives you three options to ingest the data from Iterable:
    * **Basic** : Runs the syncs at the specified time interval.
    * **CRON** : Runs the syncs based on the user-defined CRON expression.
    * **Manual** : You are required to run the syncs manually.


> ![info](/docs/images/info.svg)
> 
> For more information on the schedule types, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/>) guide.

### Selecting the data to import

You can choose the Iterable data that you want to ingest by selecting the required resources.

[![Selecting the data to import](/docs/images/cloud-extract-sources/iterable-resources.webp)](</docs/images/cloud-extract-sources/iterable-resources.webp>)

The below table mentions the sync types supported by the Iterable resources while syncing data to your warehouse destination:

Resource| Sync type| Endpoint| Primary key  
---|---|---|---  
`campaigns`| Full Refresh| `/campaigns`| `id`  
`campaigns_metrics`| Full Refresh| `/campaigns/metrics`| -  
`channels`| Full Refresh| `/channels`| `id`  
`email_bounce`| Incremental| [`/export/data.json`](<https://api.iterable.com/api/docs#export_exportDataJson>)| -  
`email_click`| Incremental| [`/export/data.json`](<https://api.iterable.com/api/docs#export_exportDataJson>)| -  
`email_complaint`| Incremental| [`/export/data.json`](<https://api.iterable.com/api/docs#export_exportDataJson>)| -  
`email_open`| Incremental| [`/export/data.json`](<https://api.iterable.com/api/docs#export_exportDataJson>)| -  
`email_send`| Incremental| [`/export/data.json`](<https://api.iterable.com/api/docs#export_exportDataJson>)| -  
`email_send_skip`| Incremental| [`/export/data.json`](<https://api.iterable.com/api/docs#export_exportDataJson>)| -  
`email_subscribe`| Incremental| [`/export/data.json`](<https://api.iterable.com/api/docs#export_exportDataJson>)| -  
`email_unsubscribe`| Incremental| [`/export/data.json`](<https://api.iterable.com/api/docs#export_exportDataJson>)| -  
`events`| Full Refresh| `/export/userEvents`| -  
`lists`| Full Refresh| `/lists`| `id`  
`list_users`| Full Refresh| `/lists/getUsers`| `listId`  
`message_types`| Full Refresh| `/messageTypes`| `id`  
`metadata`| Full Refresh| `/metadata`| -  
`templates`| Incremental| [`/export/data.json`](<https://api.iterable.com/api/docs#export_exportDataJson>)| -  
`users`| Incremental| [`/export/data.json`](<https://api.iterable.com/api/docs#export_exportDataJson>)| -  
  
> ![info](/docs/images/info.svg)
> 
> For more information on the **Full Refresh** and **Incremental** sync modes, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/#sync-modes>) guide.

Iterable is now configured as a source. RudderStack will start ingesting data from Iterable as per your specified schedule and frequency.

You can further connect this source to your data warehouse by clicking the **Add Destination** button:

[![Adding a destination](/docs/images/cloud-extract-sources/add-destination.webp)](</docs/images/cloud-extract-sources/add-destination.webp>)

> ![info](/docs/images/info.svg)
> 
> Use the **Use Existing Destination** option if you have an already-configured data warehouse destination in RudderStack. To configure a data warehouse destination from scratch, select the **Create New Destination** button.

## FAQ

#### Is it possible to have multiple Cloud Extract sources writing to the same schema?

Yes, it is.

RudderStack associates a table prefix for every Cloud Extract source writing to a warehouse schema. This way, multiple Cloud Extract sources can write to the same schema with different table prefixes.

#### Where can I find the Iterable API key?

You can get your Iterable project’s API key by logging into your Iterable dashboard and navigating to **Integrations** > **API Keys**. For more information, refer to the [Iterable documentation](<https://support.iterable.com/hc/en-us/articles/360043464871-API-Keys>).

#### How does RudderStack count the events for Cloud Extract sources?

RudderStack counts the number of records returned by the source APIs when queried during each sync. It considers each record as an event.

#### How does RudderStack count the events for Cloud Extract sources?

RudderStack counts the number of records returned by the source APIs when queried during each sync. It considers each record as an event.

#### How does RudderStack set the table name for the data sent via Cloud Extract sources?

RudderStack sets the table name for the resource you are syncing to the warehouse by adding `rudder_` to the **Table prefix** you set while configuring your Cloud Extract source in the dashboard.

[![Cloud Extract table prefix](/docs/images/cloud-extract-sources/etl-table-prefix.webp)](</docs/images/cloud-extract-sources/etl-table-prefix.webp>)

For example, if you set `test_` as the **Table prefix** in the dashboard, RudderStack sets the table name as `test_rudder_<resource_name>`, where `<resource_name>` is the name of the resource you are syncing (for example, `contacts`, `messages`, etc.).

> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add the character `_` to the prefix by default. Hence, you need to specify it while setting the prefix.