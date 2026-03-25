# Get Assistant API Reference

## Endpoint

**GET** `https://api.vapi.ai/assistant/{id}`

Retrieves a specific assistant configuration by its ID.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The unique identifier of the assistant to retrieve |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | API Key from your [Dashboard](dashboard.vapi.ai) |

## Response

### Success Response (200)

Returns an `Assistant` object with full configuration details.

### Assistant Object Structure

The Assistant schema includes:

- **Transcriber Configuration**: Choice of provider (Assembly AI, Azure, Deepgram, Eleven Labs, Gladia, Google, Talkscriber, Speechmatics, OpenAI, Cartesia, or Soniox) with language, model, and provider-specific settings

- **Fallback Plans**: Optional fallback transcriber providers for redundancy

- **Server Configuration**: Webhook URLs, headers, timeout settings, and retry logic

- **Audio Processing**: Confidence thresholds, endpointing settings, VAD (Voice Activity Detection) parameters, and custom vocabulary options

## Key Configuration Options

### Transcriber Providers Supported

- Assembly AI with speech models (universal-streaming-english/multilingual)
- Azure Speech with 100+ language options
- Deepgram with Flux and Nova models
- Eleven Labs with multiple model versions
- Gladia with fast/accurate/solaria models
- Google Gemini models
- Talkscriber with Whisper
- Speechmatics with diarization support
- OpenAI transcription models
- Cartesia ink-whisper
- Soniox with universal multilingual support

### Common Parameters

- `confidenceThreshold`: Discard transcripts below specified confidence (default: 0.4)
- `endpointing`: Timeout for detecting speech end (milliseconds)
- `customVocabulary`: Domain-specific words and phrases for improved accuracy
- `language`: Target language for transcription
- `fallbackPlan`: Secondary providers if primary fails

## Authentication

Requests require your Vapi API key in the Authorization header. Retrieve this from your Dashboard.
