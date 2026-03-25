# Get dubbed audio

GET https://api.elevenlabs.io/v1/dubbing/{dubbing_id}/audio/{language_code}

The endpoint returns a dubbed audio or video file as streamed MP3 or MP4 content. A key limitation: "If this dub has been edited using Dubbing Studio you need to use the resource render endpoint as this endpoint only returns the original automatic dub result."

## Parameters

- **dubbing_id** (path, required): ID of the dubbing project
- **language_code** (path, required): ID of the language
- **xi-api-key** (header, optional): API authentication key

## Response Codes

| Status | Description |
|--------|-------------|
| 200 | The dubbed audio or video file (binary) |
| 403 | Permission denied |
| 404 | Dubbing not found |
| 422 | Validation Error |
| 425 | Dubbing not ready |

## SDK Examples

**TypeScript/JavaScript:**
```typescript
const client = new ElevenLabsClient();
await client.dubbing.audio.get("dubbing_id", "language_code");
```

**Python:**
```python
client = ElevenLabs()
client.dubbing.audio.get(dubbing_id="dubbing_id", language_code="language_code")
```

**Go, Ruby, Java, PHP, C#, and Swift** code examples are also provided in the original documentation.
