# Member Management in RudderStack

Manage members in your organization’s workspaces, including inviting new members and managing their roles and permissions.

* * *

  * __4 minute read

  * 


This guide explains how to manage members in your organization’s workspaces, including inviting new members and managing their roles and permissions.

## Member limit

The number of team members you can add to your workspace depends on your [RudderStack plan](<https://www.rudderstack.com/pricing/>):

Plan| Member limit  
---|---  
Free| 10 members per organization  
Starter| 10 members per organization  
Growth| Unlimited  
Enterprise| Unlimited  
  
## Manage invitations

This section explains how to invite new members to your organization’s workspaces and manage their invitations.

### Invite new members

  1. Go to **Settings** > **Access Management** and click the **Invitations** tab.
  2. Click **Invite users**.

[![Invite users button in Access Management](/docs/images/access-management/member-management/invite-users.webp)](</docs/images/access-management/member-management/invite-users.webp>)

  3. Specify the email address of the member you want to invite. You can add multiple email addresses separated by commas. Then, click **Add**.

[![New members email addresses](/docs/images/access-management/member-management/enter-emails.webp)](</docs/images/access-management/member-management/enter-emails.webp>)

  4. Select the member role from the dropdown. Click **Next** to proceed.

[![Select member role](/docs/images/access-management/member-management/select-member-role.webp)](</docs/images/access-management/member-management/select-member-role.webp>)

  5. Select the groups you want to add the member to.

[![Select member groups](/docs/images/access-management/member-management/select-member-groups.webp)](</docs/images/access-management/member-management/select-member-groups.webp>)

  6. **Optional if you have followed Step 5** : Select the workspaces to add the member to. Then, click **Next**.

[![Select member workspaces](/docs/images/access-management/member-management/add-workspaces.webp)](</docs/images/access-management/member-management/add-workspaces.webp>)

> ![warning](/docs/images/warning.svg)
> 
> To invite a member to the organization, they need to be assigned to **at least one** group or workspace.

  7. You will see a confirmation window to verify the invitation details. Click **Invite** to send the invitation.


> ![info](/docs/images/info.svg)
> 
> The invitations are valid for **3 days** before they expire.

[![Confirm and send invitation](/docs/images/access-management/member-management/confirm-invitation.webp)](</docs/images/access-management/member-management/confirm-invitation.webp>)

### Delete invitations

Click the meatballs menu (`...`) next to the invitation and select **Delete invitation**.

[![Delete invitation](/docs/images/access-management/member-management/delete-invitation.webp)](</docs/images/access-management/member-management/delete-invitation.webp>)

## Manage members

This section explains how to manage members in your organization’s workspaces, including:

  * Viewing member details
  * Assigning members to groups
  * Removing members from your organization


### View member details

  1. Go to **Settings** > **Access Management** and click the **Users** tab.
  2. Click the meatballs menu (`...`) next to the member and select **View member details**.

[![View member details](/docs/images/access-management/member-management/view-member-details.webp)](</docs/images/access-management/member-management/view-member-details.webp>)

Here, you can:

  * See the workspaces the member is a part of
  * Add the member to a different workspace
  * Add a member to a group

[![View member details](/docs/images/access-management/member-management/member-details.webp)](</docs/images/access-management/member-management/member-details.webp>)

#### Add member to a different workspace

  1. Under **Individual Permissions** tab, click **Add workspace policy**.
  2. Select the workspace to add the member to and click **Add**.


> ![info](/docs/images/info.svg)
> 
> Once added, the member will automatically inherit the [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>) configured for that workspace.

### Add member to a group

  1. Go to **Settings** > **Access Management** and click the **Users** tab.
  2. Click the meatballs menu (`...`) next to the member and select **Add to groups**.
  3. Select the group to add the member to and click **Next**.

[![Add member to groups](/docs/images/access-management/member-management/add-member-to-groups.webp)](</docs/images/access-management/member-management/add-member-to-groups.webp>)

  4. In the confirmation window, click **Add** to add the member to the specified groups.


### Delete member

  1. Go to **Settings** > **Access Management** and click the **Users** tab.
  2. Click the meatballs menu (`...`) next to the member and select **Delete member**.
  3. In the confirmation window, click **Delete** to remove the member from your organization.


> ![warning](/docs/images/warning.svg)
> 
> Once removed, you will need to invite the member again for them to access your organization’s workspaces.

[![Remove member from the organization](/docs/images/access-management/member-management/delete-member.webp)](</docs/images/access-management/member-management/delete-member.webp>)

### Bulk actions

You can perform bulk actions on members in your organization, including adding multiple members to groups, or removing them from your organization.

[![Add multiple members to a group](/docs/images/access-management/member-management/bulk-actions.webp)](</docs/images/access-management/member-management/bulk-actions.webp>)

#### Add multiple members to a group

  1. Select the members you want to perform the action on.
  2. Click the **Add to groups** bulk action at the bottom.
  3. Select the groups and click **Next**.
  4. Verify the changes in the confirmation window and click **Add**.


#### Remove multiple members from your organization

  1. Select the members you want to perform the action on.
  2. Click the **Delete** bulk action at the bottom.
  3. Verify the changes in the confirmation window and click **Delete**.


## Member roles

When you invite a new member to your organization, you can assign them a role that determines if they have full or customized access to your organization’s resources.

RudderStack defines two types of roles:

Role| Access  
---|---  
Admin| Full organization access.  
Member| Effective set of permissions within a workspace, computed by aggregating:  
  


  * [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>)
  * [Group Workspace Policies](<https://www.rudderstack.com/docs/access-management/groups/>) that the member is a part of
  * [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>) configured for the member

  
  
### Manage member roles

You can upgrade or downgrade a member’s role at any time, depending on your organization’s needs.

  1. Go to **Settings** > **Access Management** and click the **Users** tab.
  2. Click the meatballs menu (`...`) next to the member and select **Make Admin** or **Make Member** , depending on the member’s current role.

[![Manage member role](/docs/images/access-management/member-management/manage-role.webp)](</docs/images/access-management/member-management/manage-role.webp>)