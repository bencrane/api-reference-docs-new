# Start Speaker Separation

## API Endpoint

**POST** `https://api.elevenlabs.io/v1/voices/pvc/{voice_id}/samples/{sample_id}/separate-speakers`

This endpoint initiates a speaker separation process for an audio sample. The feature processes voice data to isolate individual speakers within a sample.

## Path Parameters

- **voice_id** (required): The voice identifier, obtainable from the voices list endpoint
- **sample_id** (required): The identifier for the sample to process

## Optional Headers

- **xi-api-key**: API authentication key

## Response

A successful request (HTTP 200) returns:

```json
{
  "status": "ok"
}
```

The status field indicates request success. Error responses return HTTP 500 with descriptive messages.

## Error Handling

Validation errors (HTTP 422) provide detailed error information including location, message, and error type.

## Available Servers

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## SDK Examples

```python
client.voices.pvc.samples.speakers.separate(
    voice_id="21m00Tcm4TlvDq8ikWAM",
    sample_id="VW7YKqPnjY4h39yTbx2L",
)
```

Code examples are also available for TypeScript/JavaScript, Go, Ruby, Java, PHP, C#, and Swift.
