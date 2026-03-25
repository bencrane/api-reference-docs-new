# Get Call API Reference

## Endpoint

**GET** `https://api.vapi.ai/call/{id}`

Retrieves detailed information about a specific call by its ID.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The unique identifier for the call |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | API Key from [Dashboard](dashboard.vapi.ai) |

## Response

### Success Response (200)

Returns a Call object with comprehensive call details.

## Call Object Schema

The response contains extensive call information including:

### Core Call Properties

- **id**: Unique call identifier
- **createdAt**: Timestamp when call was created
- **startedAt**: When the call began
- **endedAt**: When the call terminated
- **duration**: Total call duration
- **status**: Current call status (scheduled, queued, ringing, in-progress, forwarding, ended, not-found, deletion-failed)
- **type**: Call type (inboundPhoneCall, outboundPhoneCall, webCall, vapi.websocketCall)
- **endedReason**: Detailed explanation for call termination

### Call Details

- **phoneCallProvider**: Provider used (twilio, vonage, vapi, telnyx)
- **phoneCallTransport**: Transport method (sip, pstn)
- **destination**: Transfer destination information (if transferred)
- **messages**: Array of conversation messages
- **costs**: Itemized cost breakdown
- **artifact**: Call recordings and transcripts

### Cost Information

The response includes detailed cost analysis:

- **transport**: Provider charges
- **stt**: Speech-to-text costs
- **llm**: Language model expenses
- **tts**: Text-to-speech charges
- **vapi**: Platform fees
- **total**: Cumulative cost in USD

### Message Types

Conversation messages can be:

- **UserMessage**: Customer input with timestamps
- **BotMessage**: Assistant responses
- **SystemMessage**: System notifications
- **ToolCallMessage**: Tool invocations
- **ToolCallResultMessage**: Tool execution results

## Example Request

```bash
curl -X GET "https://api.vapi.ai/call/call_abc123" \
  -H "Authorization: YOUR_API_KEY"
```

## Example Response

```json
{
  "id": "call_abc123",
  "createdAt": 1234567890.5,
  "startedAt": 1234567891.2,
  "endedAt": 1234567950.8,
  "duration": 59.6,
  "status": "ended",
  "type": "outboundPhoneCall",
  "endedReason": "customer-ended-call",
  "phoneCallProvider": "twilio",
  "phoneCallTransport": "pstn",
  "costBreakdown": {
    "transport": 0.05,
    "stt": 0.15,
    "llm": 0.20,
    "tts": 0.10,
    "vapi": 0.50,
    "total": 1.00
  },
  "messages": [
    {
      "role": "assistant",
      "message": "Hello, how can I help you today?",
      "time": 1234567891.2,
      "endTime": 1234567893.5,
      "secondsFromStart": 0
    },
    {
      "role": "user",
      "message": "I'd like to check my account balance.",
      "time": 1234567894.0,
      "endTime": 1234567897.2,
      "secondsFromStart": 3.8
    }
  ],
  "artifact": {
    "transcript": "Assistant: Hello, how can I help you today?..."
  }
}
```
