# Google Ads Cloud Extract Source Deprecated

Sync data from Google Ads to your warehouse destination via RudderStack.

* * *

  * __5 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> This source is deprecated and no longer supported as of **January 10, 2026**.

[Google Ads](<https://ads.google.com/intl/en_in/home/>) is Google’s premier online advertising platform that lets advertisers display their advertisements, service offerings, and product listings to prospective customers.

This document guides you in setting up Google Ads as a source in RudderStack. Once configured, RudderStack automatically ingests your specified Google Ads data, which can then be routed to your RudderStack-supported data warehouse destination.

> ![info](/docs/images/info.svg)
> 
> All Cloud Extract sources support sending data only to a [data warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).

## Getting started

To set up Google Ads as a source in RudderStack, follow these steps:

  1. Log into your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Sources** > **New source** > **Cloud Extract** and select **Google Ads** from the list of sources.
  3. Assign a name to your source and click **Next**.


### Connection settings

  * Give RudderStack access to your Google Ads account by clicking on the **Sign in with Google** button under **Google Credentials**.

[![Verifying credentials](/docs/images/cloud-extract-sources/g-ads-connection-settings-1.webp)](</docs/images/cloud-extract-sources/g-ads-connection-settings-1.webp>)

> ![info](/docs/images/info.svg)
> 
> If you have already connected RudderStack to your Google Ads account, your credentials will appear automatically under **Choose an account**.

Then, configure the following settings to set up the source:

[![Connection settings](/docs/images/cloud-extract-sources/g-ads-connection-settings-2.webp)](</docs/images/cloud-extract-sources/g-ads-connection-settings-2.webp>)

  * **Customer ID** : Enter the 10 digit customer ID associated with your Google Ads account **without the dashes**. For more information on obtaining the customer ID, refer to the FAQ section below.
  * **Start Date** : RudderStack will import all your historical Google Ads data **from** this date.
  * **End Date** : RudderStack will import all your Google Ads data **till** this date.


> ![info](/docs/images/info.svg)
> 
> The **Start Date** setting is valid only for the first (historical) sync.

  * **Login Customer ID for Managed Accounts** : This is a required field **if** you are using a Google Ads manager account to set up the source. Enter your 10 digit manager account customer ID **without the dashes**.
  * **Conversion Window** : Enter the [Google Ads conversion window](<https://support.google.com/google-ads/answer/3123169?hl=en>) duration.


> ![info](/docs/images/info.svg)
> 
> For more information on the conversion windows in Google Ads, refer to the FAQ section below.

### Custom GAQL queries

The **Custom GAQL Queries** option lets you create a custom GAQL query for building a customized Google Ads report. The dashboard settings are described below:

  * **Select resource** : Select the Google Ads API resource from the dropdown.
  * **Select** : Select the relevant Attributes, Segments and Metrics from the dropdown.
  * **Destination Table Name** : Specify the table name in your warehouse destination where the results for the above query will be sent.


As you select the relevant options from the dropdown, you can observe the custom GAQL query displayed in the query box. You can also use the **Reset** and **Edit query** buttons to reset or change the query respectively.

[![Connection settings](/docs/images/cloud-extract-sources/g-ads-connection-settings-4.webp)](</docs/images/cloud-extract-sources/g-ads-connection-settings-4.webp>)

The following image shows a sample custom GAQL query:

[![Connection settings](/docs/images/cloud-extract-sources/g-ads-connection-settings-5.webp)](</docs/images/cloud-extract-sources/g-ads-connection-settings-5.webp>)

You can also use the [Google Ads Query Builder tool](<https://developers.google.com/google-ads/api/fields/v12/query_validator>) to validate your queries.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack does not support creating a custom GAQL query for the `click_view` resource as it requires a [filter limiting the results to one day](<https://developers.google.com/google-ads/api/fields/v11/click_view>). You can use the `clickView` predefined stream instead.

### Destination settings

The following settings specify how RudderStack sends the data ingested from Google Ads to the connected warehouse destination:

  * **Table prefix** : RudderStack uses this prefix to create a table in your data warehouse and loads all your Google Ads data into it.


> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add special characters like `-` or `_` to the prefix by default. Hence, you need to specify it while setting the prefix.

  * **Schedule Settings** : RudderStack gives you three options to ingest the data from Google Ads:
    * **Basic** : Runs the syncs at the specified time interval.
    * **CRON** : Runs the syncs based on the user-defined CRON expression.
    * **Manual** : You are required to run the syncs manually.


> ![info](/docs/images/info.svg)
> 
> For more information on the schedule types, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/>) guide.

### Selecting the data to import

You can choose the Google Ads data you want to ingest by selecting the required resources:

[![Selecting the data to import](/docs/images/cloud-extract-sources/g-ads-connection-settings-3.webp)](</docs/images/cloud-extract-sources/g-ads-connection-settings-3.webp>)

The below table mentions the sync types supported by the Google Ads resources while syncing data to your warehouse destination:

Resource| Sync type| Primary key  
---|---|---  
`acccounts`| Full Refresh| `customer.id`  
`segments.date`  
`account_performance_report`| Incremental| `customer.id`  
`segments.date`  
`segments.ad_network`  
`segments.device`  
`ad_groups`| Full Refresh| `ad_group.id`  
`segments.date`  
`ad_group_ads`| Full Refresh| `ad_group_ad.ad.id`  
`segments.date`  
`ad_group_ad_labels`| Full Refresh| `ad_group_ad_label.resource_name`  
`ad_group_ad_report`| Incremental| -  
`ad_group_labels`| Full Refresh| `ad_group_label.resource_name`  
`campaigns`| Full Refresh| `campaign.id`  
`segments.date`  
`campaign_labels`| Full Refresh| `campaign_label.resource_name`  
`click_view`| Incremental| `click_view.gclid`  
`segments.date`  
`segments.ad_network`  
`display_topics_performance_report`| Incremental| -  
`display_keyword_performance_report`| Incremental| -  
`geographic_report`| Incremental| -  
`keyword_report`| Incremental| -  
`shopping_performance_report`| Incremental| -  
`user_location_report`| Incremental| -  
  
> ![info](/docs/images/info.svg)
> 
> For more information on the **Full Refresh** and **Incremental** sync modes, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/#sync-modes>) guide.

## FAQ

#### Where can I find my Google Ads customer ID?

The Google Ads customer ID is a unique number used to identify your Google Ads account. To get this ID:

  1. Sign in to your [Google Ads account](<https://ads.google.com/home/>).
  2. Click your profile picture in the top right corner — the customer ID is listed under **Account Information**.


See the [Google Ads Help Center](<https://support.google.com/google-ads/answer/1704344?hl=en>) for more information on finding your Google Ads customer ID.

#### What is a conversion window in Google Ads?

A conversion window is defined as the time period after the user interacts with an ad (clicks, video views, etc.) during which a conversion is recorded in Google Ads.

#### Is it possible to have multiple Cloud Extract sources writing to the same schema?

Yes, it is. RudderStack associates a table prefix for every Cloud Extract source writing to a warehouse schema. This way, multiple Cloud Extract sources can write to the same schema with different prefixes.

#### How does RudderStack count the events for Cloud Extract sources?

RudderStack counts the number of records returned by the source APIs when queried during each sync. It considers each record as an event.

#### How does RudderStack set the table name for the data sent via Cloud Extract sources?

RudderStack sets the table name for the resource you are syncing to the warehouse by adding `rudder_` to the **Table prefix** you set while configuring your Cloud Extract source in the dashboard.

[![Cloud Extract table prefix](/docs/images/cloud-extract-sources/etl-table-prefix.webp)](</docs/images/cloud-extract-sources/etl-table-prefix.webp>)

For example, if you set `test_` as the **Table prefix** in the dashboard, RudderStack sets the table name as `test_rudder_<resource_name>`, where `<resource_name>` is the name of the resource you are syncing (for example, `contacts`, `messages`, etc.).

> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add the character `_` to the prefix by default. Hence, you need to specify it while setting the prefix.