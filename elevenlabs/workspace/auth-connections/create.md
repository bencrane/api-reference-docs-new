# Create Workspace Auth Connection

This API endpoint enables creation of OAuth2 authentication connections for your workspace.

## Endpoint Details

**POST** `https://api.elevenlabs.io/v1/workspace/auth-connections`

The service supports multiple authentication schemes through a discriminated union pattern, where the `auth_type` field determines which configuration properties are required.

## Supported Authentication Types

The API accepts seven distinct authentication methods:

1. **oauth2_client_credentials** - Requires client ID, secret, and token URL
2. **custom_header_auth** - Uses a custom header name and token value
3. **basic_auth** - Standard username/password authentication
4. **oauth2_jwt** - JWT-based OAuth2 with signing algorithm and claims
5. **private_key_jwt** - Private key variant of JWT authentication
6. **bearer_auth** - Simple bearer token approach
7. **whatsapp_auth** - WhatsApp-specific authentication

## Required Parameters

All authentication configurations require:
- `name` - Connection identifier
- `provider` - Provider name
- `auth_type` - Discriminator specifying the authentication method

Additional fields vary by authentication type. For instance, OAuth2 client credentials requires `client_id`, `client_secret`, and `token_url`.

## Response Format

The endpoint returns the created connection object including a generated `id` and `used_by` field indicating which tools, MCP servers, or integration connections depend on this auth connection.

## Available Servers

The API is accessible across multiple regional endpoints including US, EU, and India residency options.
