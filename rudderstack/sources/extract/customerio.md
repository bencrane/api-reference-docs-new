# Customer.io Cloud Extract Source Deprecated

Sync data from Customer.io to your warehouse destination via RudderStack.

* * *

  * __4 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> This source is deprecated and no longer supported as of **January 10, 2026**.

[Customer.io](<https://www.customer.io>) is a popular marketing platform for sending targeted emails and push and SMS notifications to improve conversions and customer engagement.

This document guides you in setting up Customer.io as a source in RudderStack. Once configured, RudderStack automatically ingests your Customer.io data and routes it to your specified data warehouse destination.

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * All Cloud Extract sources support sending data only to a [data warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).
>   * **Important** : This source only works for the Customer.io accounts in [US data-centers](<https://customer.io/docs/data-centers>).
> 


## Getting started

To set up Customer.io as a source in RudderStack, follow these steps:

  1. Log into your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Sources** > **New source** > **Cloud Extract** and select **Customer.io** from the list of sources.
  3. Assign a name to your source and click **Continue**.


### Connection settings

To set up Customer.io as a Cloud Extract source, you need to configure the following settings:

[![Customer.io credentials](/docs/images/cloud-extract-sources/customerio-connection-settings.webp)](</docs/images/cloud-extract-sources/customerio-connection-settings.webp>)

  * **App API Key** : Enter your Customer.io API key which can be obtained in the [Customer.io dashboard](<https://fly.customer.io/login>) by navigating to **Settings** > **Account Settings** > **API Credentials**.
  * **Cutoff Days** : Enter the number of days after which RudderStack fetches the updated data.


### Destination settings

The following settings specify how RudderStack sends the data ingested from Customer.io to the connected warehouse destination:

  * **Table prefix** : RudderStack uses this prefix to create a table in your data warehouse and loads all your Customer.io data into it.


> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add special characters like `-` or `_` to the prefix by default. Hence, you need to specify it while setting the prefix.

  * **Schedule Settings** : RudderStack gives you three options to ingest the data from Customer.io:
    * **Basic** : Runs the syncs at the specified time interval.
    * **CRON** : Runs the syncs based on the user-defined CRON expression.
    * **Manual** : You are required to run the syncs manually.


> ![info](/docs/images/info.svg)
> 
> For more information on the schedule types, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/>) guide.

### Selecting the data to import

You can choose the Customer.io data you want to ingest by selecting the required resources:

[![Selecting the data to import](/docs/images/cloud-extract-sources/customerio-resources.webp)](</docs/images/cloud-extract-sources/customerio-resources.webp>)

The below table lists the syncs supported by the Customer.io resources to your warehouse destination:

Resource| Full Refresh sync| Incremental sync  
---|---|---  
`newsletters`| Yes| Yes  
`campaigns`| Yes| Yes  
`campaign_actions`| Yes| Yes  
  
> ![info](/docs/images/info.svg)
> 
> For more information on the **Full Refresh** and **Incremental** sync modes, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/#sync-modes>) guide.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack ingests the Customer.io data using the [Customer.io Beta API](<https://customer.io/docs/api/#tag/appOverview>) which limits the API requests by 10 requests per second.

Customer.io is now configured as a source. RudderStack will start ingesting data from Customer.io as per your specified schedule and frequency.

You can further connect this source to your data warehouse by clicking on **Add Destination** :

[![Adding a destination](/docs/images/cloud-extract-sources/add-destination.webp)](</docs/images/cloud-extract-sources/add-destination.webp>)

> ![success](/docs/images/tick.svg)
> 
> Use the **Use Existing Destination** option if you have an already-configured data warehouse destination in RudderStack. To configure a data warehouse destination from scratch, select the **Create New Destination** button.

## FAQ

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