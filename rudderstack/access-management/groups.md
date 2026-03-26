# Manage Group Policies

Create groups and manage their policies for your RudderStack workspace.

Available Plans

  * growth
  * enterprise


* * *

  *  __2 minute read

  * 


This guide explains how to create groups and manage their policies for your RudderStack workspace.

## Overview

The **Groups** tab lets you create groups, configure a group policy for each workspace, and add members to groups. All group members automatically inherit this workspace policy.

> ![info](/docs/images/info.svg)
> 
> Groups enable the creation of **custom roles** (Data Engineers, Marketers, etc.) and streamline permissions configuration for large teams.

### Plan-wise limits

The number of groups Admins can create in a workspace depends on the [RudderStack plan](<https://www.rudderstack.com/pricing/>):

Plan| Group limit  
---|---  
Free| Not available  
Starter| Not available  
Growth| Limited to 3 groups per organization  
Enterprise| Unlimited groups  
  
See the [Plan-wise Features](<https://www.rudderstack.com/docs/access-management/plan-wise-features/#groups>) guide for more details.

## Add a new group

  1. Go to **Settings** > **Access Management**.
  2. Under the **Groups** tab, click **Create group**.

[![Create group button in dashboard](/docs/images/access-management/create-group.webp)](</docs/images/access-management/create-group.webp>)

  3. Assign a group name and description. Then, click **Next**.

[![Group name and description](/docs/images/access-management/group-name-description.webp)](</docs/images/access-management/group-name-description.webp>)

  4. Specify the workspaces that the group will be a part of.

[![Group workspaces](/docs/images/access-management/add-group-to-workspaces.webp)](</docs/images/access-management/add-group-to-workspaces.webp>)

  5. Click **Create** to create the group.


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


## Configure group workspace policy

  1. Go to **Settings** > **Access Management** and click the **Groups** tab.
  2. Select the group for which you want to configure the policy.
  3. In the **Group Workspace Policies** tab, select the workspace for which you want to configure the group policy.

[![Select workspace to define group permissions](/docs/images/access-management/group-policy-select-workspace.webp)](</docs/images/access-management/group-policy-select-workspace.webp>)

  4. Configure permissions for different [resources](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) and [PII](<https://www.rudderstack.com/docs/access-management/policies-overview/#pii-permissions>) applicable to the group. All group members will automatically inherit these permissions.


> ![info](/docs/images/info.svg)
> 
> You may see some permissions with a green check mark. These indicate permissions inherited from the [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>) defined for the workspace.
> 
> As all groups inherit permissions from the baseline workspace policy, these inherited permissions **cannot** be changed or removed. However, you can configure **additional** permissions for the group.

  5. Click **Save** for the changes to take effect.


A sample group workspace policy is shown below:

[![Group permissions policy](/docs/images/access-management/sample-group-workspace-policy.webp)](</docs/images/access-management/sample-group-workspace-policy.webp>)