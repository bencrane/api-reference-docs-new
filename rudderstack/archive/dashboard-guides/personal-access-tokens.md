# Personal Access Tokens

Learn about Personal Access Tokens and how they enable individual users to authenticate and consume RudderStack APIs.

* * *

  * __2 minute read

  * 


This guide explains the concept of **Personal Access Tokens** in RudderStack. It also describes the steps to generate a Personal Access Token and all the operations associated with it.

## Overview

You can use Personal Access Tokens to authenticate and consume RudderStack APIs. This token is associated with an individual’s RudderStack account.

> ![warning](/docs/images/warning.svg)
> 
> Use Personal Access Tokens for development or testing purposes only. For production use cases, RudderStack recommends using a [Service Access Token](<https://www.rudderstack.com/docs/archive/dashboard-guides/service-access-tokens/>)

## Permissions

You can create and use Personal Access Tokens with the following scopes:

Token scope| Description  
---|---  
Read-Only| Access tokens will have read-only permissions.  
Read-Write| Access tokens will have both read-only and read-write permissions of the user.  
  


> ![info](/docs/images/info.svg)If a user having read-only permissions creates a **Read-Write** token, then the token will still have read-only permissions.  
  
Admin| 

> ![warning](/docs/images/warning.svg)Creation of new Personal Access Tokens with Admin scope is deprecated. However, any existing tokens with Admin scope will continue to work as before, even after migration.  
  
## Personal Access Tokens vs. Service Access Tokens

Personal Access Tokens (PAT)| Service Access Tokens (SAT)  
---|---  
Tied to a specific user within a workspace.| Not tied to an individual user.  
Used for individual tasks and testing.| Used for centralized, shared access and production use cases.  
Any processes dependent on these tokens will break if the user is removed from the organization or a breaking change is made to their permissions.| Exist at an organization or workspace level, ensuring continuity in essential workflows and pipelines using these tokens.  
  
## Generate Personal Access Token

  1. Log in to your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Settings** > **Your Profile** and scroll down to **Personal Access Tokens**. Then, click **Generate new token** :

[![New Personal Access Token in RudderStack dashboard](/docs/images/rudderstack-api/generate-personal-access-token-1.webp)](</docs/images/rudderstack-api/generate-personal-access-token-1.webp>)

  3. Enter the **Token name** , select the **Workspace** and the **Scope** from the respective dropdowns:

[![Personal Access Token name and scope](/docs/images/rudderstack-api/generate-personal-access-token-2.webp)](</docs/images/rudderstack-api/generate-personal-access-token-2.webp>)

  4. Click **Generate**.
  5. Note the Personal Access Token value.


> ![warning](/docs/images/warning.svg)
> 
> Make sure to secure the generated token — the token value is not visible again once you close this window.

[![Personal Access Token details](/docs/images/rudderstack-api/personal-access-token-3.webp)](</docs/images/rudderstack-api/personal-access-token-3.webp>)

## Delete Personal Access Token

  1. Go to **Settings** > **Your Profile** and scroll down to **Personal Access Tokens**.
  2. Click the **Delete** option next to the token and confirm by clicking **Yes, delete**.