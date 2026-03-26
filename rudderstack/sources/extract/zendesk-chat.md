# Zendesk Chat Cloud Extract Source Deprecated

Sync data from Zendesk Chat to your warehouse destination via RudderStack.

* * *

  * __4 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> This source is deprecated and no longer supported as of **January 10, 2026**.

[Zendesk Chat](<https://www.zendesk.com/in/service/messaging/live-chat/>) is a cross-platform live chat software. It lets you reach out to your customers in real-time via live chats and instant messaging.

This document guides you in setting up Zendesk Chat as a source in RudderStack. Once configured, RudderStack automatically ingests your Zendesk Chat data and routes it to your specified data warehouse destination.

> ![info](/docs/images/info.svg)
> 
> All Cloud Extract sources support sending data only to a [data warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).

## Getting started

To set up Zendesk Chat as a source in RudderStack, follow these steps:

  1. Log into your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Sources** > **New source** > **Cloud Extract** and select **Zendesk Chat** from the list of sources.
  3. Assign a name to your source and click **Continue**.


### Connection settings

To set up Zendesk Chat as a Cloud Extract source, you need to configure the following settings:

[![Zendesk Chat connection settings](/docs/images/cloud-extract-sources/zendesk-chat-connection-settings.webp)](</docs/images/cloud-extract-sources/zendesk-chat-connection-settings.webp>)

  * **Start Date** : Choose the start date from which you want RudderStack to ingest the Zendesk Chat data. RudderStack will not replicate any data before this date.


> ![warning](/docs/images/warning.svg)
> 
> You will not be able to proceed if you do not specify the start date.

  * **Subdomain** : Enter the subdomain from your Zendesk account’s URL. For example, if your Zendesk account URL is `sample.zendesk.com`, the subdomain would be `sample`.


> ![warning](/docs/images/warning.svg)
> 
> It is **mandatory** to provide a subdomain if your Zendesk account URL is of the format `sample.zendesk.com`. However, if you only have a Zendesk Chat account and the URL does not follow this format, you can skip this field and set up your source without specifying a subdomain.

  * **Authentication** : Select an authentication method from the dropdown:
    * **OAuth2.0** : Click **Connect with Zendesk Chat** to authenticate your account.
    * **Access token** : Enter your Zendesk Chat access token. Refer to the [Zendesk Chat documentation](<https://support.zendesk.com/hc/en-us/articles/4408882184986-Getting-an-OAuth-access-token-for-testing-purposes>) for more details on obtaining this token.


### Destination settings

The following settings specify how RudderStack sends the ingested data from Zendesk Chat to the warehouse destination:

  * **Table prefix** : RudderStack uses this prefix to create a table in your data warehouse and loads all your Zendesk Chat data into it.


> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add special characters like `-` or `_` to the prefix by default. Hence, you need to specify it while setting the prefix.

  * **Schedule Settings** : RudderStack gives you three options to ingest the data from Zendesk Chat:
    * **Basic** : Runs the syncs at the specified time interval.
    * **CRON** : Runs the syncs based on the user-defined CRON expression.
    * **Manual** : You are required to run the syncs manually.


> ![info](/docs/images/info.svg)
> 
> For more information on the schedule types, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/>) guide.

### Selecting the data to import

You can choose the Zendesk Chat data you want to ingest by selecting the required resources:

[![Selecting the data to import](/docs/images/cloud-extract-sources/zendesk-chat-connection-settings-2.webp)](</docs/images/cloud-extract-sources/zendesk-chat-connection-settings-2.webp>)

The below table lists the syncs supported by the Zendesk Chat resources to your warehouse destination:

Resource| Full Refresh sync| Incremental sync| API endpoint  
---|---|---|---  
`accounts`| Yes| No| `/account`  
`agent_timeline`| Yes| Yes| `/incremental/agent_timeline`  
`agents`| Yes| Yes| `/agents`  
`bans`| Yes| Yes| `/bans`  
`chats`| Yes| Yes| `/incremental/chats`  
`conversions`| Yes| Yes| `/incremental/conversions`  
`department_events`| Yes| Yes| `/incremental/department_events`  
`departments`| Yes| No| `/departments`  
`goals`| Yes| No| `/goals`  
`roles`| Yes| No| `/roles`  
`routing_settings`| Yes| No| `/routing_settings/account`  
`shortcuts`| Yes| No| `/shortcuts`  
`skills`| Yes| No| `/skills`  
`triggers`| Yes| No| `/triggers`  
  
> ![info](/docs/images/info.svg)
> 
> For more information on the **Full Refresh** and **Incremental** sync modes, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/#sync-modes>) guide.

Zendesk Chat is now configured as a source. RudderStack will start ingesting data from Zendesk Chat as per your specified schedule and frequency.

You can further connect this source to your data warehouse by clicking on **Add Destination** :

[![Adding a destination](/docs/images/cloud-extract-sources/add-destination.webp)](</docs/images/cloud-extract-sources/add-destination.webp>)

> ![success](/docs/images/tick.svg)
> 
> Use the **Use Existing Destination** option if you have an already-configured data warehouse destination in RudderStack. To configure a data warehouse destination from scratch, select the **Create New Destination** button.

## FAQ

#### Where can I find my Zendesk Chat subdomain?

You can easily identify the Zendesk Chat subdomain from your account URL. It is in the format `https://[YOUR_ZENDESK_SUBDOMAIN].zendesk.com`.

#### Is it possible to have multiple Cloud Extract sources writing to the same schema?

Yes, it is.

We have implemented a feature wherein RudderStack associates a table prefix for every Cloud Extract source writing to a warehouse schema. This way, multiple Cloud Extract sources can write to the same schema with different table prefixes.

#### How does RudderStack count the events for Cloud Extract sources?

RudderStack counts the number of records returned by the source APIs when queried during each sync. It considers each record as an event.

#### How does RudderStack set the table name for the data sent via Cloud Extract sources?

RudderStack sets the table name for the resource you are syncing to the warehouse by adding `rudder_` to the **Table prefix** you set while configuring your Cloud Extract source in the dashboard.

[![Cloud Extract table prefix](/docs/images/cloud-extract-sources/etl-table-prefix.webp)](</docs/images/cloud-extract-sources/etl-table-prefix.webp>)

For example, if you set `test_` as the **Table prefix** in the dashboard, RudderStack sets the table name as `test_rudder_<resource_name>`, where `<resource_name>` is the name of the resource you are syncing (for example, `contacts`, `messages`, etc.).

> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add the character `_` to the prefix by default. Hence, you need to specify it while setting the prefix.