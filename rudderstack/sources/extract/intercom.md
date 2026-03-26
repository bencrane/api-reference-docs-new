# Intercom Cloud Extract Source Deprecated

Sync data from Intercom to your warehouse destination via RudderStack.

* * *

  * __4 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> This source is deprecated and no longer supported as of **January 10, 2026**.

[Intercom](<https://www.intercom.com/>) is an industry-leading, real-time business messaging platform, that allows you to bring together and manage all your customer life cycle activities on a single platform.

This document guides you in setting up Intercom as a source in RudderStack. Once configured, RudderStack automatically ingests your Intercom data and routes it to your specified data warehouse destination.

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * All Cloud Extract sources support sending data only to a [data warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).
>   * This source supports **Intercom API v2.1 and above**.
> 


## Getting started

To set up Intercom as a source in RudderStack, follow these steps:

  1. Log into your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Sources** > **New source** > **Cloud Extract** and select **Intercom** from the list of sources.
  3. Assign a name to your source and click **Continue**.


### Connection settings

Next, configure the following dashboard settings:

[![Configuring Intercom](/docs/images/cloud-extract-sources/intercomv2-3.webp)](</docs/images/cloud-extract-sources/intercomv2-3.webp>)

  * Authenticate RudderStack with Intercom by clicking the **Connect with Intercom** button.
  * **Start Date** : Enter the date from which RudderStack should ingest the Intercom data. RudderStack will not replicate any data before this date.


### Destination settings

The following settings specify how RudderStack sends the data ingested from Intercom to the connected warehouse destination:

  * **Table prefix** : RudderStack uses this prefix to create a table in your data warehouse and loads all your Intercom data into it.


> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add special characters like `-` or `_` to the prefix by default. Hence, you need to specify it while setting the prefix.

  * **Schedule Settings** : RudderStack gives you three options to ingest the data from Intercom:
    * **Basic** : Runs the syncs at the specified time interval.
    * **CRON** : Runs the syncs based on the user-defined CRON expression.
    * **Manual** : You are required to run the syncs manually.


> ![info](/docs/images/info.svg)
> 
> For more information on the schedule types, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/>) guide.

### Selecting the data to import

You can choose the Intercom data you want to ingest by selecting the required resources:

[![Selecting the data to import](/docs/images/cloud-extract-sources/intercomv2-5.webp)](</docs/images/cloud-extract-sources/intercomv2-5.webp>)

The below table mentions the sync types supported by the Intercom resources while syncing data to your warehouse destination:

Resource| Sync type| Primary key| Intercom API endpoint  
---|---|---|---  
`admins`| Full Refresh| `id`| `/admins`  
`companies`| Incremental| `id`| `/companies/scroll`  
`company segments`| Incremental| `id`| `/companies/<id>/segments`  
`company attributes`| Full Refresh| `name`| `/data_attributes?model=company`  
`conversations`| Incremental| `id`| `/conversations`  
`conversation parts`| Incremental| `id`| `/conversations/<id>`  
`contacts`| Incremental| `id`| `/contacts`  
`contact attributes`| Full Refresh| `name`| `/data_attributes?model=contact`  
`segments`| Incremental| `id`| `/segments`  
`tags`| Full Refresh| `name`| `/tags`  
`teams`| Full Refresh| `name`| `/teams`  
  
> ![info](/docs/images/info.svg)
> 
> For more information on the **Full Refresh** , **Semi-Incremental** , and **Incremental** sync modes, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/#sync-modes>) guide.

## Troubleshooting

### Sync errors for older Intercom API versions

For Intercom versions less than **2.1** , data syncs to the warehouse destination will fail and throw an error. This is because many Intercom resources are not supported by the older API versions.

In such a scenario, it is highly recommended to updated your Intercom API.

> ![info](/docs/images/info.svg)
> 
> For more information on updating your Intercom API version, refer to this [Intercom support page](<https://developers.intercom.com/building-apps/docs/update-your-api-version>).

## FAQ

#### Is it possible to have multiple Cloud Extract sources writing to the same schema?

Yes, it is - RudderStack associates a table prefix for every Cloud Extract source writing to a warehouse schema. This way, multiple Cloud Extract sources can write to the same schema with different table prefixes.

#### My data syncs are failing. What should I do?

If your data syncs are failing, verify if your Intercom version is **2.1** or above. For versions less than 2.1, data syncs to the warehouse destination will fail. This is because many Intercom resources are not supported by the older API versions. In this scenario, you will need to update your Intercom API.

For more information on updating your Intercom API version, refer to the [Intercom support page](<https://developers.intercom.com/building-apps/docs/update-your-api-version>).

> ![info](/docs/images/info.svg)
> 
> If you are using Intercom 2.1 or above and are facing this issue, contact us via [email](<mailto:%20support@rudderstack.com>) or [Slack](<https://rudderstack.com/join-rudderstack-slack-community>).

#### How does RudderStack count the events for Cloud Extract sources?

RudderStack counts the number of records returned by the source APIs when queried during each sync. It considers each record as an event.

#### How does RudderStack set the table name for the data sent via Cloud Extract sources?

RudderStack sets the table name for the resource you are syncing to the warehouse by adding `rudder_` to the **Table prefix** you set while configuring your Cloud Extract source in the dashboard.

[![Cloud Extract table prefix](/docs/images/cloud-extract-sources/etl-table-prefix.webp)](</docs/images/cloud-extract-sources/etl-table-prefix.webp>)

For example, if you set `test_` as the **Table prefix** in the dashboard, RudderStack sets the table name as `test_rudder_<resource_name>`, where `<resource_name>` is the name of the resource you are syncing (for example, `contacts`, `messages`, etc.).

> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add the character `_` to the prefix by default. Hence, you need to specify it while setting the prefix.