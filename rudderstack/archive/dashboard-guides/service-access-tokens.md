# Service Access Tokens

Generate and manage organization and workspace-level service access tokens in RudderStack.

Available Plans

  * starter
  * growth
  * enterprise


* * *

  *  __3 minute read

  * 


> ![warning](/docs/images/warning.svg)
> 
> **This documentation is applicable for the legacy Permissions Management (RBAC) system.**
> 
> See [Service Access Tokens](<https://www.rudderstack.com/docs/access-management/service-access-tokens/>) for information on generating and managing Service Access Tokens in the new [Access Management (PBAC)](<https://www.rudderstack.com/docs/access-management/overview/>) system.

A **Service Access Token** (SAT) enables applications access to RudderStack APIs, providing a flexible, secure, and centralized way for you to programmatically interact with resources and services in the platform.

## Overview

Unlike [Personal Access Tokens](<https://www.rudderstack.com/docs/archive/dashboard-guides/personal-access-tokens/>) which are tied to individual users, Service Access Tokens provide centralized access to resources within an Organization or Workspace, ensuring continuity and reducing the risk of disruptions when members are removed or their [roles](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) change.

Operations performed with Service Access Tokens are logged and audited against the token, ensuring that activities are traceable to the token rather than an individual user.

> ![info](/docs/images/info.svg)
> 
> RudderStack recommends using:
> 
>   * Service Access Tokens for **production use cases** that require shared access to the services and resources across the organization or workspace.
>   * Personal Access Tokens for **testing** a service/feature or **personal use cases**.
> 


## Service Access Token types

You can generate the following two types of SATs in RudderStack:

### Organization-level SATs

Organization-level Service Access Tokens are associated with the entire organization and have the [Org Admin](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) permissions by default.

You can use these tokens **only** for authenticating your [SSO SCIM](<https://www.rudderstack.com/docs/user-guides/sso-setup/>) and the [Audit Log API](<https://www.rudderstack.com/docs/api/audit-logs-api/>).

### Workspace-level SATs

Workspace-level SATs are linked to a specific workspace. Their usage is restricted to workspace-level resources (Sources, Destinations, Transformations, Tracking Plans, etc.) and [APIs](<https://www.rudderstack.com/docs/api/>).

Workspace-level SATs **cannot** interact with organization-level functionalities like Audit Logs or SCIM provisioning.

## Generate Service Access Token

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * Only [Org admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) can **create** , **view** , and **delete** organization-level and workspace-level Service Access Tokens.
>   * The actual value of the Service Access Token is visible only to the creator at the time of creation.
>   * You can use the organization-level Service Access Token only for authenticating your [SSO SCIM](<https://www.rudderstack.com/docs/user-guides/sso-setup/>) and the [Audit Log API](<https://www.rudderstack.com/docs/api/audit-logs-api/>).
> 


  1. Go to **Settings** > **Organization** > **Service Access Tokens** tab.

[![Service Access Tokens tab in RudderStack dashboard](/docs/images/dashboard-guides/service-access-tokens/service-access-tokens.webp)](</docs/images/dashboard-guides/service-access-tokens/service-access-tokens.webp>)

  2. Click the **Organization** or **Workspace** tab depending on whether you want to generate an organization-level SAT or workspace-level SAT.
  3. Click **Generate new token**.


You will see the below settings depending on the tab chosen in Step 2:

  


  1. Enter the name of the SAT and click **Generate**.

![Generate new org level SAT](/docs/images/dashboard-guides/service-access-tokens/org-sat-generate.webp)

  2. Note the token value.

![Note org level SAT value](/docs/images/dashboard-guides/service-access-tokens/org-sat.webp)

> ![warning](/docs/images/warning.svg)
> 
> Make sure to secure the token. You will not be able to see it again once you click **Close**.

  


  1. Enter the name of the SAT.
  2. Choose the relevant workspace from the dropdown (applicable for a multi-workspace setup).
  3. Under **Token role and permissions** , assign the relevant permissions for the token. You can choose between **Admin** , **Editor** , or **Viewer** , depending on your requirement.


> ![warning](/docs/images/warning.svg)
> 
> Ensure proper assignment of roles and resource permissions to SATs to avoid unauthorized access to sensitive resources.

  4. Optionally, toggle on the **Grant edit access** setting to create, edit, or delete [Transformations](<https://www.rudderstack.com/docs/transformations/overview/>) using the token.
  5. Click **Generate**.

![Generate workspace level SAT](/docs/images/dashboard-guides/service-access-tokens/workspace-sat-generate.webp)

  6. Note the token and use it in the relevant workspace-level APIs and services.

![Create workspace level SAT](/docs/images/dashboard-guides/service-access-tokens/workspace-sat.webp)

> ![warning](/docs/images/warning.svg)
> 
> Make sure to secure the token. You will not be able to see it again once you click **Close**.