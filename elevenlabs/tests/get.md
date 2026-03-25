# Get Test

## Endpoint Overview

The GET `/v1/convai/agent-testing/{test_id}` endpoint retrieves an agent response test by its ID.

## Request Details

**Method:** GET
**Base URLs:**
- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`

### Parameters

| Name | Location | Type | Required | Description |
|------|----------|------|----------|-------------|
| `test_id` | Path | String | Yes | The identifier for a chat response test, returned upon test creation |
| `xi-api-key` | Header | String | No | API authentication key |

## Response

**Success (200):** Returns a test object with type-specific structure (llm, tool, or simulation)

**Validation Error (422):** Returns HTTP validation error details

## Response Schema

The response uses a discriminated union with three test types:

### LLM Test Type
Contains success/failure conditions and example responses for evaluating agent outputs.

### Tool Test Type
Includes tool call parameter evaluation configuration and criteria for validating tool invocations.

### Simulation Test Type
Features simulation scenarios, user personas, and configurable conversation turn limits.

All test types include:
- Test metadata (id, name, type)
- Dynamic variables for runtime substitution
- Chat history transcript
- Optional conversation metadata from source interactions

## Code Examples

**TypeScript:**
```typescript
const client = new ElevenLabsClient();
await client.conversationalAi.tests.get("TeaqRRdTcIfIu2i7BYfT");
```

**Python:**
```python
client = ElevenLabs()
client.conversational_ai.tests.get(test_id="TeaqRRdTcIfIu2i7BYfT")
```

**cURL/HTTP:** GET requests to the endpoint with the test ID in the path.

Additional implementations available in Go, Ruby, Java, PHP, C#, and Swift.
