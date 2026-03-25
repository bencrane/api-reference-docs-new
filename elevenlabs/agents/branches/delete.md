# Delete Agent Branch

The ElevenLabs API provides a DELETE endpoint for removing agent branches: `DELETE https://api.elevenlabs.io/v1/convai/agents/{agent_id}/branches/{branch_id}`

## Required Parameters

The endpoint requires two path parameters:
- `agent_id` (string): The identifier for the agent
- `branch_id` (string): The identifier for the branch to delete

An optional `xi-api-key` header can be included for authentication.

## Response

A successful deletion returns a 200 status code with no additional response body content.

## Available Server Endpoints

The API is accessible through multiple regional servers:
- Standard: `https://api.elevenlabs.io`
- US: `https://api.us.elevenlabs.io`
- EU: `https://api.eu.residency.elevenlabs.io`
- India: `https://api.in.residency.elevenlabs.io`

## SDK Implementation Examples

The page provides code samples across multiple languages including TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, all demonstrating how to make the DELETE request with the appropriate agent and branch identifiers.
