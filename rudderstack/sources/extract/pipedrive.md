# Pipedrive Cloud Extract Source Deprecated

Sync data from Pipedrive to your warehouse destination via RudderStack.

* * *

  * __4 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> This source is deprecated and no longer supported as of **January 10, 2026**.

[Pipedrive](<https://www.pipedrive.com/>) is a popular sales CRM and pipeline management tool. It lets you manage your leads, track all your customer communications, and automate administrative tasks.

This document guides you in setting up Pipedrive as a source in RudderStack. Once configured, RudderStack automatically ingests your Pipedrive data and routes it to your specified data warehouse destination.

> ![info](/docs/images/info.svg)
> 
> All Cloud Extract sources support sending data only to a [data warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).

## Getting started

To set up Pipedrive as a source in RudderStack, follow these steps:

  1. Log into your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Sources** > **New source** > **Cloud Extract** and select **Pipedrive** from the list of sources.
  3. Assign a name to your source and click **Continue**.


### Connection settings

To set up Pipedrive as a Cloud Extract source, configure the following settings:

[![Pipedrive credentials](/docs/images/cloud-extract-sources/pipedrive-connection-settings.webp)](</docs/images/cloud-extract-sources/pipedrive-connection-settings.webp>)

  * **Start Date** : Select the date from when RudderStack ingests your Pipedrive data. RudderStack will **not replicate** any data before this date.
  * **API Token** : Enter your Pipedrive API token. Refer to the [Pipedrive documentation](<https://pipedrive.readme.io/docs/how-to-find-the-api-token>) for more information on obtaining the API token.


### Destination settings

The following settings specify how RudderStack sends the data ingested from Pipedrive to the connected warehouse destination:

  * **Table prefix** : RudderStack uses this prefix to create a table in your data warehouse and loads all your Pipedrive data into it.


> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add special characters like `-` or `_` to the prefix by default. Hence, you need to specify it while setting the prefix.

  * **Schedule Settings** : RudderStack gives you three options to ingest the data from Pipedrive:
    * **Basic** : Runs the syncs at the specified time interval.
    * **CRON** : Runs the syncs based on the user-defined CRON expression.
    * **Manual** : You are required to run the syncs manually.


> ![info](/docs/images/info.svg)
> 
> For more information on the schedule types, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/>) guide.

### Selecting the data to import

You can choose the Pipedrive data you want to ingest by selecting the required resources:

[![Selecting the data to import](/docs/images/cloud-extract-sources/pipedive-v2-resources.webp)](</docs/images/cloud-extract-sources/pipedive-v2-resources.webp>)

The below table mentions the syncs supported by these resources from Pipedrive to your warehouse destination where `id` is a common primary key for all:

Resource| Sync type| Pipedrive API endpoint  
---|---|---  
`users`| Incremental| `/v1/users`  
`stages`| Incremental| `/v1/stages`  
`products`| Incremental| `/v1/products`  
`product_fields`| Full Refresh| `/v1/productFields`  
`pipelines`| Incremental| `/v1/pipelines`  
`persons`| Incremental| `/v1/persons`  
`person_fields`| Full Refresh| `/v1/personFields`  
`organizations`| Incremental| `/v1/organizations`  
`organization_fields`| Full Refresh| `/v1/organizationFields`  
`notes`| Incremental| `/v1/notes`  
`leads`| Full Refresh| `/v1/leads`  
`deals`| Incremental| `/v1/deals`  
`deal_fields`| Full Refresh| `/v1/dealFields`  
`activity_fields`| Full Refresh| `/v1/activityFields`  
`activities`| Incremental| `/v1/activities`  
  
> ![info](/docs/images/info.svg)
> 
> For more information on the **Full Refresh** , **Semi-Incremental** , and **Incremental** sync modes, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/#sync-modes>) guide.

Pipedrive is now configured as a source. RudderStack will start ingesting data from Pipedrive as per your specified schedule and frequency.

You can further connect this source to your data warehouse by clicking on **Add Destination** :

[![Adding a destination](/docs/images/cloud-extract-sources/add-destination.webp)](</docs/images/cloud-extract-sources/add-destination.webp>)

> ![success](/docs/images/tick.svg)
> 
> Use the **Use Existing Destination** option if you have an already-configured data warehouse destination in RudderStack. To configure a data warehouse destination from scratch, select the **Create New Destination** button.

## FAQ

#### Is it possible to have multiple Cloud Extract sources writing to the same schema?

Yes, it is.

RudderStack implements a feature wherein it associates a table prefix for every Cloud Extract source writing to a warehouse schema. This way, multiple Cloud Extract sources can write to the same schema with different table prefixes.

#### How does RudderStack count the events for Cloud Extract sources?

RudderStack counts the number of records returned by the source APIs when queried during each sync. It considers each record as an event.

#### How does RudderStack set the table name for the data sent via Cloud Extract sources?

RudderStack sets the table name for the resource you are syncing to the warehouse by adding `rudder_` to the **Table prefix** you set while configuring your Cloud Extract source in the dashboard.

[![Cloud Extract table prefix](/docs/images/cloud-extract-sources/etl-table-prefix.webp)](</docs/images/cloud-extract-sources/etl-table-prefix.webp>)

For example, if you set `test_` as the **Table prefix** in the dashboard, RudderStack sets the table name as `test_rudder_<resource_name>`, where `<resource_name>` is the name of the resource you are syncing (for example, `contacts`, `messages`, etc.).

> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add the character `_` to the prefix by default. Hence, you need to specify it while setting the prefix.