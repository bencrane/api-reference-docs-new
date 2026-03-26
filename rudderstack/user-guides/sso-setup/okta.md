# Okta SSO Setup

Set up the RudderStack SSO (Single Sign-On) feature with Okta.

Available Plans

  * enterprise


* * *

  *  __4 minute read

  * 


The [Okta RudderStack app](<https://www.okta.com/integrations/rudderstack/>) is available on the **Okta Integration Network (OIN)**. This guide lists the steps to set up the integration.

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * RudderStack supports only the [SAML 2.0 protocol](<https://auth0.com/intro-to-iam/what-is-saml>) for SSO.
>   * You can refer to the [Okta Manual Setup](<https://www.rudderstack.com/docs/user-guides/sso-setup/okta/manual-setup/>) guide to manually configure and enable Okta SSO for your organization.
>   * If you are anticipating any changes to your SSO like email change, make sure to [contact RudderStack support](<mailto:support@rudderstack.com>) in advance to avoid any login issues.
> 


## Supported features

The Okta-RudderStack SAML integration supports the following features:

  * SP-initiated SSO
  * JIT(Just In Time) Provisioning


For more information on these features, see [Okta Glossary](<https://help.okta.com/en/prod/Content/Topics/Reference/glossary.htm>).

Also, it supports the following SAML attributes:

Name| Value  
---|---  
FirstName| user.firstName  
LastName| user.lastName  
Email| user.email  
  
## Step 1: Add the RudderStack SSO SAML 2.0 app

> ![warning](/docs/images/warning.svg)
> 
> Before you enable SAML, note that:
> 
>   * Your users will not be able to sign in to RudderStack through their regular sign-in page once SAML is enabled. They will be able to access RudderStack only through the Okta service.
>   * RudderStack **does not** provide a backup sign-in URL where users can log in with their username and password.
>   * You can contact [RudderStack support](<mailto:support@rudderstack.com>) to disable SAML, if required.
> 


  1. [Log in to Okta](<https://www.okta.com/login/>) as an administrator.
  2. Go to the [RudderStack SSO integration page](<https://www.okta.com/integrations/rudderstack/>). Then, click **Add Integration** :

[![Add Integration](/docs/images/user-guides/rudderstack-okta-sso-1.webp)](</docs/images/user-guides/rudderstack-okta-sso-1.webp>)

  3. Select the account under **Choose an account**.
  4. Set the **Application Label** (your preferred application name) and the **Application Visibility**. Check the **Do not display application icon to users** and **Do not display application icon in the Okta Mobile App** settings, as shown. Then, click **Next**.


> ![warning](/docs/images/warning.svg)
> 
> Since the integration supports only SP-initiated flow, hiding the application icon for the users is highly recommended.

[![Application name and visibility](/docs/images/user-guides/rudderstack-okta-sso-2.webp)](</docs/images/user-guides/rudderstack-okta-sso-2.webp>)

> ![info](/docs/images/info.svg)
> 
> You need to check the **Do not display application icon to users** and **Do not display application icon in the Okta Mobile App** settings as this app will not be visible to your users.

  5. Under **Sign on methods** , choose **SAML 2.0**.
  6. Under **Metadata details** , copy the **Metadata URL**.
  7. Under **Credentials Details** , set **Application username format** to **Email**. Retain the rest of the settings and click **Done**.

[![SAML 2.0 configuration](/docs/images/user-guides/rudderstack-okta-sso-8.webp)](</docs/images/user-guides/rudderstack-okta-sso-8.webp>)

  8. Share the **Metadata URL** copied above with the [RudderStack team](<mailto:support@rudderstack.com>) to enable SAML 2.0 for your account.


## Step 2: Add the RudderStack SSO Bookmark app

> ![info](/docs/images/info.svg)
> 
> Your users will use this app to quickly access the [RudderStack dashboard](<https://app.rudderstack.com/>) using the SSO functionality.

To create the SSO bookmark app in Okta:

  1. Go to the [RudderStack SSO integration page](<https://www.okta.com/integrations/rudderstack/>). Then, click **Add Integration** :

[![Add Integration](/docs/images/user-guides/rudderstack-okta-sso-1.webp)](</docs/images/user-guides/rudderstack-okta-sso-1.webp>)

  2. Set the **Application Label** that you set previously. Then, click **Next**.


> ![warning](/docs/images/warning.svg)
> 
> Do not check the **Do not display application icon to users** and **Do not display application icon in the Okta Mobile App** settings as this app will be visible to your users.

[![Application name and visibility](/docs/images/user-guides/rudderstack-okta-sso-5.webp)](</docs/images/user-guides/rudderstack-okta-sso-5.webp>)

  3. Under **Sign on methods** , choose **Bookmark-only**. Set the **Login URL** to `https://app.rudderstack.com/sso?domain=<your_website>`, where `<your_website>` is your organization’s web domain. Under **Credentials Details** , set **Application username format** to **Email**. Retain the rest of the settings and click **Done**.

[![Bookmark sign on method and Login URL](/docs/images/user-guides/rudderstack-okta-sso-9.webp)](</docs/images/user-guides/rudderstack-okta-sso-9.webp>)

## User authentication

Once you have set up SSO, the users can authenticate to RudderStack through any of the below approaches:

  * The bookmark app set up in Step 3.

  * SP-initated SSO by following these steps:

    1. Go to <https://app.rudderstack.com/sso>.
    2. Enter your email address and click **SIGN IN**.


## SCIM configuration

You can automatically grant RudderStack access to your users by [configuring SCIM provisioning](<https://www.rudderstack.com/docs/user-guides/sso-setup/okta/scim-configuration/>) in Okta.

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

RudderStack recommends initiating the SSO authentication by following all the above SSO configuration steps correctly.

As an alternative, you can simulate the IdP-initiation authentication flow by using the Okta Bookmark app and setting the **Login URL** to `https://app.rudderstack.com/sso?domain=<your_website>`, where `<your_website>` is your organization’s web domain.

[![SSO errors](/docs/images/user-guides/sso-errors-3.webp)](</docs/images/user-guides/sso-errors-3.webp>)

#### Required String parameter ‘RelayState’ is not present

[![SSO errors](/docs/images/user-guides/sso-errors-2.webp)](</docs/images/user-guides/sso-errors-2.webp>)

The above error indicates that you did not set up your SSO app correctly. Make sure to:

  * Set the **Audience URI (SP Entity ID)** field to `urn:amazon:cognito:sp:us-east-1_ABZiTjXia`.
  * Configure the other [SAML settings](<https://www.rudderstack.com/docs/user-guides/sso-setup/okta/manual-setup/#saml-settings>) correctly.


## FAQ

#### My organization’s email domain has changed from `abc.com` to `xyz.com` and now I am unable to log in. What should I do?

Contact [RudderStack support](<mailto:support@rudderstack.com>) to make the necessary changes to your SSO configuration.