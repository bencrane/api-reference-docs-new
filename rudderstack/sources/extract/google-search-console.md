# Google Search Console Cloud Extract Source Deprecated

Sync data from Google Search Console to your warehouse destination via RudderStack.

* * *

  * __5 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> This source is deprecated and no longer supported as of **January 10, 2026**.

[Google Search Console](<https://search.google.com/search-console/about>) is Google’s web service that allows webmasters to check the indexing status of websites and optimize their visibility. It offers tools and reports to measure and optimize your website’s search traffic, performance, content, and fix issues.

This document guides you in setting up Google Search Console as a source in RudderStack. Once configured, RudderStack automatically ingests your Google Search Console data and routes it to your specified data warehouse destination.

> ![info](/docs/images/info.svg)
> 
> All Cloud Extract sources support sending data only to a [data warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).

## Getting started

To set up Google Search Console as a source in RudderStack, follow these steps:

  1. Log into your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Sources** > **New source** > **Cloud Extract** and select **Google Search Console V2** from the list of sources.
  3. Assign a name to your source and click **Continue**.


### Connection settings

Next, configure the following dashboard settings:

  * **Authentication Type** : Choose one of the following authentication types:

    * **OAuth** : Authenticate your Google Search Console account via Google (OAuth) by clicking the **Sign in with Google** button and granting the required permissions.
[![Google Analytics credentials](/docs/images/cloud-extract-sources/gsc-oauth-settings.webp)](</docs/images/cloud-extract-sources/gsc-oauth-settings.webp>)
    * **Service Account Key Authentication** : Authenticate your Google Search Console account by using your Google service account:
      * **Service Account JSON Key** : Enter the service account key in JSON format in the field. Refer to the [Google documentation](<https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys>) for more information on obtaining the service account key.
      * **Admin Email** : Enter the email associated with your service account.
[![Google Analytics credentials](/docs/images/cloud-extract-sources/gsc-auth-settings-1.webp)](</docs/images/cloud-extract-sources/gsc-auth-settings-1.webp>)


The rest of the settings are as follows:

[![SendGrid credentials](/docs/images/cloud-extract-sources/gsc-connection-settings-1.webp)](</docs/images/cloud-extract-sources/gsc-connection-settings-1.webp>)

  * **Website URL Property** : Enter the URL of the website for which you want to fetch data. Make sure you use the **exact URL** of the website as specified in the Google Search Console. Refer to the [Google documentation](<https://support.google.com/webmasters/answer/34592?hl=en>) for more information on adding the website URL property.


> ![info](/docs/images/info.svg)
> 
> If you are using a domain property in the Google Search Console, you must prefix the site URL with `sc-domain:`. For example, if the website URL is `http://www.example.com/`, then `http://www.example.com/` is a URL-prefix property and `sc-domain:example.com` is a domain property.

  * **Start Date** : Specify the date from which RudderStack should import your Google Search Console data.
  * **End Date** : Specify the date till which RudderStack should import your Google Search Console data .


> ![warning](/docs/images/warning.svg)
> 
> RudderStack will not replicate any data **after** this date. Do not set this field if you want RudderStack to sync the most recent Google Search Console data.

  * **Custom Reports (Optional)** : Use this field to sync your [custom reports](<https://support.google.com/analytics/answer/1033013?hl=en>) from Google Search Console. You can sync multiple reports.

To add a custom report, click **Add Report** and enter the **Report Name** and **Dimensions** as shown:

[![Google Analytics credentials](/docs/images/cloud-extract-sources/gcs-custom-report.webp)](</docs/images/cloud-extract-sources/gcs-custom-report.webp>)

You can also edit/delete an existing report:

[![Google Analytics credentials](/docs/images/cloud-extract-sources/gcs-edit-custom-report.webp)](</docs/images/cloud-extract-sources/gcs-edit-custom-report.webp>)[![Google Analytics credentials](/docs/images/cloud-extract-sources/gcs-delete-custom-report.webp)](</docs/images/cloud-extract-sources/gcs-delete-custom-report.webp>)


### Destination settings

The following settings specify how RudderStack sends the data ingested from Google Search Console to the connected warehouse destination:

  * **Table prefix** : RudderStack uses this prefix to create a table in your data warehouse and loads all your Google Search Console data into it.


> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add special characters like `-` or `_` to the prefix by default. Hence, you need to specify it while setting the prefix.

  * **Schedule Settings** : RudderStack gives you three options to ingest the data from Google Search Console:
    * **Basic** : Runs the syncs at the specified time interval.
    * **CRON** : Runs the syncs based on the user-defined CRON expression.
    * **Manual** : You are required to run the syncs manually.


> ![info](/docs/images/info.svg)
> 
> For more information on the schedule types, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/>) guide.

### Selecting the data to import

You can choose the Google Search Console data you want to ingest by selecting the required resources:

[![Selecting the data to import](/docs/images/cloud-extract-sources/gcs-resources.webp)](</docs/images/cloud-extract-sources/gcs-resources.webp>)

The below table mentions the syncs and API endpoints supported by these resources from Google Search Console to your warehouse destination:

Resource| Full Refresh sync| Incremental sync| Google Search Console API endpoint  
---|---|---|---  
`sites`| Yes| No| `/sites/get`  
`sitemaps`| Yes| No| `/sitemaps/list`  
`search_analytics_by_query`| No| Yes| `/searchAnalytics/query`  
`search_analytics_by_page`| No| Yes| `/searchAnalytics/query`  
`search_analytics_by_device`| No| Yes| `/searchAnalytics/query`  
`search_analytics_by_date`| No| Yes| `/searchAnalytics/query`  
`search_analytics_by_country`| No| Yes| `/searchAnalytics/query`  
`search_analytics_all_fields`| No| Yes| `/searchAnalytics/query`  
  
> ![info](/docs/images/info.svg)
> 
> For more information on the **Full Refresh** and **Incremental** sync modes, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/#sync-modes>) guide.

Google Search Console is now configured as a source. RudderStack will start ingesting data from Google Search Console as per your specified schedule and frequency.

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