# How Migration to New Access Management System Works

Learn how RudderStack maps existing workspace roles and permissions to the new Access Management system.

Available Plans

  * starter
  * growth
  * enterprise


* * *

  *  __5 minute read

  * 


> ![announcement](/docs/images/announcement.svg)
> 
> **Self-serve migration availability**
> 
> The self-serve migration feature for users on the [legacy RBAC system](<https://www.rudderstack.com/docs/access-management/glossary/#role-based-access-control-rbac>) is currently gated and will be generally available on **March 16, 2026**.
> 
> Contact your [Customer Success Manager](<mailto:support@rudderstack.com>) if you’d like to enable it for your organization in the meantime.

This guide explains how RudderStack transitions the members, [Service Access Tokens](<https://www.rudderstack.com/docs/access-management/service-access-tokens/>), and [Personal Access Tokens](<https://www.rudderstack.com/docs/access-management/personal-access-tokens/>) within your workspace to the new [Access Management system](<https://www.rudderstack.com/docs/access-management/overview/>) once you [migrate to it](<https://www.rudderstack.com/docs/access-management/migration-steps/>).

## Migration overview

During migration, RudderStack considers your [import strategy](<https://www.rudderstack.com/docs/access-management/pre-migration-considerations/#import-strategy-decision>) and maps permissions accordingly.

  * If you choose **Import members** , RudderStack imports all members to the new Access Management system with baseline, view-only permissions instead of their existing permissions.
  * If you choose **Import members with policies** , RudderStack imports all members to the new Access Management system with their existing permissions, ensuring each member’s [effective access policy](<https://www.rudderstack.com/docs/access-management/concepts/#access-policy>) has the same permissions as before.


Service Access Tokens are migrated with their existing permissions, while Personal Access Tokens continue to inherit permissions from their associated users.

## Members

When you migrate members using the **Import members with policies** [import strategy](<https://www.rudderstack.com/docs/access-management/pre-migration-considerations/#import-strategy-decision>), RudderStack performs the following assessment:

  * **Analyzes current permissions** : RudderStack reviews each user’s assigned roles and permissions in the legacy Permissions Management (RBAC) system — this includes their [role-level](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#resource-roles>) and [resource-level](<https://www.rudderstack.com/docs/archive/dashboard-guides/permissions-management/#restricting-edit-permissions-for-individual-objects>) permissions.
  * **Maps roles to policies** : The permissions a user had in the legacy RBAC system are mapped to their individual [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>).


For example, if a user had the **Connections Admin** role with permissions to create, edit, connect, and disconnect resources, these permissions will be preserved in their [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>) after migration.

## Service Access Tokens

> ![info](/docs/images/info.svg)
> 
> Service Access Tokens are automatically imported with their current permissions regardless of the [import strategy](<https://www.rudderstack.com/docs/access-management/pre-migration-considerations/#import-strategy-decision>).
> 
> See the [Migration Scenarios](<https://www.rudderstack.com/docs/access-management/migration-examples/>) guide for detailed examples of how Service Access Tokens are migrated.

Service Access Tokens created in the [legacy RBAC system](<https://www.rudderstack.com/docs/archive/dashboard-guides/service-access-tokens/#generate-service-access-token>) are automatically imported during migration and follow the same migration patterns as members.

During migration, RudderStack:

  * **Analyzes Service Access Token permissions** : RudderStack reviews each Service Access Token’s assigned roles and permissions in the legacy RBAC system — this includes their [role-level](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#resource-roles>) and [resource-level](<https://www.rudderstack.com/docs/archive/dashboard-guides/permissions-management/#restricting-edit-permissions-for-individual-objects>) permissions.
  * **Maps roles to workspace policies** : The token’s permissions in the legacy RBAC system are mapped to its workspace-level access policy in the new Access Management system.


For example, if a Service Access Token had the **Connections Admin** role with permissions to create, edit, connect, and disconnect resources, these permissions will be preserved in its workspace policy after migration.

See the [Migration Scenarios](<https://www.rudderstack.com/docs/access-management/migration-examples/>) guide for more information on how Service Access Tokens are migrated.

## Personal Access Tokens

> ![info](/docs/images/info.svg)
> 
> [Personal Access Tokens](<https://www.rudderstack.com/docs/access-management/personal-access-tokens/>) are tied to individual users — they inherit permissions of the user who created them.

After migration, Personal Access Tokens:

  * **Inherit user permissions** : Personal Access Tokens continue to inherit the permissions of the user who created them. Since user permissions are migrated to their [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>), Personal Access Tokens automatically reflect those permissions.
  * **Maintain scope behavior** : Personal Access Tokens created with **Read-Only** or **Read-Write** scopes continue to work as before, with their effective permissions determined by the user’s [Individual Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>).


See the [Migration Scenarios](<https://www.rudderstack.com/docs/access-management/migration-examples/personal-access-tokens/>) guide for detailed examples of how Personal Access Tokens are migrated.

Note the following:

  * To change a Personal Access Token’s permissions after migration, you will have to either:

    * Modify the user’s [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>)
    * Create a new Personal Access Token with the desired scope
  * **You cannot create new Personal Access Tokens with Admin scope**. However, any existing Personal Access Tokens with Admin scope will continue to work as before, even after migration.


> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Use Personal Access Tokens only for development, testing, and personal use cases.

## Resource-level permissions

> ![info](/docs/images/info.svg)
> 
> **What are resource-level permissions?**
> 
> [Resource-level permissions](<https://www.rudderstack.com/docs/archive/dashboard-guides/permissions-management/#restricting-edit-permissions-for-individual-objects>) allow Admins to restrict editing particular resources to specific users or Service Access Tokens. Admins can configure an allowlist of members and tokens who can edit a resource.

During the assessment, RudderStack considers whether [resource-level permissions](<https://www.rudderstack.com/docs/archive/dashboard-guides/permissions-management/#restricting-edit-permissions-for-individual-objects>) are configured for users and Service Access Tokens in the workspace.

If resource-level permissions are configured, RudderStack automatically configures the user’s individual [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>) and the Service Access Token’s [workspace policy](<https://www.rudderstack.com/docs/access-management/concepts/#workspace-policy>) to have the same permissions as before during migration.

For example, if a user had edit permissions for only 10 out of the 100 sources in the workspace, their [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>) will reflect [**Edit** permission](<https://www.rudderstack.com/docs/access-management/policies-overview/#edit-connect-and-create--delete-permissions>) only for those 10 sources after migration.

See the [Migration Scenarios](<https://www.rudderstack.com/docs/access-management/migration-examples/>) guide for more information on how migration works in different scenarios.

## Staging area

The migration process uses a staging area where you can configure and preview permissions policies before deploying them. This lets you:

  * Review how your current permissions map to the new system
  * Make changes to policies without affecting your current permissions


> ![info](/docs/images/info.svg)
> 
> Your existing permissions remain active until you deploy the new system from the staging area.

## What happens after migration

After migration, members and access tokens in your workspace will experience the following changes:

  * **Admins** : [Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) in the legacy RBAC system will continue to have the same level of access.
  * **Members** : Members in the legacy RBAC system will have their permissions mapped to their individual [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>).
  * **Service Access Tokens** : Service Access Tokens will have their permissions mapped to workspace-level access policies, maintaining the same access levels they had before migration.
  * **Personal Access Tokens** : Personal Access Tokens continue to inherit the permissions of their associated users, now defined by the user’s [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>).
  * **Interface** : Admins will be able to manage permissions through the new Access Management interface, which includes an intuitive policy editor to manage the [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>), [Group Workspace Policies](<https://www.rudderstack.com/docs/access-management/groups/>), and [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>).
  * **New users** : New members added to the workspace after migration will inherit the [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>) by default.
  * **Baseline Workspace Policy** : If you selected the [**Import** option](<https://www.rudderstack.com/docs/access-management/pre-migration-considerations/#import-strategy-decision>) during migration, the [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>) will be set to **view-only** for resources and **restricted access to all PII views** by default, providing Admins with a blank slate to configure workspace permissions from scratch.


## See more

  * [Migration Steps](<https://www.rudderstack.com/docs/access-management/migration-steps/>): Step-by-step instructions for performing migration to the new Access Management system
  * [Migration Scenarios](<https://www.rudderstack.com/docs/access-management/migration-examples/>): Understand how Access Management migration works in different scenarios