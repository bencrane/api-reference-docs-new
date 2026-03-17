# PATCH Update Webhook

**Endpoint:** `https://api.heyreach.io/api/public/webhooks/UpdateWebhook?webhookId=1234`

This API updates an existing webhook by modifying its configuration, such as name, URL, event type, associated campaigns, and status.

## Headers

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | `<string>` | API key header using this scheme. Example: `X-API-KEY: {API_KEY}` |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

## Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `webhookId` | string | Yes | The unique identifier of the webhook to update |

## Request Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `webhookName` | string \| null | The name of the webhook. If `null` or omitted, the original name will be kept |
| `webhookUrl` | string \| null | The URL to which the webhook will send POST requests. If `null` or omitted, the original URL will be kept |
| `eventType` | string \| null | The type of event that triggers the webhook. If `null` or omitted, the original will be kept. See values below |
| `campaignIds` | array \| null | A list of campaign IDs. If `null` or omitted, the original array will be kept. If empty, the webhook will listen for the specified `eventType` across all campaigns. If specific campaign IDs are provided, the webhook will listen only to those campaigns |
| `isActive` | boolean \| null | Determines whether the webhook should be active. If `true`, the webhook is enabled; if `false`, it is disabled. If `null`, the activation status remains unchanged |

### eventType Values

- `CONNECTION_REQUEST_SENT`
- `CONNECTION_REQUEST_ACCEPTED`
- `MESSAGE_SENT`
- `MESSAGE_REPLY_RECEIVED`
- `INMAIL_SENT`
- `INMAIL_REPLY_RECEIVED`
- `FOLLOW_SENT`
- `LIKED_POST`
- `VIEWED_PROFILE`
- `CAMPAIGN_COMPLETED`
- `LEAD_TAG_UPDATED`

## Body (raw JSON)

```json
{
  "webhookName": "string",
  "webhookUrl": "string",
  "eventType": "CONNECTION_REQUEST_SENT",
  "campaignIds": [],
  "isActive": true
}
```

## Example Request

```bash
curl --location --request PATCH 'https://api.heyreach.io/api/public/webhooks/UpdateWebhook?webhookId=1234' \
--header 'X-API-KEY: <string>' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "webhookName": "string",
  "webhookUrl": "string",
  "eventType": "CONNECTION_REQUEST_SENT",
  "campaignIds": [],
  "isActive": true
}'
```