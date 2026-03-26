# Google Sheets Cloud Extract Source Deprecated

Sync data from Google Sheets to your warehouse destination via RudderStack.

* * *

  * __5 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> This source is deprecated and no longer supported as of **January 10, 2026**.

[Google Sheets](<https://www.google.com/sheets/about/>) is a popular spreadsheet program that lets you create and manage your spreadsheets.

This document guides you in setting up Google Sheets as a source in RudderStack. Once configured, RudderStack automatically ingests your Google Sheets data and routes it to your specified data warehouse destination.

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * All Cloud Extract sources support sending data only to a [data warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).
>   * This source **does not support** shared drives.
> 


## Getting started

To set up Google Sheets as a source in RudderStack, follow these steps:

  1. Log into your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Sources** > **New source** > **Cloud Extract** and select **Google Sheets** from the list of sources.
  3. Assign a name to your source and click **Continue**.


### Connection settings

Next, configure the following dashboard settings:

[![Configuring Google Sheets](/docs/images/cloud-extract-sources/googlesheets-beta-connection-settings.webp)](</docs/images/cloud-extract-sources/googlesheets-beta-connection-settings.webp>)

  * **Authentication** : From the dropdown, select the authentication mechanism for RudderStack to connect to the Google Sheets API.
    * **Authenticate via Google (OAuth)** : To authenticate via OAuth, click the **Sign in with Google** button, select your Google account, and give RudderStack the required permissions.
    * **Service Account Key Authentication** : Enter your [service account](<https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating>) JSON credentials in the **Service Account Information** field.
  * **Spreadsheet Link** : Enter the spreadsheet’s URL from which RudderStack should ingest and sync the data.


> ![info](/docs/images/info.svg)
> 
>   * For the **Authenticate via Google (OAuth)** authentication option, RudderStack will automatically populate all spreadsheets associated with the account.
>   * For the **Service Account Key Authentication** option, you need to first provide access to the required spreadsheet. **Only the spreadsheets for which you provide the access will be listed in the dropdown**. For more information, refer to the FAQ section below.
> 


### Destination settings

The following settings specify how RudderStack sends the data ingested from Google Sheets to the connected warehouse destination:

  * **Table prefix** : RudderStack uses this prefix to create a table in your data warehouse and loads all your Google Sheets data into it.


> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add special characters like `-` or `_` to the prefix by default. Hence, you need to specify it while setting the prefix.

  * **Schedule Settings** : RudderStack gives you three options to ingest the data from Google Sheets:
    * **Basic** : Runs the syncs at the specified time interval.
    * **CRON** : Runs the syncs based on the user-defined CRON expression.
    * **Manual** : You are required to run the syncs manually.


> ![info](/docs/images/info.svg)
> 
> For more information on the schedule types, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/>) guide.

### Selecting the data to import

You can specify the Google Sheets data you want to sync by selecting the required sheet. You can also sync data from multiple sheets within the spreadsheet:

[![Selecting the data to import](/docs/images/cloud-extract-sources/googlesheets-beta-sheet.webp)](</docs/images/cloud-extract-sources/googlesheets-beta-sheet.webp>)

> ![warning](/docs/images/warning.svg)
> 
> RudderStack considers the first row of each sheet as the header. Empty sheets or sheets with an empty header will **not** be reflected in the **Select data to import** window.

You can also define the sync mode for each data resource you want to send to the destination. Click **Edit resources configuration** and specify the destination sync mode for the selected resource(s):

[![Adding a destination](/docs/images/cloud-extract-sources/edit-resources-googlesheets.webp)](</docs/images/cloud-extract-sources/edit-resources-googlesheets.webp>)

  * **Overwrite** : RudderStack adds new rows in the warehouse destination and deletes the rows from previous syncs. This is the default sync mode.
  * **Append and deduplicate** : RudderStack adds new rows and updates modified records in the warehouse destination in each sync.


The following destinations support the above sync modes:

  * Snowflake
  * Postgres
  * MySQL
  * BigQuery


Google Sheets is now configured as a source. RudderStack will start ingesting data from Google Sheets as per your specified schedule and frequency.

You can further connect this source to your data warehouse by clicking the **Add Destination** button:

[![Adding a destination](/docs/images/cloud-extract-sources/add-destination.webp)](</docs/images/cloud-extract-sources/add-destination.webp>)

> ![info](/docs/images/info.svg)
> 
> Use the **Use Existing Destination** option if you have an already-configured data warehouse destination in RudderStack. To configure a data warehouse destination from scratch, select the **Create New Destination** button.

## How RudderStack syncs data to the warehouse

If you select multiple sheets in the **Select data to import** window, RudderStack creates multiple tables (corresponding to each sheet) in the warehouse.

[![Selecting the data to import](/docs/images/cloud-extract-sources/googlesheets-beta-sheet.webp)](</docs/images/cloud-extract-sources/googlesheets-beta-sheet.webp>)

In the above example, RudderStack creates a table corresponding to each sheet (`List of Tracking Plans`, `Import Template`, and so on) in the warehouse.

While syncing data to the warehouse, RudderStack creates columns only for the headers (first rows in the sheet) which also have data present in the second row (mandatory) and beyond (optional).

> ![warning](/docs/images/warning.svg)
> 
> The mere presence of a header **does not** create a column in the destination.

## FAQ

#### How do I provide service account access to a Google sheet?

If you’re using a [service account](<https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating>) to authenticate RudderStack to sync your Google Sheets data, you must also give the required access to the service account to access the required spreadsheet. Follow these steps to provide access to the required spreadsheet:

  1. In your [Google Cloud console](<https://console.cloud.google.com/>), go to **APIs & Services** > **Credentials**.
  2. Under **Service Accounts** , copy the email address listed under **Email**.

[![Service account email](/docs/images/cloud-extract-sources/googlesheets-beta-service-account-email.webp)](</docs/images/cloud-extract-sources/googlesheets-beta-service-account-email.webp>)

  3. Go to the spreadsheet, click the **Share** button and paste the email copied above. Specify the permission you want to assign to this email.

[![Service account permissions](/docs/images/cloud-extract-sources/googlesheets-beta-service-account-permissions.webp)](</docs/images/cloud-extract-sources/googlesheets-beta-service-account-permissions.webp>)

  4. Finally, click the **Send** button.


> ![warning](/docs/images/warning.svg)
> 
> If you get the **Share outside of organization** popup, click **Share anyway**.

The Google sheet will now be accessible in the dropdown. RudderStack can now access the sheet and sync the data from it.

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