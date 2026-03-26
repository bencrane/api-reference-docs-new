# Manage Member Workspace Policy

Manage members by adding them to groups and customizing their individual workspace policy.

* * *

  * __2 minute read

  * 


This guide explains how to manage members and configure their individual workspace policy for each workspace.

## Overview

The **Users** tab in the **Access Management** section lets you:

  * View member details, upgrade or downgrade their [organization role](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>), or remove them from the organization
  * Customize a member’s workspace policy
  * Manage group membership


### Plan-wise limits

The number of members Admins can invite to a workspace depends on the [RudderStack plan](<https://www.rudderstack.com/pricing/>):

Plan| Member limit  
---|---  
Free| 10 members per organization  
Starter| 10 members per organization  
Growth| Unlimited  
Enterprise| Unlimited  
  
See the [Plan-wise Features](<https://www.rudderstack.com/docs/access-management/plan-wise-features/#member-management>) guide for more details.

## Configure member workspace policy

  1. Go to **Settings** > **Access Management** and click the **Users** tab.
  2. Select the member for which you want to configure the workspace policy.
  3. Under the **Member Workspace Policies** tab, select the workspace for which you want to configure the member policy.

[![Select workspace to configure user permissions](/docs/images/access-management/member-policy-select-workspace.webp)](</docs/images/access-management/member-policy-select-workspace.webp>)

  4. [Configure the workspace policy](<https://www.rudderstack.com/docs/access-management/policies-overview/>) for the member.


> ![info](/docs/images/info.svg)
> 
> You may see some permissions with a green check mark. These indicate permissions inherited from the [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>) and [Group Workspace Policies](<https://www.rudderstack.com/docs/access-management/groups/>) of which the member is a part.
> 
> As all members inherit permissions from the [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>) and any [Group Policies](<https://www.rudderstack.com/docs/access-management/groups/>), these inherited permissions **cannot** be changed or removed. However, you can configure **additional** permissions for the member.

  5. Click **Save** for the changes to take effect.


A sample member workspace policy is shown below:

[![Individual permissions policy](/docs/images/access-management/sample-member-workspace-policy.webp)](</docs/images/access-management/sample-member-workspace-policy.webp>)

## Manage group members

You can easily add or remove members from a group to simplify permissions management.

### Add members to a group

  1. In the **Groups** tab, click the group to which you want to add members.
  2. Go to the **Group Members** tab and click **Add group members**.

[![Add members to a group](/docs/images/access-management/add-group-members.webp)](</docs/images/access-management/add-group-members.webp>)

  3. Select the members to add to the group. Then, click **Next**.

[![Add members to a group](/docs/images/access-management/add-members-to-group.webp)](</docs/images/access-management/add-members-to-group.webp>)

  4. In the confirmation window, click **Add members** to add the members to the group.


### Remove members from a group

  1. In the **Group Members** tab, click the meatballs menu (`...`) next to the member. **Edit members** button.
  2. Click **Remove member from group**.

[![Remove member from group](/docs/images/access-management/remove-member-from-group.webp)](</docs/images/access-management/remove-member-from-group.webp>)

  3. In the confirmation window, click **Remove** to complete removal.