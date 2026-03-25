# Update Assistant API Reference

## Endpoint

**PATCH** `https://api.vapi.ai/assistant/{id}`

Updates an existing assistant configuration.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The assistant identifier |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from Dashboard" |
| `Content-Type` | string | Yes | `application/json` |

## Request Body

The request body accepts an `UpdateAssistantDTO` schema containing various configurable assistant properties including:

- Transcriber settings (provider selection, language, confidence thresholds)
- Speech model configurations
- Custom vocabulary and endpointing parameters
- Fallback transcriber plans for redundancy
- VAD (Voice Activity Detection) settings
- Diarization and formatting options

Supported transcriber providers include Assembly AI, Azure Speech, Deepgram, ElevenLabs, Gladia, Google, Speechmatics, OpenAI, Talkscriber, Cartesia, and Soniox.

## Response

**Status: 200 OK**

Returns the updated `Assistant` object containing:

- Complete assistant configuration
- Applied transcriber settings
- All custom parameters and preferences
- Current state of fallback configurations

## Key Configuration Options

**Transcription Settings:**
- Provider selection with fallback plans
- Language specification (supports 100+ languages depending on provider)
- Confidence thresholds (typically 0-1 range)
- Custom vocabulary and keyword boosting

**Endpointing:**
- End-of-turn detection sensitivity
- Silence duration thresholds (milliseconds)
- VAD-assisted endpointing toggle

**Advanced Features:**
- Speaker diarization
- Prosody detection
- Audio enhancement
- Partial transcript handling
