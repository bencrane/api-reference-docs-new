# Get Campaign API Reference

## Endpoint

**GET** `https://api.vapi.ai/campaign/{id}`

Retrieves detailed information about a specific campaign using its unique identifier.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The unique identifier of the campaign to retrieve |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from [Dashboard](dashboard.vapi.ai)" |

## Response

### Success Response (200)

**Content-Type:** `application/json`

Returns a Campaign object containing comprehensive campaign configuration and status details.

### Campaign Schema

The Campaign object includes the following key enumerations:

**CampaignStatus** - Indicates the campaign operational state:
- `scheduled`
- `in-progress`
- `ended`

**CampaignEndedReason** - Explains how a campaign concluded:
- `campaign.scheduled.ended-by-user`
- `campaign.in-progress.ended-by-user`
- `campaign.ended.success`

## Transcriber Configuration

Campaigns support multiple transcription providers with fallback options, including:

- AssemblyAI
- Azure Speech
- Custom Transcriber
- Deepgram
- ElevenLabs
- Gladia
- Google
- OpenAI
- Speechmatics
- And additional providers

Each transcriber supports configurable language settings, confidence thresholds, and specialized parameters for optimizing transcription accuracy and performance characteristics.
