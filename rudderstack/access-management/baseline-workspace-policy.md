# Manage Baseline Workspace Policy

Manage the baseline policy applicable for each workspace within your RudderStack organization.

Available Plans

  * enterprise


* * *

  *  __3 minute read

  * 


This guide explains how to manage the baseline policy applicable for each workspace within your RudderStack organization.

## Overview

The **Baseline Workspace Policies** tab lists all the workspaces available in your RudderStack organization along with details like number of groups and members within each workspace. Each workspace has one baseline policy.

[![Baseline workspace policies tab](/docs/images/access-management/baseline-workspace-policies-tab.webp)](</docs/images/access-management/baseline-workspace-policies-tab.webp>)

This tab also lets you configure and manage the baseline policy applicable to each workspace in your RudderStack organization. All the groups, members, and [Service Access Tokens](<https://www.rudderstack.com/docs/access-management/service-access-tokens/>) in that workspace automatically inherit this baseline policy.

For example, an Admin can give every member the ability to create sources and destinations for testing purposes in the **Dev** workspace.

### Use cases

Baseline workspace policies are useful for configuring permissions that should apply **by default** across an entire workspace. Some common use cases include:

  * Increasing access in **Dev** workspaces to streamline testing and troubleshooting
  * Ensuring restricted access in **Prod** workspaces to protect production pipelines and PII
  * Enabling self-serve configuration of low-impact resources (like [Alerts](<https://www.rudderstack.com/docs/data-governance/alerts/>))


#### Examples

  * Give every member the ability to create sources and destinations for testing purposes in the **Dev** workspace.
  * Give access to Live Events PII permissions in **Dev** workspace so that anyone in the workspace can test and troubleshoot, but restrict Live Events access in **Prod** to ensure InfoSec compliance.
  * Grant permissions for Alert Overrides so that different team members can configure resource-specific notifications that are relevant to their role/team.


Instead of editing each individual member’s policy or even creating a group for such use cases, they can simply configure a baseline policy to grant the [required permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#edit-connect-and-create--delete-permissions>) within that workspace.

### Plan-wise limits

Not all RudderStack plans allow customizing the baseline workspace policy. See the [Plan-wise Features](<https://www.rudderstack.com/docs/access-management/plan-wise-features/#baseline-workspace-policy>) guide for more details on baseline workspace policy limits across different plans.

## Default behavior

Unless otherwise configured by an Admin, the baseline workspace policy is set to:

  * **View-only** for [resources](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>)
  * **No access** to [PII views](<https://www.rudderstack.com/docs/access-management/policies-overview/#pii-permissions>) in [Enterprise](<https://www.rudderstack.com/enterprise-quote/>) plan
  * **Full** PII access to all members in **non-Enterprise** plans


## Configure Baseline Workspace Policy

> ![warning](/docs/images/warning.svg)
> 
> See Important considerations before configuring your baseline workspace policy.

To configure a baseline workspace policy:

  1. Select a workspace.
  2. Use the policy editor to configure the baseline workspace policy for that workspace.


> ![info](/docs/images/info.svg)
> 
> All the groups, members, and Service Access Tokens in that workspace will automatically inherit the baseline workspace policy.

[![Configure baseline workspace policy](/docs/images/access-management/configure-baseline-workspace-policy.webp)](</docs/images/access-management/configure-baseline-workspace-policy.webp>)

  3. Configure permissions for different [resources](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) and [PII](<https://www.rudderstack.com/docs/access-management/policies-overview/#pii-permissions>).
  4. Click **Save** to save the configuration and enforce the baseline workspace policy.


## Important considerations

In RudderStack’s Access Management system, the permissions are [additive](<https://www.rudderstack.com/docs/access-management/concepts/#additive-permissions-model>), meaning users inherit all permissions granted to them via the baseline workspace policy, [Group Workspace Policy](<https://www.rudderstack.com/docs/access-management/groups/>), and [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>). Permissions are accumulated, never overridden or subtracted.

When configuring a baseline workspace policy, RudderStack recommends adopting a **minimum necessary access** principle. This ensures that onboarding users with restricted access needs (like contractors or external collaborators) can be done without major rework later on.

> ![danger](/docs/images/danger.svg)
> 
> Adjusting an established baseline workspace policy later can cause broad ripple effects across your organization. It may affect the permissions of existing users and require substantial effort and rework to restore the intended security and access levels.