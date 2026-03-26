# Google Analytics Cloud Extract Source Deprecated

Sync data from Google Analytics to your warehouse destination via RudderStack.

* * *

  * __5 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> This source is deprecated and no longer supported as of **January 10, 2026**.

[Google Analytics](<https://analytics.google.com/analytics/web/#/>) is a popular analytics service that lets you track and report your website traffic across a variety of sources.

This document guides you in setting up Google Analytics as a source in RudderStack. Once configured, RudderStack automatically ingests your Google Analytics data and routes it to your specified data warehouse destination.

> ![info](/docs/images/info.svg)
> 
> All Cloud Extract sources support sending data only to a [data warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).

## Getting started

To set up Google Analytics as a Cloud Extract source in RudderStack, follow these steps:

  1. Log into your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Sources** > **New source** > **Cloud Extract** and select **Google Analytics** from the list of sources.
  3. Assign a name to your source and click **Continue**.


### Connection settings

Next, configure the following dashboard settings:

  * **Credentials** : Choose from one of the following two authentication types:

    * **Authenticate via Google (Oauth)** : Authenticate your Google Analytics account via Google (OAuth) by clicking **Sign in with Google** and granting the required permissions.
[![Google Analytics credentials](/docs/images/cloud-extract-sources/ga-oauth-settings.webp)](</docs/images/cloud-extract-sources/ga-oauth-settings.webp>)
    * **Service Account Key Authentication** : Enter the service account key in JSON format in the **Service Account JSON Key field**. Refer to the [Google documentation](<https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys>) for more information on obtaining the service account key.
[![Google Analytics credentials](/docs/images/cloud-extract-sources/ga-oauth-settings-4.webp)](</docs/images/cloud-extract-sources/ga-oauth-settings-4.webp>)


The rest of the settings are as follows:

  * **Replication Start Date** : Choose the start date from which you want RudderStack to ingest the Google Analytics data. RudderStack will not replicate any data before this date.

  * **View ID** : Enter the ID of the Google Analytics View from where you want to fetch the data.

  * **Custom Reports (Optional)** : Use this field to sync your [custom reports](<https://support.google.com/analytics/answer/1033013?hl=en>) from Google Analytics. You can sync multiple reports.

To add a custom report, click **Add Report** and enter the **Report Name** , **Metrics** , and **Dimensions** as shown:

[![Google Analytics credentials](/docs/images/cloud-extract-sources/ga-custom-report.webp)](</docs/images/cloud-extract-sources/ga-custom-report.webp>)

You can also edit/delete an existing report:

[![Google Analytics credentials](/docs/images/cloud-extract-sources/edit-custom-report.webp)](</docs/images/cloud-extract-sources/edit-custom-report.webp>)[![Google Analytics credentials](/docs/images/cloud-extract-sources/delete-custom-report.webp)](</docs/images/cloud-extract-sources/delete-custom-report.webp>)
  * **Data request time increment in days (Optional)** : Enter the number of days after which RudderStack should request data from the Google Analytics API. It is recommended to set this value to 1 to avoid getting the [sampled data](<https://support.google.com/analytics/answer/2637192#zippy=%2Cin-this-article>). The minimum and maximum allowed values for this field are 1 and 364 respectively.


### Destination settings

The following settings specify how RudderStack sends the data ingested from Google Analytics to the connected warehouse destination:

  * **Table prefix** : RudderStack uses this prefix to create a table in your data warehouse and loads all your Google Analytics data into it.


> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add special characters like `-` or `_` to the prefix by default. Hence, you need to specify it while setting the prefix.

  * **Schedule Settings** : RudderStack gives you three options to ingest the data from Google Analytics:
    * **Basic** : Runs the syncs at the specified time interval.
    * **CRON** : Runs the syncs based on the user-defined CRON expression.
    * **Manual** : You are required to run the syncs manually.


> ![info](/docs/images/info.svg)
> 
> For more information on the schedule types, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/>) guide.

### Selecting the data to import

You can choose the predefined reports from which you want to ingest the data from Google Analytics by selecting them here:

[![Selecting the data to import](/docs/images/cloud-extract-sources/ga-resources.webp)](</docs/images/cloud-extract-sources/ga-resources.webp>)

The below table mentions the syncs supported by these resources from Google Analytics to your warehouse destination:

Resource| Full Refresh sync| Incremental sync  
---|---|---  
`weekly_active_users`| Yes| Yes  
`website_overview`| Yes| Yes  
`two_weekly_active_users`| Yes| Yes  
`traffic_sources`| Yes| Yes  
`pages`| Yes| Yes  
`monthly_active_users`| Yes| Yes  
`locations`| Yes| Yes  
`four_weekly_active_users`| Yes| Yes  
`devices`| Yes| Yes  
`daily_active_users`| Yes| Yes  
  
> ![info](/docs/images/info.svg)
> 
> For more information on the **Full Refresh** and **Incremental** sync modes, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/#sync-modes>) guide.

> ![info](/docs/images/info.svg)
> 
> To sync the data in incremental mode, you must include the `ga:date` dimension in your report. Otherwise, RudderStack will sync the data in full refresh mode.

Google Analytics is now configured as a source. RudderStack will start ingesting data from Google Analytics as per your specified schedule and frequency.

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