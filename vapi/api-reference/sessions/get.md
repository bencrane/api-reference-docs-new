# Get Session API Reference

## Endpoint

**GET** `https://api.vapi.ai/session/{id}`

Retrieves details about a specific session by its ID.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The session identifier |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from Dashboard" |

## Response

### Success Response (200)

The endpoint returns a `Session` object containing comprehensive session data.

## Session Object Schema

The Session schema includes:

- **Status**: `active` or `completed` - current session state
- **Costs**: Array of cost items tracking:
  - Model costs (prompt tokens, completion tokens, cached tokens)
  - Analysis costs (summary, structured data, success evaluation)
  - Session costs in USD
- **Transcriber Configuration**: Support for multiple providers:
  - Assembly AI
  - Azure Speech
  - Custom transcriber
  - Deepgram
  - ElevenLabs
  - Gladia
  - Google
  - Speechmatics
  - OpenAI
  - Cartesia
  - Soniox
  - Talkscriber

### Fallback Transcriber Support

Each primary transcriber can include a fallback plan with alternative providers for reliability.

## Cost Tracking

Sessions track three cost types:

1. **ModelCost**: LLM usage with token counts
2. **AnalysisCost**: Post-call analysis expenses
3. **SessionCost**: Overall session charges in USD

All costs denominated in US dollars.
