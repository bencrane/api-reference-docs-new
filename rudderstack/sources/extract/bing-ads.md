# Bing Ads Cloud Extract Source Deprecated

Sync data from Bing Ads to your warehouse destination via RudderStack.

* * *

  * __4 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> This source is deprecated and no longer supported as of **January 10, 2026**.

[Bing Ads](<https://ads.microsoft.com/>) is a pay per click (PPC) advertising platform that works on both Bing and Yahoo search engines. It allows marketers to track and monitor their ad campaigns, resulting clicks, CTRs, and more.

> ![info](/docs/images/info.svg)
> 
> All Cloud Extract sources support sending data only to a [data warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).

## Getting Started

  1. Log into your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Sources** > **New source** > **Cloud Extract** and select **Bing Ads** from the list of sources.
  3. Assign a name to your source and click **Continue**.


### Connection settings

Next, configure the following dashboard settings:

[![Bing Ads credentials](/docs/images/cloud-extract-sources/bing-ads-v2-settings.webp)](</docs/images/cloud-extract-sources/bing-ads-v2-settings.webp>)

  * **Tenant ID** : Enter the Tenant ID of your Microsoft Advertising developer application. It is recommended to set it as `common` unless you need a different value.
  * **Connect with Bing Ads V2** : Click this button to give RudderStack the required permissions to access your Bing Ads account.
  * **Developer Token** : Enter your user developer token. Refer to the [Microsoft documentation](<https://learn.microsoft.com/en-us/advertising/guides/get-started?view=bingads-13#get-developer-token>) for more information on obtaining the developer token.
  * **Reports replication start date** : Select the date from when RudderStack should ingest your Bing Ads data. RudderStack will **not replicate** any data before this date.


### Destination settings

The following settings specify how RudderStack sends the data ingested from Bing Ads to the connected warehouse destination:

  * **Table prefix** : RudderStack uses this prefix to create a table in your data warehouse and loads all your Bing Ads data into it.


> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add special characters like `-` or `_` to the prefix by default. Hence, you need to specify it while setting the prefix.

  * **Schedule Settings** : RudderStack gives you three options to ingest the data from Bing Ads:
    * **Basic** : Runs the syncs at the specified time interval.
    * **CRON** : Runs the syncs based on the user-defined CRON expression.
    * **Manual** : You are required to run the syncs manually.


> ![info](/docs/images/info.svg)
> 
> For more information on the schedule types, see [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/#sync-modes>).

### Selecting the data to import

You can choose the Bing Ads data you want to ingest by selecting the required resources:

[![Selecting the data to import](/docs/images/cloud-extract-sources/bing-ads-connection-settings-2.webp)](</docs/images/cloud-extract-sources/bing-ads-connection-settings-2.webp>)

The below table mentions the syncs and primary keys supported by these resources from Bing Ads to your warehouse destination:

Resource| Sync type| Primary key  
---|---|---  
`Account Performance Report`| Incremental| `AccountId`, `TimePeriod`, `CurrencyCode`, `AdDistribution`, `DeviceType`, `Network`, `DeliveredMatchType`, `DeviceOS`, `TopVsOther`, `BidMatchType`  
`Accounts`| Full Refresh| `Id`  
`Ad Group Performance Report`| Incremental| `AccountId`, `CampaignId`, `AdGroupId`, `TimePeriod`, `CurrencyCode`, `AdDistribution`, `DeviceType`, `Network`, `DeliveredMatchType`, `DeviceOS`, `TopVsOther`, `BidMatchType`, `Language`  
`Ad Groups`| Full Refresh| `Id`  
`Ad Performance Report`| Incremental| `AccountId `, `CampaignId`, `AdGroupId`, `AdId`, `TimePeriod`, `CurrencyCode`, `AdDistribution`, `DeviceType`, `Language`, `Network`, `DeviceOS`, `TopVsOther`, `BidMatchType`, `DeliveredMatchType`  
`Ads`| Full Refresh| `Id`  
`Budget Summary Report`| Incremental| `Date`  
`Campaign Performance Report`| Full Refresh| `AccountId`, `CampaignId`, `TimePeriod`, `CurrencyCode`, `AdDistribution`, `DeviceType`, `Network`, `DeliveredMatchType`, `DeviceOS`, `TopVsOther`, `BidMatchType`  
`Campaigns`| Full Refresh| `Id`  
`Keyword Performance Report`| Incremental| `AccountId`, `CampaignId`, `AdGroupId`, `KeywordId`, `AdId`, `TimePeriod`, `CurrencyCode`, `DeliveredMatchType`, `AdDistribution`, `DeviceType`, `Language`, `Network`, `DeviceOS`, `TopVsOther`, `BidMatchType`  
  
Bing Ads is now configured as a source. RudderStack will start ingesting data from Bing Ads as per your specified schedule and frequency.

You can further connect this source to your data warehouse by clicking on **Add Destination** :

[![Adding a destination](/docs/images/cloud-extract-sources/add-destination.webp)](</docs/images/cloud-extract-sources/add-destination.webp>)

> ![success](/docs/images/tick.svg)
> 
> Use the **Use Existing Destination** option if you have an already-configured data warehouse destination in RudderStack. To configure a data warehouse destination from scratch, select the **Create New Destination** button.

## FAQ

#### How does RudderStack count the events for Cloud Extract sources?

RudderStack counts the number of records returned by the source APIs when queried during each sync. It considers each record as an event.

#### Is it possible to have multiple Cloud Extract sources writing to the same schema?

Yes, it is.

We have implemented a feature wherein RudderStack associates a table prefix for every Cloud Extract source writing to a warehouse schema. This way, multiple Cloud Extract sources can write to the same schema with different table prefixes.

#### How does RudderStack set the table name for the data sent via Cloud Extract sources?

RudderStack sets the table name for the resource you are syncing to the warehouse by adding `rudder_` to the **Table prefix** you set while configuring your Cloud Extract source in the dashboard.

[![Cloud Extract table prefix](/docs/images/cloud-extract-sources/etl-table-prefix.webp)](</docs/images/cloud-extract-sources/etl-table-prefix.webp>)

For example, if you set `test_` as the **Table prefix** in the dashboard, RudderStack sets the table name as `test_rudder_<resource_name>`, where `<resource_name>` is the name of the resource you are syncing (for example, `contacts`, `messages`, etc.).

> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add the character `_` to the prefix by default. Hence, you need to specify it while setting the prefix.