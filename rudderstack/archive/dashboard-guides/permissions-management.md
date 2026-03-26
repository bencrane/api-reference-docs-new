# Permissions Management

Manage your team’s permissions and access controls in RudderStack.

Available Plans

  * enterprise


* * *

  *  __4 minute read

  * 


> ![warning](/docs/images/warning.svg)
> 
> **This documentation is applicable for the legacy Permissions Management (RBAC) system.**
> 
> In the new [Access Management (PBAC)](<https://www.rudderstack.com/docs/access-management/overview/>) system, resource and PII permissions can be restricted at a workspace, group, or member level.

RudderStack’s permissions management feature gives you the ability to:

  * Restrict edit permissions for business-critical objects to selected users in your organization
  * Limit access to the product features where PII is exposed (for example, Live Events, debug logs, etc.) for compliance purposes


## Set granular access controls

When you [invite a member to your organization](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#invite-users>), RudderStack lets you assign any of the two default [roles](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) to them - **Org Admin** or **Org Member**.

With the granular access control capabilities, Admins can lock down business-critical objects to a select list of people. They can also restrict PII(Personally Identifiable Information) access to certain users.

With these features, you can allow certain data pipelines to be edited **only** by the users with the required access. Also, you can ensure your access controls are in compliance with the major data regulations like SOC2, GDPR, CCPA, HIPAA, etc.

> ![info](/docs/images/info.svg)
> 
> All the access-related changes are recorded in the [Audit Logs](<https://www.rudderstack.com/docs/dashboard-guides/audit-logs/>).

## Set permissions for individual resources

Go to the **Permissions** tab to set permissions for a particular resource (source, destination, or model) in the workspace. You can also specify members who can make changes to these resources.

> ![info](/docs/images/info.svg)
> 
> Only **Org Admins** can see the **Permissions** tab.

#### Permissions scope

The permissions set for a particular resource let you:

  * Connect/disconnect a resource with another resource. For example, source to destination, source to tracking plan, transformation to destination, model to reverse ETL source, etc.
  * Enable, disable, or delete a resource
  * Edit or change the resource-specific configuration


> ![info](/docs/images/info.svg)
> 
> Any action involving setting up a connection between two resources or linking/de-linking a resource with another resource requires edit permissions for both the resources. The only exception is the [SQL Models](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/models/>) which can used without explicitly setting any edit permissions.

### Assign permissions to specific members

  1. Go to the resource and click the **Permissions** tab:

[![Permissions tab within a resource](/docs/images/dashboard-guides/permissions-tab.webp)](</docs/images/dashboard-guides/permissions-tab.webp>)

  2. You will see the following options under the **Who can make changes?** section:

     * **Members and tokens with Editor permissions** : All the members and Service Access Tokens with the [relevant permissions](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#resource-roles>) can make changes to the resource
     * **Only members and Service Access Tokens you select** : Only the specified members and Service Access Tokens can make changes to the resource
  3. To allow specific members of your team to edit the resource, click **Only members and Service Access Tokens you select** and click the **Members** tab. Then, click **Add members**.


[![Add members option](/docs/images/dashboard-guides/permissions-management-add-members.webp)](</docs/images/dashboard-guides/permissions-management-add-members.webp>)

  4. In the right sidebar, select the team members from the dropdown and click **Add Members** :

[![Add members option](/docs/images/dashboard-guides/assign-member-permissions.webp)](</docs/images/dashboard-guides/assign-member-permissions.webp>)

### Assign permissions to specific SATs

  1. Go to the resource and click the **Permissions** tab:

[![Permissions tab within a resource](/docs/images/dashboard-guides/permissions-tab.webp)](</docs/images/dashboard-guides/permissions-tab.webp>)

  2. You will see the following options under the **Who can make changes?** section:

     * **Members and tokens with Editor permissions** : All the members and Service Access Tokens with the relevant [relevant permissions](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#resource-roles>) can make changes to the resource
     * **Only people and Service Access Tokens you select** : Only the specified members and access tokens can make changes to the resource
  3. To allow edit access to specific SATs within your workspace, click **Only people and Service Access Tokens you select** and click the **Service Access Tokens** tab. Then, click **Add tokens**.


[![Add tokens option](/docs/images/dashboard-guides/permissions-add-tokens.webp)](</docs/images/dashboard-guides/permissions-add-tokens.webp>)

  4. In the right sidebar, select the tokens from the dropdown and click **Add tokens** :

[![Add tokens option](/docs/images/dashboard-guides/assign-token-permissions.webp)](</docs/images/dashboard-guides/assign-token-permissions.webp>)

> ![info](/docs/images/info.svg)
> 
> You can add only [workspace-level Service Access Tokens](<https://www.rudderstack.com/docs/archive/dashboard-guides/service-access-tokens/#workspace-level-sats>). Organization-level Service Access Tokens are **not** available for selection.

## Limit access to PII

RudderStack’s data privacy options let you safeguard your customers’ privacy by controlling who has access to the raw event data containing PII(Personally Identifiable Information). You can allow anyone on your team to access the PII or restrict access only to a select list of members.

Only members with PII permissions can view the customers’ PII in the [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/>) and errors logs in your [destination’s](<https://www.rudderstack.com/docs/dashboard-guides/destinations/#overview>) **Events** tab:

[![View blocked event metrics for the source](/docs/images/data-governance/event-blocking/blocked-event-metrics-source.webp)](</docs/images/data-governance/event-blocking/blocked-event-metrics-source.webp>)

To set the PII permissions, follow these steps:

  1. In your RudderStack dashboard, go to **Settings** > **Workspace** > **Data Management** and scroll down to the **Data Privacy** section.

  2. Under **Who can view restricted data?** , select the appropriate option:

     * **Anyone on your team** : All members of your workspace can view the raw event data containing PII.
     * **Only people you select** : Only specific members with access can view the raw data.
  3. To allow specific members of your team to edit the object, click **Only people you select** , followed by **Add member**.


[![Add members](/docs/images/rs-cloud/permissions-management-5.webp)](</docs/images/rs-cloud/permissions-management-5.webp>)

  4. Finally, select the workspace members from the drop-down and click **Add Members** :

[![Add members option](/docs/images/rs-cloud/permissions-management-6.webp)](</docs/images/rs-cloud/permissions-management-6.webp>)

> ![warning](/docs/images/warning.svg)
> 
> If the **Org Admins** are removed from the access list, RudderStack will restrict them from viewing the PII.