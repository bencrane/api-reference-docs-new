# How to Migrate to New Access Management System

Step-by-step guide to migrate your existing roles and permissions to the new Access Management system.

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

This guide explains how to migrate your existing roles and permissions from the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>) to the new [Access Management system](<https://www.rudderstack.com/docs/access-management/overview/>).

## Quickstart summary

> ![success](/docs/images/tick.svg)
> 
> **Migration in 5 minutes**
> 
>   1. Go to **Settings** > **Access Management** in your dashboard.
>   2. Click **Import** and choose your import strategy (start fresh or use existing policies).
>   3. Configure your [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>) and create [Groups](<https://www.rudderstack.com/docs/access-management/groups/>) for your teams.
>   4. Review [Member Workspace Policies](<https://www.rudderstack.com/docs/access-management/members/>) and adjust as needed.
>   5. Click **Deploy** to activate the new Access Management system.
> 

> 
> Your existing permissions remain active until you deploy. You can reset and restart at any time before deployment.

## Role mapping reference

The table below shows how roles in the legacy RBAC system map to the new Access Management system:

Legacy RBAC role| New Access Management equivalent| Notes  
---|---|---  
**Admin**|  Organization Admin + Full workspace permissions| Admins retain full control. Organization-level Admin role is separate from workspace permissions.  
**Read-Write**|  Member Workspace Policy with Edit, Connect, Create & Delete permissions| Configure via [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>) or individual [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>).  
**Read-Only**|  Member Workspace Policy with View-only permissions| Default for new members. Can be set via [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>).  
**Custom roles**| [Group Policies](<https://www.rudderstack.com/docs/access-management/groups/>)| Create groups (Data Engineers, Marketers, etc.) with specific permission sets.  
  
> ![info](/docs/images/info.svg)
> 
> When you choose the **Use existing policies** import strategy, RudderStack automatically maps your current roles to individual Member Workspace Policies. You can then organize members into Groups for easier management.

## Migration overview

The migration process involves:

  * Importing your existing members (with or without their existing permissions) and [Service Access Tokens](<https://www.rudderstack.com/docs/access-management/service-access-tokens/>) into a staging area
  * Configuring [access policies](<https://www.rudderstack.com/docs/access-management/concepts/#access-policy>) for your workspace, groups, and members
  * Deploying the changes to activate the new [Access Management system](<https://www.rudderstack.com/docs/access-management/overview/>)


> ![warning](/docs/images/warning.svg)
> 
> Your existing permissions will remain active until you deploy the new Access Management system.

## Prerequisites

  * **Important** : See the [Pre-migration Considerations](<https://www.rudderstack.com/docs/access-management/pre-migration-considerations/>) guide to understand what to expect after migration
  * Only [Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) will be able to perform the migration


## Step 1: Import members and Service Access Tokens

  1. Go to **Settings** > **Access Management** in your RudderStack dashboard.
  2. You will see a **Migration Status** banner — review the migration progress and timeline.

[![Migration banner](/docs/images/access-management/migration/migration-banner.webp)](</docs/images/access-management/migration/migration-banner.webp>)

  3. In the **Migration Progress** section of the banner, click **Import**.
  4. Choose your import strategy.

Strategy| Implications| Ideal if  
---|---|---  
Start fresh| RudderStack imports members with baseline, view-only permissions.| You want to start with a blank slate and build permissions policies from the ground up.  
Use existing policies| RudderStack imports members with their existing permissions. Current user roles will be mirrored into the individual user’s [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>).| You want to retain the existing user permissions as is, without having to modify them later.  
  
> ![info](/docs/images/info.svg)
> 
> Service Access Tokens will be automatically imported with their current permissions in both import strategies.

[![Migration strategy selection](/docs/images/access-management/migration/migration-strategy.webp)](</docs/images/access-management/migration/migration-strategy.webp>)

  5. Click on **Import members** or **Import members with policies** to complete the import process.


## Step 2: Configure policies

After importing members, you can review and adjust the imported policies before deploying them.

  1. Review and configure the [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>) for your workspace.

[![Configure baseline workspace policy](/docs/images/access-management/migration/configure-baseline-workspace-policies.webp)](</docs/images/access-management/migration/configure-baseline-workspace-policies.webp>)

  2. [Create new groups](<https://www.rudderstack.com/docs/access-management/groups/#add-a-new-group>) and configure their [workspace policies](<https://www.rudderstack.com/docs/access-management/groups/#configure-group-workspace-policy>) with specific permission sets.

[![Create groups](/docs/images/access-management/migration/create-groups.webp)](</docs/images/access-management/migration/create-groups.webp>)

  3. Fine-tune users’ [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>) as needed.

[![Configure member policies](/docs/images/access-management/migration/configure-member-policies.webp)](</docs/images/access-management/migration/configure-member-policies.webp>)

> ![success](/docs/images/tick.svg)
> 
> You can reset the staging area at any time to revert any changes made to the policies and restart the migration process again.
> 
> See Reset staging area for more information.

## Step 3: Deploy and enforce the new system

> ![danger](/docs/images/danger.svg)
> 
> **The deployment is irreversible**
> 
> Make sure you’ve reviewed and configured all permissions correctly before deploying. After deployment, the new Access Management system will be active and the legacy RBAC system will **no longer be available**.

  1. Review your staging area configuration to ensure all access policies are configured correctly.
  2. In the **Migration Progress** section, click **Deploy**.
  3. Confirm the deployment when prompted.


Once migration is complete, you will see the following banner:

[![Migration complete banner](/docs/images/access-management/migration/migration-success-banner.webp)](</docs/images/access-management/migration/migration-success-banner.webp>)

> ![success](/docs/images/tick.svg)
> 
> After migration, you can leverage the new Access Management system to make any changes to the access policies — they will reflect in the workspace immediately.

## Manage permissions after migration

Once migration is complete, you can:

  * Configure your [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>) that automatically applies to all new members joining that workspace
  * [Create new groups](<https://www.rudderstack.com/docs/access-management/groups/#add-a-new-group>) and fine-tune their [workspace policy](<https://www.rudderstack.com/docs/access-management/groups/#configure-group-workspace-policy>) with specific permission sets
  * Fine-tune users’ [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>) as needed


See the [Policies Overview](<https://www.rudderstack.com/docs/access-management/policies-overview/>) guide for more information.

## Reset staging area

The migration staging area lets you configure and preview permissions policies before deploying them, allowing you to:

  * Review how your current permissions map to the new system
  * Make changes to policies without affecting your current permissions


Clicking on **Reset staging area** clears all imported members and policy configurations, allowing you to restart the migration process from scratch.

## Troubleshooting

Issue| Solution  
---|---  
Import fails or does not complete| Try resetting the staging area and import again  
Deploy button is disabled| Make sure the import step has completed successfully  
Permissions don’t match expectations| 

  * Make sure you have selected the right [import strategy](<https://www.rudderstack.com/docs/access-management/pre-migration-considerations/#import-strategy-decision>). Reset the staging area and try again, if required
  * Review the [How Migration Works](<https://www.rudderstack.com/docs/access-management/how-migration-works/>) guide to understand how permissions are mapped
  * You can also adjust member policies after deployment

  
  
## See more

  * [How Migration Works](<https://www.rudderstack.com/docs/access-management/how-migration-works/>): Learn about the technical process of migration and what happens after deployment
  * [Migration Scenarios](<https://www.rudderstack.com/docs/access-management/migration-examples/>): Understand how migration works in different scenarios