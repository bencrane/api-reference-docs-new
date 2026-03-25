# List Evals API Reference

## Endpoint

**GET** `https://api.vapi.ai/eval`

## Description

This endpoint retrieves a paginated list of evaluations (evals) from your Vapi organization. Evals are used to test assistant responses against expected behaviors using mock conversations.

## Authentication

**Required Header:**
- `Authorization`: Your API key from the [Vapi Dashboard](dashboard.vapi.ai)

## Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | No | Filter by specific eval ID |
| `page` | number | No | Page number for pagination (default: 1) |
| `limit` | number | No | Max items per page (default: 100) |
| `sortOrder` | string | No | Sort direction: `ASC` or `DESC` (default: DESC) |
| `createdAtGt` | date-time | No | Items created after this timestamp |
| `createdAtLt` | date-time | No | Items created before this timestamp |
| `createdAtGe` | date-time | No | Items created on or after this timestamp |
| `createdAtLe` | date-time | No | Items created on or before this timestamp |
| `updatedAtGt` | date-time | No | Items updated after this timestamp |
| `updatedAtLt` | date-time | No | Items updated before this timestamp |
| `updatedAtGe` | date-time | No | Items updated on or after this timestamp |
| `updatedAtLe` | date-time | No | Items updated on or before this timestamp |

## Response Schema

### Success Response (200)

```json
{
  "results": [
    {
      "id": "string",
      "orgId": "string",
      "name": "string",
      "description": "string",
      "type": "chat.mockConversation",
      "messages": [
        {
          "role": "user|assistant|system|tool",
          "content": "string",
          "toolCalls": [],
          "judgePlan": {}
        }
      ],
      "createdAt": "2024-01-01T00:00:00Z",
      "updatedAt": "2024-01-01T00:00:00Z"
    }
  ],
  "metadata": {
    "itemsPerPage": 100,
    "totalItems": 50,
    "currentPage": 1,
    "itemsBeyondRetention": false,
    "createdAtLe": "2024-01-31T23:59:59Z",
    "createdAtGe": "2024-01-01T00:00:00Z"
  }
}
```

## SDK Example

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")

# List all evals with default pagination
response = client.eval.eval_controller_get_paginated()

# List evals with custom parameters
response = client.eval.eval_controller_get_paginated(
    page=2,
    limit=50,
    sortOrder="ASC"
)
```

## Key Fields Explained

- **messages**: Array of mock conversation messages and evaluation checkpoints
- **type**: Fixed to `chat.mockConversation` for current implementations
- **judgePlan**: Evaluation strategy (exact match, regex, or AI-based judging)
