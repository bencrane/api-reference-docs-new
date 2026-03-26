# Dashboard Overview

Manage your data pipelines and use different RudderStack features.

* * *

  * __7 minute read

  * 


Once you [sign up](<https://app.rudderstack.com/signup>) for RudderStack, you are directed to the RudderStack dashboard where you can set up and manage your sources, destinations, and various RudderStack features.

This guide walks you through all the settings available in the RudderStack dashboard.

## Getting started checklist

This checklist gives you different options to add a source and destination to set up a connection, view live events, invite other members in your workspace, and more.

[![Get started checklist](/docs/images/rs-cloud/get-started.webp)](</docs/images/rs-cloud/get-started.webp>)

## Directory

**Directory** is a catalog of all the RudderStack-supported sources and destinations. You can search for any source/destination from this view and set them up.

## Collect

This section lets you set up your data pipelines by connecting different sources and destinations across your customer data stack.

### Connections

This option shows all the connections between your sources and destinations. You also see the following options:

  * [Add source](<https://www.rudderstack.com/docs/dashboard-guides/sources/#add-a-source>)
  * [Add destination](<https://www.rudderstack.com/docs/dashboard-guides/destinations/#add-a-destination>)
  * **Data Plane URL** : Required for routing and processing events to RudderStack.

[![Data Plane URL](/docs/images/rs-cloud/data-plane-url.webp)](</docs/images/rs-cloud/data-plane-url.webp>)

> ![info](/docs/images/info.svg)
> 
> If you’re using [RudderStack Open Source](<https://app.rudderstack.com/signup?type=opensource>), you must [set up your own data plane](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/data-plane-setup/>) in your preferred environment.
> 
> An open source data plane URL looks like `http:localhost:8080` where `8080` is typically the port where your RudderStack data plane is hosted.

### Sources

This option lists all the configured sources in your workspace. You can add a new source by clicking the **New Source** button.

### Destinations

This option lists all the configured destinations in your workspace. You can add a new destination by clicking the **New Destination** button.

### Transformations

[Transformations](<https://www.rudderstack.com/docs/transformations/overview/>) let you transform your events using custom JavaScript/Python functions before sending them to your destinations. You can also create your own [Transformation Libraries](<https://www.rudderstack.com/docs/transformations/libraries/>) to reuse code in other transformations.

## Unify

This section highlights the following RudderStack features to unify your data.

### Profiles

[Profiles](<https://www.rudderstack.com/docs/profiles/overview/>) let you centralize and resolve customer identities and build features on top of it to create a customer 360 view.

## Activate

This section highlights the following RudderStack features to activate your data for a variety of use cases.

### Audiences

[Audiences](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/audiences/>) lets you create customer sets that meet a specific criteria and sync them to the destinations connected to your Reverse ETL sources. This is helpful when you want to send targeted messaging to different customer groups.

### Models

[Models](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/models/>) lets you define and execute custom SQL queries on your warehouse, fetch the resultant data, and send it specific destinations via RudderStack.

## Govern

This section provides various data governance options related to data quality and compliance.

### Data Catalog

[Data Catalog](<https://www.rudderstack.com/docs/data-governance/data-catalog/>) lets you create events and properties for configuring tracking plans. You can use this option to define all the necessary details for your events and properties like name, type, description, category, etc.

### Tracking Plans

[Tracking plans](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>) let you proactively monitor and act on non-compliant event data coming into your RudderStack sources based on predefined plans. You can ensure data quality by validating live events delivered to RudderStack against the expected events and their properties.

## Monitor

The options in this section let you monitor your warehouse syncs and get better observability into the events flowing in and out of RudderStack.

### Health

RudderStack’s [Health dashboard](<https://www.rudderstack.com/docs/data-governance/health-dashboard/>) lets you monitor all your Event Stream and Reverse ETL pipelines. It also provides realtime observability metrics for the tracking plans linked to your sources, including validation errors, violation types, etc.

### Syncs

This option provides detailed metrics on the events synced to your warehouse destinations. You can also filter the event data based on a specific source or destination by using the filter option in the header or sync the data manually by using the **Sync Now** button.

[![RudderStack Syncs](/docs/images/rs-cloud/syncs-dashboard.webp)](</docs/images/rs-cloud/syncs-dashboard.webp>)

### Grafana

> ![info](/docs/images/info.svg)
> 
> Grafana dashboards are available in the RudderStack [Starter, Growth, and Enterprise](<https://rudderstack.com/pricing>) plans.

The [Grafana dashboard](<https://www.rudderstack.com/docs/user-guides/administrators-guide/rudderstack-grafana-dashboard/>) gives you a real-time view of the events sent and received by RudderStack. It provides better observability and performance monitoring of your RudderStack setup.

Note that only [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) in your workspace can access the Grafana dashboard.

## Settings

This option lets you manage various account, workspace, and organization-specific settings.

### Your Profile

This section lists the various profile-specific settings related to your account.

#### Access policy

This section gives you an overview of your organization access role and the workspace-level roles and permissions assigned to you.

See [Access Management](<https://www.rudderstack.com/docs/access-management/overview/>) to set and manage these access policies for your organization members.

#### Security

This section lets you review and update your security settings like:

  * Changing the RudderStack account password
  * Setting up two-factor (2FA) authentication for your personal account


> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * If you are an [Admin](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) and want to enforce 2FA for all the organization members, use the **Require 2FA** toggle in the Organization settings.
>   * Org Admins **cannot** update an individual user’s 2FA settings.
> 


[![2FA authentication for the user profile](/docs/images/access-management/dashboard-guides/security.webp)](</docs/images/access-management/dashboard-guides/security.webp>)

#### Personal Access Tokens

You can generate a [Personal Access Token](<https://www.rudderstack.com/docs/access-management/personal-access-tokens/>) to use the RudderStack APIs for testing and development purposes.

### Workspace

This section lists the various workspace-specific settings.

#### General

This section displays your workspace information like name and workspace ID. The RudderStack team uses this ID for tracking data internally and enabling specific features for your account.

#### Workspace token

> ![info](/docs/images/info.svg)
> 
> The workspace token is available only in the [Free](<https://www.rudderstack.com/pricing/>) and [Open Source](<https://app.rudderstack.com/signup?type=opensource>) plans to help you set up a self-hosted deployment.

The workspace token is a unique identifier of your RudderStack workspace.

To get your workspace token, go to **Settings** > **Workspace**. The workspace token is present in the **General** tab.

[![Workspace Token](/docs/images/rs-cloud/workspace-token.webp)](</docs/images/rs-cloud/workspace-token.webp>)

To view the workspace token, click the show icon and enter the password associated with your RudderStack account.

> ![warning](/docs/images/warning.svg)
> 
> By default, the workspace token is hidden for security purposes — only [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) can access the workspace token.

#### Data management

This section lets you configure the data retention and data privacy settings for your workspace.

See [Data management](<https://www.rudderstack.com/docs/dashboard-guides/data-management/>) to learn more about this feature.

#### Audit Logs

> ![info](/docs/images/info.svg)
> 
> Audit Logs are available only in the RudderStack [Enterprise](<https://www.rudderstack.com/enterprise-quote/>) plan.

The [Audit Logs](<https://www.rudderstack.com/docs/dashboard-guides/audit-logs/>) feature lets you track user activities within your workspace, like creating or modifying sources and destinations, transformations, implementing Multi-Factor Authentication (MFA), and more.

#### Alerts

The **Alerts** tab lets you [configure workspace-level alerts](<https://www.rudderstack.com/docs/data-governance/alerts/>) for event processing or delivery failures across your Event Stream and Reverse ETL pipelines.

#### Credentials

> ![info](/docs/images/info.svg)
> 
> The Credential Store feature is available only in RudderStack [Starter, Growth, and Enterprise](<https://www.rudderstack.com/pricing/>) plans.

[Credential Store](<https://www.rudderstack.com/docs/transformations/credentials/>) is a central repository in the RudderStack dashboard for securely storing and efficiently managing your configuration data like user secrets and API keys.

By storing secrets and variables in the credential store, you can avoid hardcoding sensitive information in your [Transformations](<https://www.rudderstack.com/docs/transformations/overview/>) and prevent any security risks.

### Organization

This section lists the various organization-specific settings.

#### General

The **General** tab lets you change your organization name and enforce two-factor authentication for **all** members in your RudderStack organization.

You can also view the **Organization ID** in this tab.

[![Organization settings](/docs/images/access-management/dashboard-guides/organization-settings.webp)](</docs/images/access-management/dashboard-guides/organization-settings.webp>)

##### Require 2FA toggle

The **Require 2FA** toggle is an organization-level setting that mandates all the organization members to have multi-factor authentication (MFA) enabled to log in to their RudderStack account.

[![Organization 2FA settings](/docs/images/access-management/dashboard-guides/organization-2fa.webp)](</docs/images/access-management/dashboard-guides/organization-2fa.webp>)

> ![info](/docs/images/info.svg)
> 
> When the **Require 2FA** setting is toggled on, RudderStack enforces all users to set up MFA during the login process. It does not affect users who already have MFA configured.

Note that:

  * The **Require 2FA** setting is different from the individual user’s 2FA settings. It only mandates MFA setup during login — it does not disable or modify the existing user-level MFA settings configured in the Your Profile section.
  * If a user belongs to multiple organizations and at least one organization has the **Require 2FA** toggle enabled, the user will be required to set up and use MFA as long as they are a member of that organization.


#### Usage

In this section, you can view your organization’s event usage by product (Event Stream and Reverse ETL). It also indicates your current RudderStack plan and when your billing cycle resets.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack calculates the monthly event volume based on the events ingested at source and **not** the events sent to the destinations.
> 
> Filtering selective events to destinations using [Transformations](<https://www.rudderstack.com/docs/transformations/overview/>) will not result in a lower event volume.

### Access Management

RudderStack’s [Access Management](<https://www.rudderstack.com/docs/access-management/overview/>) system lets you control access by configuring policies for workspaces, groups, members and Service Access Tokens.

#### Base Workspace Policies

The **Base Workspace Policies** tab lets you configure the baseline policy applicable to each workspace in your RudderStack organization.

All the groups, members, and [Service Access Tokens](<https://www.rudderstack.com/docs/access-management/service-access-tokens/>) in that workspace automatically inherit this baseline policy.

See [Manage Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>) for more information.

#### Groups

The **Groups** tab lets you create groups, configure a group policy for each workspace, and add members to groups. All group members automatically inherit this workspace policy.

See [Manage Group Policies](<https://www.rudderstack.com/docs/access-management/groups/>) for more information.

#### Users

The **Users** tab lets you:

  * View member details, upgrade or downgrade their organization role, or remove them from the organization
  * Customize a member’s workspace policy
  * Manage group membership


See [Manage Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>) for more information.

#### Invitations

Use the **Invitations** tab to invite new members to your organization’s workspaces.

See [Member Management](<https://www.rudderstack.com/docs/access-management/member-management/>) for more information.

#### Service Access Tokens

Use the **Service Access Tokens** tab to generate and manage Service Access Tokens.

A [Service Access Token (SAT)](<https://www.rudderstack.com/docs/access-management/service-access-tokens/>) enables applications access to RudderStack APIs, providing a flexible, secure, and centralized way for you to programmatically interact with resources and services in the platform.

> ![info](/docs/images/info.svg)
> 
> For production use cases, RudderStack recommends using a Service Access Token instead of [Personal Access Token](<https://www.rudderstack.com/docs/access-management/personal-access-tokens/>).