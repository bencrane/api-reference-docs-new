# Delete Eval API Reference

## Endpoint

**DELETE** `https://api.vapi.ai/eval/{id}`

## Description

This endpoint removes an evaluation configuration from the Vapi system. When called successfully, it returns the deleted evaluation object.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The unique identifier of the eval to delete |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from [Dashboard](dashboard.vapi.ai)" |

## Response

### Success Response (200)

Returns the deleted `Eval` object with the following structure:

```json
{
  "id": "string",
  "orgId": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "updatedAt": "2024-01-01T00:00:00Z",
  "name": "string",
  "description": "string",
  "type": "chat.mockConversation",
  "messages": [
    {
      "role": "user|assistant|system|tool",
      "content": "string"
    }
  ]
}
```

### Response Schema Details

**Eval Object Properties:**

- `id` (string): The evaluation's unique identifier
- `orgId` (string): Organization identifier
- `createdAt` (datetime): Creation timestamp
- `updatedAt` (datetime): Last modification timestamp
- `name` (string, optional): Descriptive name of the evaluation
- `description` (string, optional): Detailed explanation of evaluation purpose
- `type` (enum): Fixed to `chat.mockConversation`
- `messages` (array): Mock conversation messages and evaluation checkpoints

## SDK Example

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")

client.eval.eval_controller_remove(id="id")
```
