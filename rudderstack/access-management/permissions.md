# Feature-wise Permissions

Understand the permissions required to use different RudderStack features in the new Access Management system.

* * *

  * __10 minute read

  * 


This guide provides a comprehensive reference of the permissions required to use different RudderStack features in the new Access Management system.

It also lists the permissions required to use the same features in the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>) for comparison.

## APIs

> ![info](/docs/images/info.svg)
> 
> To consume APIs, you require a [Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/>) with specific permissions.

### Audit Logs API

  * **Access Management system** : Organization-level Service Access Token
  * **Legacy RBAC system** : Organization-level Service Access Token


See [Audit Logs API](<https://www.rudderstack.com/docs/api/audit-logs-api/#prerequisites>) for more details.

### Data Catalog API

  * **Access Management system** : Workspace-level Service Access Token with the following permissions:

Resource| Permissions  
---|---  
Tracking Plans| **Create & Delete**, **Edit**  
Data Catalog| **Edit**  
  
  * **Legacy RBAC system** : Workspace-level Service Access Token with **Admin** permissions


See [Data Catalog API](<https://www.rudderstack.com/docs/api/data-catalog-api/tracking-plans/>) for more details.

### Event Audit API

  * **Access Management system** : Workspace-level Service Access Token with **no** dedicated permissions
  * **Legacy RBAC system** : Workspace-level Service Access Token with **Viewer** permissions


See [Event Audit API](<https://www.rudderstack.com/docs/api/event-audit-api/>) for more details.

### HTTP API

No dedicated permissions are required to consume the HTTP API — it uses your [source write key](<https://www.rudderstack.com/docs/api/http-api/#prerequisites>) for authentication.

### Pixel API

No dedicated permissions are required to consume the Pixel API — it uses your [source write key](<https://www.rudderstack.com/docs/api/pixel-api/#prerequisites>) for authentication.

### Profiles API

  * **Access Management system** : Workspace-level Service Access Token with the following permissions:

Resource| Permissions  
---|---  
Profiles| **Edit**  
  
  * **Legacy RBAC system** : Workspace-level Service Access Token with **Editor** permissions


See [Profiles API](<https://www.rudderstack.com/docs/api/profiles-api/#prerequisites>) for more details.

### Reverse ETL Connections API

  * **Access Management system** : Workspace-level Service Access Token with the following permissions:

Resource| Permissions  
---|---  
Tables / SQL Models / Audiences| **Edit** , **Connect**  
Destinations| **Edit** , **Connect**  
PII permissions  
Enterprise plan only| **Reverse ETL Sync Failure Samples** configured for the required source  
  
  * **Legacy RBAC system** : Workspace-level Service Access Token with **Admin** permissions


See [Reverse ETL Connections API](<https://www.rudderstack.com/docs/api/retl-connections-api/#prerequisites>) for more details.

### Test API

  * **Access Management system** : Workspace-level Service Access Token with **no** dedicated permissions
  * **Legacy RBAC system** : Workspace-level Service Access Token with **Viewer** permissions


See [Test API](<https://www.rudderstack.com/docs/api/test-api/#prerequisites>) for more details.

### Transformations API

  * **Access Management system** : Workspace-level Service Access Token with the following permissions:

Resource| Permissions  
---|---  
Transformations| **Create & Delete**, **Connect** , **Edit**  
Transformation Libraries| **Edit**  
Destinations| **Connect**  
  
  * **Legacy RBAC system** : Workspace-level Service Access Token with **Admin** permissions with **Grant edit access** toggled on under **Transformations**.

[![workspace-level Service Access Token with Transformations Admin permission](/docs/images/access-management/permissions/legacy/admin-transformations.webp)](</docs/images/access-management/permissions/legacy/admin-transformations.webp>)

See [Transformations API](<https://www.rudderstack.com/docs/api/transformation-api/#prerequisites>) for more details.

### User Suppression API

  * **Access Management system** : Workspace-level Service Access Token with **no** dedicated permissions
  * **Legacy RBAC system** : Workspace-level Service Access Token with **Viewer** permissions


See [User Suppression API](<https://www.rudderstack.com/docs/api/user-suppression-api/#prerequisites>) for more details.

## AI Features

> ![info](/docs/images/info.svg)
> 
> To use these features, you require a [Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/>) with specific permissions.

### Rudder AI Reviewer

  * **Access Management system** : Workspace-level Service Access Token with **no** dedicated permissions
  * **Legacy RBAC system** : Workspace-level Service Access Token with **Viewer** permissions


See [Rudder AI Reviewer](<https://www.rudderstack.com/docs/ai-features/rudder-ai-reviewer/get-started/#prerequisites>) for more details.

## CLI and Dev Tools

> ![info](/docs/images/info.svg)
> 
> To use these tools, you require a [Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/>) with specific permissions.

### RudderTyper

  * **Access Management system** : Workspace-level Service Access Token with **no** dedicated permissions
  * **Legacy RBAC system** : Workspace-level Service Access Token with **Viewer** permissions


See [RudderTyper](<https://www.rudderstack.com/docs/dev-tools/ruddertyper/#prerequisites>) for more details.

### Rudder CLI

> ![info](/docs/images/info.svg)
> 
> To use Rudder CLI, you require a [Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/>) with specific permissions to manage the resources you want to manage.

#### Tracking Plans and Data Catalog

  * **Access Management system** : Workspace-level Service Access Token with the following permissions:

Resource| Permissions  
---|---  
Tracking Plans| **Create & Delete**, **Edit**  
Data Catalog| **Edit**  
  
  * **Legacy RBAC system** : Workspace-level Service Access Token with **Admin** permissions


See [CLI-based Tracking Plans and Data Catalog Management](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/quickstart/#prerequisites>) for more details.

#### Event Stream Sources

  * **Access Management system** : Workspace-level Service Access Token with the following permissions:

Resource| Permissions| Description  
---|---|---  
Event Stream Sources| **Create & Delete**| Create or delete Event Stream sources in the workspace  
Event Stream Sources| **Edit**|  Make changes to the configuration of Event Stream sources  
Event Stream Sources| **Connect**|  Connect an Event Stream source to a Tracking Plan  
Tracking Plans| **Edit** , **Connect**|  Connect a Tracking Plan to an Event Stream source  
  
  * **Legacy RBAC system** : Workspace-level Service Access Token with **Admin** permissions


See [Manage Event Stream Sources using Rudder CLI](<https://www.rudderstack.com/docs/sources/event-streams/sdks/manage-sources-with-rudder-cli/quickstart/#prerequisites>) for more details.

#### SQL Models

  * **Access Management system** : Workspace-level Service Access Token with the following permissions:

Resource| Permissions  
---|---  
SQL Models| **Create & Delete**, **Edit**  
  
  * **Legacy RBAC system** : Workspace-level Service Access Token with **Admin** permissions


See [Manage SQL Models using Rudder CLI](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/create-new-resource/#prerequisites>) for more details.

#### Transformations and Transformation Libraries

  * **Access Management system** : Workspace-level Service Access Token with the following permissions:

Resource| Permissions  
---|---  
Transformations| **Create & Delete**, **Edit** , **Connect**  
Transformation Libraries| **Edit**  
  
  * **Legacy RBAC system** : Workspace-level Service Access Token with **Admin** role and **Grant edit access** toggled on under **Transformations**


See [Manage Transformations and Transformation Libraries using Rudder CLI](<https://www.rudderstack.com/docs/transformations/manage-transformations-with-rudder-cli/quickstart/#prerequisites>) for more details.

## Data Governance

This section lists the permissions required to use different Data Governance features in the new Access Management system.

### Tracking Plans

  * **Access Management system** :

    * [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have full access to create and manage tracking plans
    * Members must have the following permissions:

Resource| Permissions  
---|---  
Tracking Plans| **Create & Delete**, **Edit** , **Connect**  
Data Catalog| **Edit**  
  
  * **Legacy RBAC system** :

    * [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) have full access to create and manage Tracking Plans
    * Members with the **Connections Admin** role in their workspace policy can create and manage Tracking Plans
    * Members with the **Connections Editor** role in their workspace policy can only connect Tracking Plans to Event Stream sources


See the [Tracking Plans documentation](<https://www.rudderstack.com/docs/data-governance/tracking-plans/create-tracking-plans/#required-permissions>) for more details.

### Data Catalog

  * **Access Management system** :

    * [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have full access to manage Data Catalog
    * Members must have the following permissions:

Resource| Permissions  
---|---  
Data Catalog| **Edit**  
  
  * **Legacy RBAC system** :

    * [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) have full access to manage Data Catalog
    * Members must have the **Connections Admin** role in their workspace policy


See the [Data Catalog documentation](<https://www.rudderstack.com/docs/data-governance/data-catalog/properties/#required-permissions>) for more details.

### Bot Management

  * **Access Management system** :

    * [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have full access to the Bot Management feature
    * Members must have the **Bot Management** permission
  * **Legacy RBAC system** :

    * [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) have full access to the Bot Management feature
    * Members must have the **Connections Admin** role in their workspace policy


See the [Bot Management documentation](<https://www.rudderstack.com/docs/data-governance/bot-management/#required-permissions>) for more details.

### Event Blocking

  * **Access Management system** : Only [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) can manage event blocking
  * **Legacy RBAC system** : Only [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) can manage event blocking


See [Event Blocking](<https://www.rudderstack.com/docs/data-governance/event-blocking/#enable-event-blocking>) for more details.

### Alerts

  * **Access Management system** :

    * Only [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) can set up workspace-level alerts
    * [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) and Members with the **Alert Overrides** permission can set up resource-level alerts
  * **Legacy RBAC system** :

    * Only [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) can set up workspace-level alerts
    * [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) and members with the **Connections Admin** role in their workspace policy can set up resource-level alerts


See [Configurable Alerts](<https://www.rudderstack.com/docs/data-governance/alerts/#required-permissions>) for more details.

## Data Pipelines

This section lists the permissions required to manage data pipelines and their associated resources.

### Event Stream Sources

  * **Access Management system** :

    * [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have full access to create and manage event stream sources
    * Members can have the following permissions in their workspace policy:

Resource| Permissions  
---|---  
Event Stream Sources| **Edit** , **Connect** , **Create & Delete**  
  
  * **Legacy RBAC system** :

    * [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) have full access to create and manage Event Stream sources
    * Members with the **Connections Admin** role in their workspace policy can create and manage Event Stream sources
    * Members with the **Connections Editor** role in their workspace policy can only edit the Event Stream source configuration and connect Event Stream sources to destinations


See [Event Stream Sources](<https://www.rudderstack.com/docs/sources/event-streams/#required-permissions>) for more details.

### Reverse ETL Sources

  * **Access Management system** :

    * [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have full access to create and manage reverse ETL sources
    * Members can have the following permissions in their workspace policy:

Resource| Permissions  
---|---  
Tables / SQL Models / Audiences| **Edit** , **Connect** , **Create & Delete**  
  
  * **Legacy RBAC system** :

    * [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) have full access to create and manage reverse ETL sources
    * Members with the **Connections Admin** role in their workspace policy can create and manage reverse ETL sources
    * Members with the **Connections Editor** role in their workspace policy can only edit the reverse ETL source configuration and connect reverse ETL sources to destinations


See [Reverse ETL Sources](<https://www.rudderstack.com/docs/sources/reverse-etl/#required-permissions>) for more details.

### Destinations

  * **Access Management system** :

    * [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have full access to create and manage destinations
    * Members can have the following permissions in their workspace policy:

Resource| Permissions  
---|---  
Destinations| **Edit** , **Connect** , **Create & Delete**  
  
  * **Legacy RBAC system** :

    * [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) have full access to create and manage destinations
    * Members with the **Connections Admin** role in their workspace policy can create and manage destinations
    * Members with the **Connections Editor** role in their workspace policy can only edit the destination configuration and connect destinations to sources


See [Destinations](<https://www.rudderstack.com/docs/destinations/overview/#required-permissions>) for more details.

### Airflow Orchestrator

  * **Access Management system** : Workspace-level Service Access Token with the following permissions:

Resource| Permissions  
---|---  
Tables / SQL Models / Audiences| **Edit** , **Connect**  
Destinations| **Edit** , **Connect**  
Profiles| **Edit** , **Connect**  
  
  * **Legacy RBAC system** : Workspace-level Service Access Token with **Admin** permissions


See [RudderStack Airflow Integration](<https://www.rudderstack.com/docs/data-pipelines/orchestration/airflow/#prerequisites>) for more details.

### Dagster Orchestrator

  * **Access Management system** : Workspace-level Service Access Token with the following permissions:

Resource| Permissions  
---|---  
Tables / SQL Models / Audiences| **Edit** , **Connect**  
Destinations| **Edit** , **Connect**  
Profiles| **Edit** , **Connect**  
  
  * **Legacy RBAC system** : Workspace-level Service Access Token with **Admin** permissions


See [RudderStack Dagster Integration](<https://www.rudderstack.com/docs/data-pipelines/orchestration/dagster/#prerequisites>) for more details.

## Profiles

  * **Access Management system** :

    * [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have full access to create and manage Profiles projects
    * Members can have the following permissions in their workspace policy:

Resource| Permissions  
---|---  
Profiles| **Edit** , **Create & Delete**, **Connect**  
  
  * **Legacy RBAC system** :

    * [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) have full access to create and manage Profiles projects
    * Members with the **Connections Admin** role in their workspace policy can create and manage Profiles projects
    * Members with the **Connections Editor** role in their workspace policy can only edit the Profiles project configuration and connect Profiles projects to destinations


See [Profiles Quickstart](<https://www.rudderstack.com/docs/profiles/overview/quickstart/#required-permissions>) for more details.

### Activation API

  * **Access Management system** : Workspace-level Service Access Token with the following permissions:

Resource| Permissions  
---|---  
PII Permission| **Destination Data Access** for the specific Redis destination  
  
  * **Legacy RBAC system** : Workspace-level Service Access Token with **Admin** permissions


See [Activation API](<https://www.rudderstack.com/docs/profiles/dev-docs/activation-api/#prerequisites>) for more details.

### Profiles Audit

  * **Access Management system** : Workspace-level Service Access Token with **no** dedicated permissions
  * **Legacy RBAC system** : Workspace-level Service Access Token with **Viewer** permissions


See the [Profiles Audit documentation](<https://www.rudderstack.com/docs/profiles/dev-docs/profiles-audit/#prerequisites>) for more details.

## SSO and Audit Logs

This section lists the permissions required to use the Audit Logs and different SSO setups.

### Audit Logs

  * **Access Management system** : Only [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) can access the Audit Logs
  * **Legacy RBAC system** : Only [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) can access the Audit Logs


See [Audit Logs](<https://www.rudderstack.com/docs/dashboard-guides/audit-logs/>) for more details.

### Okta SSO (SCIM)

  * **Access Management system** : Organization-level Service Access Token
  * **Legacy RBAC system** : Organization-level Service Access Token


See [Okta SCIM Configuration](<https://www.rudderstack.com/docs/user-guides/sso-setup/okta/scim-configuration/#prerequisites>) for more details.

### Azure Entra ID SSO (SCIM)

  * **Access Management system** : Organization-level Service Access Token
  * **Legacy RBAC system** : Organization-level Service Access Token


See [Azure Entra ID SSO Setup](<https://www.rudderstack.com/docs/user-guides/sso-setup/azure/#prerequisites>) for more details.

## Transformations

  * **Access Management system** :

    * [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have full access to create and manage transformations
    * Members can have the following permissions in their workspace policy:

Resource| Permissions  
---|---  
Transformations| **Edit** , **Connect** , **Create & Delete**  
  
  * **Legacy RBAC system** :

    * Org Admins have full access
    * Members must have the **Grant edit access** permission in **Transformations and Library** toggled on to create, edit, and delete transformations
    * Members with the **Connections Admin** or **Connections Editor** role in their workspace policy can only connect transformations to destinations


See [Transformations](<https://www.rudderstack.com/docs/transformations/create/#required-permissions>) for more details.

### Libraries

  * **Access Management system** :

    * [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have full access to create and manage transformation libraries
    * Members must have the **Transformation Libraries** permission in their workspace policy
  * **Legacy RBAC system** :

    * Org Admins have full access
    * Members must have the **Grant edit access** permission in **Transformations and Library** toggled on to create, edit, and delete transformation libraries


See [Transformation Libraries](<https://www.rudderstack.com/docs/transformations/libraries/#required-permissions>) for more details.

### Credential Store

  * **Access Management system** :

    * [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have full access to the credential store
    * Members must have the **Credential Store** permission in their workspace policy
  * **Legacy RBAC system** :

    * [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) have full access to the credential store
    * Members must have the **Connections Admin** role in their workspace policy


See [Credential Store](<https://www.rudderstack.com/docs/transformations/credentials/#required-permissions>) for more details.

### Transformation Action

  * **Access Management system** : Workspace-level Service Access Token with the following permissions:

Resource| Permissions  
---|---  
Transformations| **Edit** , **Connect** , **Create & Delete**  
Transformation Libraries| **Edit**  
  
  * **Legacy RBAC system** : Workspace-level Service Access Token with **Admin** role and **Grant edit access** toggled on under **Transformations**


See [Transformation Action](<https://www.rudderstack.com/docs/transformations/transformation-action/#prerequisites>) for more details.