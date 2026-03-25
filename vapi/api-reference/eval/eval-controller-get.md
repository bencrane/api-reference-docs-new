# Get Eval API Reference

## Endpoint

**GET** `https://api.vapi.ai/eval/{id}`

## Description

Retrieves a specific evaluation configuration by its ID. This endpoint allows you to fetch the details of a previously created eval, including its mock conversation messages and evaluation criteria.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The unique identifier of the eval to retrieve |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from [Dashboard](dashboard.vapi.ai)" |

## Response Schema

### 200 Success Response

The response contains the complete Eval object with the following structure:

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier for the eval |
| `orgId` | string | Organization ID |
| `name` | string | Name identifying what the eval checks |
| `description` | string | Detailed description of the eval's purpose |
| `type` | string | Fixed to `chat.mockConversation` |
| `messages` | array | Mock conversation and evaluation checkpoints |
| `createdAt` | string (date-time) | Creation timestamp |
| `updatedAt` | string (date-time) | Last update timestamp |

### Messages Array

Contains mixed message types:
- **Mock Messages**: Simulate conversation flow (user, assistant, system, tool responses)
- **Evaluation Messages**: Checkpoints that validate model responses against criteria

Each message includes:
- `role`: The message author's role
- `content`: Message text
- `judgePlan` (evaluations only): Defines how to assess responses (exact match, regex, or LLM-as-judge)

## Example Request

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")

response = client.eval.eval_controller_get(id="eval_123")
```

## Example Response

```json
{
  "id": "eval_123",
  "orgId": "org_456",
  "name": "Customer Service Response Validation",
  "description": "Evaluates if assistant provides accurate product information",
  "type": "chat.mockConversation",
  "messages": [
    {
      "role": "user",
      "content": "What are your business hours?"
    },
    {
      "role": "assistant",
      "content": "We're open Monday-Friday, 9AM-5PM EST"
    },
    {
      "role": "assistant",
      "judgePlan": {
        "type": "exact",
        "content": "We're open Monday-Friday, 9AM-5PM EST"
      }
    }
  ],
  "createdAt": "2024-01-15T10:30:00Z",
  "updatedAt": "2024-01-15T10:30:00Z"
}
```
