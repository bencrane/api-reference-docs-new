# DELETE Delete Webhook

**Endpoint:** `https://api.heyreach.io/api/public/webhooks/DeleteWebhook?webhookId=1234`

This API deletes an existing webhook.

## Headers

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | `<string>` | API key header using this scheme. Example: `X-API-KEY: {API_KEY}` |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

## Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `webhookId` | string | Yes | The unique identifier of the webhook to delete |

## Example Request

```bash
curl --location --request DELETE 'https://api.heyreach.io/api/public/webhooks/DeleteWebhook?webhookId=1234' \
--header 'X-API-KEY: <string>' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data ''
```