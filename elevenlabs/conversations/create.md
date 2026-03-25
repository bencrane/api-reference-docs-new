# Send Conversation Feedback

## API Endpoint

**POST** `https://api.elevenlabs.io/v1/convai/conversations/{conversation_id}/feedback`

This endpoint allows you to submit feedback for a specific conversation.

## Request Details

**Content-Type:** `application/json`

### Path Parameters
- `conversation_id` (required): The identifier of the conversation receiving feedback

### Headers
- `xi-api-key` (optional): API authentication key

### Request Body

```json
{
  "feedback": "like"
}
```

The feedback field accepts one of two values: `"like"` or `"dislike"`

## Response

**Success (200):** Returns feedback confirmation

**Validation Error (422):** Returns validation error details

## Implementation Examples

The documentation provides working code samples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift. Each example demonstrates posting feedback to the endpoint using the appropriate HTTP client library for that language.

### TypeScript SDK Example
```typescript
const client = new ElevenLabsClient();
await client.conversationalAi.conversations.feedback.create("21m00Tcm4TlvDq8ikWAM", {
    feedback: "like",
});
```

### Python SDK Example
```python
client = ElevenLabs()
client.conversational_ai.conversations.feedback.create(
    conversation_id="21m00Tcm4TlvDq8ikWAM",
    feedback="like",
)
```

## Available Servers

- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`
