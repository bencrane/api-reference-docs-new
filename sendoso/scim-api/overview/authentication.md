# Authentication & Authorization

Sendoso implements OAuth 2.0 using the Authorization Code grant type. OAuth is an open standard for access delegation, commonly used as a way for Internet users to grant websites or applications access to their information on other websites but without giving them the passwords.

## Getting Started

To use the SCIM API, you must register your application and obtain credentials by contacting developers@sendoso.com. This provides you with a client ID and client secret specific to the SCIM API.

## OAuth Flow

### Step 1: Authorization Endpoint

Direct users to `https://app.sendoso.com/oauth/authorize` with these parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `client_id` | string | Yes | Your application identifier |
| `redirect_uri` | string | Yes | Where users return after authorization |
| `response_type` | string | Yes | Must be `code` |
| `scope` | string | No | Should be set to `scim` |
| `state` | string | No | Optional security parameter for CSRF prevention |

### Step 2: User Grants Access

After login and consent, the authorization server redirects to your redirect URI with an authorization `code` parameter.

### Step 3: Exchange Code for Token

POST to `https://app.sendoso.com/oauth/token` with:

| Parameter | Value |
|-----------|-------|
| `grant_type` | `authorization_code` |
| `code` | The received authorization code |
| `redirect_uri` | Same URI from step 1 |
| `client_id` | Your application ID |
| `client_secret` | Your application secret |

## Token Response

The server returns an access token valid for 7200 seconds (2 hours), along with a refresh token and metadata including `created_at` timestamp.

## Using Access Tokens

Include in request headers as:

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## Refreshing Tokens

POST to the token endpoint with `grant_type` set to `refresh_token` and your refresh token. Refresh tokens only expire after they are used.

## Revoking Tokens

POST to `https://app.sendoso.com/oauth/revoke` with Basic authorization (Base64-encoded credentials) and the token parameter to revoke access.
