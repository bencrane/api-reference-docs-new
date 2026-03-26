# Access Management FAQ

Frequently asked questions about RudderStack’s Access Management system, including migrating from the legacy RBAC system, working with access tokens, and troubleshooting.

* * *

  * __10 minute read

  * 


This FAQ covers common questions about RudderStack’s Access Management system, including the transition from the legacy Permissions Management (RBAC) system.

## General concepts

#### What’s the difference between RBAC and PBAC?

The legacy **Permissions Management (RBAC)** system used [role-based access control](<https://www.rudderstack.com/docs/access-management/glossary/#role-based-access-control-rbac>), which assigned predefined roles that bundled permissions together. You couldn’t customize what each role could do.

The new **Access Management** system uses [Policy-based Access Control (PBAC)](<https://www.rudderstack.com/docs/access-management/glossary/#policy-based-access-control-pbac>), which allows granular, independent control of specific actions (**Edit** , **Connect** , **Create & Delete**) on individual resources. This gives Admins the flexibility to grant only the exact permissions needed without over-provisioning access.

Aspect| Legacy RBAC system| Access Management system  
---|---|---  
Permission granularity| Fixed role bundles| Individual permissions  
Resource-level control| Limited| Full support  
Custom roles| Not available| Create via Groups  
PII restrictions| Not available| Enterprise feature  
  
#### Why should I migrate to Access Management?

Access Management offers several advantages over the legacy RBAC system:

  * **Granular control** : Assign specific permissions to specific resources instead of broad role-based access.
  * **Additive model** : Permissions stack naturally through Baseline, Group, and Member policies without confusion.
  * **Custom roles via Groups** : Define reusable permission sets for teams like “Data Engineers” or “Marketing.”
  * **Scalability** : Manage enterprise workspaces efficiently with policy inheritance.
  * **PII controls** : Restrict sensitive data access (Enterprise plan).
  * **Clear audit trails** : Easier to understand who has what access and why.


#### How does the additive permissions model work?

Permissions from three levels combine to create a member’s effective access:
    
    
    Baseline Workspace Policy (applies to all users with access to the workspace)
            +
    Group Workspace Policies (if member is in groups)
            +
    Member Workspace Policy (individual customizations)
            =
    Final Access Policy
    

Permissions only **add** — they never subtract or override. This ensures minimum necessary access while allowing targeted expansion.

> ![info](/docs/images/info.svg)
> 
> If a member inherits **Edit** permission on sources from the baseline policy, **Connect** permission from their group policy, and **Create & Delete** from their member policy, they end up with all three permissions combined.

#### What’s the relationship between permissions, policies, and access policies?

  * **Permissions** are individual actions: Edit, Connect, Create & Delete.
  * **Workspace Policies** bundle permissions together and can be applied at three levels: Baseline, Group, or Member.
  * An **Access Policy** is the effective set of permissions a specific member has, calculated by combining their Baseline, Group, and Member workspace policies.


#### What’s a workspace in the context of Access Management?

A workspace is an isolated environment (like **Prod** or **Dev**) with its own access policies and resources. Each workspace has its own:

  * Baseline Workspace Policy
  * Group Workspace Policies
  * Member Workspace Policies


Access Management operates at the workspace level, meaning permissions are scoped to specific workspaces. A member can have different permissions in different workspaces.

## Policies and permissions

#### How do multiple policies stack and combine?

All applicable policies are merged into a **union**. There’s no conflict resolution needed because permissions only accumulate.

**Example:**

  * Baseline grants: View on all sources
  * Group grants: Edit on all sources
  * Member grants: Create & Delete on specific sources


**Result:** Member can View all sources, Edit all sources, and Create & Delete specific sources.

#### Where can I find my access policy for the workspace?

Go to **Settings** > **Your Profile** > **Access Policy** to see your access policy for the workspace. Here you can see the permissions for various resources in the workspace, including PII.

#### Can I override or remove a baseline policy permission?

No — the [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>) represents the minimum access floor for everyone in a workspace. Once a permission is granted at the baseline level, it cannot be removed at group or member levels. You can only add permissions on top of the baseline.

> ![warning](/docs/images/warning.svg)
> 
> Admins should adopt a “minimum necessary access” principle when configuring the baseline policy — start restrictive and add permissions selectively via groups and member policies.

#### What happens when policies seem to conflict?

In the additive model, there are no true conflicts — permissions combine. However, if you grant broader permissions at baseline (like Edit all sources) and later want to restrict someone, you’ll need to reconfigure the baseline (which affects everyone).

**Best practice:** Keep baseline permissions minimal and grant additional access through Groups or Member policies.

#### Can I assign different policies to the same member for different workspaces?

Yes — each member has separate workspace policies for each workspace they’re assigned to. For example:

  * A marketer might have Edit permissions on Destinations in the **Prod** workspace
  * The same marketer might have full access in the **Dev** workspace


#### What resources can be controlled with granular permissions?

You can control permissions for:

  * Event Stream Sources
  * Destinations
  * Transformations and Transformation Libraries
  * Tracking Plans
  * Data Catalog
  * Reverse ETL sources (Tables, SQL Models, Audiences)
  * Profiles
  * Bot Management
  * Credentials
  * Alerts, and more


Most resources also support **granular resource-level restrictions** , allowing you to grant **Edit** permission for only specific sources, destinations, etc.

See the [Policies Overview](<https://www.rudderstack.com/docs/access-management/policies-overview/>) guide for more information on the resources that you can control using granular permissions.

## Migration

#### Will my existing permissions be preserved during migration?

It depends on your **import strategy** :

  * **Use existing policies** : RudderStack maps each user’s legacy roles to their individual Member Workspace Policy, preserving their current access.
  * **Start fresh** : Members get only baseline view-only permissions, and you rebuild policies from scratch.


> ![info](/docs/images/info.svg)
> 
> RudderStack migrates the existing Service Access Tokens with their current permissions regardless of the import strategy.

#### Can I roll back after migration?

No — **migration is irreversible**. Once deployed, the legacy RBAC system is no longer available.

> ![warning](/docs/images/warning.svg)
> 
> Carefully review all staged policies before clicking **Deploy**. The staging area lets you preview and adjust everything before the permanent switch.

#### How long does migration take?

The migration process involves three stages that you control:

  1. **Import** : Import members and tokens (automated)
  2. **Configure** : Adjust policies in the staging area
  3. **Deploy** : Activate the new system (instant)


You control the timeline by choosing when to deploy.

#### Does migration happen at workspace level or organization level?

Migration happens at the **organization level** — it applies to all workspaces in your organization simultaneously. You cannot migrate individual workspaces separately.

> ![info](/docs/images/info.svg)
> 
> For multi-workspace organizations, align policies across all workspaces before deployment.

#### What’s the staging area and why does it matter?

The staging area is a preview environment where you configure new policies before going live. Your existing (legacy) permissions remain active until you deploy.

This lets you:

  * Review the migration mapping
  * Make adjustments to policies
  * Verify everything looks correct
  * Reset and re-import if needed


Once you click **Deploy** , the staging area becomes live and permanently replaces the legacy system.

#### How are legacy user roles mapped to the new system?

Legacy roles are mapped to individual Member Workspace Policies:

Legacy role| New permissions  
---|---  
Connections Admin| **Edit** , **Connect** , **Create & Delete** on all resources  
Connections Editor| **Edit** and **Connect** only  
Connections Viewer| No permissions beyond the [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>)  
  
> ![info](/docs/images/info.svg)
> 
> RudderStack **preserves** resource-level restrictions from the legacy system in the new system.

#### What happens to resource-level permissions during migration?

If a user had edit access restricted to only 10 out of 100 sources in the legacy system, their Member Workspace Policy will be configured to grant Edit permission for exactly those 10 sources after migration. RudderStack analyzes and replicates these restrictions.

#### How are Personal Access Tokens handled during migration?

Personal Access Tokens continue to inherit permissions from their associated user. Since user permissions are migrated to Member Workspace Policies, tokens automatically reflect those policies.

  * **Read-Only** and **Read-Write** scopes continue to work as before
  * You **cannot** create new Admin-scoped PATs (existing ones continue to work)


#### How are Service Access Tokens migrated?

RudderStack **always** migrates Service Access Tokens (SATs) with their current permissions. If a SAT had the **Admin** role, it gets mapped to an equivalent workspace policy with full resource permissions.

RudderStack automatically migrates SATs and they don’t require manual remapping.

#### What happens to new members added after migration?

New members automatically inherit the [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>) of each workspace they join. They don’t inherit individual or group policies unless explicitly assigned to those groups.

## Tokens

#### When should I use Personal Access Tokens (PAT) vs Service Access Tokens (SAT)?

Use case| Recommended token  
---|---  
Development and testing| PAT  
Personal tool integrations| PAT  
Production data pipelines| SAT  
Automated workflows (Airflow, etc.)| SAT  
Multi-person shared access| SAT  
Audit requirements| SAT  
  
> ![warning](/docs/images/warning.svg)
> 
> Personal Access Tokens are tied to individual users and break if that user leaves the organization. Use Service Access Tokens for any production use case to ensure continuity.

#### What permissions can PATs have?

PATs can have **Read-Only** or **Read-Write** scope:

  * **Read-Only** : Can only view resources
  * **Read-Write** : Can view and modify resources (within user’s permissions)


**Important:** PATs inherit the permissions of the user who created them, constrained by the scope. A **Read-Write** PAT cannot grant more permissions than the user has.

> ![info](/docs/images/info.svg)
> 
> You cannot generate new **Admin-scoped** PATs. Existing Admin PATs will continue to work.

#### What permissions can workspace-level SATs have?

Workspace-level SATs have **fully configurable permissions** — you can grant Edit, Connect, and Create & Delete on specific resources, just like member policies.

> ![warning](/docs/images/warning.svg)
> 
> Once created, you **cannot edit** a workspace-level SAT’s access policy. You must delete and recreate it if permissions need to change.

#### What’s the difference between organization-level and workspace-level SATs?

Aspect| Organization-level SAT| Workspace-level SAT  
---|---|---  
Scope| Entire organization| Single workspace  
Use cases| SSO SCIM provisioning, Audit Log API| Workspace-level resource management and API access  
Permissions| Admin-level| Configurable  
Create in| Organization settings| Workspace settings  
  
Use organization-level SATs **only** for SSO SCIM and Audit Log API access — you cannot use them for workspace operations.

## Setup and configuration

#### How do I get started configuring Access Management?

  1. **Set up the Baseline Workspace Policy** : Define minimum permissions everyone in the workspace should have.
  2. **Create Groups** : Define custom roles like “Data Engineers” or “Marketers” with appropriate permissions.
  3. **Configure Group Policies** : Assign permissions to each group per workspace.
  4. **Customize Member Policies** : Add individual exceptions for users needing special access.


> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Start with minimum baseline access and expand as needed. See the following guides for detailed steps:
> 
>   * [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>)
>   * [Group Policies](<https://www.rudderstack.com/docs/access-management/groups/>)
>   * [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>)
> 


#### What’s the “minimum necessary access” principle and why is it important?

This principle means setting the baseline policy to grant only the minimum permissions needed for everyone. It’s important because:

  * The baseline applies to **everyone** in the workspace
  * Permissions are **additive** — you can’t remove baseline permissions later
  * Setting a broad baseline means everyone gets that access


**Best practice:** Start restrictive, add permissions selectively through Groups and Member policies.

#### Can I use groups to define custom roles?

Yes — [Groups](<https://www.rudderstack.com/docs/access-management/groups/>) let you create custom roles and assign consistent policies to all group members. Examples:

  * **Data Engineers** : Full access to sources and transformations
  * **Marketers** : Edit access to specific destinations
  * **Data Analysts** : View access with PII restrictions


All members in a group automatically inherit that group’s [workspace policy](<https://www.rudderstack.com/docs/access-management/groups/#configure-group-workspace-policy>).

#### What are the plan-wise limits for groups and members?

Feature| Free/Starter| Growth| Enterprise  
---|---|---|---  
Groups| Not available| 3 per org| Unlimited  
Members| 10 per org| Unlimited| Unlimited  
PII permissions| N/A (full access)| N/A (full access)| Full control  
Custom baseline| No| No| Yes  
  
## Troubleshooting

#### Why was my access denied?

Access is determined by combining Baseline + Group + Member policies. If denied, you may lack the required permission on that specific resource. Check if:

  * Does your **Baseline Workspace Policy** grant the permission?
  * Are you in a **Group** with that permission?
  * Is the permission in your **Member Workspace Policy**?
  * For connections: Do you have both **Edit** and **Connect** on **both** resources?
  * For PII access: Do you have the specific **PII permission** (Enterprise only)?


RudderStack’ shows tooltips if you lack permissions. Admins can view each member’s effective policy in **Settings > Access Management > Users**.

#### What’s the difference between Edit, Connect, and Create & Delete permissions?

Permission| What it allows  
---|---  
**Edit**|  Modify configuration of existing resources  
**Connect**|  Connect two resources together (requires **Edit** \+ **Connect** on both)  
**Create & Delete**| Create new resources or delete existing ones  
  
These are independent — you can have Edit without Create & Delete, or Connect without either.

> ![info](/docs/images/info.svg)
> 
> To connect a source to a destination, you need **Edit** and **Connect** permissions on **both** the source and the destination.

#### Are PII permissions only for Enterprise?

Yes — Enterprise plans can control who sees Personally Identifiable Information in:

  * Live events
  * Failure samples
  * Event payloads


Non-Enterprise plans grant full PII access to all members by default. This is a key security feature for regulated industries.

#### Can I copy policies between workspaces?

No — there’s no built-in feature to copy a Dev workspace policy to Prod. Admins must manually configure each workspace’s baseline and group policies.

> ![info](/docs/images/info.svg)
> 
> This is identified as a future enhancement. For now, document your policy configurations to ensure consistency across workspaces in your organization.