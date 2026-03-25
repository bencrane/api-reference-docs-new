# Get API Keys

## Endpoint Overview

The ElevenLabs API provides a GET endpoint to retrieve all API keys associated with a service account:

**Endpoint:** `GET https://api.elevenlabs.io/v1/service-accounts/{service_account_user_id}/api-keys`

**Purpose:** "Get all API keys for a service account"

## Request Parameters

- **service_account_user_id** (path, required): String identifier for the service account
- **xi-api-key** (header, optional): API authentication key

## Response Schema

A successful 200 response returns a `WorkspaceApiKeyListResponseModel` containing an array of API key objects. Each key object includes:

- `name`: Key identifier name
- `hint`: Descriptive hint for the key
- `key_id`: Unique key identifier
- `service_account_user_id`: Associated service account
- `created_at_unix`: Creation timestamp
- `is_disabled`: Boolean status (default: false)
- `permissions`: Array of permission types granted
- `character_limit`: Maximum character allowance
- `character_count`: Current character usage
- `hashed_xi_api_key`: Hashed key value

## Available Permissions

The system supports 47+ permission types including text_to_speech, speech_to_text, models management, voice operations, dubbing, projects, webhooks, and workspace administration functions.

## SDK Implementation Examples

Code examples are provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating how to call the list operation across different platforms.
