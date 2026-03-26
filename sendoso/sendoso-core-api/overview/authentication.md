# Authentication & Authorization

Sendoso implements OAuth 2.0 with the Authorization Code grant type. This allows applications to access user resources without handling passwords directly.

## Getting Started

To begin, contact `developers@sendoso.com` requesting a client ID and client secret. By default, Postman's redirect URI is supported; production implementations should specify custom URIs during registration.

## OAuth Flow

### Step 1: Authorization Endpoint

Direct users to `https://app.sendoso.com/oauth/authorize` with these parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `client_id` | string | Yes | Your application identifier |
| `redirect_uri` | string | Yes | Your callback endpoint |
| `response_type` | string | Yes | Must be `"code"` |
| `scope` | string | No | Space-separated permissions |
| `state` | string | No | CSRF protection value |

### Available Scopes

| Scope | Description |
|-------|-------------|
| `public` | Basic user information access |
| `write` | Send gifts on user's behalf |
| `update` | Modify account details |
| `marketplace` | Marketplace API access |
| `smartsend` | SmartSend API access |

Example scope request: `scope=write update`

### Step 2: User Authorization

After login and consent, users are redirected to your `redirect_uri` with an authorization `code` parameter.

### Step 3: Token Exchange

POST to `https://app.sendoso.com/oauth/token` with:

| Parameter | Value |
|-----------|-------|
| `grant_type` | `"authorization_code"` |
| `code` | The received authorization code |
| `redirect_uri` | Your callback endpoint |
| `client_id` | Your application ID |
| `client_secret` | Your application secret |

**Response includes:**

| Field | Description |
|-------|-------------|
| `access_token` | For API requests (2-hour lifespan) |
| `token_type` | Always `"bearer"` |
| `expires_in` | Always `7200` seconds |
| `refresh_token` | For obtaining new access tokens |
| `scope` | Granted permissions |
| `created_at` | Token creation timestamp |

## Using Access Tokens

Include tokens in request headers:

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## Token Refresh

POST to `https://app.sendoso.com/oauth/token` with:

| Parameter | Value |
|-----------|-------|
| `grant_type` | `"refresh_token"` |
| `refresh_token` | Your refresh token |
| `client_id` | Your application ID |
| `client_secret` | Your application secret |

Returns a new access token and refresh token. Refresh tokens only expire after they are used.

## Token Revocation

POST to `https://app.sendoso.com/oauth/revoke?token=YOUR_ACCESS_TOKEN` with Basic authorization header containing base64-encoded `client_id:client_secret`.
