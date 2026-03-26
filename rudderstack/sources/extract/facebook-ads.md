# Facebook Ads Cloud Extract Source Deprecated

Sync data from Facebook Ads to your warehouse destination via RudderStack.

* * *

  * __4 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> This source is deprecated and no longer supported as of **January 10, 2026**.

[Facebook Ads](<https://www.facebook.com/business/ads>) is an online advertising platform that lets you create and run cross-device marketing campaigns and track their performance with easy to read reports.

This document guides you in setting up Facebook Ads as a source in RudderStack. Once configured, RudderStack automatically ingests your specified Facebook Ads data and routes it to your data warehouse.

> ![info](/docs/images/info.svg)
> 
> All Cloud Extract sources support sending data only to a [data warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).

## Getting started

To set up Facebook Ads as a source in RudderStack, follow these steps:

  1. Log into your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Sources** > **New source** > **Cloud Extract** and select **Facebook Ads** from the list.
  3. Assign a name to your source and click **Continue**.


### Connection settings

  1. Click **Connect with Facebook Ads** and grant RudderStack the necessary permissions to access your Facebook Ads data.


> ![info](/docs/images/info.svg)
> 
> Your Facebook Ads account and the related details will then automatically appear under **Choose an account**.

[![Facebook Ads connection settings](/docs/images/cloud-extract-sources/fb-ads-1.webp)](</docs/images/cloud-extract-sources/fb-ads-1.webp>)

  2. In the **Source Settings** , configure the following settings:

[![Facebook Ads connection settings](/docs/images/cloud-extract-sources/fb-ads-2.webp)](</docs/images/cloud-extract-sources/fb-ads-2.webp>)

  * **Page** : Enter the name of the Facebook page from where you want to ingest the Ads data.
  * **Historical data** : Specify the timeframe for which RudderStack should fetch the historical data during the first sync.
  * **Attribution window** : Specify the [attribution window](<https://www.facebook.com/business/help/2198119873776795?id=768381033531365>), that is, the number of days between a person viewing/clicking your ad and subsequently taking an action. Facebook measures the ad actions based on the clicks and views of your ad.


> ![warning](/docs/images/warning.svg)
> 
> RudderStack will not sync the data older than the selected timeframe for the historical data.

### Destination settings

The following settings specify how RudderStack sends the ingested data from Facebook Ads to the warehouse destination:

  * **Table prefix** : RudderStack uses this prefix to create a table in your data warehouse and loads all your Facebook Ads data into it.


> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add special characters like `-` or `_` to the prefix by default. Hence, you need to specify it while setting the prefix.

  * **Schedule Settings** : RudderStack gives you three options to ingest the data from Facebook Ads:
    * **Basic** : Runs the syncs at the specified time interval.
    * **CRON** : Runs the syncs based on the user-defined CRON expression.
    * **Manual** : You are required to run the syncs manually.


> ![info](/docs/images/info.svg)
> 
> For more information on the schedule types, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/>) guide.

### Selecting the data to import

Choose the Facebook Ads data that you wish to ingest via RudderStack. You can either select all data or choose specific Facebook Ads data attributes as per your requirement.

[![Selecting the data to import](/docs/images/cloud-extract-sources/fb-ads-3.webp)](</docs/images/cloud-extract-sources/fb-ads-3.webp>)

Facebook Ads is now configured as a source. RudderStack will start ingesting data from Facebook Ads as per your specified schedule and frequency.

You can further connect this source to your data warehouse by clicking on **Add Destination** :

[![Adding a destination](/docs/images/cloud-extract-sources/add-destination.webp)](</docs/images/cloud-extract-sources/add-destination.webp>)

> ![success](/docs/images/tick.svg)
> 
> Use the **Use Existing Destination** option if you have an already-configured data warehouse destination in RudderStack. To configure a data warehouse destination from scratch, select the **Create New Destination** button.

## FAQ

#### Is it possible to have multiple Cloud Extract sources writing to the same schema?

Yes, it is.

RudderStack associates a table prefix for every Cloud Extract source writing to a warehouse schema. This way, multiple Cloud Extract sources can write to the same schema with different table prefixes.

#### What Facebook Ads data does RudderStack import?

Property| Table name| Description  
---|---|---  
**Account Insights**| **`account_insights`**|  This table contains insights, aggregated for the whole account. Insights include total impressions, CPP, CPC, Reach, and CPM.  
**Campaigns**| **`campaigns`**|  This table holds information about your campaigns. The columns of this table include: `name`, `objective`, `account_id`, and`status`.  
**AdSets**| **`adsets`**|  This tables has information about your Ad Sets. The columns of this table are: `bid_amount`,`updated_time`,`campaign_id`,`daily_budget`,`lifetime_budget`, and `pacing_type`.  
**Ads**| **`ads`**|  This table contains information about your Facebook Ads.  
**Ad Creatives**| **`ad_creatives`**|  This table contains the creative content for your Facebook Ads account that you can use in your ads.  
  
#### How can I avoid sync errors due to rate limits?

To avoid sync errors due to rate limits, set the **Page Size of Requests** setting to 500 from the default value of 50. This allows RudderStack to make fewer calls to the Facebook API. Note that the maximum value for this setting is 1000.

#### How does RudderStack count the events for Cloud Extract sources?

RudderStack counts the number of records returned by the source APIs when queried during each sync. It considers each record as an event.

#### How does RudderStack set the table name for the data sent via Cloud Extract sources?

RudderStack sets the table name for the resource you are syncing to the warehouse by adding `rudder_` to the **Table prefix** you set while configuring your Cloud Extract source in the dashboard.

[![Cloud Extract table prefix](/docs/images/cloud-extract-sources/etl-table-prefix.webp)](</docs/images/cloud-extract-sources/etl-table-prefix.webp>)

For example, if you set `test_` as the **Table prefix** in the dashboard, RudderStack sets the table name as `test_rudder_<resource_name>`, where `<resource_name>` is the name of the resource you are syncing (for example, `contacts`, `messages`, etc.).

> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add the character `_` to the prefix by default. Hence, you need to specify it while setting the prefix.