# Single Sign-On (SSO) Configuration

> https://documentation.enigma.com/console/sso-configuration

## Overview

"Single sign-on lets your team sign in to Enigma Console using your organization's identity provider (IdP)." The platform supports SAML 2.0 compliant providers including Okta, Azure AD, Google Workspace, and OneLogin.

## Prerequisites

Before implementation, ensure you have:

- Admin or Owner role in your Enigma organization
- Administrative access to your identity provider
- Ability to create SAML applications in your IdP

## How SSO Works

The system uses "SAML 2.0 with a service provider (SP) initiated flow":

1. User visits `https://console.enigma.com/login` and clicks **Log in with SSO**
2. User enters their email address
3. Enigma redirects to the identity provider
4. User authenticates with IdP
5. IdP sends SAML assertion back to Enigma
6. Enigma validates assertion and signs user in

## Configuration Steps

### Step 1: Create SAML Application in IdP

Navigate to your IdP's application catalog and create a new SAML 2.0 application with placeholder values initially.

### Step 2: Configure Enigma

Sign into Enigma Console and navigate to **Settings > Access > SSO**.

#### Provide IdP SAML Metadata

Choose one method:

| Method | Description |
|--------|-------------|
| Metadata URL | Paste your IdP's metadata endpoint; Enigma fetches automatically |
| Metadata file | Upload XML metadata document (UTF-8 encoding required) |

#### Map SAML Attributes

Configure attribute mappings:

| Enigma Attribute | Description | Required | Common IdP Names |
|------------------|-------------|----------|------------------|
| `email` | User's email address | Yes | `user.email`, `email`, `emailAddress` |
| `given_name` | User's first name | Yes | `user.firstName`, `givenName`, `firstName` |
| `family_name` | User's last name | Yes | `user.lastName`, `surname`, `familyName` |
| `name` | User's full display name | Yes | `user.displayName`, `name`, `displayName` |

**Note:** "Attribute names are case-sensitive" and must match exactly.

#### Copy Enigma Sign-On Settings

After saving, Enigma displays:

| Setting | Description |
|---------|-------------|
| Assertion Consumer URL | Endpoint where IdP sends SAML responses |
| Service Provider Entity ID | Enigma's unique identifier as service provider |

### Step 3: Update IdP Configuration

Return to your IdP and update:

1. Set **Assertion Consumer Service (ACS) URL** to the value from Enigma
2. Set **SP Entity ID** (Audience URI) to Enigma's Service Provider Entity ID
3. Configure attribute mappings for required attributes
4. Assign users or groups to the application

### Step 4: Test Connection

1. Open private/incognito browser window
2. Go to `https://console.enigma.com/login`
3. Click **Log in with SSO**
4. Enter email address
5. Verify redirect to IdP and successful authentication

**Note:** "Configuration changes may take a few minutes to propagate."

## Important Limitation

"Users must always start from the Enigma sign-in page. Clicking the Enigma application tile directly from your IdP dashboard doesn't work." Direct users to `https://console.enigma.com/login` instead.

## Troubleshooting

### Invalid SAML Response Error

This typically indicates attribute mapping issues:

- Verify exact attribute name matches including capitalization
- Confirm IdP sends all four required attributes
- Ensure IdP's metadata URL is internet-accessible

### SSO Option Not Visible

- SSO sign-in available at `https://console.enigma.com/login`
- Users must click **Log in with SSO** and enter email
- Wait 2-3 minutes for configuration changes to propagate

### Duplicate Provider Error

This occurs when "your IdP has already been configured for another Enigma organization." Each IdP links to only one organization. Contact Enigma support for transfer assistance.

---

*Last updated: Apr 14, 2026*
