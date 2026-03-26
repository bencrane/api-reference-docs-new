# Workspaces

Switch between multiple workspaces in your RudderStack organization.

Available Plans

  * starter
  * growth
  * enterprise


* * *

  *  __4 minute read

  * 


RudderStack’s **Workspaces** feature lets you switch between multiple environments within a RudderStack organization. It provides a clean user experience with organization-level clarity on billing and usage.

## Organization and workspace hierarchy

This section defines an organization and workspace in RudderStack.

### Organization

When you [sign up for RudderStack](<https://app.rudderstack.com/signup>), your email is associated with a top-level user account, also referred to as an **organization**.

> ![info](/docs/images/info.svg)
> 
> RudderStack calculates billing and events usage at an organization level.

To view the organization details and manage its settings, go to **Settings** > **Organization** in your RudderStack dashboard.

[![Organization settings](/docs/images/access-management/dashboard-guides/organization-settings.webp)](</docs/images/access-management/dashboard-guides/organization-settings.webp>)

If your email is associated with multiple RudderStack organizations, you will see multiple organizations along with the number of workspaces in it once you log in:

[![Select organization view](/docs/images/dashboard-guides/workspaces/select-organization.webp)](</docs/images/dashboard-guides/workspaces/select-organization.webp>)

You can select your preferred organization. To switch to a different organization and view the associated workspaces, click the **Switch organization** button:

[![Switch organization](/docs/images/dashboard-guides/workspaces/switch-organization.webp)](</docs/images/dashboard-guides/workspaces/switch-organization.webp>)

### Workspaces

A **workspace** is an environment or nested grouping of resources and related settings. It is walled from other workspaces and you can use it for your development and production use-cases. See Workspace types for more information.

> ![info](/docs/images/info.svg)
> 
> Depending on your RudderStack plan, your organization can have multiple workspaces. See Available workspaces by plan for more information.

To view the workspace details and manage its settings, go to **Settings** > **Workspace** in your RudderStack dashboard.

[![Workspace in RudderStack](/docs/images/dashboard-guides/workspaces/workspace.webp)](</docs/images/dashboard-guides/workspaces/workspace.webp>)

You will see the following tabs in this view:

#### General

Option| Description  
---|---  
Workspace name| Name of the workspace — click the **Edit** icon to update the workspace name  
Environment| Workspace type (Dev/Prod) — see Workspace types for more information  
Workspace ID| Unique identifier for the workspace — click to copy the ID to the clipboard  
  
#### Data Management

Option| Description  
---|---  
Data retention| Configure the [data retention strategy](<https://www.rudderstack.com/docs/dashboard-guides/data-management/>) for your workspace  
Sample event data| Opt in to store and delete sample events and responses on a rolling 30-day basis  
Data governance| Enable the [Event Audit API](<https://www.rudderstack.com/docs/api/event-audit-api/>) to get detailed metadata about events flowing through RudderStack to help with diagnostics and troubleshooting  
  
These events are also available for import, streamlining the process of creating and managing your [Tracking Plans](<https://www.rudderstack.com/docs/data-governance/tracking-plans/create-tracking-plans/#pull-from-source>)  
  
#### Audit Logs

The **Audit Logs** tab lets you track user activities within the workspace.

See the [Audit Logs](<https://www.rudderstack.com/docs/dashboard-guides/audit-logs/>) guide for more information.

#### Alerts

The **Alerts** tab lets you set workspace and source-level alerts for your Event Stream sources and destinations.

See the [Alerts](<https://www.rudderstack.com/docs/data-governance/alerts/>) guide for more information.

#### Credentials

The **Credentials** tab lets you store configuration data like secrets and variables and use them in your transformations.

See the [Credentials](<https://www.rudderstack.com/docs/transformations/credentials/>) guide for more information.

## Workspace types

RudderStack provides the following workspace types:

  * **Production** : In this workspace, you can set up stable and optimized data pipelines made available to your customers and end-users.
  * **Development** : In this workspace, you can set up, test, and debug your data pipelines for optimal performance without affecting your end-users. You can also experiment with various RudderStack features.


See Available workspaces by plan for more information on the number of workspaces you can set up based on your RudderStack plan.

#### Key differences between the Development and Production workspaces in RudderStack

  * Users can have different resource permissions in the **Development** and **Production** workspaces. For example, a user might have the permissions to create and delete a source in the Development workspace but not in the Production workspace.
  * The Development workspace users will not be able to push sources, destinations, and pipeline configurations into the Production workspace and vice versa.
  * The Development workspace exists on a slightly different infrastructure to the Production workspace. There could be slightly longer processing times for features like [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/>) as compared to the Production workspace, which runs in a dedicated environment for the users.


## Add members to a workspace

You can add members to a workspace while [inviting them](<https://www.rudderstack.com/docs/access-management/member-management/#invite-new-members>) to your organization.

> ![info](/docs/images/info.svg)
> 
> If you are on the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), the steps for adding members to a workspace vary slightly:
> 
>   * **Org Admins** get added to all the workspaces in the organization by default.
>   * **Org Members** get added to the workspaces they are invited to.
> 

> 
> See the [User Management](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#invite-users>) guide for more information.

## Switch workspaces

To switch between workspaces, click **Workspace** > **Switch workspace**. Then, select the workspace you want to view.

[![Switch workspace](/docs/images/dashboard-guides/workspaces/switch-workspace.webp)](</docs/images/dashboard-guides/workspaces/switch-workspace.webp>)

## Access control

The owner of the RudderStack account is assigned the role of an **Admin** by default. They can invite other members as **Admins** or **Members**.

> ![warning](/docs/images/warning.svg)
> 
> **Important consideration while inviting users**
> 
> If you [invite a user](<https://www.rudderstack.com/docs/access-management/member-management/#invite-new-members>) to your organization as **Admin** , they will have admin permissions for all the workspaces within the organization that you add them to.

## Available workspaces by plan

RudderStack plan| Number of workspaces| Availability  
---|---|---  
Free| 1 (Production)| Available by default  
Starter| 2 (1 Production, 1 Development)| Available by default  
Growth| 2 (1 Production, 1 Development)| Available by default  
Enterprise| Custom| Contact the [RudderStack team](<mailto:support@rudderstack.com>) to set up workspaces based on your contract