# Update Campaign API Reference

## Endpoint

**PATCH** `https://api.vapi.ai/campaign/{id}`

Updates an existing campaign with new configuration details.

## Parameters

### Path Parameters
- **id** (string, required): The unique identifier of the campaign to update

### Header Parameters
- **Authorization** (string, required): API key retrieved from your Vapi dashboard

### Request Body
The request body accepts an `UpdateCampaignDTO` schema containing campaign configuration updates.

## Response

**Status Code: 200 OK**

Returns the updated `Campaign` object with all current configuration settings.

## Key Configuration Options

The update request supports extensive transcription and call handling settings:

### Transcriber Options
Multiple transcription providers available:
- Assembly AI
- Azure Speech
- Deepgram
- ElevenLabs
- Gladia
- Google
- Speechmatics
- Talkscriber
- OpenAI
- Cartesia
- Soniox
- Custom transcriber

### Transcriber Features
- Language selection for each provider
- Confidence thresholds (typically 0.0-1.0 range)
- Custom vocabulary and keyword boosting
- VAD (Voice Activity Detection) settings
- Endpointing configuration
- Fallback transcriber plans for reliability

### Common Transcriber Parameters
- `confidenceThreshold`: Minimum confidence for transcript acceptance
- `language`: Target language for transcription
- `endpointing`: Timeout for silence detection
- `customVocabulary`: Domain-specific terminology
- `fallbackPlan`: Alternative transcriber if primary fails

## Authentication

Include your API key in the Authorization header to authenticate requests.

---

**Reference:** https://docs.vapi.ai/api-reference/campaigns/campaign-controller-update
