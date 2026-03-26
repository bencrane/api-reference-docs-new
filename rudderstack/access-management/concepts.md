# Access Management Key Concepts

Learn about the key concepts and terms related to Access Management in RudderStack.

* * *

  * __3 minute read

  * 


This guide covers the key concepts and terms related to the design and functionality of RudderStack’s Access Management system.

## Policy-based Access Control (PBAC)

RudderStack’s Access Management system is based on **Policy-based Access Control (PBAC)**.

> ![info](/docs/images/info.svg)
> 
> Policy-based Access Control (PBAC) allows Admins to define granular permissions for resources and actions, and assign them to users directly via an access policy.

## Additive permissions model

The Access Management system follows an **additive permissions model** , meaning permissions from the [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>), [Group Workspace Policies](<https://www.rudderstack.com/docs/access-management/groups/>), and [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>) are combined.

Inherited permissions from lower levels cannot be removed at higher levels. Access only expands — **it does not contract**.

For example:

  * A baseline workspace policy might grant **Edit** permission on **Event Stream Sources**.
  * A group workspace policy might grant **Connect** permission on **Event Stream Sources**.
  * A member workspace policy might grant **Create & Delete** permission on **Event Stream Sources**.


The member’s effective access policy would then include all three permissions for **Event Stream Sources**.

## Permission

A **permission** defines a specific action a user can take, like **Edit** , **Connect** , or **Create & Delete**. Permissions are the most granular building blocks of access and always refer to actions on specific resources, like sources, destinations, transformations, etc.

> ![info](/docs/images/info.svg)
> 
> Permissions **do not** grant access by themselves — you must assign them to members via an access policy.

## Access policy

A member’s **access policy** is the effective set of permissions they have in a workspace. It is computed by aggregating:

  * The [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>)
  * Any [Group Workspace Policies](<https://www.rudderstack.com/docs/access-management/groups/>)
  * The member’s [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>)


## Workspace policy

A **workspace policy** is a named bundle of permissions. Policies can be:

  * Applied as **Baseline** , applicable to the entire workspace
  * Assigned to **Groups** created within the workspace
  * Assigned to individual **Members** in the workspace


Each policy defines what members can and cannot do in the given workspace.

### Baseline Workspace Policy

Every workspace has **one baseline policy** that applies to all groups and members. This ensures consistent baseline access for all users, such as view-only permissions for resources or restricted access to PII.

Unless otherwise configured by an Admin, the baseline workspace policy is set to:

  * **View-only** for [resources](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>)
  * **No access** to [PII views](<https://www.rudderstack.com/docs/access-management/policies-overview/#pii-permissions>) in [Enterprise](<https://www.rudderstack.com/enterprise-quote/>) plan
  * **Full** PII access to all members in **non-Enterprise** plans


### Group policies

Each group can have one workspace policy configured per workspace. Members of the group will inherit all permissions from both:

  * [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>)
  * [Group Workspace Policy](<https://www.rudderstack.com/docs/access-management/groups/>)


This allows Admins to create custom roles and share consistent access patterns without manual duplication.

### Member policies

You can customize and configure a workspace policy for an individual member. This policy **extends** permissions from the [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>) and [Group Workspace Policies](<https://www.rudderstack.com/docs/access-management/groups/>) — it does not override them.