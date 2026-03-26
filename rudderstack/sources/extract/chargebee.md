# Chargebee Cloud Extract Source Deprecated

Sync data from Chargebee to your warehouse destination via RudderStack.

* * *

  * __4 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> This source is deprecated and no longer supported as of **January 10, 2026**.

[Chargebee](<https://www.Chargebee.com/>) is a subscription billing and revenue management platform. It lets you streamline your revenue operations via features like subscription workflow automation, cutting-edge revenue reporting, and more.

This document guides you in setting up Chargebee as a source in RudderStack. Once configured, RudderStack automatically ingests your specified Chargebee data, which can then be routed to your RudderStack-supported data warehouse destination.

> ![info](/docs/images/info.svg)
> 
> All Cloud Extract sources support sending data only to a [data warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).

## Getting started

To set up Chargebee as a source in RudderStack, follow these steps:

  1. Log into your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Sources** > **New source** > **Cloud Extract** and select **Chargebee** from the list of sources.
  3. Assign a name to your source and click **Next**.


### Connection settings

Enter the following connection credentials to authenticate your Chargebee account with RudderStack:

[![Chargebee connection settings](/docs/images/cloud-extract-sources/chargebee-1.webp)](</docs/images/cloud-extract-sources/chargebee-1.webp>)

  * **Site** : Enter your Chargebee site name.
  * **API Key** : Enter your [Chargebee API key](<https://www.chargebee.com/docs/2.0/api_keys.html>).
  * **Start Date** : Enter the date from which RudderStack should import your historical Chargebee data.
  * **Product Catalog** : Select your [Chargebee Product Catalog version](<https://www.chargebee.com/docs/2.0/product-catalog.html>) from the dropdown.


> ![warning](/docs/images/warning.svg)
> 
> RudderStack does not support changing the **Product Catalog** version once you have successfully set up the source.

### Destination settings

The following settings specify how RudderStack sends the data ingested from Chargebee to the connected warehouse destination:

  * **Table prefix** : RudderStack uses this prefix to create a table in your data warehouse and loads all your Chargebee data into it.


> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add special characters like `-` or `_` to the prefix by default. Hence, you need to specify it while setting the prefix.

  * **Schedule Settings** : RudderStack gives you three options to ingest the data from Chargebee:
    * **Basic** : Runs the syncs at the specified time interval.
    * **CRON** : Runs the syncs based on the user-defined CRON expression.
    * **Manual** : You are required to run the syncs manually.


> ![info](/docs/images/info.svg)
> 
> For more information on the schedule types, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/>) guide.

### Selecting the data to import

You can choose the Chargebee data you want to ingest by selecting the required resources:

[![Selecting the data to import](/docs/images/cloud-extract-sources/chargebee-2.webp)](</docs/images/cloud-extract-sources/chargebee-2.webp>)

The below table mentions the sync types supported by the Chargebee resources while syncing data to your warehouse destination, with `id` as the primary key for all:

Resource| Sync type  
---|---  
`coupon`| Incremental  
`credit note`| Incremental  
`customer`| Incremental  
`event`| Incremental  
`invoice`| Incremental  
`order`| Incremental  
`subscription`| Incremental  
`transaction`| Incremental  
`addon`| Incremental  
`plan`| Incremental  
`item`| Incremental  
`item prices`| Incremental  
`attached items`| Semi-incremental  
  
> ![info](/docs/images/info.svg)
> 
> For more information on the **Semi-Incremental** and **Incremental** sync modes, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/#sync-modes>) guide.

## FAQ

#### How do I obtain the Chargebee API key?

The Chargebee API key is required to authenticate your app and regulate its access to the Chargebee API. To obtain the API key, log into your Chargebee dashboard and go to **Settings** > **Configure Chargebee** > **API Keys and Webhooks**. Then, click the **API Keys** tab. Your API key should be listed here.

For more information, refer to the [Chargebee documentation](<https://www.chargebee.com/docs/2.0/api_keys.html>).

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