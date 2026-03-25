# Delete Squad API Reference

## Endpoint

**DELETE** `https://api.vapi.ai/squad/{id}`

Removes a squad from your Vapi account.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The squad identifier to delete |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from Dashboard" |

## Response

**Status Code:** 200

**Content-Type:** application/json

Returns the deleted Squad object with all its configuration details, including:
- Squad metadata (id, name, created/updated timestamps)
- Associated assistants and their transfer configurations
- Transcriber settings and fallback plans
- System prompts and message content
- Voice and language settings

## Example Request

```bash
curl -X DELETE https://api.vapi.ai/squad/{id} \
  -H "Authorization: your-api-key"
```

## Example Response

```json
{
  "id": "squad_abc123",
  "name": "Customer Support Squad",
  "createdAt": "2024-01-15T10:30:00Z",
  "updatedAt": "2024-01-20T14:22:00Z",
  "assistants": [
    {
      "name": "billing-specialist",
      "type": "assistant"
    },
    {
      "name": "technical-support",
      "type": "assistant"
    }
  ]
}
```

## Related Documentation

See the [full API reference](https://docs.vapi.ai/api-reference/squads/delete) for additional details and integration examples.
