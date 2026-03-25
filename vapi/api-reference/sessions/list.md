# List Sessions API Reference

## Endpoint

**GET** `https://api.vapi.ai/session`

List and filter voice sessions from the Vapi platform.

## Description

Retrieve a paginated list of sessions with extensive filtering and sorting options. Sessions represent individual voice interactions.

## Authentication

**Required Header:**
- `Authorization`: Your API Key (obtain from [Dashboard](dashboard.vapi.ai))

## Query Parameters

### Session Filtering
- **id** (string): Filter by unique session identifier
- **name** (string): Filter by session name
- **assistantId** (string): Filter by specific assistant ID
- **assistantIdAny** (string): Filter by multiple assistant IDs (comma-separated)
- **squadId** (string): Filter by squad ID
- **workflowId** (string): Filter by workflow ID

### Customer Information Filtering
- **number** (string): Customer phone number
- **sipUri** (string): Customer SIP URI
- **email** (string): Customer email address
- **externalId** (string): Customer external ID
- **customerNumberAny** (string): Multiple phone numbers (comma-separated)
- **phoneNumberId** (string): Specific phone number ID
- **phoneNumberIdAny** (array of strings): Multiple phone number IDs

### Telephony Configuration
- **numberE164CheckEnabled** (boolean, default: true): Toggle E.164 validation
  - `true`: Enforce standard PSTN format (e.g., +14155551234)
  - `false`: Allow non-standard formats for SIP trunks
- **extension** (string): Extension dialed after call connection
- **assistantOverrides** (object): Assistant customizations for specific customers

### Temporal Filtering
- **createdAtGt** (datetime): Sessions created after this timestamp
- **createdAtLt** (datetime): Sessions created before this timestamp
- **createdAtGe** (datetime): Sessions created on or after this timestamp
- **createdAtLe** (datetime): Sessions created on or before this timestamp
- **updatedAtGt** (datetime): Sessions updated after this timestamp
- **updatedAtLt** (datetime): Sessions updated before this timestamp
- **updatedAtGe** (datetime): Sessions updated on or after this timestamp
- **updatedAtLe** (datetime): Sessions updated on or before this timestamp

### Pagination
- **page** (number, default: 1): Page number for results
- **limit** (number, default: 100): Maximum items per page
- **sortOrder** (enum): Sort direction
  - `ASC`: Ascending order
  - `DESC`: Descending order (default)

## Response Schema

### SessionPaginatedResponse
Returns paginated session data with cost breakdowns and metadata.

**Session Status Values:**
- `active`: Ongoing session
- `completed`: Finished session

**Cost Types:**
- **ModelCost**: LLM usage costs
  - `promptTokens`: Input tokens consumed
  - `completionTokens`: Output tokens generated
  - `cachedPromptTokens`: Cached tokens (reduced billing)
  - `cost`: USD amount

- **AnalysisCost**: Post-call analysis costs
  - `analysisType`: summary, structuredData, successEvaluation, structuredOutput
  - `promptTokens`, `completionTokens`, `cachedPromptTokens`, `cost`

- **SessionCost**: Base session charge in USD

## Example Request

```
GET https://api.vapi.ai/session?assistantId=abc123&limit=10&sortOrder=DESC&page=1
Headers:
  Authorization: your-api-key
```

## Example Response

```json
{
  "sessions": [
    {
      "id": "session-123",
      "name": "Customer Call",
      "status": "completed",
      "assistantId": "abc123",
      "createdAt": "2024-01-15T10:30:00Z",
      "updatedAt": "2024-01-15T10:35:00Z",
      "costs": [
        {
          "type": "model",
          "model": {},
          "promptTokens": 150,
          "completionTokens": 200,
          "cachedPromptTokens": 50,
          "cost": 0.25
        },
        {
          "type": "session",
          "cost": 0.10
        }
      ]
    }
  ],
  "page": 1,
  "limit": 10,
  "total": 45
}
```

## Key Notes

- **E164 Validation**: The parameter allows flexibility for non-PSTN scenarios while maintaining validation for alphanumeric characters
- **Cost Tracking**: Sessions include detailed breakdowns of model usage and analysis costs
- **Filtering Flexibility**: Combine multiple filters for precise result sets
- **Pagination**: Default returns 100 items; adjust `limit` and `page` for custom ranges
