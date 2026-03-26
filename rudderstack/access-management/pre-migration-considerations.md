# Pre-migration Considerations

Understand what to expect before migrating to the new Access Management system.

Available Plans

  * starter
  * growth
  * enterprise


* * *

  *  __3 minute read

  * 


> ![announcement](/docs/images/announcement.svg)
> 
> **Self-serve migration availability**
> 
> The self-serve migration feature for users on the [legacy RBAC system](<https://www.rudderstack.com/docs/access-management/glossary/#role-based-access-control-rbac>) is currently gated and will be generally available on **March 16, 2026**.
> 
> Contact your [Customer Success Manager](<mailto:support@rudderstack.com>) if you’d like to enable it for your organization in the meantime.

Before you begin migration to the new [Access Management system](<https://www.rudderstack.com/docs/access-management/overview/>), it is important to understand how your current permissions will map to the new system and what changes to expect. This will help you make informed decisions during the migration process, particularly when choosing your import strategy.

## Migration scope

Migration to the new Access Management system happens at the **organization level** , not at the workspace level. This means:

  * When you migrate, the migration applies to **all workspaces** within your organization
  * You cannot migrate individual workspaces separately
  * All members and [Service Access Tokens](<https://www.rudderstack.com/docs/access-management/service-access-tokens/>) in all workspaces in your organization are migrated to the new Access Management system together


> ![warning](/docs/images/warning.svg)
> 
> If your organization has multiple workspaces, make sure to check and fine-tune each workspace’s [baseline policy](<https://www.rudderstack.com/docs/access-management/migration-steps/#step-2-configure-policies>) before deploying the new Access Management system.

## Roles to member permissions

After migration, the permissions a user had in the legacy Permissions Management (RBAC) system (**Viewer** , **Connections Editor** , **Connections Admin** , etc.) will be mapped to their individual [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>).

This means that instead of assigning specific roles to members, each member will have their previous permissions preserved as a customized workspace policy applicable for them.

> ![success](/docs/images/tick.svg)
> 
> This approach gives Admins more granular control over individual member permissions while maintaining the same access levels they had before.

## Baseline Workspace Policy

New members added to a workspace after migration will inherit its [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>) by default.

> ![warning](/docs/images/warning.svg)
> 
> This behavior is different from the legacy RBAC system where new members inherited permissions based on their assigned role.
> 
> After migration, you will need to explicitly configure the [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>) to grant the default permissions you want new members to have when they join your workspace.

Also, note that unless configured by Admins, the baseline workspace policy contains [view-only permissions](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/#default-behavior>) for all resources with restricted access to PII.

## Granular resource-level permissions

Admins will be able to grant [**Edit** , **Connect** , and **Create & Delete**](<https://www.rudderstack.com/docs/access-management/policies-overview/#edit-connect-and-create--delete-permissions>) permissions independently on specific resources.

This provides more flexibility than the legacy RBAC system, where permissions were bundled into roles. You can now configure permissions at a more granular level, allowing you to grant specific actions on specific resources without giving broader access.

## Import strategy decision

During migration, you will need to choose an import strategy that determines how your existing permissions are translated into the new system:

Strategy| Implications| Ideal if  
---|---|---  
Start fresh| RudderStack imports members with baseline, view-only permissions.| You want to start with a blank slate and build permissions policies from the ground up.  
Use existing policies| RudderStack imports members with their existing permissions. Current user roles will be mirrored into the individual user’s [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>).| You want to retain the existing user permissions as is, without having to modify them later.  
  
> ![info](/docs/images/info.svg)
> 
> Service Access Tokens will be automatically imported with their current permissions in both import strategies.

## Migration process

See the [Migration Guide](<https://www.rudderstack.com/docs/access-management/migration-steps/>) for step-by-step instructions on performing the migration.

## See more

  * [How Migration Works](<https://www.rudderstack.com/docs/access-management/how-migration-works/>): Learn about the technical process of migration
  * [Key Concepts](<https://www.rudderstack.com/docs/access-management/concepts/>): Understand the core concepts of Access Management