# Delete Secret API Documentation

## Endpoint Overview

The ElevenLabs API provides a DELETE endpoint at `https://api.elevenlabs.io/v1/convai/secrets/{secret_id}` to remove workspace secrets that are not currently in use.

## Key Details

**Purpose:** "Delete a workspace secret if it's not in use"

**HTTP Method:** DELETE

**Path Parameter:**
- `secret_id` (required, string): The identifier of the secret to remove

**Optional Header:**
- `xi-api-key`: API authentication key

## Response Codes

- **200:** Operation completed successfully
- **422:** Validation error (returns detailed error information)

## Implementation Examples

The documentation provides code samples across multiple languages including TypeScript/JavaScript, Python, Go, Ruby, Java, PHP, C#, and Swift. The TypeScript example demonstrates basic usage:

```typescript
const client = new ElevenLabsClient();
await client.conversationalAi.secrets.delete("secret_id");
```

The Python equivalent follows a similar pattern using the ElevenLabs SDK's `conversational_ai.secrets.delete()` method with the secret identifier as a parameter.

## Available API Servers

The endpoint is accessible through multiple regional servers:
- Standard US endpoint
- EU residency endpoint
- India residency endpoint
