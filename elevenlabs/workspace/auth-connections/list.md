# Get Workspace Auth Connections

## Endpoint Overview

The GET endpoint at `https://api.elevenlabs.io/v1/workspace/auth-connections` retrieves all authentication connections configured for a workspace.

## Request Details

**HTTP Method:** GET

**Base URL:** https://api.elevenlabs.io (with regional alternatives available)

**Optional Header Parameter:**
- `xi-api-key` (header, optional): API authentication key

## Response Structure

A successful 200 response returns a `ListAuthConnectionsResponse` object containing an array of auth connections. Each connection object includes:

- `id`: Unique identifier
- `name`: Connection name
- `provider`: Service provider
- `auth_type`: One of eight supported authentication types
- `used_by`: Dependencies showing which tools, MCP servers, and integration connections use this auth connection

## Supported Authentication Types

The endpoint supports eight distinct authentication schemes:

1. **api_integration_oauth2_auth_code** - OAuth2 authorization code flow
2. **basic_auth** - Username/password authentication
3. **bearer_auth** - Bearer token authentication
4. **custom_header_auth** - Custom HTTP header-based auth
5. **oauth2_client_credentials** - OAuth2 client credentials flow
6. **oauth2_jwt** - OAuth2 with JWT assertion
7. **private_key_jwt** - Private key JWT authentication
8. **whatsapp_auth** - WhatsApp-specific authentication

## SDK Implementation Examples

The documentation provides ready-to-use code samples across multiple languages:
- TypeScript/JavaScript (using ElevenLabsClient)
- Python (using ElevenLabs client library)
- Go, Ruby, Java, PHP, C#, and Swift

All examples demonstrate the same straightforward operation: instantiate the client and call the list method on auth connections.
