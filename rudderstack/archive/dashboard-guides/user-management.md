# Members (User Management)

Manage users across your organization and workspaces and assign them relevant roles.

* * *

  * __5 minute read

  * 


> ![warning](/docs/images/warning.svg)
> 
> **This documentation is applicable for the legacy Permissions Management (RBAC) system.**
> 
> See [Member Management](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) for the latest information on managing users and their permissions across organization and workspaces in the new [Access Management (PBAC)](<https://www.rudderstack.com/docs/access-management/overview/>) system.

RudderStack’s user management feature lets you easily collaborate with other members of your organization. It provides different options to manage users and their permissions at the [workspace](<https://www.rudderstack.com/docs/dashboard-guides/workspaces/>) level.

## Manage users in organization

RudderStack lets you invite users and manage their permissions within your organization’s workspaces.

### Invite users

You can invite users to an organization either as Org Admin or Org Member.

> ![warning](/docs/images/warning.svg)
> 
> The invitations are valid for 3 days before expiring.

The following sections detail the steps to invite users with these permissions.

#### Org Admin

To invite a user with **Org Admin** permissions:

  1. Go to **Settings** > **Organization**. Go to the **Members** tab and click the **Invite member** button:

[![Invite member](/docs/images/dashboard-guides/user-management/invite-member.webp)](</docs/images/dashboard-guides/user-management/invite-member.webp>)

  2. Enter the member’s **Email address** and select **Organization Role** as **admin** from the dropdown. You can send multiple invites at once by clicking **Add another member**. Finally, click **Send invite(s)** to proceed.


> ![info](/docs/images/info.svg)
> 
> The **Admin** user gets access to all the workspaces within that organization by default.

[![Set email address and org role](/docs/images/dashboard-guides/user-management/invite-user-role.webp)](</docs/images/dashboard-guides/user-management/invite-user-role.webp>)

  3. Enter your password to send the invite(s). The user will be automatically added to the organization once they accept the invitation.


#### Org Member

To invite a user with **Org Member** permissions:

  1. Go to **Settings** > **Organization**. Go to the **Members** tab and click the **Invite member** button:

[![Invite member](/docs/images/dashboard-guides/user-management/invite-member.webp)](</docs/images/dashboard-guides/user-management/invite-member.webp>)

  2. Enter the member’s **Email address** and select **Organization Role** as **member** from the dropdown. You can send multiple invites at once by clicking **Add another member**. Finally, click **Send invite(s)** to proceed.

[![Set email address and org role](/docs/images/dashboard-guides/user-management/invite-user-member.webp)](</docs/images/dashboard-guides/user-management/invite-user-member.webp>)

  2. Click **Add workspaces** next to the invited user.

[![Invite member](/docs/images/dashboard-guides/user-management/org-member-workspace.webp)](</docs/images/dashboard-guides/user-management/org-member-workspace.webp>)

  3. Select the specific workspace(s) you want to add the user to and click **Add workspace(s)**.

[![Invite member](/docs/images/dashboard-guides/user-management/add-member-to-workspace.webp)](</docs/images/dashboard-guides/user-management/add-member-to-workspace.webp>)

The user will be automatically added to the specified workspace(s) once they accept the invitation.

### Remove users

To remove a user from the organization, click the meatballs menu next to the user and select **Remove member**. Then, enter your password to confirm.

[![Edit access policy](/docs/images/dashboard-guides/user-management/remove-member.webp)](</docs/images/dashboard-guides/user-management/remove-member.webp>)

### Edit access policy

> ![info](/docs/images/info.svg)
> 
> Only **Org Admins** can edit the access policies of other members, including other **Org Admins**.

  1. In the **Members** tab, click the meatballs menu next to the user and select **Edit access policy** :

[![Edit access policy](/docs/images/dashboard-guides/user-management/edit-access-policy-latest.webp)](</docs/images/dashboard-guides/user-management/edit-access-policy-latest.webp>)

  2. Click the edit icon corresponding to the Organization role or the specific workspace for which you want to change the user’s permissions.

[![Edit access policy](/docs/images/dashboard-guides/user-management/edit-access-policy-3.webp)](</docs/images/dashboard-guides/user-management/edit-access-policy-3.webp>)

  3. Make the necessary changes, click **Save** , and enter your password to confirm.

[![Edit user role to Member](/docs/images/dashboard-guides/user-management/downgrade-user.webp)](</docs/images/dashboard-guides/user-management/downgrade-user.webp>)

Note that:

  * When you upgrade a user with **Member** role to **Admin** , they will automatically get full edit access to all the resources.

  * When you downgrade a user with **Admin** role to **Member** , RudderStack resets all access permissions to read-only. You need to manually set the permissions for each resource and click **Save** to update the access policy.


## Manage users in workspaces

RudderStack lets you add/remove users and assign them relevant user roles within your [workspaces](<https://www.rudderstack.com/docs/dashboard-guides/workspaces/#workspaces>).

> ![info](/docs/images/info.svg)
> 
> Only the RudderStack Starter, Growth, and Enterprise plans have access to [multiple workspaces](<https://www.rudderstack.com/docs/dashboard-guides/workspaces/#available-workspaces-by-plan>) within an organization.

As the [Org AdminAn Org Admin is an invited user with full access to the organization.](</docs/resources/glossary/#org-admin>) has admin access over all the workspaces within an organization, only they can add/remove **Org members** and edit their access policies for different workspaces.

### Add users

You can choose to add an existing **Org Member** to a [specific workspace](<https://www.rudderstack.com/docs/dashboard-guides/workspaces/#workspace-types>):

  1. Click the meatballs menu next to the user and select **Add workspace(s)**. Note that you will see this option only if the user isn’t already added to that workspace.

[![Add to workspace](/docs/images/dashboard-guides/user-management/add-workspace-member.webp)](</docs/images/dashboard-guides/user-management/add-workspace-member.webp>)

  2. Select the workspace(s) you want to add the user to and click **Add workspace(s)**.

[![Select workspaces](/docs/images/dashboard-guides/user-management/user-add-workspace-latest.webp)](</docs/images/dashboard-guides/user-management/user-add-workspace-latest.webp>)

### Remove users

You can remove an **Org member** from a specific workspace by clicking the workspace next to the user and clicking **Remove from workspace** , as shown:

[![Remove user from workspace](/docs/images/dashboard-guides/user-management/remove-user-from-workspace.webp)](</docs/images/dashboard-guides/user-management/remove-user-from-workspace.webp>)

### Edit access policy

  1. In the **Members** tab, click the workspace next to the user and select **Edit access policy** :

[![Edit access policy for workspace](/docs/images/dashboard-guides/user-management/edit-access-policy-workspace.webp)](</docs/images/dashboard-guides/user-management/edit-access-policy-workspace.webp>)

  2. Click the edit icon corresponding to the Organization role or the workspace for which you want to change the user’s permissions.

[![Edit access policy](/docs/images/dashboard-guides/user-management/edit-user-role-permissions.webp)](</docs/images/dashboard-guides/user-management/edit-user-role-permissions.webp>)

  3. Make the necessary changes, click **Save** , and enter your password to confirm.


## Role definitions

Term| Level| Definition  
---|---|---  
Organization roles| Organization| Highest abstraction level that determines if a user has a full access or customized access to specific resources.  
  
**Example** : Org Admin, Org Member  
Resource roles| Workspace| Predefined access to specific resources. A user can have multiple resource roles that grant access to all or some resources.  
  
**Example** : Connections Admin/Editor/Viewer, Transformations Admin  
  
## Role permissions

The following sections detail the access policies set for organization-level and resource-level roles.

> ![warning](/docs/images/warning.svg)
> 
> Role permissions are packaged differently in various RudderStack plans. See Plan-wise features for more information.

### Organization roles

Name| Access policy  
---|---  
Org Admin| Full organization access.  
Org Member| Dependent on resource roles.  
  
### Resource roles

#### Connections

Name| What user can do| What user cannot do  
---|---|---  
Admin| 

  * Create and delete sources and destinations.
  * Create and delete models.
  * Connect and disconnect sources from destinations.
  * Edit source and destination configurations.
  * Connect or disconnect transformations.
  * Connect or disconnect models.
  * Link or unlink Tracking Plans.
  * CRUD operations on any resource for which there is no specific role (for example, Audience, Profiles).

| -  
Editor| 

  * Connect and disconnect sources from destinations.
  * Edit source and destination configurations.
  * Connect or disconnect transformations.
  * Connect or disconnect models.
  * Link or unlink Tracking Plans.

| Create and delete sources and destinations.  
Viewer| Read-only access.| Create, edit, or delete anything.  
  
#### Transformations and Library

Name| What user can do| What user cannot do  
---|---|---  
Grant edit access| Create, edit, or delete transformations/libraries.| Connect and disconnect transformations/libraries.  
  
## Plan-wise features

Feature| Free| Starter/Growth| Enterprise  
---|---|---|---  
Organization roles| 

  * Org Admin
  * Org Member

| 

  * Org Admin
  * Org Member

| 

  * Org Admin
  * Org Member

  
Resource roles| None| 

  * Connections
  * Transformations

| 

  * Connections
  * Transformations

  
[Assign user access to PII](<https://www.rudderstack.com/docs/dashboard-guides/data-management/#limiting-access-to-pii-related-features>)| No| No| Yes  
  
> ![info](/docs/images/info.svg)
> 
> **Summary**
> 
>   * All [RudderStack plans](<https://rudderstack.com/pricing/>) have these organization roles - **Org Admin** and **Org Member**.
> 
>   * RudderStack’s **Free** plan does not have any granular, resource-level roles. It only has following roles:
> 
>     * **Org Admin** : Full organization access
>     * **Org Member** : View-only access
>   * Resource roles are available in paid RudderStack plans and expand by tier
> 
>   * The [PII controls](<https://www.rudderstack.com/docs/dashboard-guides/data-management/#limiting-access-to-pii-related-features>) feature is available only in the [Enterprise plan](<https://www.rudderstack.com/enterprise-quote/>)
> 
> 


### Member limit

Plan| Member limit  
---|---  
[Free](<https://app.rudderstack.com/signup>)| 10  
[Starter](<https://www.rudderstack.com/pricing/>)| 10  
[Growth](<https://www.rudderstack.com/pricing/>)| Unlimited  
[Enterprise](<https://www.rudderstack.com/enterprise-quote/>)| Unlimited