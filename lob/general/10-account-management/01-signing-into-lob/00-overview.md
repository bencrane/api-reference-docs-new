# Signing into Lob

## Sign in to your Lob dashboard <a href="#sign-in-to-your-lob-dashboard-0" id="sign-in-to-your-lob-dashboard-0"></a>

### Default login <a href="#default-login-1" id="default-login-1"></a>

<table data-header-hidden><thead><tr><th width="404"></th><th></th></tr></thead><tbody><tr><td><ol><li>Click <strong>Log in</strong> on <a href="https://www.lob.com/">Lob.com</a>.<br></li><li>Enter your <strong>Email Address</strong> and <strong>Password</strong> to sign in.</li></ol><p><br></p></td><td><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2F7cmmTrEBQha4vhUn7OtO%2FScreen%20Shot%202023-01-03%20at%2012.53.46%20PM.png?alt=media&#x26;token=dde64ca9-262e-48c1-938b-95455e5fd1bd" alt=""></td></tr></tbody></table>

### Single Sign-On (SSO) login <a href="#single-sign-on-sso-login-2" id="single-sign-on-sso-login-2"></a>

<table data-header-hidden><thead><tr><th width="407"></th><th></th></tr></thead><tbody><tr><td>If your organization has <a href="#set-up-lob-sso-with-okta-4">Single Sign-On</a> (SSO) enabled, you will be redirected to a separate SSO login page after entering your email and password in the default login screen (as seen above). <br><br></td><td><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FfHN6yS3TMcBuS2c7ZpTm%2FScreen%20Shot%202023-01-03%20at%2012.48.51%20PM.png?alt=media&#x26;token=b4335d8b-e09f-4676-8189-b854367701ec" alt=""></td></tr><tr><td>Confirm your pre-populated company email, and click "Sign In With SSO" to log into your account.</td><td></td></tr></tbody></table>

## Reset your password <a href="#reset-your-password-3" id="reset-your-password-3"></a>

<table data-header-hidden><thead><tr><th width="387"></th><th></th></tr></thead><tbody><tr><td><p>1. Click <strong>Log In</strong> on <a href="https://www.lob.com/">Lob.com</a>.</p><p></p><p>2. Click <strong>Forgot Password?</strong></p><p></p><p>3. Enter your <strong>Email Address</strong> then click <strong>Send Reset Link</strong>.<br></p></td><td><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2Fjhs4mnnmRVV0zE4Ke9to%2FScreen%20Shot%202023-01-03%20at%201.18.37%20PM.png?alt=media&#x26;token=c49a548a-7a00-4a10-a741-e0c0b72552d2" alt=""></td></tr><tr><td><p>4. Click <strong>Create New Password</strong> in the password reset email sent to you. </p><p></p><p>5. Enter a <strong>New Password</strong> then enter the same password in the <strong>Confirm New Password</strong> field. </p><p></p><p>6. Click <strong>Update</strong>. You password is now reset.</p></td><td><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FBiI082WiMxiHzLwhbC7g%2FScreen%20Shot%202023-01-03%20at%201.08.02%20PM.png?alt=media&#x26;token=8c20a5d5-6c17-4f39-a7b6-0bd4f39429ef" alt=""></td></tr></tbody></table>

## Set up Lob SSO with Okta <a href="#set-up-lob-sso-with-okta-4" id="set-up-lob-sso-with-okta-4"></a>

{% hint style="info" %}
Access via SSO is exclusive to Enterprise Edition customers. Upgrade to the appropriate [Print & Mail Edition](https://dashboard.lob.com/#/settings/editions) to gain access.
{% endhint %}

These instructions should also apply to configuring with other identity providers, such as OneLogin and Google IdP.

1. Create an application in Okta for Lob using this [guide‍](https://developer.okta.com/docs/guides/build-sso-integration/saml2/create-your-app/).
2. Name the application.​\
   ![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1629282011117-1629282011117.png)<br>
3. Add these SAML settings:
   * For **Single sign on URL**, enter: <https://api.lob.com/v1/sessions/saml>
   * Select **Use this for Recipient URL and Destination URL**
   * For **Audience URI (SP Entity ID)**, enter: <https://api.lob.com/v1/sessions/metadata.xml>
   * For **Name ID format**, choose **EmailAddress**.
   * For **Application username**, choose **Email**.<br>
4. Your SAML settings should match the screenshot below\
   \
   ![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1629282092826-1629282092826.png)

Once your new application is created in Okta, you need to copy the SAML metadata generated from your IDP and paste it into Lob's dashboard.

1. View your SAML IDP metadata in Okta by clicking the **Sign On** tab in the application.
2. Click the **Identity Provider metadata** link.\
   ![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1634265827886-1634265827886.png)\
   \
   This opens a new web page containing the XML you need.\
   ![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1634266143015-1634266143014.png)<br>
3. Login to Lob's dashboard and hover on your name in the top right corned then click **Settings**.
4. Scroll down to Single Sign-on in the [Account tab](https://dashboard.lob.com/settings/account) and paste the metadata from your IDP, and then click **Save**.\
   ![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1649024373219-Screen%20Shot%202022-04-03%20at%203.12.30%20PM.png)

{% hint style="warning" %}
**Note:** Only Lob administrators will be able to see the Single Sign-on configuration in the Lob dashboard.
{% endhint %}

## Best practices <a href="#best-practices-5" id="best-practices-5"></a>

Even if your company has an active SSO integration with Lob, each individual user will still need to accept their company's invite before being able to log in using SSO. Otherwise they will be sent to the normal sign-in screen.

SSO is a hard cutover for your account, so once SSO is configured then ALL users for that account will only be able to sign in through SSO. If there is an issue with the IDP metadata, e.g. an incorrect SSO URL, then all users for that account will possibly be locked out. It is strongly recommended to test SSO by signing into Lob's dashboard through another session.

If you are locked out of your account because of incorrect IDP metadata, contact <support@lob.com> to revert your account back to the normal login flow.