# Access Management Policies Overview

Configure policies that apply to your workspace, groups, and individual members.

* * *

  * __5 minute read

  * 


This guide introduces the concept of an access policy in RudderStack’s Access Management system.

## Overview

An access policy is a bundle of configured permissions. The process of configuring an access policy is the same for a [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>), [Group Policies](<https://www.rudderstack.com/docs/access-management/groups/>), [Member Policies](<https://www.rudderstack.com/docs/access-management/members/>), and [Access Tokens](<https://www.rudderstack.com/docs/access-management/service-access-tokens/>).

The permissions within an access policy are organized into two broad categories:

  * Resource permissions
  * PII permissions


## Resource permissions

The **Resources** section lets you configure permissions for all RudderStack resources. These include:

  * Event Stream [Sources](<https://www.rudderstack.com/docs/sources/event-streams/>) and [Destinations](<https://www.rudderstack.com/docs/destinations/streaming-destinations/>)
  * [Reverse ETL Sources](<https://www.rudderstack.com/docs/sources/reverse-etl/>) created via tables, SQL models, and Audiences
  * [Transformations](<https://www.rudderstack.com/docs/transformations/overview/>) and [Transformation Libraries](<https://www.rudderstack.com/docs/transformations/libraries/>)
  * [Tracking Plans](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>) and [Data Catalog](<https://www.rudderstack.com/docs/data-governance/data-catalog/>)
  * [Profiles](<https://www.rudderstack.com/docs/profiles/overview/>)
  * Ability to override [Alerts](<https://www.rudderstack.com/docs/data-governance/alerts/>) and retry warehouse syncs (for both sources and destinations).
  * [Bot management](<https://www.rudderstack.com/docs/data-governance/bot-management/>) and the ability to manage [Credentials](<https://www.rudderstack.com/docs/transformations/credentials/>) to securely store sensitive keys and secrets for use in transformations.


> ![info](/docs/images/info.svg)
> 
> For many resources, you can configure permissions at a resource level, meaning you can choose a subset of resources to which the permission applies.

A sample resource permissions policy configuration for a workspace is shown below:

[![Resource permissions](/docs/images/access-management/resource-permissions.webp)](</docs/images/access-management/resource-permissions.webp>)

### Edit, Connect, and Create & Delete permissions

You can assign **Edit** , **Connect** , and **Create & Delete** permissions to resources.

Permission| Description  
---|---  
Edit| Make changes to the configuration of resources.  
Connect| Connect two resources.  
Create & Delete| Create or delete resources for a resource type.  
  
### Permissions dependencies

Depending on the type of resource, some permissions have dependencies across resources. The table below provides details on dependencies.

Resource| Permission| Dependencies  
---|---|---  
  
  * Sources
  * Destinations
  * Transformations
  * Tracking Plans
  * Tables
  * Audiences
  * SQL Models

| **Connect**| **Edit** and **Connect** permissions are required on **both** resources (source and destination, transformation and destination, source and Tracking Plan, etc.) to make a successful connection  
Data Catalog| **Edit** events and properties that are part of a Tracking Plan| **Edit** permission for that Tracking Plan  
  
## PII permissions

> ![announcement](/docs/images/announcement.svg)
> 
> The ability to configure PII permissions is available only in RudderStack’s [Enterprise](<https://www.rudderstack.com/enterprise-quote/>) plan.

The **PII** section lets you configure permissions for viewing parts of the platform where payloads might contain PII. These include:

  * Live events from Event Stream pipelines (Sources, Destinations, and Transformations)

  * Live events from Reverse ETL sources (created via tables, SQL models, or Audiences)

  * [Sample events](<https://www.rudderstack.com/docs/dashboard-guides/data-management/#sample-event-data>) that include:

    * Destination delivery failures
    * Transformation errors
    * Tracking Plan violations


### Configurable permissions

The following table lists all the configurable PII permissions:

PII permission| Description  
---|---  
Destination Live Events| View [live events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/#destination-live-events>) for a destination  
Destination Failure Samples| View [failure samples](<https://www.rudderstack.com/docs/dashboard-guides/event-metrics/#view-failed-event-details>) for a destination  
Destination Data Access| Access data from the [Activation API](<https://www.rudderstack.com/docs/profiles/dev-docs/activation-api/>)  
Event Stream Source Live Events| View [live events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/#source-live-events>) ingested by an Event Stream source  
Table Live Events| View live events from a Reverse ETL source created via a warehouse table  
Audience Live Events| View live events from a Reverse ETL source created via an [Audience](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/audiences/>)  
SQL Model Live Events| View live events from a Reverse ETL source created via a [SQL Model](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/models/>)  
Reverse ETL Sync Failure Samples| View failure samples for a Reverse ETL sync  
Transformation Live Events| View [live events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/#transformation-live-events>) flowing through a transformation  
Transformation Failure Samples| View [failure samples](<https://www.rudderstack.com/docs/dashboard-guides/event-metrics/#view-transformation-error-details>) for a transformation  
Tracking Plan Violations| View [Tracking Plan violations](<https://www.rudderstack.com/docs/data-governance/tracking-plans/violation-management/>)  
  
> ![info](/docs/images/info.svg)
> 
> **PII permissions for transformations connected to destinations**
> 
> If you connect a transformation to a destination, you will see [transformation failures](<https://www.rudderstack.com/docs/dashboard-guides/event-metrics/#view-transformation-error-details>) (which are a part of that pipeline) along with other [event failure metrics](<https://www.rudderstack.com/docs/dashboard-guides/event-metrics/#view-failed-event-details>) in the destination’s **Events** tab and [Health dashboard](<https://www.rudderstack.com/docs/data-governance/health-dashboard/#get-failure-metrics>).
> 
> In this case, you need only the **Destination Failure Samples** PII permission for the specific destination — the **Transformation Failure Samples** PII permission is not required.

A sample PII policy configuration as a part of the [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>) is shown below:

[![PII permissions for a workspace](/docs/images/access-management/example-pii-permissions.webp)](</docs/images/access-management/example-pii-permissions.webp>)

## Granular resource and PII permissions

> ![success](/docs/images/tick.svg)
> 
> The granular resource and PII restrictions apply across both the RudderStack dashboard and API layers, ensuring comprehensive privacy control.

You can configure **Edit** and PII permissions for specific resources within your workspace. To grant **Edit** permission for a subset of Event Stream sources, click the dropdown next to **Event Streams** and select the sources.

[![Edit permissions example](/docs/images/access-management/specific-edit-permissions.webp)](</docs/images/access-management/specific-edit-permissions.webp>)

Similarly, you can grant PII access to [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/>) for a subset of sources:

[![PII permissions given to specific resources](/docs/images/access-management/specific-pii-permissions.webp)](</docs/images/access-management/specific-pii-permissions.webp>)

### Example

Suppose a workspace has three Event Stream sources (`S1`, `S2`, and `S3`) and three destinations (`D1`, `D2`, and `D3`). You can configure the [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>) to grant:

  * **Edit** permission only for sources `S1` and `S2`
  * **Edit** permission only for destinations `D1` and `D2`
  * **Connect** permission for sources
  * **Connect** permission for destinations
  * PII permission to view live events only for source `S1`


The baseline access policy then looks as follows:

[![Resource permissions example](/docs/images/access-management/granular-resource-permissions-example.webp)](</docs/images/access-management/granular-resource-permissions-example.webp>)[![PII permissions example](/docs/images/access-management/granular-pii-permissions-example.webp)](</docs/images/access-management/granular-pii-permissions-example.webp>)

#### What the member can do

A member inheriting the above baseline policy **will** be able to:

  * Edit only sources `S1` and `S2`
  * Edit only destinations `D1` and `D2`
  * Connect sources `S1` and `S2` to destinations `D1` and `D2`
  * View Live Events for source `S1`


#### What the member cannot do

The member **will not** be able to:

  * Edit source `S3`
  * Edit destination `D3`
  * Make any connections to source `S3`
  * Make any connections to destination `D3`
  * View Live Events for sources `S2` and `S3`
  * View Live Events or failure samples for destinations `D1`, `D2`, and `D3`


Members without the above granular permissions will see greyed-out UI elements with explanatory tooltips, as shown below:

**Without resource permissions**

[![User without resource permissions](/docs/images/access-management/no-permissions.webp)](</docs/images/access-management/no-permissions.webp>)

**Without PII permissions**

[![User without PII permissions](/docs/images/access-management/no-pii-permissions.webp)](</docs/images/access-management/no-pii-permissions.webp>)

### Plan-wise limits

See the [Plan-wise Features](<https://www.rudderstack.com/docs/access-management/plan-wise-features/#granular-resource-permissions>) guide for more details on granular resource and PII permission limits across different RudderStack plans.