# GET GetChatroom

**Endpoint:** `https://api.heyreach.io/api/public/inbox/GetChatroom/:accountId/:conversationId`

Get a LinkedIn conversation with its messages by Id.

### Headers

| Header | Value |
|---|---|
| `X-API-KEY` | `<string>` — API key header using this scheme. Example: `"X-API-KEY: {API_KEY}"` |
| `Accept` | `text/plain` |

### Path Variables

| Variable | Type | Required |
|---|---|---|
| `accountId` | integer | Yes |
| `conversationId` | string | Yes |

### Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/inbox/GetChatroom/:accountId/:conversationId' \
--header 'X-API-KEY: <string>' \
--header 'Accept: text/plain'
```

### Example Response

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