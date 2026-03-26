# Salesforce Cloud Extract Source Deprecated

Sync data from Salesforce to your warehouse destination via RudderStack.

* * *

  * __4 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> This source is deprecated and no longer supported as of **January 10, 2026**.

[Salesforce](<https://salesforce.com/>) is an industry leader in enterprise CRM. It offers a suite of enterprise applications revolving around marketing automation, customer support, application development, and analytics.

This document guides you in setting up Salesforce as a source in RudderStack. Once configured, RudderStack automatically ingests your specified Salesforce data, which can then be routed to your RudderStack-supported data warehouse destination.

> ![info](/docs/images/info.svg)
> 
> All Cloud Extract sources support sending data only to a [data warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).

## Getting started

To set up Salesforce as a source in RudderStack, follow these steps:

  1. Log into your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Sources** > **New source** > **Cloud Extract** and select **Salesforce** from the list of sources.
  3. Assign a name to your source and click **Continue**.


### Connection settings

To set up Salesforce as a Cloud Extract source, you need to configure the following settings:

[![Salesforce credentials](/docs/images/cloud-extract-sources/salesforce-connection-settings-1.webp)](</docs/images/cloud-extract-sources/salesforce-connection-settings-1.webp>)

  * Enable the **Sandbox** checkbox if your app is in the Salesforce [sandbox](<https://help.salesforce.com/s/articleView?id=sf.create_test_instance.htm&type=5>) mode.


> ![warning](/docs/images/warning.svg)
> 
> It is highly recommended to keep the checkbox unchecked if you’re unsure whether your app is in a Salesforce sandbox.

  * Click **Connect with Salesforce V2** and connect your Salesforce account with RudderStack.
  * **Start Date** : Choose the start date from which you want RudderStack to ingest the Salesforce data. RudderStack will not replicate any data before this date.


> ![warning](/docs/images/warning.svg)
> 
> If you do not specify the start date, RudderStack will replicate all your data by default.

> ![info](/docs/images/info.svg)
> 
> RudderStack replicates all Salesforce data associated with the `updated` field. If not present, it picks the data associated with the `created` field.
> 
> **RudderStack only reads your Salesforce data and does not write to it**.

  * **Salesforce Object filtering criteria** : This optional setting lets you add the filtering criteria to read and ingest only the Salesforce objects relevant to you.

[![Salesforce credentials](/docs/images/cloud-extract-sources/salesforce-connection-settings-2.webp)](</docs/images/cloud-extract-sources/salesforce-connection-settings-2.webp>)

### Destination settings

The following settings specify how RudderStack sends the data ingested from Salesforce to the connected warehouse destination:

  * **Table prefix** : RudderStack uses this prefix to create a table in your data warehouse and loads all your Salesforce data into it.


> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add special characters like `-` or `_` to the prefix by default. Hence, you need to specify it while setting the prefix.

  * **Schedule Settings** : RudderStack gives you three options to ingest the data from Salesforce:
    * **Basic** : Runs the syncs at the specified time interval.
    * **CRON** : Runs the syncs based on the user-defined CRON expression.
    * **Manual** : You are required to run the syncs manually.


> ![info](/docs/images/info.svg)
> 
> For more information on the schedule types, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/>) guide.

### Selecting the data to import

Choose the Salesforce data that you wish to ingest via RudderStack. You can either select all data or choose specific Salesforce data attributes as per your requirement.

[![Selecting the data to import](/docs/images/cloud-extract-sources/salesforce-connection-settings-3.webp)](</docs/images/cloud-extract-sources/salesforce-connection-settings-3.webp>)

> ![info](/docs/images/info.svg)
> 
> For more information on how RudderStack syncs your Salesforce data, refer to the FAQ section below.

Salesforce is now configured as a source. RudderStack will start ingesting data from Salesforce as per your specified schedule and frequency.

You can further connect this source to your data warehouse by clicking on **Add Destination** :

[![Adding a destination](/docs/images/cloud-extract-sources/add-destination.webp)](</docs/images/cloud-extract-sources/add-destination.webp>)

> ![success](/docs/images/tick.svg)
> 
> Use the **Use Existing Destination** option if you have an already-configured data warehouse destination in RudderStack. To configure a data warehouse destination from scratch, select the **Create New Destination** button.

## FAQ

#### Can I connect my Salesforce source to multiple data warehouse destinations?

You can connect **only one data warehouse destination** per Cloud Extract source. If you wish to send data to multiple warehouses, you can configure multiple Cloud Extract sources with the same settings and connect them to each data warehouse.

#### How does RudderStack handle the Salesforce rate limits?

RudderStack automatically stops the sync process if the Salesforce [rate limits](<https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm>) are hit. Once the limits are lifted, RudderStack starts the next data sync from the point it last stopped.

#### Is it possible to have multiple Cloud Extract sources writing to the same schema?

Yes, it is.

RudderStack associates a table prefix for every Cloud Extract source writing to a warehouse schema. This way, multiple Cloud Extract sources can write to the same schema with different table prefixes.

> ![info](/docs/images/info.svg)
> 
> For more information on setting a table prefix, refer to the Destination settings section above.

#### How does RudderStack count the events for Cloud Extract sources?

RudderStack counts the number of records returned by the source APIs when queried during each sync. It considers each record as an event.

#### How does RudderStack set the table name for the data sent via Cloud Extract sources?

RudderStack sets the table name for the resource you are syncing to the warehouse by adding `rudder_` to the **Table prefix** you set while configuring your Cloud Extract source in the dashboard.

[![Cloud Extract table prefix](/docs/images/cloud-extract-sources/etl-table-prefix.webp)](</docs/images/cloud-extract-sources/etl-table-prefix.webp>)

For example, if you set `test_` as the **Table prefix** in the dashboard, RudderStack sets the table name as `test_rudder_<resource_name>`, where `<resource_name>` is the name of the resource you are syncing (for example, `contacts`, `messages`, etc.).

> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add the character `_` to the prefix by default. Hence, you need to specify it while setting the prefix.