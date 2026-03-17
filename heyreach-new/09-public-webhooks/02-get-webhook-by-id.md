# GET Get Webhook By Id

**Endpoint:** `https://api.heyreach.io/api/public/webhooks/GetWebhookById?webhookId=123`

Get a webhook by Id.

## Headers

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | `<string>` | API key header using this scheme. Example: `X-API-KEY: {API_KEY}` |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `webhookId` | integer | Yes | |

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/webhooks/GetWebhookById?webhookId=123' \
--header 'X-API-KEY: <string>' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data ''
```

## Example Response

```json
{
  "id": 123,
  "webhookName": "My Webhook Name",
  "webhookUrl": "https://webhook.site/my-webhook-url",
  "eventType": "CONNECTION_REQUEST_SENT",
  "campaignIds": [
    123,
    124
  ],
  "isActive": true
}
```