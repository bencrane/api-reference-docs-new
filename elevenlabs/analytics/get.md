# Get Live Count

**Endpoint:** `GET https://api.elevenlabs.io/v1/convai/analytics/live-count`

**Purpose:** Retrieve the count of active ongoing conversations through the ElevenLabs Conversational AI analytics service.

## Key Parameters

- **agent_id** (optional, query): Filters analytics results to a specific agent
- **xi-api-key** (optional, header): Authentication header

## Response Format

The API returns a JSON object containing:
- **count** (integer): The number of active ongoing conversations

## Available Server Endpoints

- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`

## Supported Implementation Languages

SDK examples are provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift. Each demonstrates how to call the analytics endpoint with optional agent filtering.

## Error Handling

The API returns a 422 response for validation errors, with detailed error information in the response body.
