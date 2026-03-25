# Get Chat API Reference

## Endpoint

**GET** `https://api.vapi.ai/chat/{id}`

Retrieves a chat object by its ID.

## Parameters

### Path Parameters
- **id** (string, required): The unique identifier of the chat to retrieve

### Header Parameters
- **Authorization** (string, required): API key obtained from the [Dashboard](dashboard.vapi.ai)

## Response

### 200 OK
Returns a Chat object with the following structure:

The response includes comprehensive chat configuration including:
- Transcriber settings (provider, language, model options)
- Fallback transcriber plans for provider redundancy
- Support for multiple transcription providers:
  - AssemblyAI
  - Azure Speech
  - Deepgram
  - ElevenLabs
  - Gladia
  - Google
  - Talkscriber
  - Speechmatics
  - OpenAI
  - Cartesia
  - Soniox
  - Custom transcribers

### Transcriber Configuration Example

Each transcriber can include:
- Provider identification
- Language settings (region/locale specific)
- Model selection
- Confidence thresholds
- Custom vocabulary support
- Speech detection parameters
- Endpointing configuration
- Fallback provider chains

## Key Features

**Multiple Provider Support**: Integrates with 12+ transcription services, enabling flexible deployment choices

**Fallback Mechanisms**: "This is the plan for transcriber provider fallbacks in the event that the primary transcriber provider fails"

**Customization Options**: Confidence thresholds, VAD settings, custom vocabulary, and language-specific parameters

**Regional Deployment**: EU and US region options for data sovereignty compliance

## Example Request

```bash
curl -X GET https://api.vapi.ai/chat/{id} \
  -H "Authorization: your-api-key"
```
