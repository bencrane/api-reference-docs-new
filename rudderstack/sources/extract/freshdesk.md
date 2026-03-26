# Freshdesk Cloud Extract Source Deprecated

Sync data from Freshdesk to your warehouse destination via RudderStack.

* * *

  * __4 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> This source is deprecated and no longer supported as of **January 10, 2026**.

[Freshdesk](<https://freshdesk.com/>) is a popular customer support software which provides cutting-edge, cross-channel customer support features including bots and various other self-service solutions.

This document guides you in setting up Freshdesk as a source in RudderStack. Once configured, RudderStack automatically ingests your specified Freshdesk data, which can then be routed to your RudderStack-supported data warehouse destination.

> ![info](/docs/images/info.svg)
> 
> All Cloud Extract sources support sending data only to a [data warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).

## Getting Started

To set up Freshdesk as a source in RudderStack, follow these steps:

  1. Log into your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Sources** > **New source** > **Cloud Extract** and select **Freshdesk** from the list of sources.
  3. Assign a name to your source and click **Continue**.


### Connection settings

To set up Freshdesk as a Cloud Extract source, you need to configure the following settings:

[![Freshdesk credentials](/docs/images/cloud-extract-sources/freshdesk-connection-settings-4.webp)](</docs/images/cloud-extract-sources/freshdesk-connection-settings-4.webp>)

  * **Domain** : Enter your Freshdesk domain from the URL (for example, `test.freshdesk.com`).
  * **API Key** : Enter your Freshdesk API key. Refer to the FAQ section for more information on obtaining the API key.
  * **Requests per minute** : Enter the number of requests that Freshdesk can use per minute. The rate limit **does not allow** more than 50 requests per minute per app per Freshdesk account.
  * **Start Date** : Enter the date from which RudderStack should import your historical Freshdesk data.


### Destination settings

The following settings specify how RudderStack sends the data ingested from Freshdesk to the connected warehouse destination:

  * **Table prefix** : RudderStack uses this prefix to create a table in your data warehouse and loads all your Freshdesk data into it.


> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add special characters like `-` or `_` to the prefix by default. Hence, you need to specify it while setting the prefix.

  * **Schedule Settings** : RudderStack gives you three options to ingest the data from Freshdesk:
    * **Basic** : Runs the syncs at the specified time interval.
    * **CRON** : Runs the syncs based on the user-defined CRON expression.
    * **Manual** : You are required to run the syncs manually.


> ![info](/docs/images/info.svg)
> 
> For more information on the schedule types, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/>) guide.

### Selecting the data to import

You can choose the Freshdesk data you want to ingest by selecting the required resources:

[![Selecting the data to import](/docs/images/cloud-extract-sources/freshdesk-resources.webp)](</docs/images/cloud-extract-sources/freshdesk-resources.webp>)

The below table mentions the syncs and API endpoints supported by these resources from Freshdesk to your warehouse destination:

Resource| Supported sync mode| Primary key| Freshdesk API endpoint|   
---|---|---|---|---  
`time_entries`| Full Refresh| `id`| `/time_entries`|   
`tickets`| Incremental| `id`| `/tickets`|   
`ticket_fields`| Full Refresh| `id`| `/ticket_fields`|   
`surveys`| Full Refresh| `id`| `/surveys`|   
`solution_folders`| Full Refresh| `id`| `/solutions/categories/[id]/folders`|   
`solution_categories`| Full Refresh| `id`| `/solutions/categories`|   
`solution_articles`| Full Refresh| `id`| `/solutions/folders/[id]/articles`|   
`sla_policies`| Full Refresh| `id`| `/sla_policies`|   
`settings`| Full Refresh| `primary_language`| `/settings/helpdesk`|   
`scenario_automations`| Full Refresh| `id`| `/scenario_automations`|   
`satisfaction_ratings`| Incremental| `id`| `/surveys/satisfaction_ratings`|   
`roles`| Full Refresh| `id`| `/roles`|   
`products`| Full Refresh| `id`| `/products`|   
`groups`| Full Refresh| `id`| `/groups`|   
`email_mailboxes`| Full Refresh| `id`| `/email/mailboxes`|   
`email_configs`| Full Refresh| `id`| `/email_configs`|   
`discussion_topics`| Full Refresh| `id`| `/discussions/forums/[id]/topics`|   
`discussion_forums`| Full Refresh| `id`| `/discussions/categories/[category_id]/forums`|   
`discussion_comments`| Full Refresh| `id`| `/discussions/topics/[id]/comments`|   
`discussion_categories`| Full Refresh| `id`| `/discussions/categories`|   
`conversations`| Semi-Incremental| `id`| `/tickets/[id]/conversations`|   
`contacts`| Incremental| `id`| `/contacts`|   
`companies`| Full Refresh| `id`| `/companies`|   
`canned_responses`| Full Refresh| `id`| `/canned_response_folders/[id]/responses`|   
`canned_response_folders`| Full Refresh| `id`| `/canned_response_folders`|   
`business_hours`| Full Refresh| `id`| `/business_hours`|   
`agents`| Full Refresh| `id`| `/agents`|   
  
> ![info](/docs/images/info.svg)
> 
> For more information on the **Full Refresh** , **Semi-Incremental** , and **Incremental** sync modes, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/#sync-modes>) guide.

Freshdesk is now configured as a source. RudderStack will start ingesting data from Freshdesk as per your specified schedule and frequency.

You can further connect this source to your data warehouse by clicking on **Add Destination** :

[![Adding a destination](/docs/images/cloud-extract-sources/add-destination.webp)](</docs/images/cloud-extract-sources/add-destination.webp>)

> ![success](/docs/images/tick.svg)
> 
> Use the **Use Existing Destination** option if you have an already-configured data warehouse destination in RudderStack. To configure a data warehouse destination from scratch, select the **Create New Destination** button.

## FAQ

#### Where can I find the Freshdesk API Key?

To get your Freshdesk API key, follow these steps:

  1. Log into your [Freshdesk account](<https://freshdesk.com/login>).
  2. Click your profile in the top right section of the dashboard and go to **Profile Settings**.
  3. You can find the Freshdesk API key in the right sidebar:

[![Freshdesk API key](/docs/images/cloud-extract-sources/freshdesk-connection-settings-2.webp)](</docs/images/cloud-extract-sources/freshdesk-connection-settings-2.webp>)

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