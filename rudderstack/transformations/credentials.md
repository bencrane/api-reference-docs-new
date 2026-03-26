# Transformation Credentials

Securely store configuration data like user secrets and API keys and reuse them in transformations.

Available Plans

  * starter
  * growth
  * enterprise


* * *

  *  __3 minute read

  * 


The credential store is a central repository in the [RudderStack dashboard](<https://app.rudderstack.com/>) for securely storing and efficiently managing your configuration data.

> ![success](/docs/images/tick.svg)
> 
> By storing secrets and variables in RudderStack’s credential store, you can avoid hardcoding sensitive information in your transformations and avoid any security risks.

## Credentials overview

RudderStack supports two types of credentials - **Secrets** and **Variables**.

Credential| Description| Examples  
---|---|---  
Secret| Lets you store sensitive information as encrypted text values and use them as environment variables in your [transformations](<https://www.rudderstack.com/docs/transformations/overview/>).  
  
Note that you **cannot** see the secrets in the dashboard after setting them.| Passwords, app secrets, API tokens.  
Variable| Lets you store non-sensitive configuration data as non-encrypted strings.| Application configuration, paths.  
  
## Access credential store

Go to **Settings** > **Workspace** > **Credentials** to access the credential store and create your secrets and variables.

> ![info](/docs/images/info.svg)
> 
> This tab is visible in only the RudderStack [Starter, Growth, and Enterprise](<https://www.rudderstack.com/pricing/>) plans.

[![RudderStack credential store](/docs/images/dashboard-guides/credential-store.webp)](</docs/images/dashboard-guides/credential-store.webp>)

## Required permissions

  * [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have full access to create and manage secrets and variables in the credential store
  * [Members](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) must have the [**Credential Store**](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) permission in their workspace policy


**Click here to see how these permissions appear in the workspace policy**.  
![Permissions to manage credential store in RudderStack dashboard](/docs/images/access-management/credential-store.webp)  


#### Permissions for legacy RBAC system

In the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), only [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) and members with the [**Connections Admin** role](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#connections>) in their workspace policy can access and manage secrets and variables in the credential store.

[![Credential store permissions in the legacy framework](/docs/images/access-management/tracking-plan-permissions-legacy-framework.webp)](</docs/images/access-management/tracking-plan-permissions-legacy-framework.webp>)

## Create secrets

  1. Go to the **Secrets** tab of the credential store.
  2. Click **New secret**.
  3. Enter the secret name and value.


> ![warning](/docs/images/warning.svg)
> 
> Secret names can contain only alphanumeric characters and underscores and they cannot start with a number.

  4. Click **Add** to save the secret.

[![Create secret in credential store](/docs/images/features/transformations/credentials/create-secret.webp)](</docs/images/features/transformations/credentials/create-secret.webp>)

To edit a secret, click the edit icon, enter the new secret value, and click **Save**. Note that the previous secret value will **not** be visible.

[![Edit secret in credential store](/docs/images/features/transformations/credentials/edit-secret.webp)](</docs/images/features/transformations/credentials/edit-secret.webp>)

## Create variables

  1. Go to the **Variables** tab of the credential store.
  2. Click **New variable**.
  3. Enter the variable name and value.


> ![warning](/docs/images/warning.svg)
> 
> Note the following:
> 
>   * Variable names must contain only alphanumeric characters and underscores.
>   * They cannot start with a number.
>   * The name must not exceed 2048 characters.
> 


  4. Click **Add** to save the variable.

[![Create secret in credential store](/docs/images/features/transformations/credentials/create-variable.webp)](</docs/images/features/transformations/credentials/create-variable.webp>)

To edit a variable, click the edit icon, enter the new value, and click **Save**.

## Use credentials in transformations

Once you create the credentials in the credential store, you can reuse them by referencing them within the `getCredential()` function in your transformations.

See [Runtime Functions in Transformations](<https://www.rudderstack.com/docs/transformations/runtime-functions/#getCredential>) for more information on using the `getCredential` function.

Note the following while using credentials in transformations:

  * Any workspace member can use the credentials in their transformations.
  * You **cannot** use credentials in [transformation libraries](<https://www.rudderstack.com/docs/transformations/libraries/>).
  * `getCredential` is a restricted keyword in transformations. You must not use it for naming functions or variables.
  * RudderStack drops the event in case of any error while [using the `getCredential` function](<https://www.rudderstack.com/docs/transformations/runtime-functions/#getCredential>) in a transformation that is connected to a destination.


> ![warning](/docs/images/warning.svg)
> 
> Do not log or embed secrets in the event payload from the transformation.
> 
> All workspace users (including read-only users) have access to the transformation logs and live events and can get access to these secrets if you do not handle them properly in the transformation.