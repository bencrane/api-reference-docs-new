# Create Single Use Token

## Overview
This endpoint generates time-limited single-use tokens with embedded authentication for frontend clients.

**Endpoint:** `POST https://api.elevenlabs.io/v1/single-use-token/{token_type}`

## Parameters

| Name | Location | Required | Type | Description |
|------|----------|----------|------|-------------|
| token_type | Path | Yes | String | Token type (enum: `realtime_scribe`, `tts_websocket`) |
| xi-api-key | Header | No | String | API authentication key |

## Response

**Success (200):**
Returns a JSON object containing:
- `token` (string): "A time bound single use token that expires after 15 minutes. Will be consumed on use."

**Validation Error (422):**
Returns HTTP validation error details.

## Available Servers
- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## SDK Implementation Examples

**TypeScript/JavaScript:**
```typescript
const client = new ElevenLabsClient();
await client.tokens.singleUse.create("realtime_scribe");
```

**Python:**
```python
client = ElevenLabs()
client.tokens.single_use.create(token_type="realtime_scribe")
```

**cURL/HTTP:**
```
POST https://api.elevenlabs.io/v1/single-use-token/realtime_scribe
```

Additional examples available in Go, Ruby, Java, PHP, C#, and Swift.
