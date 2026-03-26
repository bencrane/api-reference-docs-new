# OneLogin SSO Setup

Set up the RudderStack SSO (Single Sign-On) feature with OneLogin.

Available Plans

  * enterprise


* * *

  *  __4 minute read

  * 


This guide lists the steps to configure and enable OneLogin SSO for your organization.

> ![info](/docs/images/info.svg)
> 
> RudderStack supports only the [SAML 2.0 protocol](<https://auth0.com/intro-to-iam/what-is-saml>) for SSO.

## Configure RudderStack SSO app

  1. Log into your [OneLogin portal](<https://app.onelogin.com/login>) and click **Administration** in the top menu:

[![Administration option in OneLogin](/docs/images/user-guides/onelogin-1.webp)](</docs/images/user-guides/onelogin-1.webp>)

  2. From the top menu, go to **Applications** > **Applications** :

[![Applications option](/docs/images/user-guides/onelogin-2.webp)](</docs/images/user-guides/onelogin-2.webp>)

  3. Then, click **Add App** :

[![Add App option](/docs/images/user-guides/onelogin-3.webp)](</docs/images/user-guides/onelogin-3.webp>)

  4. In the resulting **Find Applications** page, search for **SAML Custom Connector (Advanced)**. From the search results, select the application:

[![Select SAML Custom Connector option](/docs/images/user-guides/onelogin-4.webp)](</docs/images/user-guides/onelogin-4.webp>)

  5. Name your SAML app and click **Save** :

[![Select SAML app name](/docs/images/user-guides/onelogin-5.webp)](</docs/images/user-guides/onelogin-5.webp>)

  6. In the **Configuration** tab, enter the settings as shown in the following image:

[![SAML app configuration](/docs/images/user-guides/onelogin-6.webp)](</docs/images/user-guides/onelogin-6.webp>)

The settings to be configured are listed in the following table:

Setting| Value  
---|---  
Audience (EntityID)| `urn:amazon:cognito:sp:us-east-1_ABZiTjXia`  
Recipient| `https://auth2.rudderstack.com/saml2/idpresponse`  
ACS (Consumer) URL Validator| `^https:\/\/auth2\.rudderstack\.com\/saml2\/idpresponse\/\$`  
ACS (Consumer) URL| `https://auth2.rudderstack.com/saml2/idpresponse`  
Login URL| `https://app.rudderstack.com/sso?domain=<your_website>`  
  
> ![warning](/docs/images/warning.svg)
> 
> Make sure you enter the correct domain name in the **Login URL** setting.
> 
> For example, if your employee email is `john@example.com`, then your **Login URL** will be `https://app.rudderstack.com/sso?domain=example.com`.

  7. From the dropdown, select the **SAML initiator** and **SAML nameID format** fields as shown:

[![SAML settings](/docs/images/user-guides/onelogin-7.webp)](</docs/images/user-guides/onelogin-7.webp>)

> ![success](/docs/images/tick.svg)
> 
> Configure the other SAML settings related to the assertion validity, encryption method, etc. as per your organizational requirements.

  8. Next, go to the **Parameters** tab and add the custom parameters as shown below:

[![Custom parameters](/docs/images/user-guides/onelogin-8.webp)](</docs/images/user-guides/onelogin-8.webp>)

The custom parameters and their values are listed in the following table:

Parameter| Value  
---|---  
Email| `Email`  
LastName| `Name`  
NameID value| `Email`  
  
> ![info](/docs/images/info.svg)
> 
> For the **LastName** custom attribute, you can specify a single field `Name` \- which specifies how you would like to see your employees on the RudderStack web app.

  9. To add any other custom parameter, click the **+** button, enter the **Field name** , and select the value from the dropdown:

[![Custom parameter configuration](/docs/images/user-guides/onelogin-9.webp)](</docs/images/user-guides/onelogin-9.webp>)

> ![warning](/docs/images/warning.svg)
> 
> Make sure you enable (tick) the **Include in SAML assertion** flag for each custom parameter.

  10. Click **Save** to save the configuration.


## Enable SSO

Go to the **SSO** tab of your app and copy the **Issuer URL** :

[![Issuer URL](/docs/images/user-guides/onelogin-10.webp)](</docs/images/user-guides/onelogin-10.webp>)

> ![success](/docs/images/tick.svg)
> 
> The **Issuer URL** is the SAML metadata endpoint that contains the certificate and any other information required to enable SSO for your organization.

Share this **Issuer URL** with the RudderStack team.

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

As an alternative, you can simulate the IdP-initiation authentication flow by configuring the RudderStack SSO app and setting the **Login URL** field to `https://app.rudderstack.com/sso?domain=<your-website>]` where `<your_website>` is your organization’s web domain.

[![SAML app configuration](/docs/images/user-guides/onelogin-6.webp)](</docs/images/user-guides/onelogin-6.webp>)

#### Required String parameter ‘RelayState’ is not present

[![SSO errors](/docs/images/user-guides/sso-errors-2.webp)](</docs/images/user-guides/sso-errors-2.webp>)

The above error indicates that you did not set up your SSO app correctly. Make sure to:

  * Set the **Audience (EntityID)** field to `urn:amazon:cognito:sp:us-east-1_ABZiTjXia`.
  * Set the **SAML nameID format** to **Email**.
  * Configure the other SAML settings (Step 6 under Configure RudderStack SSO app) correctly.


## FAQ

#### My organization’s email domain has changed from `abc.com` to `xyz.com` and now I am unable to log in. What should I do?

Contact [RudderStack support](<mailto:support@rudderstack.com>) to make the necessary changes to your SSO configuration.