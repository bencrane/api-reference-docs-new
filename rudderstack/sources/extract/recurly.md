# Recurly Cloud Extract Source Deprecated

Sync data from Recurly to your warehouse destination via RudderStack.

* * *

  * __4 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> This source is deprecated and no longer supported as of **January 10, 2026**.

[Recurly](<https://recurly.com/>) is a subscription management platform that maximizes the subscriber lifetime value with expertise, technology, and insights for the global brands.

This document guides you in setting up Recurly as a source in RudderStack. Once configured, RudderStack automatically ingests your specified Recurly data, which can then be routed to your RudderStack-supported data warehouse destination.

> ![info](/docs/images/info.svg)
> 
> All Cloud Extract sources support sending data only to a [data warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).

## Getting started

To set up Recurly as a source in RudderStack, follow these steps:

  1. Log into your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Sources** > **New source** > **Cloud Extract** and select **Recurly** from the list of sources.
  3. Assign a name to your source and click **Continue**.


### Connection settings

[![Recurly credentials](/docs/images/cloud-extract-sources/recurly-connection-settings.webp)](</docs/images/cloud-extract-sources/recurly-connection-settings.webp>)

  * **API Key** : Enter your Recurly API key by going to your Recurly dashboard and navigating to **Integrations** > **API Credentials**.
  * **begin_time** : Enter the date when the Recurly API should start the replication.
  * **end_time** : Enter the date at which the Recurly API stops the replication. RudderStack will not import any data records after this timestamp.


> ![info](/docs/images/info.svg)
> 
> For more information on how to obtain the Recurly API key, refer to the FAQ section below.

### Destination settings

The following settings specify how RudderStack sends the data ingested from Recurly to the connected warehouse destination:

  * **Table prefix** : RudderStack uses this prefix to create a table in your data warehouse and loads all your Recurly data into it.


> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add special characters like `-` or `_` to the prefix by default. Hence, you need to specify it while setting the prefix.

  * **Schedule Settings** : RudderStack gives you three options to ingest the data from Recurly:
    * **Basic** : Runs the syncs at the specified time interval.
    * **CRON** : Runs the syncs based on the user-defined CRON expression.
    * **Manual** : You are required to run the syncs manually.


> ![info](/docs/images/info.svg)
> 
> For more information on the schedule types, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/>) guide.

### Selecting the data to import

You can choose the Recurly data you want to ingest by selecting the required resources:

[![Selecting the data to import](/docs/images/cloud-extract-sources/recurly-connection-settings-1.webp)](</docs/images/cloud-extract-sources/recurly-connection-settings-1.webp>)

The below table mentions the sync types supported by the Recurly resources while syncing data to your warehouse destination, with `id` as the primary key for all:

Resource| Sync type  
---|---  
`export_dates`| Full Refresh  
`accounts`| Incremental  
`account_coupon_redemptions`| Incremental  
`account_notes`| Incremental  
`add_ons`| Incremental  
`billing_infos`| Incremental  
`coupons`| Incremental  
`credit_payments`| Incremental  
`invoices`| Incremental  
`line_items`| Incremental  
`measured_units`| Incremental  
`plans`| Incremental  
`shipping_addresses`| Incremental  
`shipping_methods`| Incremental  
`subscriptions`| Incremental  
`transactions`| Incremental  
`unique_coupons`| Incremental  
  
> ![info](/docs/images/info.svg)
> 
> For more information on the **Full Refresh** and **Incremental** sync modes, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/#sync-modes>) guide.

## FAQ

#### How do I obtain the Recurly API key?

To obtain the API key for configuring the Recurly Cloud Extract source, follow these steps:

  1. Log into your [Recurly dashboard](<https://recurly.com/>).
  2. Go to **Integrations** > **API Credentials** to find the API key as shown:

[![Recurly API key](/docs/images/cloud-extract-sources/recurly-connection-settings-2.webp)](</docs/images/cloud-extract-sources/recurly-connection-settings-2.webp>)

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