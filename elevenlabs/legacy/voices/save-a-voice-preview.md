# Save a voice preview

POST https://api.elevenlabs.io/v1/text-to-voice/create-voice-from-preview

The endpoint enables users to "Add a generated voice to the voice library."

## API Details

**Endpoint:** `/v1/text-to-voice/create-voice-from-preview`

**Method:** POST

**Available Servers:**
- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

**Authentication:** Optional `xi-api-key` header parameter

**Response:** Returns a successful response on status 200

## SDK Implementation Examples

The page provides code samples across multiple programming languages:

- **TypeScript/JavaScript:** Uses `ElevenLabsClient` with `saveAVoicePreview()` method
- **Python:** Implements via `ElevenLabs` client's `save_a_voice_preview()` function
- **Go, Ruby, Java, PHP, C#, and Swift:** Demonstrate direct HTTP POST requests to the endpoint

All examples show basic POST request implementation without request body parameters or detailed response structures documented on this reference page.
