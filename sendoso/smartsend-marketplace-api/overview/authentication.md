# Authentication & Authorization

Sendoso implements OAuth 2.0 with the Authorization Code grant type per RFC 6749 Section 4.1.

## Getting Started

Contact developers@sendoso.com to obtain a client ID and client secret. Postman's redirect URI is pre-approved; production deployments should specify custom redirect URIs during registration.

## OAuth Flow

### Step 1: Direct User to Authorization

Redirect users to `https://app.sendoso.com/oauth/authorize` with these parameters:

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
| `public` | Basic user information |
| `write` | Send gifts on user's behalf |
| `update` | Modify account details |
| `marketplace` | Marketplace API access |
| `smartsend` | SmartSend API access |

### Step 2: User Grants Access

After login and consent, users redirect to your `redirect_uri` with an authorization `code` parameter.

### Step 3: Exchange Code for Token

POST to `https://app.sendoso.com/oauth/token`:

```json
{
  "grant_type": "authorization_code",
  "code": "RECEIVED_CODE",
  "redirect_uri": "YOUR_REDIRECT_URI",
  "client_id": "YOUR_CLIENT_ID",
  "client_secret": "YOUR_CLIENT_SECRET"
}
```

### Token Response

```json
{
  "access_token": "2YotnFZFEjr1zCsicMWpAA",
  "token_type": "bearer",
  "expires_in": 7200,
  "refresh_token": "tGzv3JOkF0XG5Qx2TlKWIA",
  "scope": "public",
  "created_at": 1693513711
}
```

Token lifespan: 2 hours (7200 seconds).

## Using Access Tokens

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## Refresh Tokens

POST to `https://app.sendoso.com/oauth/token`:

```json
{
  "grant_type": "refresh_token",
  "refresh_token": "YOUR_REFRESH_TOKEN",
  "client_id": "YOUR_CLIENT_ID",
  "client_secret": "YOUR_CLIENT_SECRET"
}
```

Refresh tokens expire only after use; the response returns both new access and refresh tokens.

## Token Revocation

POST to `https://app.sendoso.com/oauth/revoke`:

```bash
curl --request POST 'https://app.sendoso.com/oauth/revoke?token=YOUR_ACCESS_TOKEN' \
  --header 'Authorization: Basic ENCODED_CLIENT_ID_AND_SECRET'
```

The Authorization header requires Base64-encoded credentials: `Base64(client_id:client_secret)`.
