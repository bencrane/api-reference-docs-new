# Google Analytics 4 Cloud Extract Source Deprecated

Sync data from Google Analytics 4 to your warehouse destination via RudderStack.

* * *

  * __5 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> This source is deprecated and no longer supported as of **January 10, 2026**.

[Google Analytics 4](<https://analytics.google.com/>) is an analytics service that enables you to measure traffic and engagement across your websites and apps.

This document guides you in setting up Google Analytics 4 as a source in RudderStack. Once configured, RudderStack automatically ingests your Google Analytics 4 data and routes it to your specified data warehouse destination.

> ![info](/docs/images/info.svg)
> 
> All Cloud Extract sources support sending data only to a [data warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).

## Getting started

To set up Google Analytics 4 as a source in RudderStack, follow these steps:

  1. Log into your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Sources** > **New source** > **Cloud Extract** and select **Google Analytics 4** from the list of sources.
  3. Assign a name to your source and click **Continue**.


### Connection settings

Next, configure the following dashboard settings:

  * **Credentials** : From the dropdown, select the authentication mechanism for RudderStack to connect to the Google Analytics 4 API.
    * **Authenticate via Google (OAuth)** : To authenticate via OAuth, click the **Sign in with Google** button, select your Google account, and give RudderStack the required permissions.
    * **Service Account Key Authentication** : Enter your [service account](<https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating>) JSON credentials in the **Service Account Information** field.

[![Google Analytics 4 authentication](/docs/images/cloud-extract-sources/google-analytics-4-connection-settings-1.webp)](</docs/images/cloud-extract-sources/google-analytics-4-connection-settings-1.webp>)

The other settings are as follows:

[![Google Analytics 4 dashboard settings](/docs/images/cloud-extract-sources/google-analytics-4-connection-settings-2.webp)](</docs/images/cloud-extract-sources/google-analytics-4-connection-settings-2.webp>)

  * **Property ID** : Specify the [Google Analytics 4 property identifier](<https://developers.google.com/analytics/devguides/reporting/data/v1/property-id>) whose events are tracked.
  * **Date Range Start Date** : Choose the start date from which you want RudderStack to ingest the Google Analytics 4 data. RudderStack will not replicate any data before this date.
  * **Custom Reports** : Use this setting to sync your custom [Google Analytics 4 reports](<https://support.google.com/analytics/answer/10445879?hl=en>). To add a custom report, click **Add Report** and specify the **Report Name** , **Metrics** , and **Dimensions** :

[![Google Analytics 4 custom reports](/docs/images/cloud-extract-sources/google-analytics-4-custom-report.webp)](</docs/images/cloud-extract-sources/google-analytics-4-custom-report.webp>)

> ![info](/docs/images/info.svg)
> 
> You can sync multiple reports, and edit or delete a custom report.

  * **Data request time increment in days** : Enter the number of days after which RudderStack requests data from the Google Analytics 4 API. The minimum and maximum allowed values for this field are 1 and 364 respectively.


> ![info](/docs/images/info.svg)
> 
> It is highly recommended to set this value to 1. A higher value will lead to faster syncs, but it is more likely to apply sampling on your data, causing potential inaccuracies in the results.

### Destination settings

The following settings specify how RudderStack sends the data ingested from Google Analytics 4 to the connected warehouse destination:

  * **Table prefix** : RudderStack uses this prefix to create a table in your data warehouse and loads all your Google Analytics 4 data into it.


> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add special characters like `-` or `_` to the prefix by default. Hence, you need to specify it while setting the prefix.

  * **Schedule Settings** : RudderStack gives you three options to ingest the data from Google Analytics 4:
    * **Basic** : Runs the syncs at the specified time interval.
    * **CRON** : Runs the syncs based on the user-defined CRON expression.
    * **Manual** : You are required to run the syncs manually.


> ![info](/docs/images/info.svg)
> 
> For more information on the schedule types, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/>) guide.

### Selecting the data to import

You can choose the predefined Google Analytics 4 reports from which you want to ingest the data by selecting them in this window:

[![Selecting the data to import](/docs/images/cloud-extract-sources/google-analytics-4-data-import-settings.webp)](</docs/images/cloud-extract-sources/google-analytics-4-data-import-settings.webp>)

> ![info](/docs/images/info.svg)
> 
> Any custom reports configured using the **Custom Reports** dashboard setting will also be shown here.

The below table mentions the sync types supported by the Google Analytics 4 resources while syncing data to your warehouse destination:

Resource| Sync type| Primary key  
---|---|---  
`daily_active_users`| Incremental| `uuid`  
`devices`| Incremental| `uuid`  
`four_weekly_active_users`| Incremental| `uuid`  
`locations`| Incremental| `uuid`  
`pages`| Incremental| `uuid`  
`traffic_sources`| Incremental| `uuid`  
`website_overview`| Incremental| `uuid`  
`weekly_active_users`| Incremental| `uuid`  
  
For syncing all reports, RudderStack uses the `analyticsdata.googleapis.com/v1beta/{property_id}/runReport` API.

> ![warning](/docs/images/warning.svg)
> 
> This source only supports **Incremental** reports with **date** as a required dimension.

> ![info](/docs/images/info.svg)
> 
> For more information on the **Incremental** sync mode, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/#sync-modes>) guide.

Google Analytics 4 is now configured as a source. RudderStack will start ingesting data from Google Analytics 4 as per your specified schedule and frequency.

You can further connect this source to your data warehouse by clicking the **Add Destination** button:

[![Adding a destination](/docs/images/cloud-extract-sources/add-destination.webp)](</docs/images/cloud-extract-sources/add-destination.webp>)

> ![info](/docs/images/info.svg)
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

#### Why am I getting a `403 Client Error` while setting up the Google Analytics 4 source?

You must assign the following permissions in Google Analytics 4 to set it up as an Extract source successfully:
    
    
    const scope_google_analytics = [
      'https://www.googleapis.com/auth/userinfo.profile',
      'https://www.googleapis.com/auth/userinfo.email',
      'https://www.googleapis.com/auth/analytics.readonly',
    ];