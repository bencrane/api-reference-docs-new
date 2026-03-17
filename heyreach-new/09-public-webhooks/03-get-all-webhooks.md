# POST GetAllWebhooks

**Endpoint:** `https://api.heyreach.io/api/public/webhooks/GetAllWebhooks`

Get all webhooks.

## Headers

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | `<string>` | API key header using this scheme. Example: `X-API-KEY: {API_KEY}` |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

## Body (raw JSON)

```json
{
  "offset": 0,
  "limit": 100
}
```

## Example Request

```bash
curl --location --request GET 'https://api.heyreach.io/api/public/webhooks/GetAllWebhooks' \
--header 'X-API-KEY: <string>' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "offset": 0,
  "limit": 100
}'
```

## Example Response

```json
{
  "totalCount": 1,
  "items": [
    {
      "id": 123,
      "webhookName": "string",
      "webhookUrl": "string",
      "eventType": "CONNECTION_REQUEST_SENT",
      "campaignIds": [
        123
      ],
      "isActive": true
    }
  ]
}
```