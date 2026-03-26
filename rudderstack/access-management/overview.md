# Access Management Overview

Customize user permissions and streamline access to resources across your organization.

* * *

  * __4 minute read

  * 


> ![announcement](/docs/images/announcement.svg)
> 
> **Migrating from Permissions Management (RBAC)?**
> 
> The [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/access-management/glossary/#role-based-access-control-rbac>) **is in the process of being deprecated** and will be removed in a future release. RudderStack recommends migrating to the new Access Management system for enhanced security, granular control, and better compliance capabilities.
> 
> The self-serve migration feature is currently gated for legacy RBAC users and will be generally available on **March 16, 2026**. Contact your [Customer Success Manager](<mailto:support@rudderstack.com>) to enable it for your organization.
> 
>   * [Understand the pre-migration considerations](<https://www.rudderstack.com/docs/access-management/pre-migration-considerations/>)
>   * [Start your migration now](<https://www.rudderstack.com/docs/access-management/migration-steps/>)
>   * [Learn how the migration works](<https://www.rudderstack.com/docs/access-management/how-migration-works/>)
> 


RudderStack’s **Access Management** system gives you enterprise-grade access configuration across the entire platform. Built to be flexible, scalable, and clear, it lets Admins quickly and confidently implement permissions through an intuitive and powerful policy model.

## Why Access Management?

RudderStack’s Access Management system replaces the legacy Permissions Management (RBAC) system with a more powerful **Policy-based Access Control (PBAC)** model. Some benefits are listed below:

Benefit| Description  
---|---  
**Granular control**|  Define permissions at the resource level, not just by role. Grant access to specific sources, destinations, or transformations instead of broad categories.  
**Enhanced security**|  Implement least-privilege access with precision. Users get exactly what they need and nothing more.  
**Compliance-ready**|  Meet InfoSec and audit requirements with clear, traceable permission policies. PII access controls help you maintain data privacy standards.  
**Additive permission model**|  Permissions are only added, never overridden. This makes access policies predictable and easy to reason about.  
**Scalable architecture**|  Manage permissions efficiently across large teams using groups, baseline policies, and inheritance.  
  
> ![success](/docs/images/tick.svg)
> 
> The Access Management system makes it easy for Admins to define **who can perform what actions** across RudderStack — at the workspace, group, and individual member levels.

## Key features

Regardless of your organization’s size, securely managing access to sensitive data and platform functionality is critical. RudderStack’s Access Management system ensures that:

  * Developers, analysts, and marketers get exactly the access they need and no more.
  * Fine-grained control over PII-related features simplifies InfoSec compliance even in complex team structures.
  * Access is auditable and intentional — the policies are clear, traceable, and built for scale.


## Use cases

  * Grant a team of **senior data engineers** edit access to all sources and destinations in a production workspace so that they can modify and troubleshoot production pipelines.
  * Allow an individual **marketer** to configure tools like Braze or Adobe Analytics without touching technical features like [Transformations](<https://www.rudderstack.com/docs/transformations/overview/>).
  * Let **developers** build and test specific Transformations without the ability to connect them to Destinations.
  * Use **Groups** to define permissions for a list of users and workspaces.


## How it works

RudderStack’s Access Management system is based on **permissions** , which are bundled into **workspace policies** and ultimately rolled up into an individual member’s **access policy**.

[![How Access Management works](/docs/images/access-management/how-access-management-works.webp)](</docs/images/access-management/how-access-management-works.webp>)

### 1\. Workspace context

Access evaluation begins in the context of a specific workspace, where policies are defined and applied (for example, a **Prod** or **Dev** workspace).

### 2\. Gather applicable policies

RudderStack gathers all policies assigned to a member:

  * **Baseline Workspace Policy** : Applies to every member and group in the workspace.
  * **Group Workspace Policies** : Inherited from any groups the member belongs to.
  * **Member Workspace Policy** : Directly assigned to the individual member.


### 3\. Union of permissions

The system combines **all** permissions from the above policies into a single **Access Policy**. This is an **additive model** — permissions are only added, never overridden or removed.

### 4\. Result: Effective permissions

The resulting access policy defines what the member can or cannot do in the workspace, that is, what resources they can access, configure, or edit.

## Get started

  1. Go to **Settings** > **Access Management** in your dashboard.
  2. Set up your **Baseline Workspace Policy** to define baseline permissions for the workspace.
  3. Create and assign **Group Policies** for specific roles like **Data Engineering** , **Marketing** , **Data Ops** , and more.
  4. Add **Member policies** for users with additional access needs.


See the following guides for more information on the different access policies:

  * Configure a [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>)
  * Configure [Group Workspace Policies](<https://www.rudderstack.com/docs/access-management/groups/>)
  * Configure [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>)


## Current limitations

The following features are not available in the Access Management (PBAC) system currently and will be added in future releases:

  * Users onboarded via [SCIM](<https://www.rudderstack.com/docs/user-guides/sso-setup/>) cannot be auto-assigned to groups — they will automatically inherit the permissions specified in the [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>).
  * You cannot tag or categorize resources for dynamic permissioning.
  * Admins cannot copy permission settings between workspaces, for example, from **Dev** to **Prod**.