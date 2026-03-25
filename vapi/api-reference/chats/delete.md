# Delete Chat API Reference

## Endpoint

**DELETE** `https://api.vapi.ai/chat/{id}`

## Description

Remove a chat resource from the system using its unique identifier.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The unique identifier for the chat to delete |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from Dashboard" |

## Response

### Success Response (200)

Returns the deleted Chat object in JSON format.

**Schema:** `Chat`

The response includes the complete chat resource that was removed, containing all chat configuration details including transcriber settings, fallback plans, and other associated metadata.

## Implementation Notes

The endpoint accepts a chat ID in the URL path and requires authentication via API key in the Authorization header. Upon successful deletion, the API returns a 200 status code with the deleted chat object as confirmation.

The Chat schema supports extensive configuration options across multiple transcription providers including AssemblyAI, Azure Speech, Deepgram, ElevenLabs, Gladia, Google, Speechmatics, OpenAI, Cartesia, Soniox, and custom transcribers, along with comprehensive fallback provider options.
