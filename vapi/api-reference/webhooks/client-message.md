# Client Message Webhook API Reference

## Endpoint

**POST** `https://{yourserver}.com/client`

## Description

Webhook messages sent to client-side SDKs during call operations. Configure desired messages via `assistant.clientMessages`.

## Request

**Content-Type:** `application/json`

### Request Body Schema

The endpoint accepts a `ClientMessage` payload containing various message types related to call events.

## Response

**Status Code:** `200`

**Content-Type:** `application/json`

### Response Schema

The response should conform to `ClientInboundMessage` schema, which contains messages the client SDK can send to control the call.

## Key Message Types

### Workflow Node Started
- **Type:** `workflow.node.started`
- **Trigger:** When the active workflow node changes
- **Includes:** Associated phone number details across multiple provider types (BYO, Twilio, Vonage, Vapi, Telnyx)

### Custom Messages
Supports multilingual message variants through `TextContent`:
- **Type field:** "text"
- **Language support:** ISO 639-1 language codes (extensive list from 'aa' to 'zu')
- **Use case:** "Specify variants of the same content, one per language"

### Tool-Related Messages
- **request-complete:** Triggered when tool execution succeeds
- **request-failed:** Triggered when tool execution fails
- **Supports:** Conditional triggering based on tool call arguments

## Notable Features

- **Multilingual support:** Automatic translation to active language if variant unavailable
- **Conditional logic:** Messages can trigger based on parameter comparisons (eq, neq, gt, gte, lt, lte)
- **Cost tracking:** Detailed breakdowns for transport, transcriber, model, voice, analysis, and knowledge base usage
- **Message history:** Includes user, system, bot, and tool call messages with timestamps and metadata
