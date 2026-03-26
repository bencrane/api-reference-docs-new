# ActiveCampaign Cloud Extract Source Deprecated

Sync data from ActiveCampaign to your warehouse destination via RudderStack.

* * *

  * __4 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> This source is deprecated and no longer supported as of **January 10, 2026**.

[ActiveCampaign](<https://www.activecampaign.com/>) is a popular marketing automation and CRM platform that lets you drive effective customer engagement and retention.

This document guides you in setting up ActiveCampaign as a source in RudderStack. Once configured, RudderStack automatically ingests your specified ActiveCampaign data, which can then be routed to your RudderStack-supported data warehouse destination.

> ![info](/docs/images/info.svg)
> 
> All Cloud Extract sources support sending data only to a [data warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).

## Getting started

To set up ActiveCampaign as a source in RudderStack, follow these steps:

  1. Log into your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Sources** > **New source** > **Cloud Extract** and select **ActiveCampaign** from the list of sources.
  3. Assign a name to your source and click **Next**.


### Connection settings

  1. Click **Create Credentials from Scratch**. You will then see the following screen:

[![ActiveCampaign credentials](/docs/images/cloud-extract-sources/activecampaign-connection-settings.webp)](</docs/images/cloud-extract-sources/activecampaign-connection-settings.webp>)

  2. Enter the following connection credentials to authenticate your ActiveCampaign account with RudderStack:


  * **Account Name** : Enter your ActiveCampaign account name. You can find it in your ActiveCampaign dashboard by going to the **Settings** > **Account** section.
  * **URL** : Enter your ActiveCampaign API access URL. You can find it in your ActiveCampaign dashboard by going to the **Settings** > **Developer** section.
  * **API Key** : Enter your ActiveCampaign API key. You can find it in your ActiveCampaign dashboard by going to the **Settings** > **Developer** section.


> ![info](/docs/images/info.svg)
> 
> For more information on obtaining the ActiveCampaign account name, URL, and API key, refer to the FAQ section below.

### Destination settings

The following settings specify how RudderStack sends the data ingested from ActiveCampaign to the connected warehouse destination:

  * **Table prefix** : RudderStack uses this prefix to create a table in your data warehouse and loads all your ActiveCampaign data into it.


> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add special characters like `-` or `_` to the prefix by default. Hence, you need to specify it while setting the prefix.

  * **Schedule Settings** : RudderStack gives you three options to ingest the data from ActiveCampaign:
    * **Basic** : Runs the syncs at the specified time interval.
    * **CRON** : Runs the syncs based on the user-defined CRON expression.
    * **Manual** : You are required to run the syncs manually.


> ![info](/docs/images/info.svg)
> 
> For more information on the schedule types, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/>) guide.

### Selecting the data to import

Choose the ActiveCampaign data that you wish to ingest via RudderStack. You can either select all data or choose specific ActiveCampaign data attributes as per your requirement.

[![Selecting the data to import](/docs/images/cloud-extract-sources/activecampaign-connection-settings-2.webp)](</docs/images/cloud-extract-sources/activecampaign-connection-settings-2.webp>)

ActiveCampaign is now configured as a source. RudderStack will start ingesting data from ActiveCampaign as per your specified schedule and frequency.

You can further connect this source to your data warehouse by clicking on **Add Destination** :

[![Adding a destination](/docs/images/cloud-extract-sources/add-destination.webp)](</docs/images/cloud-extract-sources/add-destination.webp>)

> ![success](/docs/images/tick.svg)
> 
> Use the **Use Existing Destination** option if you have an already-configured data warehouse destination in RudderStack. To configure a data warehouse destination from scratch, select the **Create New Destination** button.

## FAQ

#### How do I obtain the ActiveCampaign account name?

Go to your ActiveCampaign dashboard and locate it under **Settings** > **Account** > **Account Information** :

[![ActiveCampaign account name](/docs/images/cloud-extract-sources/activecampaign-connection-settings-4.webp)](</docs/images/cloud-extract-sources/activecampaign-connection-settings-4.webp>)

#### How do I obtain the ActiveCampaign API key and URL?

Go to your ActiveCampaign dashboard and locate these under **Settings** > **Developer** > **API Access** :

[![ActiveCampaign API key and URL](/docs/images/cloud-extract-sources/activecampaign-connection-settings-3.webp)](</docs/images/cloud-extract-sources/activecampaign-connection-settings-3.webp>)

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