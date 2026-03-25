# Delete Draft API Documentation

## Endpoint Overview

The Delete Draft endpoint allows you to remove a draft version of an agent using a DELETE request to `https://api.elevenlabs.io/v1/convai/agents/{agent_id}/drafts`.

## Required Parameters

Two parameters are necessary for this operation:

1. **agent_id** (path parameter): The id of an agent. This is returned on agent creation.
2. **branch_id** (query parameter): The ID of the agent branch to use

An optional `xi-api-key` header can be included for authentication.

## Response Handling

A successful deletion returns a 200 status code with a generic response body. Validation errors result in a 422 response containing details about what failed.

## Implementation Examples

The documentation provides code samples across multiple languages:

- **TypeScript/JavaScript**: Uses the ElevenLabsClient with `conversationalAi.agents.drafts.delete()`
- **Python**: Implements the call via the ElevenLabs client library
- **Go, Ruby, Java, PHP, C#, and Swift**: Show direct HTTP DELETE requests to the API endpoint with the agent_id in the path and branch_id as a query parameter

Each example demonstrates passing the required agent and branch identifiers to successfully delete an agent draft.
