# Create Assistant API Reference

## Endpoint

**POST** `https://api.vapi.ai/assistant`

Creates a new assistant with specified configuration settings.

## Authentication

**Required Header:**
- `Authorization`: API Key (retrieve from [Dashboard](dashboard.vapi.ai))

## Request Body

The request accepts a `CreateAssistantDTO` schema containing assistant configuration options.

### Key Configuration Sections

#### Transcriber Options

Multiple transcription providers are supported:

- **AssemblyAI** - Streaming speech-to-text with customizable confidence thresholds and VAD-assisted endpointing
- **Azure Speech** - Multi-language support with segmentation strategies (Default, Time, Semantic)
- **Deepgram** - Multiple model variants (Flux, Nova) with keyword and keyterm prompting
- **ElevenLabs** - Real-time transcription with configurable VAD parameters
- **Gladia** - Fast/Accurate models with automatic or manual language detection
- **Google** - Gemini-based transcription across multiple model versions
- **Speechmatics** - Standard/Enhanced operating points with diarization support
- **OpenAI** - GPT-based transcription models
- **Cartesia**, **Soniox**, **Talkscriber** - Additional provider options
- **Custom Transcriber** - WebSocket-based custom implementation

Each transcriber supports:
- Language selection
- Confidence thresholds
- Custom vocabulary/keywords
- Endpointing configuration
- Fallback provider chains

## Response

**Status Code:** `201 Created`

Returns an `Assistant` object containing the created assistant's configuration and metadata.

## Reference

Full documentation: https://docs.vapi.ai/api-reference/assistants/create
