# Create Chat (OpenAI Compatible) - API Reference

## Endpoint

**POST** `https://api.vapi.ai/chat/responses`

**Content-Type:** `application/json`

## Description

This endpoint creates a chat response using an OpenAI-compatible interface. It supports both streaming and non-streaming response formats.

## Authentication

**Required Header:**
- `Authorization`: Your API Key from the Dashboard (https://dashboard.vapi.ai)

## Request Body

The request body follows the `OpenAIResponsesRequest` schema, which includes configuration for transcribers, language models, and other chat parameters.

### Transcriber Options

The API supports multiple transcription providers:

- **Assembly AI** - Streaming English/multilingual models with confidence thresholds and VAD-assisted endpointing
- **Azure Speech** - Supports 100+ languages with segmentation strategies (Default, Time, Semantic)
- **Deepgram** - Multiple models (Flux, Nova, Enhanced, Base) with keyword and keyterm prompting
- **ElevenLabs** - Scribe models with VAD sensitivity configuration
- **Gladia** - Fast/accurate/solaria models with custom vocabulary and audio enhancement
- **Google** - Gemini models (various versions) for multilingual transcription
- **OpenAI** - GPT-4o and GPT-4o-mini transcribe models
- **Speechmatics** - Standard/enhanced operating points with diarization and custom vocabulary
- **Talkscriber** - Whisper model for cost-effective transcription
- **Cartesia** - Ink-whisper model
- **Soniox** - Real-time transcription with custom vocabulary

Each transcriber supports optional fallback configuration for provider redundancy.

## Response

**Status:** `200 OK`

**Content-Type:** `application/json`

The response returns either:
- Non-streaming format: Complete JSON response
- Streaming format: Server-sent events or chunked JSON responses

Both follow the OpenAI Responses API format for compatibility.

## Key Features

- **Multi-provider support** with automatic failover through fallback plans
- **Language coverage** spanning 100+ languages depending on provider
- **Confidence thresholds** to filter low-quality transcriptions
- **Custom vocabulary** support for domain-specific accuracy
- **VAD (Voice Activity Detection)** for intelligent endpointing
- **Diarization** capabilities (select providers)
- **Real-time streaming** transcription available

## Additional Configuration

Transcribers can be configured with:
- Language selection
- Confidence and sensitivity thresholds
- Custom vocabulary/keywords
- Speech model selection
- Endpointing behavior
- Audio enhancement options
- Regional deployment preferences

---

**Reference:** https://docs.vapi.ai/api-reference/chats/create-response
