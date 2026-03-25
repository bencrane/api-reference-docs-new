# Delete Workspace Auth Connection

**Endpoint:** `DELETE https://api.elevenlabs.io/v1/workspace/auth-connections/{auth_connection_id}`

**Purpose:** Remove an authentication connection from your workspace.

## Key Details

- **Required Parameter:** `auth_connection_id` (path parameter)
- **Optional Header:** `xi-api-key` for authentication
- **Success Response:** HTTP 200 with JSON content
- **Error Response:** HTTP 422 for validation errors

## Available Implementation Examples

The documentation provides code samples across multiple programming languages:

- **JavaScript/TypeScript** - Using the ElevenLabs SDK
- **Python** - Native Python client library
- **Go** - Using standard HTTP package
- **Ruby** - Net::HTTP implementation
- **Java** - Unirest HTTP client
- **PHP** - Guzzle HTTP client
- **C#** - RestSharp library
- **Swift** - URLSession framework

Each example demonstrates the straightforward process of sending a DELETE request to the specified endpoint with the authentication connection ID you wish to remove.
