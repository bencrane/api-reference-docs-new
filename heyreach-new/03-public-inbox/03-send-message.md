# POST SendMessage

**Endpoint:** `https://api.heyreach.io/api/public/inbox/SendMessage`

Send a message to a LinkedIn conversation.

### Parameters

- `linkedInAccountId` — The id of your LinkedIn sender

### Headers

| Header | Value |
|---|---|
| `X-API-KEY` | `<string>` — API key header using this scheme. Example: `"X-API-KEY: {API_KEY}"` |
| `Content-Type` | `application/json` |
| `Accept` | `text/plain` |

### Body (raw JSON)

```json
{
  "message": "Hi there",
  "subject": "Hi there",
  "conversationId": "2-ODM0YmIzNzgtOGEyOS00ZTYzLWExYTItNmM0MWNhMjNlNGZjXzAxMw==",
  "linkedInAccountId": 123
}
```

### Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/inbox/SendMessage' \
--header 'X-API-KEY: <string>' \
--header 'Content-Type: application/json' \
--data '{
  "message": "<string>",
  "subject": "<string>",
  "conversationId": "<string>",
  "linkedInAccountId": "<integer>"
}'
```

### Example Response

No response body. This request doesn't return any response body.