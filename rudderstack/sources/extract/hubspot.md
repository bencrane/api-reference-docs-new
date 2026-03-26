# HubSpot Cloud Extract Source Deprecated

Sync data from HubSpot to your warehouse destination via RudderStack.

* * *

  * __4 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> This source is deprecated and no longer supported as of **January 10, 2026**.

[HubSpot](<https://www.HubSpot.com/>) is a leading marketing and CRM platform that helps you track leads as well as inbound marketing and sales.

This document guides you in setting up HubSpot as a source in RudderStack. Once configured, RudderStack automatically ingests your HubSpot data and routes it to your specified data warehouse destination.

> ![info](/docs/images/info.svg)
> 
> All Cloud Extract sources support sending data only to a [data warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).

## Getting started

To set up HubSpot as a source in RudderStack, follow these steps:

  1. Log into your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Sources** > **New source** > **Cloud Extract** and select **HubSpot** from the list of sources.
  3. Assign a name to your source and click **Continue**.


### Connection settings

  * **HubSpot Credentials** : Click **Connect with HubSpot** and grant RudderStack the necessary permissions to access your HubSpot data.


> ![info](/docs/images/info.svg)
> 
> Your HubSpot account and the related details will then automatically appear under **Choose an account**.

  * **Start Date** : Select the date from when RudderStack ingests your HubSpot data. RudderStack will not replicate any data before this date.


### Destination settings

The following settings specify how RudderStack sends the ingested data from HubSpot to the warehouse destination:

  * **Table prefix** : RudderStack uses this prefix to create a table in your data warehouse and loads all your HubSpot data into it.


> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add special characters like `-` or `_` to the prefix by default. Hence, you need to specify it while setting the prefix.

  * **Schedule Settings** : RudderStack gives you three options to ingest the data from HubSpot:
    * **Basic** : Runs the syncs at the specified time interval.
    * **CRON** : Runs the syncs based on the user-defined CRON expression.
    * **Manual** : You are required to run the syncs manually.


> ![info](/docs/images/info.svg)
> 
> For more information on the schedule types, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/>) guide.

### Selecting the data to import

You can choose the HubSpot data you want to ingest by selecting the required resources:

[![Selecting the data to import](/docs/images/cloud-extract-sources/hubspot-connection-settings-2.webp)](</docs/images/cloud-extract-sources/hubspot-connection-settings-2.webp>)

The below table mentions the syncs and API endpoints supported by the HubSpot resources to your warehouse destination:

Resource| Full Refresh sync| Incremental sync| HubSpot API endpoint  
---|---|---|---  
`campaigns`| Yes| No| `/email/public/v1/campaigns/{campaignId}`  
`companies`| Yes| Yes| `/crm/v3/objects/company`  
`contact_lists`| Yes| Yes| `/contacts/v1/lists`  
`contacts`| Yes| Yes| `/crm/v3/objects/contact`  
`contacts_list_memberships`| Yes| No| `/contacts/v1/lists/all/contacts/all`  
`deal_pipelines`| Yes| No| `/crm-pipelines/v1/pipelines/deals`  
`deals`| Yes| Yes| `/crm/v3/objects/deals/search`  
`email_events`| Yes| Yes| `/email/public/v1/events`  
`engagements`| Yes| Yes| `/engagements/v1/engagements/paged` or  
[`/engagements/v1/engagements/recent/modified`](<https://legacydocs.hubspot.com/docs/methods/engagements/get-recent-engagements>)  
`feedback_submissions`| Yes| Yes| `/crm/v3/objects/feedback_submissions`  
`forms`| Yes| No| `/marketing/v3/forms/`  
`form_submissions`| Yes| No| `/form-integrations/v1/submissions/forms/:form_guid`  
`line_items`| Yes| Yes| `/crm/v3/objects/line_items`  
`marketing_emails`| Yes| No| `/marketing-emails/v1/emails/with-statistics`  
`owners`| Yes| No| `/owners/v2/owners/`  
`property_history`| Yes| Yes| `/crm/v3/objects/products`  
`subscription_changes`| Yes| Yes| `/email/public/v1/subscriptions/timeline`  
`tickets`| Yes| Yes| `/crm/v3/objects/tickets`  
`ticket_pipelines`| Yes| No| `/crm/v3/pipelines/ticket`  
`workflows`| Yes| No| `/automation/v3/workflows`  
  
> ![info](/docs/images/info.svg)
> 
> For more information on the **Full Refresh** and **Incremental** sync modes, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/#sync-modes>) guide.

Note that the objects in the `engagements` stream can be of the following types:

  * `call`
  * `email`
  * `meeting`
  * `note`
  * `task`


Depending on the engagement type, RudderStack sets different properties for the object in the `engagements_metadata` table in the warehouse destination:

Engagement type| `engagements_metadata` columns with non-null values  
---|---  
`call`| `toNumber`, `fromNumber`, `status`, `externalId`,  
`durationMilliseconds`, `externalAccountId`, `recordingUrl`,  
`body`, `disposition`  
`email`| `subject`, `html`, `text`  
`meeting`| `body`, `startTime`, `endTime`, `title`  
`note`| `body`  
`task`| `body`, `status`, `forObjectType`  
  
> ![info](/docs/images/info.svg)
> 
> For the `email` engagement type, RudderStack also creates the records in the following four related tables:
> 
>   * `engagements_metadata_from`
>   * `engagements_metadata_to`
>   * `engagements_metadata_cc`
>   * `engagements_metadata_bcc`
> 


HubSpot is now configured as a source. RudderStack will start ingesting data from HubSpot as per your specified schedule and frequency.

You can further connect this source to your data warehouse by clicking on **Add Destination** :

[![Adding a destination](/docs/images/cloud-extract-sources/add-destination.webp)](</docs/images/cloud-extract-sources/add-destination.webp>)

> ![success](/docs/images/tick.svg)
> 
> Use the **Use Existing Destination** option if you have an already-configured data warehouse destination in RudderStack. To configure a data warehouse destination from scratch, select the **Create New Destination** button.

## FAQ

#### Is it possible to have multiple Cloud Extract sources writing to the same schema?

Yes, it is.

RudderStack associates a table prefix for every Cloud Extract source writing to a warehouse schema. This way, multiple Cloud Extract sources can write to the same schema with different table prefixes.

#### How does RudderStack sync the HubSpot data?

Upon configuring the source, RudderStack first connects to your HubSpot instance and pulls all historical data from the **Start Date** specified in the dashboard settings. Subsequently, RudderStack syncs the data to your warehouse based on your specified sync schedule and frequency.

#### How does RudderStack count the events for Cloud Extract sources?

RudderStack counts the number of records returned by the source APIs when queried during each sync. It considers each record as an event.

#### How does RudderStack set the table name for the data sent via Cloud Extract sources?

RudderStack sets the table name for the resource you are syncing to the warehouse by adding `rudder_` to the **Table prefix** you set while configuring your Cloud Extract source in the dashboard.

[![Cloud Extract table prefix](/docs/images/cloud-extract-sources/etl-table-prefix.webp)](</docs/images/cloud-extract-sources/etl-table-prefix.webp>)

For example, if you set `test_` as the **Table prefix** in the dashboard, RudderStack sets the table name as `test_rudder_<resource_name>`, where `<resource_name>` is the name of the resource you are syncing (for example, `contacts`, `messages`, etc.).

> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add the character `_` to the prefix by default. Hence, you need to specify it while setting the prefix.