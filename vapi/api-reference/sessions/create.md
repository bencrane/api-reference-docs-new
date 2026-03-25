# Create Session API Reference

## Endpoint

**POST** `https://api.vapi.ai/session`

Creates a new session for voice interactions.

## Authentication

**Required Header:**
- `Authorization`: Your API Key from the Dashboard

## Request Body

The request accepts a `CreateSessionDTO` schema with the following structure:

### Session Status
- **status**: `"active"` | `"completed"` - Current session state

### Transcriber Configuration

Multiple transcriber providers are supported as the primary transcriber:

**Supported Providers:**
- Assembly AI
- Azure Speech
- Deepgram
- ElevenLabs
- Gladia
- Google
- OpenAI
- Speechmatics
- Talkscriber
- Cartesia
- Soniox
- Custom Transcriber

Each provider has specific configuration options (language, model, confidence thresholds, etc.)

### Fallback Plan

Optional fallback transcribers can be specified to automatically switch providers if the primary fails:

```
fallbackPlan:
  transcribers: [Array of transcriber configurations]
```

## Response

**Status Code:** `201 Created`

**Content-Type:** `application/json`

Returns a `Session` object containing the created session details.

## Common Configuration Examples

**Assembly AI Example:**
- Provider: `"assembly-ai"`
- Language options: `"multi"`, `"en"`
- Speech Model: `"universal-streaming-english"` (default)

**Deepgram Example:**
- Provider: `"deepgram"`
- Model: Various (e.g., `"nova-3"`, `"flux-general-en"`)
- Language: Supports 60+ languages

**Azure Example:**
- Provider: `"azure"`
- Supports 100+ language codes
- Segmentation strategies: `"Default"`, `"Time"`, `"Semantic"`
