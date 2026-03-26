# RudderStack Sources

Add and manage sources in the RudderStack dashboard.

* * *

  * __3 minute read

  * 


A **source** is a platform or an application (web, mobile, server-side, or a third-party cloud app) from where RudderStack tracks and collects the data.

RudderStack supports the following source types:

  * [Event Streams](<https://www.rudderstack.com/docs/sources/event-streams/>)
  * [Reverse ETL](<https://www.rudderstack.com/docs/sources/reverse-etl/>)


## Add a source

  1. Log in to your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. From the left sidebar, go to **Collect** > **Sources**.
  3. Click **New source**.
  4. Select the source from the list.
  5. Assign a name to the source and click **Continue** to complete the setup.


> ![warning](/docs/images/warning.svg)
> 
> Setting up Reverse ETL sources require some additional configuration. See the [source-specific documentation](<https://www.rudderstack.com/docs/sources/reverse-etl/>) for detailed steps.

## Overview

Once you set up a source, you will see the following information on the source page:

[![Source information](/docs/images/dashboard-guides/sources/source-information.webp)](</docs/images/dashboard-guides/sources/source-information.webp>)

Just below your source name, you will see the following options:

Option| Description  
---|---  
Resource ID| Unique identifier for the RudderStack source — click to copy the ID to the clipboard.  
Write key| The source write key used to send events to the source.  
Setup guide| Link to the source-specific documentation  
Live events| Lets you view the [source live events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/#source-live-events>)  
Alerts| The bell icon on the top right corner indicating the number of active alerts for the source.  
  


> ![tip](/docs/images/tip.svg)**Tip:** Click the icon to get an alert summary and take appropriate remedial actions immediately. See [Alerts](<https://www.rudderstack.com/docs/data-governance/alerts/>) for more information on this feature.  
  
Click the meatballs menu (**…**) to access the following options:

Setting| Description  
---|---  
Rename| Lets you rename the source  
Enable / Disable| Lets you enable or disable the source  
Delete| Lets you delete the source  
  


> ![warning](/docs/images/warning.svg)You cannot delete a source that is connected to any destination.  
  
> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * RudderStack does not accept any events if the source is disabled.
>   * You will get a `404` error with the message `Source is disabled` if you send events to a disabled source.
>   * RudderStack does not count events sent to a disabled source in the total event volume and does not charge for them.
> 


## Tab details

The following sections explain the various tabs available on the source page.

### Setup

The **Setup** tab includes the installation snippet and write key to set up your source.

### Overview

The **Overview** tab gives you a quick overview of the source, including:

  * List of the connected destinations
  * Option to connect to a new or existing destination via the **Add destination** button

[![Source overview tab](/docs/images/dashboard-guides/sources/source-overview-tab.webp)](</docs/images/dashboard-guides/sources/source-overview-tab.webp>)

### Events

The **Events** tab displays the event delivery metrics like total number of events, [bot events](<https://www.rudderstack.com/docs/data-governance/bot-management/>), [blocked events](<https://www.rudderstack.com/docs/data-governance/event-blocking/>) and number of ingested events.

If you have a [Tracking Plan](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>) connected to the source, you can also see the [event validation metrics](<https://www.rudderstack.com/docs/data-governance/tracking-plans/#observability>) like number of successfully validated events and events that violate Tracking Plan rules.

See [Event Metrics](<https://www.rudderstack.com/docs/dashboard-guides/event-metrics/>) for more information on this tab.

### Settings

The **Settings** tab displays the following source-specific settings:

Setting| Description  
---|---  
Temporarily store data in staging area| If enabled, lets RudderStack resend your events in case of failure.  
Enable geolocation enrichment| If enabled, lets you enrich your events with geolocation data. See [Geolocation Enrichment at Source](<https://www.rudderstack.com/docs/data-governance/geolocation-service/>) for more information.  
Bot event management| Lets you override the bot management settings set at the workspace level for this particular source. See [Bot Management](<https://www.rudderstack.com/docs/data-governance/bot-management/>) for more information.  
  
### Alerts

The **Alerts** tab lets you set specific alert overrides applicable to this source.

See [Configurable Alerts](<https://www.rudderstack.com/docs/data-governance/alerts/#resource-level-alerts>) for more information.

### Audit Logs

> ![info](/docs/images/info.svg)
> 
> Audit Logs are available only in the RudderStack [Enterprise](<https://www.rudderstack.com/enterprise-quote/>) plan.

The **Audit Logs** tab lets you view the [Audit Logs](<https://www.rudderstack.com/docs/dashboard-guides/audit-logs/>) for the source.

### Tracking Plans

The **Tracking Plans** tab lets you link or unlink a [Tracking Plan](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>) with the source.

### Permissions

> ![warning](/docs/images/warning.svg)
> 
> This setting is visible only to [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) in the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>) in the RudderStack [Enterprise](<https://www.rudderstack.com/enterprise-quote/>) plan.

You can use the **Permissions** tab to determine which members in your workspace can make changes to the source. This is useful when you want to set granular controls for the resources within your workspace.

See [Permissions Management](<https://www.rudderstack.com/docs/archive/dashboard-guides/permissions-management/#restricting-edit-permissions-for-individual-objects>) for more details.