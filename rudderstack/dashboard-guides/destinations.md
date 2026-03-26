# RudderStack Destinations

Add and manage destinations in the RudderStack dashboard.

* * *

  * __3 minute read

  * 


A **destination** is a cloud tool or platform where you want to send events via RudderStack.

RudderStack currently supports over 180 [cloud](<https://www.rudderstack.com/docs/destinations/streaming-destinations/>) and [warehouse](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>) destinations.

## Add a destination

  1. Log in to your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. From the left sidebar, go to **Collect** > **Destinations**.
  3. Click **New destination**.
  4. Select the destination from the list.
  5. Assign a name to the destination and click **Continue**.
  6. Select a source to connect to this destination.


> ![info](/docs/images/info.svg)
> 
> You will see all the compatible sources for the destination in this view.

  5. Configure the destination with the relevant connection settings. See the [destination-specific documentation](<https://www.rudderstack.com/docs/destinations/overview/>) for details.


## Overview

Once you set up a destination, you will see the following information on the destination page:

[![Destination information](/docs/images/dashboard-guides/destinations/destination-information.webp)](</docs/images/dashboard-guides/destinations/destination-information.webp>)

Just below your destination name, you will see the following options:

Option| Description  
---|---  
Resource ID| Unique identifier for the RudderStack destination — click to copy the ID to the clipboard.  
Setup guide| Link to the destination-specific documentation  
Live events| Lets you view the [destination live events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/#destination-live-events>)  
Alerts| The bell icon on the top right corner indicating the number of active alerts for the destination.  
  


> ![tip](/docs/images/tip.svg)**Tip:** Click the icon to get an alert summary and take appropriate remedial actions immediately. See [Alerts](<https://www.rudderstack.com/docs/data-governance/alerts/>) for more information on this feature.  
  
Click the meatballs menu (**…**) to access the following options:

Setting| Description  
---|---  
Rename| Lets you rename the destination  
Clone| Lets you clone/duplicate the destination with the same configuration settings  
Enable / Disable| Lets you enable or disable the destination  
Delete| Lets you delete the destination  
  


> ![warning](/docs/images/warning.svg)You cannot delete a destination that is connected to any source.  
  
## Tab details

The following sections explain the various tabs available on the destination page.

### Sources

The **Sources** tab displays all the sources connected to the destination and their status.

Click the meatballs menu (**…**) to disconnect a source.

### Transformation

The **Transformation** tab lets you connect a [Transformation](<https://www.rudderstack.com/docs/transformations/overview/>) to transform your events before sending them to this destination.

Click **Add a transformation** to connect a new transformation or choose an existing transformation from the list.

### Events

The **Events** tab displays the event delivery metrics like:

  * Events delivered successfully
  * Failed events (due to processing, transformation, and delivery errors)
  * P95 latency across all Event Stream sources


> ![info](/docs/images/info.svg)
> 
> **Important consideration**
> 
> RudderStack shows the P95 latency metric only for [Event Stream destinations](<https://www.rudderstack.com/docs/destinations/streaming-destinations/>) connected to sources in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>). It is **not applicable** for:
> 
>   * [Reverse ETL connections](<https://www.rudderstack.com/docs/sources/reverse-etl/>)
>   * [Warehouse destinations](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>)
>   * Event Stream destinations connected to sources in [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>)
> 


You can filter these metrics by source and duration (past 2 hours, 1 day, 7 days, or 30 days). RudderStack also shows you the event delivery and latency trends in this view along with details on delivery failures.

See [Event Metrics](<https://www.rudderstack.com/docs/dashboard-guides/event-metrics/>) for more information on this tab.

### Configuration

The **Configuration** tab lets you edit the destination’s connection settings.

Click the **Edit configuration** button to make the required changes.

> ![warning](/docs/images/warning.svg)
> 
> Make sure to click the **Finish** button for the changes to take effect.

### Syncs

The **Syncs** tab is present in all [warehouse destinations](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>). It shows the sync details for the sources connected to the warehouse, like:

  * Source and schema name
  * Timestamp of the first and last event in the upload batch
  * Duration of the sync


### Alerts

The **Alerts** tab lets you set specific alert overrides applicable to this destination.

See [Configurable Alerts](<https://www.rudderstack.com/docs/data-governance/alerts/#resource-level-alerts>) for more information.

### Audit Logs

> ![info](/docs/images/info.svg)
> 
> Audit Logs are available only in the RudderStack [Enterprise](<https://www.rudderstack.com/enterprise-quote/>) plan.

The **Audit Logs** tab lets you view the [Audit Logs](<https://www.rudderstack.com/docs/dashboard-guides/audit-logs/>) for the destination.

### Permissions

> ![warning](/docs/images/warning.svg)
> 
> This setting is visible only to [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) in the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>) in the RudderStack [Enterprise](<https://www.rudderstack.com/enterprise-quote/>) plan.

You can use the **Permissions** tab to determine which members in your workspace can make changes to the destination. This is useful when you want to set granular controls for the resources within your workspace.

See [Permissions Management](<https://www.rudderstack.com/docs/archive/dashboard-guides/permissions-management/#restricting-edit-permissions-for-individual-objects>) for more details.