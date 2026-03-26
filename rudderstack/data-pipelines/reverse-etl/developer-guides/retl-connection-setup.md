# Set Up Reverse ETL Connection

Connect your Reverse ETL sources to destinations in RudderStack.

* * *

  * __8 minute read

  * 


This guide explains how to set up a Reverse ETL connection in RudderStack.

> ![info](/docs/images/info.svg)
> 
> RudderStack has a source-destination connection limit for the Reverse ETL feature in some plans:
> 
>   * **Free and Starter plans** : You can set up to 10 connections.
>   * **Growth and Enterprise plans** : You can set up unlimited connections.
> 


## Overview

Follow these steps to set up a Reverse ETL connection in RudderStack:

  1. Create a Reverse ETL source
  2. Connect it to a destination
  3. Specify the data mappings
  4. Define a sync schedule
  5. Configure advanced settings
  6. Activate the connection


## Required permissions

  * [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have full access to set up and manage Reverse ETL connections.
  * [Members](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) must have the following [permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) in their workspace policy:

Resource| Permission  
---|---  
Tables / SQL Models / Audiences| **Edit** , **Connect**  
Destinations| **Edit** , **Connect**  
  
#### Permissions for legacy RBAC system

In the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), only [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) and members with the **Connections Editor** or **Connections Admin** role in their workspace policy can set up Reverse ETL connections.

[![Reverse ETL connections permissions in the legacy framework](/docs/images/access-management/data-catalog-permissions-legacy-framework.webp)](</docs/images/access-management/data-catalog-permissions-legacy-framework.webp>)

## Add source

> ![info](/docs/images/info.svg)
> 
> Reverse ETL connections are source-driven, meaning you must first create a source and then connect it to a destination.

  1. Sign in to your [RudderStack dashboard](<https://app.rudderstack.com/>) and click **\+ Add source** in the default **Connections** view.

[![Add source](/docs/images/get-started/quickstart/add-source.webp)](</docs/images/get-started/quickstart/add-source.webp>)

  2. Under **Sources** , click **Reverse ETL** and select your warehouse source.
  3. Configure your source. See the [source-specific documentation](<https://www.rudderstack.com/docs/sources/reverse-etl/#supported-reverse-etl-sources>) for configuration details.


> ![warning](/docs/images/warning.svg)
> 
> RudderStack requires some warehouse-specific permissions to sync data from it. These permissions are listed in the source documentation, for example, see [BigQuery permissions](<https://www.rudderstack.com/docs/sources/reverse-etl/google-bigquery/#granting-permissions>).
> 
> Make sure to grant these permissions **before** you set up the source.

## Connect destination

Once you have created a [Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>), you can connect it to:

  * A new [destination](<https://www.rudderstack.com/docs/destinations/overview/>), or
  * An existing destination that is **not already connected** to any other source.


To connect a destination:

  1. Click **Use existing destination** or **Set up a new destination** depending on your requirement.


> ![warning](/docs/images/warning.svg)
> 
> You can connect an [Audience](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/audiences/>) source only to [Audience and List destinations](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/>).

[![Connect destination options](/docs/images/retl-sources/connect-destination.webp)](</docs/images/retl-sources/connect-destination.webp>)

  2. Enter the connection settings for the destination. See the [destination-specific documentation](<https://www.rudderstack.com/docs/destinations/streaming-destinations/>) for more details on these settings.


### 1:many connections

RudderStack supports connecting a Reverse ETL source to multiple destinations.

> ![info](/docs/images/info.svg)
> 
> **Event usage/billing in 1:many connections**
> 
> When sending data from a Reverse ETL source to multiple destinations, RudderStack sends the record to each destination separately — this means you will be charged on a **per connection basis**.

### Many:1 connections

RudderStack also supports connecting **multiple** Reverse ETL sources to a single downstream destination. However, this feature is available only for the below destinations currently — support for more integrations is coming soon.

[![Facebook Custom Audience logo](/docs/images/logos/destinations/facebook.svg)Facebook Custom Audience](</docs/destinations/reverse-etl-destinations/facebook-custom-audience/>)[![Google Ads Remarketing Lists \(Customer Match\) logo](/docs/images/logos/destinations/googleads.svg)Google Ads Remarketing Lists (Customer Match)](</docs/destinations/reverse-etl-destinations/google-ads-remarketing-lists/>)

  


## Specify data mappings

RudderStack provides two options to map your warehouse columns to specific destination fields before syncing your data:

  * [Map with Visualizer](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/visual-data-mapper/>)
  * [Map with JSON](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/json-data-mapping/>)


> ![info](/docs/images/info.svg)
> 
> RudderStack supports the **Map with Visualizer** option only for [selected destinations](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/visual-data-mapper/#supported-destinations>).
> 
> Other destinations that do not support Visual Data Mapper have the **Map with JSON** option by default, with the **Map with Visualizer** option greyed out.

The steps to set the data mappings (using JSON) are listed below:

  1. Select the **Sync mode** to specify how RudderStack syncs each record to the destination. RudderStack supports two [sync modes](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/>):

Sync mode| Description  
---|---  
Upsert| In this mode, RudderStack inserts new records and updates the existing records in the destination while syncing the data.  
Mirror| In this mode, RudderStack ‘mirrors’ the source by keeping the destination data the same as the source data. It performs insertion, deletion, and updates to the records while syncing the data.  
  
Note that:

  * Only [select destinations](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/#mirror-mode>) support this mode.
  * RudderStack does not support `track` event type for this mode.

  
  
  2. If you have set the sync mode to **Upsert** , you can also use the **Use cursor column** setting for managing incremental syncs. See [Cursor Column Support](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/cursor-column-support/>) guide for more information on this setting.

  3. Select the **Event Type** \- RudderStack supports sending the synced data to your downstream destinations as `identify` or `track` events.

     * If you select `track` as the **Event Type** , you also need to set the event name that is sent to the downstream destination. This is because every `track` event requires a name.
     * You can also set the column name as the event name by turning on the **Lookup event name by column** toggle and selecting the column from the dropdown:

[![Schema tab options in RudderStack](/docs/images/warehouse-actions-sources/event-name-table-track.webp)](</docs/images/warehouse-actions-sources/event-name-table-track.webp>)

  3. Set at least one user identifier from `user_id` or `anonymous_id` in the **Choose user identifier** setting.

[![Map with JSON feature](/docs/images/data-pipelines/map-with-json.webp)](</docs/images/data-pipelines/map-with-json.webp>)

  4. Preview the resulting data and make the necessary changes before proceeding.


## Schedule syncs

You can configure the schedule settings and sync frequency at the connection level. This is because a source might be connected to multiple destinations and the sync interval and frequency might need to be configured differently for each connection.

RudderStack determines how and when to run a sync based on the [sync schedule](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-schedule-settings/>) you set for your Reverse ETL connection.

Schedule type| Description  
---|---  
Basic| Run syncs at a given time interval and specified time (in UTC).  
CRON| Run syncs based on a specified CRON expression (in UTC).  
Manual| Run syncs manually.  
[![Sync schedule](/docs/images/retl-sources/schedule-syncs.webp)](</docs/images/retl-sources/schedule-syncs.webp>)

## Configure advanced settings

> ![warning](/docs/images/warning.svg)
> 
> This option is available only if you have set up a new destination.

Once you create a connection successfully, you can configure the optional advanced settings to receive the data correctly in your destination.

[![Advanced destination configuration](/docs/images/retl-sources/advanced-config-destination.webp)](</docs/images/retl-sources/advanced-config-destination.webp>)

  1. Click **Configure your destination**.
  2. Specify the advanced settings and click **Save**.


## Activate connection

  1. Activate the destination by turning on the toggle.
  2. Turn on the connection to activate the connection.

![Activate destination](/docs/images/retl-sources/activate-destination.webp)

You will be redirected to the connections page.

![Connections page](/docs/images/retl-sources/connections-page.webp)

RudderStack will send data to your destination as per the specified sync frequency. Click **Sync now** to manually trigger a new sync.

Click **Turn on the connection** to activate the connection.

![Activate connection](/docs/images/retl-sources/activate-connection.webp)

You will be redirected to the connections page.

![Connections page](/docs/images/retl-sources/connections-page.webp)

RudderStack will send data to your destination as per the specified sync frequency. Click **Sync now** to manually trigger a new sync.

## Stop data syncs for connection

Go to the connection page and turn off the connection toggle to stop data syncs for the connection.

Note that the **Sync Now** button is greyed out and the connection status is **Paused** until you turn on the connection again.

[![Turn off connection](/docs/images/retl-sources/disable-connection.webp)](</docs/images/retl-sources/disable-connection.webp>)

## Update mapping configuration

Go to the **Schema** tab of your connection and click **Update** to change the mapping configuration and update your column selection. Then, click **Save** to update and save the configuration.

> ![warning](/docs/images/warning.svg)
> 
> The **Object** (for VDM mapping), **Sync mode** , **Event type** , and **User identifier** fields are not editable.

[![Update connection configuration](/docs/images/retl-sources/update-connection-configuration.webp)](</docs/images/retl-sources/update-connection-configuration.webp>)

## Update connection settings

Go to the **Settings** tab of your connection to:

  * Get the **Connection ID**.
  * Change the sync schedule and frequency.
  * Specify the settings to retain sync logs in your warehouse and retry syncing failed records. See [Syncs Observability](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-observability/>) for more information.
  * Delete the connection permanently.

[![Update connection settings](/docs/images/retl-sources/retl-connection-settings.webp)](</docs/images/retl-sources/retl-connection-settings.webp>)

## View all connections for Reverse ETL source

Go to the **Overview** tab of your Reverse ETL source. Here, you will see all the destinations connected to that source. Click the required destination or click **View** > **Connection details** to go to the connection’s page.

[![Connection details](/docs/images/retl-sources/connection-details.webp)](</docs/images/retl-sources/connection-details.webp>)

RudderStack automatically redirects you to the **Syncs** tab where you can view the latest sync details or check past syncs.

## View sync details

Go to the **Syncs** tab to see detailed metrics on the latest sync. You can also view details of the past syncs (up to 1 month). These details include:

Metric| Details  
---|---  
Status| The sync status. It can be one of the following:  
  


  * Aborted
  * Completed, with failures
  * Completed, no failures

  
Sync mode| Defines how RudderStack syncs data to the destination. It can be one of the following:  
  


  * Upsert
  * Mirror

  
Sync type| Determines the scope of the sync. It can be one of the following:  
  


  * Incremental: RudderStack syncs only the newly added data in the warehouse since the last sync.
  * Full: RudderStack syncs all the data irrespective of whether it was synced to the destination previously.

  
Trigger| Determines how the sync was triggered. It can be one of the following:  
  


  * Manual
  * Scheduled, as per the sync schedule

  
Sync start time| Determines when the sync was triggered.  
Duration| The sync duration.  
  
You can also see the following source and destination-specific metrics:

  * Number of synced rows.
  * Deltas (new records since last sync) with the number of records inserted, deleted, and updated.
  * Invalid records not synced to destination.


  * Successfully synced records with the number of records inserted, deleted, and updated.
  * Number of dropped records.
  * Number of records that failed to sync.


[![Sync details](/docs/images/retl-sources/sync-details-1.webp)](</docs/images/retl-sources/sync-details-1.webp>)

### View invalid records

> ![warning](/docs/images/warning.svg)
> 
> **Required permissions**
> 
>   * [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have full access to view the invalid records resulting during a Reverse ETL sync.
>   * [Members](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) must have the [**Reverse ETL Sync Failure Samples**](<https://www.rudderstack.com/docs/access-management/policies-overview/#pii-permissions>) PII permission to see these invalid records.
> 


Click **View invalid records** and click a row to see all the invalid records that RudderStack did not sync to the destination.

You also see the error message and sample erroneous rows in this view.

[![View invalid records](/docs/images/retl-sources/invalid-records.webp)](</docs/images/retl-sources/invalid-records.webp>)

### View sync graph

> ![warning](/docs/images/warning.svg)
> 
> This graph is only available for:
> 
>   * The latest sync.
>   * Syncs performed using [Upsert mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/#upsert-mode>).
> 


RudderStack provides an intuitive visual graph detailing the records sent to the destination over time. The X-axis represents the time of the day and the Y-axis represents the number of records classified as:

  * Successfully synced records
  * Dropped records
  * Records that failed to sync

[![View sync graph](/docs/images/retl-sources/sync-graph.webp)](</docs/images/retl-sources/sync-graph.webp>)

Switch to the **Retries** tab to get a graphical view of the retries over time. The X-axis represents the retry time of the day and the Y-axis represents the number of retry attempts.

[![Sync retries graph](/docs/images/retl-sources/sync-retries.webp)](</docs/images/retl-sources/sync-retries.webp>)