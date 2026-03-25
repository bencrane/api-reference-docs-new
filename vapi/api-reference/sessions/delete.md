# Delete Session API Reference

## Endpoint

**DELETE** `https://api.vapi.ai/session/{id}`

Removes a session from the system.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The unique identifier of the session to delete |

### Headers

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from Dashboard" |

## Response

### Success Response (200)

Returns the deleted session object with the following structure:

```json
{
  "type": "string",
  "status": "active | completed",
  "costs": [
    {
      "type": "model | analysis | session",
      "cost": "number (USD)"
    }
  ]
}
```

### Session Cost Schema

The response includes cost tracking information:

- **ModelCost**: Tracks prompt tokens, completion tokens, cached tokens, and model usage costs
- **AnalysisCost**: Includes summary, structuredData, successEvaluation, or structuredOutput analysis types
- **SessionCost**: Overall session-level cost in USD

### Status Values

- `active`: Session is currently running
- `completed`: Session has finished

## Key Fields Explained

- **type**: Indicates cost category (model, analysis, or session)
- **cost**: Billing amount in USD
- **promptTokens**: Input tokens consumed
- **completionTokens**: Output tokens generated
- **cachedPromptTokens**: Cached tokens billed at reduced rates (OpenAI, Azure OpenAI)

## Notes

- The deletion operation returns the final session state before removal
- Cost data reflects all consumables during the session lifetime
- Cached prompt tokens apply only to providers supporting prompt caching
