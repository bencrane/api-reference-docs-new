# Migration Example: Users and Tokens with Resource-level Permission Restrictions

Example of how migration works when users and Service Access Tokens have resource-level permission restrictions in their access policy.

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

The examples in this guide show how migration works when a user has [resource-level permission restrictions](<https://www.rudderstack.com/docs/archive/dashboard-guides/permissions-management/#restricting-edit-permissions-for-individual-objects>) configured as a part of their role in the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#role-permissions>).

These examples demonstrate how RudderStack preserves granular resource-level permissions during migration, maintaining the same restricted access the member had before.

> ![info](/docs/images/info.svg)
> 
> **Important: Service Access Tokens Migration**
> 
> The migration examples in this guide also apply to [Service Access Tokens](<https://www.rudderstack.com/docs/archive/dashboard-guides/service-access-tokens/>) with resource-level permission restrictions.

## Connections Admin role

The example in this section covers a migration scenario for members with the **Connections Admin** role.

### Scenario

A user with a [Member](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) role has the following access policy in the legacy RBAC system:

  * **Connections Admin** role with permissions to create, edit, connect, and disconnect resources (sources, destinations, transformations, Tracking Plans, etc.)
  * **Full edit access** to create, edit, and delete transformations and transformation libraries

[![](/docs/images/access-management/migration/connections-admin-pre-migration-permissions.webp)](</docs/images/access-management/migration/connections-admin-pre-migration-permissions.webp>)

In addition, the user **does not** have permissions to edit or make changes to **3 sources** (configurable via the [Permissions](<https://www.rudderstack.com/docs/archive/dashboard-guides/permissions-management/#restricting-edit-permissions-for-individual-objects>) tab in the source page):

[![Source permissions configuration showing restricted access](/docs/images/access-management/migration/source-permissions.webp)](</docs/images/access-management/migration/source-permissions.webp>)

### Migration result

> ![info](/docs/images/info.svg)
> 
> This example assumes **no changes were made** to the [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>) or the individual’s [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>) in [staging](<https://www.rudderstack.com/docs/access-management/migration-steps/#step-2-configure-policies>).

After migration, the user’s individual [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>) in the new Access Management system will look as follows:

[![](/docs/images/access-management/migration/connections-admin-resources-post-migration-restricted.webp)](</docs/images/access-management/migration/connections-admin-resources-post-migration-restricted.webp>)[![](/docs/images/access-management/migration/connections-admin-resources-post-migration.webp)](</docs/images/access-management/migration/connections-admin-resources-post-migration.webp>)

The member’s permissions are preserved, with **full access** to all resources and PII views, **except for 3 sources** where they no longer have edit permissions.

> ![info](/docs/images/info.svg)
> 
> This is in contrast to the [previous example](<https://www.rudderstack.com/docs/access-management/migration-examples/no-resource-level-restrictions/#connections-admin-role>), where the member had edit permissions for all sources.

## Connections Editor role

The example in this section covers a migration scenario for members with the **Connections Editor** role.

### Scenario

A user with a [Member](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) role has the following access policy in the legacy RBAC system:

  * **Connections Editor** role with permissions to edit, connect, and disconnect resources (sources, destinations, transformations, Tracking Plans, etc.)
  * **No edit access** to create, edit, and delete transformations and transformation libraries

[![](/docs/images/access-management/migration/connections-editor-pre-migration-permissions.webp)](</docs/images/access-management/migration/connections-editor-pre-migration-permissions.webp>)

In addition, the user **does not** have permissions to edit or make changes to **3 sources** (configurable via the [Permissions](<https://www.rudderstack.com/docs/archive/dashboard-guides/permissions-management/#restricting-edit-permissions-for-individual-objects>) tab in the source page):

[![Source permissions configuration showing restricted access](/docs/images/access-management/migration/source-permissions.webp)](</docs/images/access-management/migration/source-permissions.webp>)

### Migration result

> ![info](/docs/images/info.svg)
> 
> This example assumes **no changes were made** to the [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>) or the individual’s [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>) in [staging](<https://www.rudderstack.com/docs/access-management/migration-steps/#step-2-configure-policies>).

After migration, the user’s individual [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>) in the new Access Management system will look as follows:

[![](/docs/images/access-management/migration/connections-editor-resources-post-migration-restricted.webp)](</docs/images/access-management/migration/connections-editor-resources-post-migration-restricted.webp>)[![Migration example showing new permissions model for PII](/docs/images/access-management/migration/connections-editor-pii-post-migration.webp)](</docs/images/access-management/migration/connections-editor-pii-post-migration.webp>)

The member’s permissions are preserved during migration so that they:

  * **Can** edit and connect resources except the **3 sources** where they no longer have edit permissions
  * **Cannot** create or delete resources
  * **Cannot** edit, connect, or create/delete transformations and transformation libraries


## Connections Viewer role

The **Connections Viewer** role is a read-only role and does not have **Edit** permissions by default. Hence, resource-level permission restrictions do not apply to them.

Their permissions will be migrated as explained in the [No Resource-level Restrictions example](<https://www.rudderstack.com/docs/access-management/migration-examples/no-resource-level-restrictions/#connections-viewer-role>).