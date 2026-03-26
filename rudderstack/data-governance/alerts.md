# Configurable Alerts in RudderStack

Set up workspace and resource level alerts for critical data issues.

Available Plans

  * starter
  * growth
  * enterprise


* * *

  *  __9 minute read

  * 


RudderStack’s smart alerting capabilities let you set up notifications for critical data issues so you can take appropriate actions immediately before they escalate into major problems.

## Overview

With RudderStack’s alerting feature, you can configure alerts for:

  * Event Stream latency
  * Event delivery failures
  * Pre-sync or sync failures
  * Event volume drops
  * Transformation failures
  * Tracking Plan violations
  * Partial row failures and fatal syncs (for Reverse ETL connections)
  * Profiles run failures


You can also use the alerting feature to:

  * Set up alert delivery channels of your choice like email, custom webhook, Slack, or any other tool. Once the alert threshold is hit, RudderStack automatically delivers alerts to these systems.
  * Set failure thresholds at the workspace and resource level, so you are alerted only when necessary.


## Required permissions

  * Only [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) can set up workspace-level alerts.
  * Only [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) and [Members](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) with the [**Alert Overrides**](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) permission can set up resource-level alerts.

[![Alert Overrides permissions in new Access Management system](/docs/images/access-management/alert-overrides.webp)](</docs/images/access-management/alert-overrides.webp>)

#### Permissions for legacy RBAC system

In the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>):

  * Only [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) can set up workspace-level alerts
  * Only [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) and members with the **Connections Admin** role in their workspace policy can set up resource-level alerts

[![Data Catalog permissions in the legacy framework](/docs/images/access-management/tracking-plan-permissions-legacy-framework.webp)](</docs/images/access-management/tracking-plan-permissions-legacy-framework.webp>)

## Workspace level alerts

Go to **Settings** > **Workspace** and click the **Alerts** tab to set up the workspace-level alerts.

[![Alerts option in RudderStack dashboard](/docs/images/data-governance/configurable-alerts/alerts-tab.webp)](</docs/images/data-governance/configurable-alerts/alerts-tab.webp>)

RudderStack automatically delivers alerts on the configured channels if the failures exceed the threshold percentage within the last one hour.

> ![warning](/docs/images/warning.svg)
> 
> If you set the error threshold to 0%, even a single failure in processing or delivering events will trigger an alert.

The following sections detail the different alert types available per RudderStack feature:

### Event Stream

In this section, you can configure alerts and set thresholds for the following incidents:

Failure type| Description| Applicable to  
---|---|---  
Cloud destination pipeline failures| Failures in processing or delivering events to a destination due to incorrect credentials, destination downtime, network error, or any other reason.| [Event Stream destinations](<https://www.rudderstack.com/docs/destinations/streaming-destinations/>)  
P95 latency  
Enterprise plan only| Maximum latency for 95% of the events to reach the destination.  
  
See P95 latency alerts for more details.| [Event Stream destinations](<https://www.rudderstack.com/docs/destinations/streaming-destinations/>)  
Warehouse pre-sync failures| Failures in processing or storing the events in object storage before forwarding them to the warehouse destination.| [Warehouse destinations](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>)  
Warehouse sync failures| Failures in syncing events to a warehouse destination, that is, syncs to a warehouse destination are aborted. Possible reasons include:  
  


  * Incorrect warehouse connection credentials
  * Warehouse settings changed/updated midway through the syncs
  * Source/destination downtime or network error

| [Warehouse destinations](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>)  
Low event volume  
Beta| Event volume drop in the last one hour is more than the configured threshold, as compared to the same period from the last week.  
  
See Low event volume alerts for more details.| [Event Stream sources](<https://www.rudderstack.com/docs/sources/event-streams/>)  
Tracking Plan violations| [Tracking Plan violations](<https://www.rudderstack.com/docs/data-governance/tracking-plans/violation-management/#violation-types>) for a particular source, that is, the incoming source events and properties do not comply with the Tracking Plan connected to that source.| [Event Stream sources](<https://www.rudderstack.com/docs/sources/event-streams/>)  
Transformation failures  
Beta| Failures in processing events due to errors in the transformation.  
  
See Transformation failure alerts for more details.| [Transformations](<https://www.rudderstack.com/docs/transformations/overview/>)  
  
#### P95 latency alerts

> ![announcement](/docs/images/announcement.svg)
> 
> P95 latency alerts are available only in the [Enterprise plan](<https://www.rudderstack.com/enterprise-quote/>).

RudderStack triggers the **P95 latency** alert if the maximum latency experienced by 95% of the events to reach the destination exceeds the specified threshold.

For example, if you send 100 events to an Event Stream destination and the P95 latency alert threshold is set to 15 minutes, then 95 of those events should be delivered in **strictly less than** the specified threshold (that is, 15 minutes). Otherwise, RudderStack triggers an alert.

> ![warning](/docs/images/warning.svg)
> 
> **Important considerations**
> 
> The P95 latency metric and alerts are applicable **only** for [Event Stream destinations](<https://www.rudderstack.com/docs/destinations/streaming-destinations/>) connected to sources in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>). They are **not applicable** for:
> 
>   * [Reverse ETL connections](<https://www.rudderstack.com/docs/sources/reverse-etl/>)
>   * [Warehouse destinations](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>)
>   * Event Stream destinations connected to sources in [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>)
> 


Go to the **Events** tab of your Event Stream destination and click the **Latency** tab to check the average P95 latency across all Event Stream sources.

[![P95 latency for destination](/docs/images/data-governance/configurable-alerts/p95-latency-events.webp)](</docs/images/data-governance/configurable-alerts/p95-latency-events.webp>)

To view the P95 latency for events coming from a particular source, filter the Event Stream source from the dropdown:

[![View source-specific P95 latency](/docs/images/data-governance/configurable-alerts/filter-source-latency.webp)](</docs/images/data-governance/configurable-alerts/filter-source-latency.webp>)

#### Low event volume alerts

![Github Badge](https://img.shields.io/badge/Stability-Beta-blue?style=flat)  


RudderStack triggers the **Low event volume** alert if the event volume drop for an [Event Stream source](<https://www.rudderstack.com/docs/sources/event-streams/>) in the last one hour exceeds the configured threshold compared to the event volume for the same time period in the last week.

The **Low event volume** alert is triggered based on the below formula:

[![Equation to calculate low event volume triggers](/docs/images/data-governance/configurable-alerts/low-event-volume-equation.webp)](</docs/images/data-governance/configurable-alerts/low-event-volume-equation.webp>)

For example, you will get an alert if:

  * An Event Stream source ingests 450 events within the last hour (for example, 11 a.m. to 12 p.m.), but it ingested 1000 events from 11 a.m. to 12 p.m. a week before.
  * The alert threshold was set to 50%.


In this case, RudderStack triggers an alert as the volume drop percentage (55%) exceeds the configured threshold (50%).

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * A 0% threshold indicates that RudderStack triggers an alert **even if** the number of ingested events in the past one hour is the same as last week. That is, `last_week_window_count` = `current_window_count`.
>   * A 100% threshold indicates that RudderStack triggers an alert if the source ingested **no** events in the last one hour but some events (>0) exactly a week before. That is, `current_window_count` = 0 and `last_week_window_count` > 0.
> 


#### Transformation failure alerts

![Github Badge](https://img.shields.io/badge/Stability-Beta-blue?style=flat)  


RudderStack triggers the **Transformation failures** alert if the [transformation](<https://www.rudderstack.com/docs/transformations/overview/>) failures in the last one hour exceed the configured threshold.

For example, you will get an alert if:

  * You set the alert threshold to 10%.
  * The transformation ingests 100 events in the past one hour.
  * 11 events are dropped due to a transformation error, that is, failure to transform the event correctly as per the specified logic.


### Reverse ETL

In this section, you can configure alerts for the following incidents applicable to all your [Reverse ETL sources](<https://www.rudderstack.com/docs/sources/reverse-etl/>):

Failure type| Description  
---|---  
Partial row failures| Failures in syncing records from the warehouse source to the connected destination.  
Fatal syncs| Fatal errors causing a running sync to be aborted. Possible reasons include:

  * Incorrect warehouse connection credentials
  * Warehouse settings changed/updated midway through the syncs
  * Source/destination downtime or network error

  
  
### Profiles

In this section, you can configure alerts for the following incidents applicable to your [Profiles](<https://www.rudderstack.com/docs/profiles/overview/>) runs:

Failure type| Description  
---|---  
Run failures  
Beta| Failures encountered while running your Profiles project.  
  
### Custom alerts

Click the **Custom alerts** setting present below each failure type to view the resources for which custom alert overrides are configured:

[![Custom alert setting](/docs/images/data-governance/configurable-alerts/custom-alerts-setting.webp)](</docs/images/data-governance/configurable-alerts/custom-alerts-setting.webp>)

The resulting sidebar lists all the resources with custom alerts categorized by failure type. You also see the following information:

  * **Name** : The resource name.
  * **Subscribed** : Whether alerts are on or off for that failure type.
  * **Threshold** : Custom alert threshold value set for that resource.


Click on a resource to change these settings.

[![Custom alerts](/docs/images/data-governance/configurable-alerts/custom-alerts.webp)](</docs/images/data-governance/configurable-alerts/custom-alerts.webp>)

## Resource level alerts

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * Once you set the alert overrides for a particular resource, any changes to the workspace-level settings will not be applicable for that resource.
>   * You cannot change the alert delivery channels for a particular resource.
> 


Go to the resource (source or destination) for which you want to customize the alert settings. Then, click the **Settings** tab and scroll down to the alerts section.

[![Resource-level alert settings](/docs/images/data-governance/configurable-alerts/resource-level-alert-settings.webp)](</docs/images/data-governance/configurable-alerts/resource-level-alert-settings.webp>)

If configured, you will see the workspace-level alert settings and thresholds enabled for the resource by default. You can change these settings and set custom thresholds for this resource.

Once you change the settings, you will automatically see the following message pop up:

[![Resource-level alerts](/docs/images/data-governance/configurable-alerts/resource-level-alerts.webp)](</docs/images/data-governance/configurable-alerts/resource-level-alerts.webp>)

### Resource-specific alert types

The following table lists the alert types applicable to a particular resource:

Resource type| Alert type  
---|---  
Event Stream source| 

  * Low event volume
  * Tracking Plan violations

  
Event Stream destination| 

  * P95 Latency (only for cloud mode)
  * Cloud destination failures

  
Warehouse destination| 

  * Warehouse pre-sync failures
  * Warehouse sync failures

  
Reverse ETL source| 

  * Partial row failures
  * Fatal syncs

  
Profiles project| Run failures  
  
## Set up alert delivery channels

You can set up dedicated alert channels to get notified whenever your sources or destinations have failures or errors. This allows you to take proactive measures to fix the problems before they escalate into major issues.

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * You can set up separate alert delivery channels for your Event Stream and Reverse ETL pipelines.
>   * Toggling off alerts for a channel automatically removes all the configurations. You will have to reconfigure the channel to use it again.
>   * RudderStack limits the alert delivery to one alert per resource per alert type for each configured channel every 24 hours.
> 


RudderStack provides the following options to set up channels for delivery alerts:

### Slack

Toggle on the **Slack** setting to receive alerts on your preferred Slack channel.

[![Slack channel configuration for alerts](/docs/images/data-governance/configurable-alerts/slack-alerts.webp)](</docs/images/data-governance/configurable-alerts/slack-alerts.webp>)

Set the Slack channel and authorize RudderStack to post the alerts by clicking **Allow**. Note that you should be an admin of the Slack workspace to grant RudderStack the necessary permissions to post to that channel.

> ![info](/docs/images/info.svg)
> 
> While setting the Slack channel, you will see a **This app is not approved by Slack** ribbon at the top. This is because Slack has not reviewed the app yet. However, it is completely safe to install.

[![Slack channel configuration for alerts](/docs/images/data-governance/configurable-alerts/configure-slack-channel.webp)](</docs/images/data-governance/configurable-alerts/configure-slack-channel.webp>)

Once the alert is triggered, RudderStack automatically sends a notification on the specified Slack channel. Click **Review on RudderStack** to go to the specific resource (source or destination) to investigate and fix the errors.

[![Slack alerts](/docs/images/data-governance/configurable-alerts/slack-alerts-new.webp)](</docs/images/data-governance/configurable-alerts/slack-alerts-new.webp>)

### Microsoft Teams

> ![info](/docs/images/info.svg)
> 
> To use MS Teams for alerts delivery, you must [create an incoming webhook](<https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook?tabs=newteams%2Cdotnet>) for the Teams channel you wish to use.

Toggle on the **MS Teams** setting and enter the incoming webhook URL to receive alerts on your preferred Teams channel.

[![Teams channel configuration for alerts](/docs/images/data-governance/configurable-alerts/teams-alerts.webp)](</docs/images/data-governance/configurable-alerts/teams-alerts.webp>)

Once the alert is triggered, RudderStack automatically sends a notification on the specified Teams channel:

[![Teams alerts](/docs/images/data-governance/configurable-alerts/teams-alerts-2.webp)](</docs/images/data-governance/configurable-alerts/teams-alerts-2.webp>)

Click **Review on RudderStack** to go to the specific resource (source or destination) to investigate and fix the errors.

### Webhook

Toggle on the **Webhook** setting to forward the alerts to custom webhook channels.

RudderStack sends the alerts as a `POST` request to the configured endpoint while following the Prometheus styling format.

> ![info](/docs/images/info.svg)
> 
> Prometheus is a widely accepted monitoring and alerting tool. Its alert format is compatible with various other monitoring and incident management tools like Squadcast, PagerDuty, etc.

A sample webhook response is shown:
    
    
    {
      "alerts": [{
        "endsAt": "0001-01-01T00:00:00Z",
        "labels": {
          "severity": "critical",
          "alertname": "partial-row-failures",
          "workspace": "<workspace_name>",
          "destination": "Failing Webhook",
          "workspaceId": "<workspace_id>",
          "organization": "<org_name>",
          "destinationId": "<destination_id>",
          "organizationId": "<org_id>",
          "configuredThreshold": 61
        },
        "status": "firing",
        "startsAt": "2024-02-05T00:02:49.933Z",
        "annotations": {
          "description": "Errors in processing or delivering events to Failing Webhook destination have exceeded the configured threshold of 61% within last 1 hour"
        },
        "fingerPrint": "d9885cc7f11b8db0"
      }],
      "status": "firing"
    }
    

#### Send alerts to downstream tools

You can also leverage webhooks to forward the alerts to any RudderStack-supported downstream tool:

  1. Set up a [webhook source](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/webhook-source/>). Note the webhook URL containing the source write key parameter.

[![Webhook source](/docs/images/data-governance/configurable-alerts/webhook-source.webp)](</docs/images/data-governance/configurable-alerts/webhook-source.webp>)

  2. Set up a [destination integration](<https://www.rudderstack.com/docs/destinations/streaming-destinations/>), for example, [PagerDuty](<https://www.rudderstack.com/docs/destinations/streaming-destinations/pagerduty/>). Connect it to the webhook source created in Step 1.
  3. Once you set up the connection, specify the webhook source URL obtained in Step 1 in the **Enter URL** field where RudderStack forwards the alerts.

[![Webhook configuration for alerts](/docs/images/data-governance/configurable-alerts/webhook-alerts.webp)](</docs/images/data-governance/configurable-alerts/webhook-alerts.webp>)

### Email

Toggle on the **Email** setting and specify comma-separated email addresses of the users who would like to receive the alerts.

[![Email alerts](/docs/images/data-governance/configurable-alerts/email.webp)](</docs/images/data-governance/configurable-alerts/email.webp>)

Once the alert is triggered, these users will automatically get email alerts to investigate and fix the errors.

[![Email alerts](/docs/images/data-governance/configurable-alerts/email-alert-new.webp)](</docs/images/data-governance/configurable-alerts/email-alert-new.webp>)

## Alert frequency

RudderStack limits the alert delivery to one alert per resource (source or destination) per alert type for each configured channel every 24 hours.

This alerting logic ensures you are not spammed with notifications, especially in cases where you have configured multiple alert types for your pipelines and some resources have their own overrides (custom alert settings) in place.

#### Use case

Suppose you get a Partial row failures alert for a particular Reverse ETL source. You will not get another alert for the same failure type for another 24 hours even if your data syncs are scheduled at a lesser frequency (for example, every one, five, or 12 hours).

However, if that source encounters another failure type like a fatal sync, RudderStack will trigger an alert.