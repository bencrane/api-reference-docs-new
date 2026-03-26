# Zendesk Support Cloud Extract Source Deprecated

Sync data from Zendesk Support to your warehouse destination via RudderStack.

* * *

  * __4 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> This source is deprecated and no longer supported as of **January 10, 2026**.

[Zendesk Support](<https://support.zendesk.com/hc/en-us>) is a popular ticketing system and support platform. It lets you offer customer support through various mediums such as email, mobile, social media, and voice.

This document guides you in setting up Zendesk Support as a source in RudderStack. Once configured, RudderStack automatically ingests your Zendesk Support data and routes it to your specified data warehouse destination.

> ![info](/docs/images/info.svg)
> 
> All Cloud Extract sources support sending data only to a [data warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).

## Getting started

To set up Zendesk Support as a source in RudderStack, follow these steps:

  1. Log in to your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Collect** > **Sources** > **New Source** > **Cloud Extract**. From the list of sources, select **Zendesk Support**.
  3. Assign a name to your source and click **Continue**.


## Connection settings

  * **Start Date** : Choose the start date from which you want RudderStack to ingest the Zendesk Support data. RudderStack will not replicate any data before this date.


> ![warning](/docs/images/warning.svg)
> 
> If you do not specify the start date, RudderStack will replicate all your data by default.

  * **Subdomain** : Enter the subdomain from your Zendesk account’s URL. For example, if your Zendesk account URL is `sample.zendesk.com`, the subdomain would be `sample`.
  * **Authentication** : Select an authentication method from the dropdown:
    * **OAuth2.0** : Click **Connect with Zendesk Support** to authenticate your account.
    * **API token** : Enter the **Email** used to log in to the Zendesk account and the **API token**. See [Zendesk documentation](<https://support.zendesk.com/hc/en-us/articles/4408889192858-Generating-a-new-API-token>) for more details on obtaining the API Token.


### Destination settings

The following settings specify how RudderStack sends the ingested data from Zendesk Support to the connected warehouse destination:

  * **Table prefix** : RudderStack uses this prefix to create a table in your data warehouse and loads all your Zendesk Support data into it.


> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add special characters like `-` or `_` to the prefix by default. Hence, you need to specify it while setting the prefix.

  * **Schedule Settings** : RudderStack gives you three options to ingest the data from Zendesk Support:
    * **Basic** : Runs the syncs at the specified time interval.
    * **CRON** : Runs the syncs based on the user-defined CRON expression.
    * **Manual** : You are required to run the syncs manually.


> ![info](/docs/images/info.svg)
> 
> For more information on the schedule types, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/>) guide.

### Select data to import

You can import specific Marketo data by selecting the required resources:

Resource| Sync type  
---|---  
`audit_logs`| Semi-Incremental  
`automations`| Semi-Incremental  
`brands`| Full Refresh  
`custom_roles`| Full Refresh  
`group_memberships`| Semi-Incremental  
`groups`| Full Refresh, Incremental  
`macros`| Full Refresh, Incremental  
`organizations`| Full Refresh, Incremental  
`organization_memberships`| Semi-Incremental  
`satisfaction_ratings`| Full Refresh, Incremental  
`schedules`| Full Refresh  
`sla_policies`| Full Refresh  
`tags`| Full Refresh  
`ticket_audits`| Semi-Incremental  
`ticket_comments`| Full Refresh, Incremental  
`ticket_events`| Incremental  
`ticket_fields`| Full Refresh, Incremental  
`ticket_forms`| Semi-Incremental  
`ticket_metric_events`| Full Refresh, Incremental  
`ticket_metrics`| Semi-Incremental  
`tickets`| Full Refresh, Incremental  
`triggers`| Semi-Incremental  
`users`| Full Refresh, Incremental  
`views`| Semi-Incremental  
  
> ![info](/docs/images/info.svg)
> 
> For more information on the **Full Refresh** , **Incremental** , and **Semi-Incremental** sync modes, see [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/#sync-modes>).

> ![warning](/docs/images/warning.svg)
> 
> There are some rate limits while sending requests to the Zendesk Support API. See [Zendesk documentation](<https://developer.zendesk.com/api-reference/introduction/rate-limits/>) for more details on these limits.

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