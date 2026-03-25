# List Calls API Reference

## Endpoint

**GET** `https://api.vapi.ai/call`

## Description

Retrieves a list of calls from the Vapi system with optional filtering and pagination capabilities.

## Parameters

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | No | Unique identifier for a specific call |
| `assistantId` | string | No | Filter calls by assistant ID |
| `phoneNumberId` | string | No | Filter by phone number (phone call types only) |
| `limit` | number | No | Maximum items to return (default: 100) |
| `createdAtGt` | date-time | No | Returns items created after this timestamp |
| `createdAtLt` | date-time | No | Returns items created before this timestamp |
| `createdAtGe` | date-time | No | Returns items created on or after this timestamp |
| `createdAtLe` | date-time | No | Returns items created on or before this timestamp |
| `updatedAtGt` | date-time | No | Returns items updated after this timestamp |
| `updatedAtLt` | date-time | No | Returns items updated before this timestamp |
| `updatedAtGe` | date-time | No | Returns items updated on or after this timestamp |
| `updatedAtLe` | date-time | No | Returns items updated on or before this timestamp |

### Header Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `Authorization` | string | Yes | API key from your Vapi Dashboard |

## Response

**Status Code: 200**

Returns an array of Call objects with comprehensive call data including:

- Call metadata (ID, status, timestamps)
- Call type (inbound/outbound phone, web, websocket)
- Assistant and phone number details
- Call duration and transcript
- Cost breakdown across transport, transcription, LLM, TTS, and Vapi services
- Message conversation history
- Transfer destinations and outcomes
- Call analysis results

## Key Call Properties

| Property | Type | Description |
|----------|------|-------------|
| `id` | string | Unique call identifier |
| `type` | CallType | Call classification |
| `status` | CallStatus | Current call state |
| `startedAt` | date-time | Call initiation timestamp |
| `endedAt` | date-time | Call termination timestamp |
| `endedReason` | CallEndedReason | Explanation for call termination |
| `duration` | number | Call length in seconds |
| `costs` | array | Itemized cost breakdown |
| `messages` | array | Conversation transcript |
| `destination` | CallDestination | Transfer target if applicable |
