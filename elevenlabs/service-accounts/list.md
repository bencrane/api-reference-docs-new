# Get Service Accounts

**Endpoint:** `GET https://api.elevenlabs.io/v1/service-accounts`

**Purpose:** "List all service accounts in the workspace"

## Key Details

The API supports multiple regional servers:
- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## Request Parameters

An optional `xi-api-key` header (string type) can be included, though it's not required.

## Response Structure

A successful 200 response returns a `WorkspaceServiceAccountListResponseModel` containing:
- **service-accounts** (array): List of service account objects, each with:
  - service_account_user_id (string, required)
  - name (string, required)
  - created_at_unix (integer)
  - api-keys (array of API key objects, required)
  - default_sharing_groups (array of group permission objects)

Each API key includes properties like name, hint, key_id, permissions array, character limits, and hashed credentials.

## Error Handling

A 422 response indicates validation errors with details about what failed.

## SDK Usage Examples

**TypeScript:** Call `client.serviceAccounts.list()`

**Python:** Call `client.service_accounts.list()`

**Other Languages:** Go, Ruby, Java, PHP, C#, and Swift implementations are provided using standard HTTP GET requests to the endpoint.
