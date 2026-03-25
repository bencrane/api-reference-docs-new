# Get Signed URL

**Endpoint:** `GET https://api.elevenlabs.io/v1/convai/conversation/get-signed-url`

**Purpose:** Retrieve a signed URL to initiate a conversation with an authorized agent.

## Required Parameters

- **agent_id** (query, string): The identifier for the target agent

## Optional Parameters

- **include_conversation_id** (query, boolean): When enabled, returns a conversation_id but prevents reuse of the signature
- **branch_id** (query, string): Specifies which branch to utilize
- **environment** (query, string): Sets the context for variable resolution (defaults to 'production')
- **xi-api-key** (header, string): API authentication key

## Response

**Status 200 - Success:**
Returns a JSON object containing:
- **signed_url** (string): The authenticated URL for starting a conversation

**Status 422 - Validation Error:**
Returns validation error details

## Available Server URLs

- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`

## Implementation Examples

The documentation provides complete code samples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift showing how to construct and execute this GET request with the appropriate parameters.
