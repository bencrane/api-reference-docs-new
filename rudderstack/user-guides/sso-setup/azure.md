# Microsoft Azure Entra ID (formerly Azure AD) SSO Setup

Set up the RudderStack SSO (Single Sign-On) feature with Microsoft Azure Entra ID.

Available Plans

  * enterprise


* * *

  *  __5 minute read

  * 


This guide lists the steps to set up your Azure Entra ID SAML integration with RudderStack.

## Overview

This integration supports the following features:

  * SP-initiated SSO
  * JIT(Just In Time) Provisioning


> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * RudderStack supports only the [SAML 2.0 protocol](<https://auth0.com/intro-to-iam/what-is-saml>) for SSO.
>   * RudderStack does not support some SCIM features like importing users and groups, removing users, and syncing passwords. See Known issues before you set up SSO for your organization.
> 


## Step 1: Create new application

  1. Sign in to [Microsoft Entra ID Admin Center](<https://entra.microsoft.com/>).
  2. From the left sidebar, go to **Applications** > **Enterprise applications**.
  3. Under **Manage** , click **All applications** followed by **New application**.

[![New application option](/docs/images/user-guides/azure-sso/rudderstack-azure-sso-1.webp)](</docs/images/user-guides/azure-sso/rudderstack-azure-sso-1.webp>)

  4. In the **Microsoft Entra App Gallery** , click **Create your own application**.

[![Create your own application option](/docs/images/user-guides/azure-sso/rudderstack-azure-sso-2.webp)](</docs/images/user-guides/azure-sso/rudderstack-azure-sso-2.webp>)

  5. In the expanded right sidebar, enter the name of your app.
  6. Under **What are you looking to do with your application?** , select **Integrate any other application you don’t find in the gallery (Non-gallery)**.

[![Initial configuration](/docs/images/user-guides/azure-sso/rudderstack-azure-sso-3.webp)](</docs/images/user-guides/azure-sso/rudderstack-azure-sso-3.webp>)

  7. Click the **Create** button at the bottom and wait for a few seconds for Azure to provision the app. You will then be redirected to the admin view of the app.


## Step 2: Set up SAML

  1. In the left sidebar of the newly provisioned app, click **Single sign-on** under **Manage**. Then, click **SAML**.

[![SAML SSO method](/docs/images/user-guides/azure-sso/rudderstack-azure-sso-5.webp)](</docs/images/user-guides/azure-sso/rudderstack-azure-sso-5.webp>)

  2. Click the meatballs menu (`...`) to the right of **Basic SAML Configuration**. In the expanded right sidebar, fill in the following information:

Field| Value  
---|---  
Identifier (Entity ID)  
Required| `urn:amazon:cognito:sp:us-east-1_ABZiTjXia`  
Reply URL (Assertion Consumer Service URL)  
Required| `https://auth2.rudderstack.com/saml2/idpresponse`  
Sign on URL  
Required| `https://app.rudderstack.com/sso?domain=<YOUR_EMAIL_DOMAIN>`  
  


> ![info](/docs/images/info.svg)Replace `<YOUR_EMAIL_DOMAIN>` with your organization’s email domain.  
>   
> **Note** : Specify only a single email domain for the `<YOUR_EMAIL_DOMAIN>` parameter — no comma-separated list or array of domains is allowed.  
  
Relay State| -  
  
  3. Click the meatballs menu (`...`) to the right of **Attributes & Claims** and remove any **Additional claims**. Then, click **Add new claim** and enter the following information:

Field| Value| Notes  
---|---|---  
Email| `user.mail`| -  
LastName| `user.displayname`| Choose your preferred name, for example, display name or surname.  
Unique User Identifier| `user.userprincipalname`| -  
  
  4. Copy the **App Federation Metadata URL** and share it with the [RudderStack team](<mailto:support@rudderstack.com>).

[![Metadata URL](/docs/images/user-guides/azure-sso/rudderstack-azure-sso-8.webp)](</docs/images/user-guides/azure-sso/rudderstack-azure-sso-8.webp>)

## Step 3: Set up SCIM

This section lists the steps to set up SCIM provisioning in Azure Entra ID.

### Prerequisites

Before setting up SCIM provisioning, make sure to generate an [organization-level Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#organization-sat>) in the RudderStack workspace for which you want to enable SCIM.

> ![warning](/docs/images/warning.svg)
> 
> Make sure to create an **organization-level** Service Access Token. Otherwise, your SCIM provisioning tasks will fail.

#### Token permissions for legacy RBAC system

If you are on the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), generate an [Organization-level Service Access Token](<https://www.rudderstack.com/docs/archive/dashboard-guides/service-access-tokens/#generate-service-access-token>).

### SCIM configuration

  1. In the left sidebar of your app, go to **Manage** > **Provisioning** > **Get started**.

[![Provisioning](/docs/images/user-guides/azure-sso/rudderstack-azure-sso-9.webp)](</docs/images/user-guides/azure-sso/rudderstack-azure-sso-9.webp>)

  2. Under **Provisioning Mode** , choose **Automatic** and enter the following credentials:

Field| Value  
---|---  
Tenant URL  
Required| `https://api.rudderstack.com/scim/v2`  
Secret Token| Your Service Access Token obtained in the Prerequisites section.  
[![Provisioning](/docs/images/user-guides/azure-sso/rudderstack-azure-sso-10.webp)](</docs/images/user-guides/azure-sso/rudderstack-azure-sso-10.webp>)

  3. Click **Test Connection** \- it should be successful.


> ![announcement](/docs/images/announcement.svg)
> 
> If you see a `403 - Forbidden` error, contact the [RudderStack team](<mailto:support@rudderstack.com>) to enable SCIM for your organization.

## Enable SSO login

RudderStack does not support IdP-initiated authentication. Make sure the users log in through `https://app.rudderstack.com/sso`.

## Known issues

RudderStack does not support the following SCIM features currently:

  * Import users
  * Import groups
  * Push groups (coming soon)
  * Remove users
  * Sync password
  * Enhanced group push


> ![warning](/docs/images/warning.svg)
> 
> RudderStack does not support removing users - this is because it uses SCIM with SAML, where removing a user from Azure Entra ID implies that they also lose the ability to authenticate to RudderStack completely (logins via passwords, Google, etc. are completely blocked).
> 
> Instead, RudderStack supports deactivating the user which means they only lose access to the organization.

## Debugging

There are times when an SSO login might fail for some users due to some reason. In such cases, the RudderStack team requires a HAR (HTTP Archive) file to inspect the requests and identify any SSO-related issues.

> ![info](/docs/images/info.svg)
> 
> A HAR file is a log of exported network requests from the user’s browser. See the [HAR Analyzer](<https://toolbox.googleapps.com/apps/har_analyzer/>) guide for steps on generating this file depending on your browser.

Once you generate the HAR file, share it with the [RudderStack team](<mailto:support@rudderstack.com>) to troubleshoot the issue.

> ![warning](/docs/images/warning.svg)
> 
> Note the following before capturing your HAR file:
> 
>   * Start from `https://app.rudderstack.com/sso` with a clean session, preferably in incognito mode of your browser.
>   * Complete the SSO flow until the step where you face an error.
>   * Your HAR file might contain sensitive data - make sure to redact it using a text editor before sharing it with the team.
> 


The following sections contain solutions for some common errors you might encounter while setting up SSO:

#### Invalid samlResponse or relayState from identity provider

[![SSO errors](/docs/images/user-guides/sso-errors-1.webp)](</docs/images/user-guides/sso-errors-1.webp>)

The above error indicates you tried the [IdP](<https://support.okta.com/help/s/article/okta-saml?language=en_US>)-initiated authentication flow. As stated above, this integration supports only Service Provider (SP)-initiated SSO flow.

RudderStack recommends initiating the SSO authentication by following all the above SSO configuration steps correctly and making sure the users log in through `https://app.rudderstack.com/sso`.

#### Required String parameter ‘RelayState’ is not present

[![SSO errors](/docs/images/user-guides/sso-errors-2.webp)](</docs/images/user-guides/sso-errors-2.webp>)

The above error indicates that you did not set up your SSO app correctly. Make sure to:

  * Set the **Identifier (Entity ID)** field to `urn:amazon:cognito:sp:us-east-1_ABZiTjXia`.
  * Under **Attributes & Claims**, set the **Email** field to `user.email`.
  * Configure the other SAML settings correctly.


## FAQ

#### My organization’s email domain has changed from `abc.com` to `xyz.com` and now I am unable to log in. What should I do?

Contact [RudderStack support](<mailto:support@rudderstack.com>) to make the necessary changes to your SSO configuration.