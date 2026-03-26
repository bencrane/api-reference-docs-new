# Marketo Cloud Extract Source Deprecated

Sync data from Marketo to your warehouse destination via RudderStack.

* * *

  * __4 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> This source is deprecated and no longer supported as of **January 10, 2026**.

[Marketo](<https://marketo.com>) is a leading marketing automation platform. It offers effective behavior tracking and personalized marketing solutions to enhance users’ product experience.

This document guides you in setting up Marketo as a source in RudderStack. Once configured, RudderStack automatically ingests your specified Marketo data and routes it to your specified data warehouse destination.

> ![warning](/docs/images/warning.svg)
> 
> All Cloud Extract sources support sending data only to a [data warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).

## Getting started

  1. Log in to your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Collect** > **Sources** > **New Source** > **Cloud Extract**. From the list of sources, select **Marketo**.
  3. Name your source and click **Continue**.


## Connection settings

  * **Client ID** : Enter your Marketo client ID.
  * **Client Secret** : Enter the associated client secret.


> ![info](/docs/images/info.svg)
> 
> For steps on obtaining the Marketo client ID and secret, see FAQ.
> 
> See [Marketo API documentation](<https://developers.marketo.com/rest-api/authentication/>) for more information on these credentials.

  * **Start date** : Select the date from when RudderStack should ingest your Shopify data. RudderStack will **not replicate** any data before this date.
  * **Domain URL** : Enter your Marketo base URL. See [Marketo API documentation](<https://developers.marketo.com/rest-api/base-url/>) for more information on obtaining this URL.


### Destination settings

The following settings specify how RudderStack sends the data ingested from Marketo to the connected warehouse destination:

  * **Table prefix** : RudderStack uses this prefix to create a table in your data warehouse and loads all your Marketo data into it.


> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add special characters like `-` or `_` to the prefix by default. Hence, you need to specify it while setting the prefix.

  * **Schedule Settings** : RudderStack gives you three options to ingest the data from Marketo:
    * **Basic** : Runs the syncs at the specified time interval.
    * **CRON** : Runs the syncs based on the user-defined CRON expression.
    * **Manual** : You are required to run the syncs manually.


> ![info](/docs/images/info.svg)
> 
> For more information on the schedule types, see [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/>).

  * **Frequency** : Specify how often RudderStack should run the data syncs.
  * **Sync Starting At** : Set the time to start the sync (in UTC).


### Select data to import

You can import specific Marketo data by selecting the required resources:

Resource| Sync type| Primary key| Cursor field| Bulk extract support  
---|---|---|---|---  
`activity_types`| Full Refresh| `id`| -| No  
`campaigns`| Incremental| -| `createdAt`| No  
`leads`| Incremental| -| `updatedAt`| Yes  
`lists`| Incremental| -| -| No  
`programs`| Incremental| -| `updatedAt`| No  
`activities_X`| Incremental| `marketoGUID`| `activityDate`| Yes  
  
> ![info](/docs/images/info.svg)
> 
> For more information on the **Full Refresh** and **Incremental** sync modes, see [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/#sync-modes>).

## FAQ

#### Is it possible to have multiple Cloud Extract sources writing to the same schema?

Yes, it is.

We have implemented a feature wherein RudderStack associates a table prefix for every Cloud Extract source writing to a warehouse schema. This way, multiple Cloud Extract sources can write to the same schema with different table prefixes.

#### How do I obtain the Marketo client ID and secret?

To set up the Marketo API service and obtain the client ID and secret associated with it, follow these steps:

  1. Log into your Marketo instance and click the **Admin** tab.
  2. Select **LaunchPoint**.

[![](/docs/images/event-stream-destinations/marketo-launchpoint.webp)](</docs/images/event-stream-destinations/marketo-launchpoint.webp>)

  3. Here, you will able to see all installed services used for connecting to Marketo.
  4. Click **View Details** in your API service to see the associated client ID and secret. Use these credentials to configure the Marketo source in RudderStack.

[![](/docs/images/event-stream-destinations/marketo-service-details.webp)](</docs/images/event-stream-destinations/marketo-service-details.webp>)

#### How does RudderStack count the events for Cloud Extract sources?

RudderStack counts the number of records returned by the source APIs when queried during each sync. It considers each record as an event.

#### How does RudderStack set the table name for the data sent via Cloud Extract sources?

RudderStack sets the table name for the resource you are syncing to the warehouse by adding `rudder_` to the **Table prefix** you set while configuring your Cloud Extract source in the dashboard.

[![Cloud Extract table prefix](/docs/images/cloud-extract-sources/etl-table-prefix.webp)](</docs/images/cloud-extract-sources/etl-table-prefix.webp>)

For example, if you set `test_` as the **Table prefix** in the dashboard, RudderStack sets the table name as `test_rudder_<resource_name>`, where `<resource_name>` is the name of the resource you are syncing (for example, `contacts`, `messages`, etc.).

> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add the character `_` to the prefix by default. Hence, you need to specify it while setting the prefix.