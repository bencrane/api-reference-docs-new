# Personal Access Tokens

Learn about Personal Access Tokens and how they enable individual users to authenticate and consume RudderStack APIs.

Available Plans

  * starter
  * growth
  * enterprise


* * *

  *  __3 minute read

  * 


> ![warning](/docs/images/warning.svg)
> 
> **Use Personal Access Tokens for development or testing purposes only.**
> 
> For production use cases, RudderStack recommends using the following over a Personal Access Token:
> 
>   * [Workspace-level Service Access Tokens](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#workspace-level-sats>) for working with workspace-level resources and APIs
>   * [Organization-level Service Access Tokens](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#organization-level-sats>) for working with [SSO SCIM](<https://www.rudderstack.com/docs/user-guides/sso-setup/>) and the [Audit Log API](<https://www.rudderstack.com/docs/api/audit-logs-api/>).
> 


This guide explains the concept of **Personal Access Tokens** in RudderStack’s Access Management system. It also describes the steps to generate a Personal Access Token and all the operations associated with it.

## Overview

To consume the public RudderStack APIs, you need a **Personal Access Token** (PAT). This access token is associated with an individual’s RudderStack account.

### Permissions

You can create and use Personal Access Tokens with the following scopes:

Token scope| Description  
---|---  
Read-Only| Access tokens will have read-only permissions.  
Read-Write| Access tokens will have both read-only and read-write permissions of the user.  
  


> ![info](/docs/images/info.svg)If a user having read-only permissions creates a **Read-Write** token, then the token will still have read-only permissions.  
  
Admin| 

> ![warning](/docs/images/warning.svg)Creation of new Personal Access Tokens with Admin scope is deprecated. However, any existing Admin PATs will continue to work as before, even after migration.  
  
## Personal Access Tokens vs. Service Access Tokens

Personal Access Tokens (PAT)| Service Access Tokens (SAT)  
---|---  
Tied to a specific user within a workspace.| Not tied to an individual user.  
Used for individual tasks and testing.| Used for centralized, shared access and production use cases.  
Any processes dependent on these tokens will break if the user is removed from the organization or a breaking change is made to their permissions.| Exist at an organization or workspace level, ensuring continuity in essential workflows and pipelines using these tokens.  
  
## Generate Personal Access Token

  1. Log in to your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Settings** > **Your Profile** and scroll down to **Personal Access Tokens**. Then, click **Generate new token** :

[![New Personal Access Token in RudderStack dashboard](/docs/images/rudderstack-api/personal-access-token.webp)](</docs/images/rudderstack-api/personal-access-token.webp>)

  3. Enter the **Token name** , select the **Workspace** and the **Scope** from the respective dropdowns:

[![Personal Access Token name and scope](/docs/images/rudderstack-api/personal-access-token-scope.webp)](</docs/images/rudderstack-api/personal-access-token-scope.webp>)

  4. Click **Generate**.
  5. Note the Personal Access Token value.


> ![warning](/docs/images/warning.svg)
> 
> Make sure to secure the generated token — the token value is not visible again once you close this window.

[![Personal Access Token details](/docs/images/rudderstack-api/personal-access-token-3.webp)](</docs/images/rudderstack-api/personal-access-token-3.webp>)

## Delete Personal Access Token

  1. Go to **Settings** > **Your Profile** and scroll down to **Personal Access Tokens**.
  2. Click the **Delete** option next to the token and confirm by clicking **Yes, delete**.


## Migrate old Personal Access Tokens

After migration, Personal Access Tokens:

  * **Inherit user permissions** : Personal Access Tokens continue to inherit the permissions of the user who created them. Since user permissions are migrated to their [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>), Personal Access Tokens automatically reflect those permissions.
  * **Maintain scope behavior** : Personal Access Tokens created with **Read-Only** or **Read-Write** scopes continue to work as before, with their effective permissions determined by the user’s [Individual Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>).


See the [Migration Scenarios](<https://www.rudderstack.com/docs/access-management/migration-examples/personal-access-tokens/>) guide for detailed examples of how Personal Access Tokens are migrated to the new Access Management system.