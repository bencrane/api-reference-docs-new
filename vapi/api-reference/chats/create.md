# Create Chat API Reference

## Endpoint

**POST** `https://api.vapi.ai/chat`

## Description

Creates a new chat with optional SMS delivery via transport field. Requires at least one of: `assistantId`/`assistant`, `sessionId`, or `previousChatId`. Note: `sessionId` and `previousChatId` are mutually exclusive.

### Transport Field Configuration

The transport field enables SMS delivery with two modes:

1. **New conversation** — provide `transport.phoneNumberId` and `transport.customer` to create a new session
2. **Existing conversation** — provide `sessionId` to use existing session data

**Important:** Cannot specify both `sessionId` and transport fields together.

The `transport.useLLMGeneratedMessageForOutbound` flag controls whether input is processed by LLM (true, default) or forwarded directly as SMS (false).

## Parameters

### Headers

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Authorization | string | Yes | "Retrieve your API Key from Dashboard" (dashboard.vapi.ai) |
| Content-Type | string | Yes | application/json |

## Request Body

Schema: `CreateChatDTO`

The request body supports numerous transcriber configurations and assistant settings. Key components include:

- **assistantId** or **assistant** — Assistant identifier or full configuration
- **sessionId** — Session identifier (mutually exclusive with `previousChatId`)
- **previousChatId** — Reference to previous chat (mutually exclusive with `sessionId`)
- **transport** — SMS delivery configuration with phoneNumberId, customer, and useLLMGeneratedMessageForOutbound flag

## Response

**Status Code: 200**

Content-Type: `application/json`

Schema: `chats_create_Response_200`

Returns either a non-streaming chat response or streaming chat response depending on configuration.

## Transcriber Options

Supported transcription providers include:

- AssemblyAI
- Azure Speech
- Custom Transcriber
- Deepgram
- ElevenLabs
- Gladia
- Google
- OpenAI
- Speechmatics
- Talkscriber
- Cartesia
- Soniox

Each provider supports language selection, model configuration, and fallback transcriber plans.

---

**Reference:** https://docs.vapi.ai/api-reference/chats/create
