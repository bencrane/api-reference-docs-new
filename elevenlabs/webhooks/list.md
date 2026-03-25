# List Workspace Webhooks

## Endpoint Overview
The API provides a GET endpoint at `https://api.elevenlabs.io/v1/workspace/webhooks` to retrieve all webhooks configured for a workspace.

## Key Parameters

**Query Parameters:**
- `include_usages` (optional, boolean): "Whether to include active usages of the webhook, only usable by admins" — defaults to false
- `xi-api-key` (optional, header): API authentication key

## Response Structure

A successful 200 response returns a `WorkspaceWebhookListResponseModel` containing an array of webhooks. Each webhook object includes:

- **name**: Display identifier
- **webhook_id**: Unique webhook identifier
- **webhook_url**: HTTPS callback URL
- **is_disabled**: Manual disable status
- **is_auto_disabled**: Automatic disable status after repeated failures
- **created_at_unix**: Creation timestamp
- **auth_type**: Authentication method (hmac, oauth2, or mtls)
- **usage**: Array of configured trigger types (ConvAI Agent Settings, ConvAI Settings, Voice Library Removal Notices, Speech to Text)
- **most_recent_failure_error_code**: Last callback error code
- **most_recent_failure_timestamp**: Last failure time

## Supported Implementation Languages

Code examples are provided for TypeScript/JavaScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating standard HTTP GET requests to the endpoint with optional query parameters.
