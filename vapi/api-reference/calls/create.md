# Create Call API Reference

## Endpoint

**POST** `https://api.vapi.ai/call`

Creates a new phone call with specified configuration.

## Authentication

**Required Header:**
- `Authorization`: API Key from [Dashboard](dashboard.vapi.ai)

## Request Body

The request accepts a `CreateCallDTO` object with the following primary components:

### Core Call Parameters
- **Transcriber Configuration**: Select from multiple providers (Assembly AI, Azure, Deepgram, ElevenLabs, Gladia, Google, Talkscriber, Speechmatics, OpenAI, Cartesia, or Soniox)
- **Fallback Plan**: Optional transcriber fallbacks if primary provider fails
- **Phone/Contact Details**: Recipient information for call routing

### Transcriber Options

**Assembly AI**
- Provider: `assembly-ai`
- Languages: `multi`, `en`
- Models: `universal-streaming-english`, `universal-streaming-multilingual`
- Confidence threshold (default 0.4)
- End-of-turn detection thresholds

**Deepgram**
- Models: `flux-general-en`, `nova-3`, `nova-2`, `enhanced`, `base`, `whisper`
- 60+ language support
- Smart formatting, profanity filter, numerals conversion
- Keyword and keyterm prompting

**Azure Speech**
- 100+ language support
- Segmentation strategies: `Default`, `Time`, `Semantic`
- Configurable silence timeout and maximum segment duration

**Gladia**
- Models: `fast`, `accurate`, `solaria-1`
- Language behavior: `manual`, `automatic single language`, `automatic multiple languages`
- Custom vocabulary support
- Audio enhancement and prosody detection

**Other Providers**: Google, ElevenLabs, OpenAI, Speechmatics, Soniox, Cartesia, Talkscriber with respective language and model options

### Fallback Configuration

Transcribers support hierarchical fallback chains. If the primary provider fails, the system automatically attempts subsequent providers in the specified order.

## Response

**Status Code: 201 Created**

Returns a call object containing:
- Unique call identifier
- Configuration details
- Status information
- Timestamps

## Notes

- API Key retrieval available through the Vapi Dashboard
- Reference documentation: https://docs.vapi.ai/api-reference/calls/create
- Partial transcripts can be disabled per provider
- Custom vocabulary limits vary by transcriber (e.g., Assembly AI: 2500 characters)
