# Service Access Tokens

Learn about Service Access Tokens and how they enable centralized, secure access to RudderStack APIs at the organization or workspace level.

Available Plans

  * starter
  * growth
  * enterprise


* * *

  *  __3 minute read

  * 


This guide explains the concept of **Service Access Tokens** in RudderStack’s Access Management system. It also describes the steps to generate them and manage their permissions.

## Overview

A **Service Access Token** (SAT) enables applications to access RudderStack APIs. It provides a flexible, secure, and centralized way for you to programmatically interact with resources and services in the RudderStack platform.

Unlike [Personal Access Tokens](<https://www.rudderstack.com/docs/access-management/personal-access-tokens/>) which are tied to individual users, SATs provide centralized access to resources within an organization or workspace, ensuring continuity and reducing the risk of disruptions when members are removed or their [roles](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) change.

Operations performed with SATs are logged and audited against the SAT, ensuring that activities are traceable to the token rather than an individual user.

## Personal Access Tokens vs. Service Access Tokens

Personal Access Tokens (PAT)| Service Access Tokens (SAT)  
---|---  
Tied to a specific user within a workspace.| Not tied to an individual user.  
Used for individual tasks and testing.| Used for centralized, shared access and production use cases.  
Any processes dependent on these tokens will break if the user is removed from the organization or a breaking change is made to their permissions.| Exist at an organization or workspace level, ensuring continuity in essential workflows and pipelines using these tokens.  
  
> ![info](/docs/images/info.svg)
> 
> RudderStack recommends using:
> 
>   * SATs for your **production** use cases that require shared access to the services and resources across the organization or workspace.
>   * PATs for **testing** a service/feature or **personal** use cases.
> 


## Service Access Token types

You can generate the following two types of SATs in RudderStack:

### Organization-level SATs

Organization-level SATs are associated with the entire organization and have [Admin](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) permissions by default.

You can use them **only** for authenticating your [SSO SCIM](<https://www.rudderstack.com/docs/user-guides/sso-setup/>) and [Audit Log API](<https://www.rudderstack.com/docs/api/audit-logs-api/>).

### Workspace-level SATs

Workspace-level SATs are linked to a specific workspace. Their usage is restricted to workspace-level resources (sources, destinations, transformations, Tracking Plans, etc.) and APIs.

> ![warning](/docs/images/warning.svg)
> 
> You cannot use workspace-level SATs to interact with organization-level functionalities like Audit Logs or SCIM provisioning.

## Generate Service Access Token

  1. Go to **Settings** > **Access Management** > **Service Access Tokens**.


> ![info](/docs/images/info.svg)
> 
> Only [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) can see the **Service Access Tokens** tab and **create** or **delete** Service Access Tokens.

[![Service Access Tokens tab in RudderStack dashboard](/docs/images/access-management/service-access-tokens/sat-tab.webp)](</docs/images/access-management/service-access-tokens/sat-tab.webp>)

  2. Click the **Organization** or **Workspace** tab depending on whether you want to generate an organization-level SAT or workspace-level SAT.


### Organization SAT

  1. In the **Organization** tab, click **Generate new token**.
  2. Enter the name of the SAT and click **Generate**.

[![Generate organization level Service Access Token in RudderStack dashboard](/docs/images/access-management/service-access-tokens/org-sat-generate.webp)](</docs/images/access-management/service-access-tokens/org-sat-generate.webp>)

  3. Note the token value.


> ![warning](/docs/images/warning.svg)
> 
> Secure the token — you will not be able to see it again once you click **Close**.

[![Organization level Service Access Token generated in RudderStack dashboard](/docs/images/access-management/service-access-tokens/org-sat-token.webp)](</docs/images/access-management/service-access-tokens/org-sat-token.webp>)

### Workspace SAT

  1. Under **Service Access Tokens** , click the **Workspace** tab.

[![Workspace tab in Service Access Tokens section](/docs/images/access-management/service-access-tokens/workspace-tab.webp)](</docs/images/access-management/service-access-tokens/workspace-tab.webp>)

  2. Click **Generate new token**.
  3. Enter the name of the SAT.
  4. Choose the relevant workspace (applicable for a multi-workspace organization) where the token will be applicable. Then, click **Next**.

[![Workspace level Service Access Token generation in RudderStack dashboard](/docs/images/access-management/service-access-tokens/workspace-sat-name.webp)](</docs/images/access-management/service-access-tokens/workspace-sat-name.webp>)

  5. Under **Workspace SAT access policy** , configure the [access policy](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) for the token.


> ![warning](/docs/images/warning.svg)
> 
> **Important** : Once generated, you cannot edit the access policy of the workspace-level Service Access Token.

[![Workspace level Service Access Token access policy in RudderStack dashboard](/docs/images/access-management/service-access-tokens/workspace-sat-policy.webp)](</docs/images/access-management/service-access-tokens/workspace-sat-policy.webp>)

  6. Click **Generate** to generate the token.
  7. Note the token and use it in the relevant workspace-level APIs and services.


> ![warning](/docs/images/warning.svg)
> 
> Secure the token value — you will not be able to see it again once you click **Close**.

[![Workspace level Service Access Token generated in RudderStack dashboard](/docs/images/access-management/service-access-tokens/workspace-token-generated.webp)](</docs/images/access-management/service-access-tokens/workspace-token-generated.webp>)

## Migration of old Service Access Tokens

When you [migrate to the new Access Management system](<https://www.rudderstack.com/docs/access-management/migration-steps/>), the previously-created Service Access Tokens are automatically imported with their current permissions.

See the [Migration Scenarios](<https://www.rudderstack.com/docs/access-management/migration-examples/>) guide for detailed examples of how Service Access Tokens are migrated to the new Access Management system.