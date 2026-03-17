# POST IsConnection

**Endpoint:** `https://api.heyreach.io/api/public/MyNetwork/IsConnection`

Gets a value indicating if the lead is a connection to the sender.

## Headers

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | `<string>` | API key header using this scheme. Example: `X-API-KEY: {API_KEY}` |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

## Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `senderAccountId` | number | Yes | The id of the sender account for which to check |
| `leadProfileUrl` | string | Optional | The LinkedIn URL of the lead |
| `leadLinkedInId` | string | Optional | The LinkedIn ID of the lead |

> **Note:** Either `leadProfileUrl` or `leadLinkedInId` should be specified in the request. If both are specified there will be an error.

## Body (raw JSON)

```json
{
  "senderAccountId": 0,
  "leadProfileUrl": "string",
  "leadLinkedInId": "string"
}
```

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/MyNetwork/IsConnection' \
--header 'X-API-KEY: <string>' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "senderAccountId": 0,
  "leadProfileUrl": "https://www.linkedin.com/in/john_doe/",
  "leadLinkedInId": null
}'
```

## Example Response

```json
{
  "isConnection": true
}
```