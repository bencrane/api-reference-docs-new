# PublicWebhooks

## POST Create Webhook

**Endpoint:** `https://api.heyreach.io/api/public/webhooks/CreateWebhook`

This API creates a new webhook that listens to specified events, optionally filtered by campaign IDs.

### Headers

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | `<string>` | API key header using this scheme. Example: `X-API-KEY: {API_KEY}` |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

### Request Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `webhookName` | string | The name of the webhook |
| `webhookUrl` | string | The URL to which the webhook will send POST requests |
| `eventType` | string | The type of event that triggers the webhook. See values below |
| `campaignIds` | array | A list of campaign IDs. If empty, the webhook will listen for the specified `eventType` across all campaigns. If specific campaign IDs are provided, the webhook will listen only to those campaigns |

### eventType Values

| Value | Description |
|-------|-------------|
| `CONNECTION_REQUEST_SENT` | |
| `CONNECTION_REQUEST_ACCEPTED` | |
| `MESSAGE_SENT` | |
| `MESSAGE_REPLY_RECEIVED` | Only the first reply |
| `INMAIL_SENT` | |
| `INMAIL_REPLY_RECEIVED` | Only the first reply |
| `EVERY_MESSAGE_REPLY_RECEIVED` | Including replies for both messages and inmails |
| `FOLLOW_SENT` | |
| `LIKED_POST` | |
| `VIEWED_PROFILE` | |
| `CAMPAIGN_COMPLETED` | |
| `LEAD_TAG_UPDATED` | |

### Body (raw JSON)

```json
{
  "webhookName": "string",
  "webhookUrl": "string",
  "eventType": "CONNECTION_REQUEST_SENT",
  "campaignIds": []
}
```

### Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/webhooks/CreateWebhook' \
--header 'X-API-KEY: <string>' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "webhookName": "string",
  "webhookUrl": "string",
  "eventType": "CONNECTION_REQUEST_SENT",
  "campaignIds": []
}'
```