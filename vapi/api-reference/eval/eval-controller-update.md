# Update Eval API Reference

## Endpoint

**PATCH** `https://api.vapi.ai/eval/{id}`

## Description

Updates an existing evaluation configuration that tests assistant behavior through mock conversations.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The unique identifier of the eval to update |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from Dashboard" |
| `Content-Type` | string | Yes | `application/json` |

## Request Body

The request accepts a `UpdateEvalDTO` object with the following properties:

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No | Identifies what the eval validates |
| `description` | string | No | Details the eval's purpose without affecting conversation flow |
| `type` | string | No | Currently fixed to `chat.mockConversation` |
| `messages` | array | No | Mock conversation array containing message sequences and evaluation checkpoints |

### Message Types

Messages can be one of these types:
- `ChatEvalAssistantMessageMock` - Simulated assistant response
- `ChatEvalUserMessageMock` - Simulated user input
- `ChatEvalSystemMessageMock` - System-level instruction
- `ChatEvalAssistantMessageEvaluation` - Checkpoint validating assistant output
- `ChatEvalToolResponseMessageMock` - Simulated tool response
- `ChatEvalToolResponseMessageEvaluation` - Checkpoint validating tool behavior

## Response

**Status Code:** 200 OK

Returns an `Eval` object containing:

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Eval identifier |
| `orgId` | string | Organization identifier |
| `name` | string | Eval name |
| `description` | string | Eval description |
| `type` | string | Fixed value: `chat.mockConversation` |
| `messages` | array | Updated message array |
| `createdAt` | string (ISO 8601) | Creation timestamp |
| `updatedAt` | string (ISO 8601) | Last update timestamp |

## Example Request

```json
{
  "name": "Customer Service Response Test",
  "description": "Validates assistant provides helpful customer support",
  "type": "chat.mockConversation",
  "messages": [
    {
      "role": "user",
      "content": "What are your business hours?"
    },
    {
      "role": "assistant",
      "content": "We're open Monday-Friday, 9am-6pm EST"
    }
  ]
}
```

## Example Response

```json
{
  "id": "eval_abc123",
  "orgId": "org_xyz789",
  "name": "Customer Service Response Test",
  "description": "Validates assistant provides helpful customer support",
  "type": "chat.mockConversation",
  "messages": [
    {
      "role": "user",
      "content": "What are your business hours?"
    },
    {
      "role": "assistant",
      "content": "We're open Monday-Friday, 9am-6pm EST"
    }
  ],
  "createdAt": "2024-01-15T10:30:00Z",
  "updatedAt": "2024-01-20T14:45:00Z"
}
```

## SDK Example (Python)

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")

response = client.eval.eval_controller_update(id="eval_abc123")
```
