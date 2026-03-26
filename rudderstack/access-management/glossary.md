# Access Management Glossary

Understand key terms used in RudderStack’s Access Management system.

* * *

  * __3 minute read

  * 


This glossary alphabetically defines some commonly used terms in RudderStack’s **Access Management** system and documentation.

## Access policy

An [access policy](<https://www.rudderstack.com/docs/access-management/concepts/#access-policy>) acts as a container for one or more permissions. You can assign an access policy at the workspace, group, or member level.

## Access Token

Access tokens are used for programmatic access to RudderStack APIs. RudderStack supports two types of access tokens:

  * A [Personal Access Token (PAT)](<https://www.rudderstack.com/docs/access-management/personal-access-tokens/>) is tied to an individual user
  * A [Service Access Token (SAT)](<https://www.rudderstack.com/docs/access-management/service-access-tokens/>) is tied to a service account and its own permissions


## Admin

Admins have full administrative access across the RudderStack platform, including workspaces, members, the Access Management settings, billing and plan information, and more.

## Group

A group is a collection of members that share a policy per workspace. Groups allow Admins to create custom roles and share consistent access patterns without manual duplication.

## Member

A member is a user in RudderStack. A member’s [Access Policy](<https://www.rudderstack.com/docs/access-management/concepts/#access-policy>) determines what they can and cannot do in a given workspace.

## Member workspace policy

A member workspace policy is a bundle of permissions that apply only to a specific member. It is useful for fine-tuning access.

For example, you can grant **Edit** access for **Event Stream Sources** to a group of developers, but grant **Connect** permissions for **Event Stream Sources** only to that team’s manager through their individual member workspace policy.

## Organization roles

RudderStack’s Access Management system offers two roles within an organization:

  * **Member** : Users with configurable workspace access and policies.
  * **Admin** : Platform administrators with full admin access across all workspaces, including the ability to manage members


See [Member Management](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) for more information.

## Permission

[Permissions](<https://www.rudderstack.com/docs/access-management/concepts/#permission>) represent specific actions that a user can take and are the building blocks for policies.

### Edit

The **Edit** permission lets a user change the configuration of an existing resource.

For example, a member granted **Edit** permission on a specific destination can change its configuration settings in the dashboard.

### Connect

The **Connect** permission grants the ability to connect one resource to another. For example, connecting an Event Stream source to a destination, a transformation to a destination, etc.

> ![info](/docs/images/info.svg)
> 
> To make a connection, that is, build a data pipeline, a member must have both **Edit** and **Connect** permissions on both resources.

### Create & Delete

The **Create & Delete** permission lets a user create new resources or delete existing resources for a specific resource type.

For example, a member granted **Create & Delete** permission for **Event Stream Sources** can add or delete Event Stream sources.

## PII permissions

> ![announcement](/docs/images/announcement.svg)
> 
> The ability to configure PII permissions is available only in RudderStack’s [Enterprise](<https://www.rudderstack.com/enterprise-quote/>) plan.

The **PII permissions** control whether a user can access views or APIs that expose Personally Identifiable Information (PII) in payloads.

## Policy-based Access Control (PBAC)

RudderStack’s Access Management system is based on **Policy-based Access Control (PBAC)** , which lets Admins define granular permissions for resources and actions and assign them to users directly via an access policy.

See [Key Concepts](<https://www.rudderstack.com/docs/access-management/concepts/#policy-based-access-control-pbac>) for more details.

## Resource

A configurable unit within RudderStack, for example:

  * **Event Stream Sources**
  * **Destinations**
  * **Transformations**
  * **Tracking Plans**
  * **Data Catalog**


Resources are permission-scoped and governed through policies.

## Role-based Access Control (RBAC)

RudderStack’s [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#role-permissions>) assigned broad, predefined roles to users rather than granular, per-resource permissions.

> ![warning](/docs/images/warning.svg)
> 
> The legacy RBAC system is deprecated and replaced by the Access Management (PBAC) system, which offers enhanced security, granular control, and compliance capabilities.
> 
> See the [Migration Guide](<https://www.rudderstack.com/docs/access-management/migration-steps/>) guide to transition to the new system.

## Workspace

A workspace is an isolated environment (for example, **Prod** or **Dev**) where access policies and resources are scoped independently.