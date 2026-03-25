# Create Campaign API Reference

## Endpoint

**POST** `https://api.vapi.ai/campaign`

## Description

Creates a new campaign for voice AI interactions.

## Authentication

**Required Header:**
- `Authorization`: Your API Key from the [Dashboard](dashboard.vapi.ai)

## Request Body

The request body must contain a `CreateCampaignDTO` schema with campaign configuration details.

### Key Configuration Options

#### Transcriber Configuration

Multiple transcription providers are supported:

- **Assembly AI**: Streaming transcription with customizable confidence thresholds and speech models
- **Azure Speech**: Multi-language support with segmentation strategies
- **Deepgram**: Multiple model options (Flux, Nova series) with endpointing control
- **ElevenLabs**: VAD-based transcription with configurable sensitivity
- **Gladia**: Fast/accurate models with custom vocabulary support
- **Google**: Gemini model integration for transcription
- **Speechmatics**: Enhanced accuracy with speaker diarization
- **OpenAI**: GPT-4o transcription models
- **Cartesia**: Ink-whisper model support
- **Soniox**: Universal multi-language transcription
- **Custom Transcriber**: WebSocket-based custom provider integration

#### Fallback Plans

All primary transcribers support fallback configuration with alternate providers for reliability.

## Response

**Status Code:** `201 Created`

Returns a `Campaign` object containing:
- Campaign ID and metadata
- Configured transcriber settings
- Fallback provider chain
- All campaign parameters

## Example Request Structure

```json
{
  "transcriber": {
    "provider": "deepgram",
    "model": "nova-3",
    "language": "en-US",
    "endpointing": 10
  },
  "fallbackPlan": {
    "transcribers": [
      {
        "provider": "assembly-ai",
        "language": "en"
      }
    ]
  }
}
```

## Notes

- Provider-specific parameters vary; consult individual provider documentation
- Fallback transcribers execute sequentially if primary provider fails
- Custom vocabularies enhance accuracy for domain-specific terminology
- Confidence thresholds filter low-quality transcriptions
