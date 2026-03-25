# Get Squad API Reference

## Endpoint

**GET** `https://api.vapi.ai/squad/{id}`

## Description

Retrieves a squad object by its ID from the Vapi API.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The unique identifier for the squad |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | API key retrieved from the Dashboard |

## Response

### Success Response (200)

**Content-Type:** `application/json`

Returns a `Squad` object with the following structure:

The Squad schema includes configuration for:
- **Assistants:** Multiple assistant definitions that can be transferred between
- **Transfer Settings:** Configuration for routing between squad members including:
  - Transfer destination messages
  - Transfer modes (rolling-history, swap-system-message-in-history, delete-history, swap-system-message-in-history-and-remove-transfer-tool-messages)
  - Context engineering plans for message handling
- **Transcription:** Primary and fallback transcriber providers (Assembly AI, Azure, Deepgram, ElevenLabs, Gladia, Google, Talkscriber, Speechmatics, OpenAI, Cartesia, Soniox, or custom)
- **Transcriber Options:** Language selection, confidence thresholds, model specifications, and provider-specific configurations

## Example Request

```bash
curl -X GET "https://api.vapi.ai/squad/{id}" \
  -H "Authorization: your-api-key"
```

## Example Response

```json
{
  "id": "squad-123",
  "name": "Support Squad",
  "assistants": [
    {
      "name": "sales-assistant",
      "type": "assistant"
    },
    {
      "name": "support-assistant",
      "type": "assistant"
    }
  ],
  "transcriber": {
    "provider": "deepgram",
    "model": "nova-2",
    "language": "en"
  }
}
```

## Reference

Full documentation: https://docs.vapi.ai/api-reference/squads/get
