# Dub Segment API Documentation

## Endpoint Overview

The Dub Segment endpoint allows you to "regenerate the dubs for either the entire resource or the specified segments/languages."

**Endpoint:** `POST https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}/dub`

## Request Parameters

### Path Parameters
- **dubbing_id** (required): ID of the dubbing project

### Header Parameters
- **xi-api-key** (optional): Authentication key

### Request Body
The endpoint accepts a JSON object with:

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| segments | array of strings | Yes | Dub only this list of segments |
| languages | array of strings | No | Dub only these languages for each segment |

## Response

**Success (200):** Returns a `SegmentDubResponse` object containing:
- **version** (integer): Version number

**Validation Error (422):** Returns validation error details

## SDK Examples

### TypeScript
```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.resource.dub("dubbing_id", {
        segments: ["segments"],
    });
}
main();
```

### Python
```python
from elevenlabs import ElevenLabs

client = ElevenLabs()
client.dubbing.resource.dub(
    dubbing_id="dubbing_id",
    segments=["segments"],
)
```

### Go, Ruby, Java, PHP, C#, and Swift examples are also provided in the original documentation.

## API Servers

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io
