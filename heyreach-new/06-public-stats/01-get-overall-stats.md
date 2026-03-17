# POST Get Overall Stats

**Endpoint:** `https://api.heyreach.io/api/public/stats/GetOverallStats`

Gets the overall stats for the specified filters.

## Headers

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | `<string>` | API key header using this scheme. Example: `X-API-KEY: {API_KEY}` |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

## Body Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `accountIds` | integer[] | Array of Ids of the LinkedIn senders. If empty, all senders will be included |
| `campaignIds` | integer[] | Array of Ids of the campaigns to be included. If empty, all campaigns will be included |
| `startDate` | string (ISO 8601) | Start date for the filter range |
| `endDate` | string (ISO 8601) | End date for the filter range |

## Body (raw JSON)

```json
{
  "accountIds": [1234],
  "campaignIds": [],
  "startDate": "2024-12-17T00:00:00.000Z",
  "endDate": "2024-12-19T23:59:59.999Z"
}
```

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/stats/GetOverallStats' \
--header 'X-API-KEY: <string>' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "accountIds": [1234],
  "campaignIds": [],
  "startDate": "2024-12-17T00:00:00.000Z",
  "endDate": "2024-12-19T23:59:59.999Z"
}'
```

## Example Response

```json
{
  "byDayStats": {
    "2024-12-17T00:00:00Z": {
      "profileViews": 0,
      "postLikes": 0,
      "follows": 0,
      "messagesSent": 723,
      "totalMessageStarted": 593,
      "totalMessageReplies": 136,
      "inmailMessagesSent": 0,
      "totalInmailStarted": 0,
      "totalInmailReplies": 0,
      "connectionsSent": 4650,
      "connectionsAccepted": 637,
      "messageReplyRate": 0.22934233,
      "inMailReplyRate": 0,
      "connectionAcceptanceRate": 0.13698925
    },
    "2024-12-18T00:00:00Z": {
      "profileViews": 0,
      "postLikes": 0,
      "follows": 0,
      "messagesSent": 1033,
      "totalMessageStarted": 592,
      "totalMessageReplies": 119,
      "inmailMessagesSent": 0,
      "totalInmailStarted": 0,
      "totalInmailReplies": 0,
      "connectionsSent": 5161,
      "connectionsAccepted": 652,
      "messageReplyRate": 0.20101352,
      "inMailReplyRate": 0,
      "connectionAcceptanceRate": 0.1263321
    },
    "2024-12-19T00:00:00Z": {
      "profileViews": 0,
      "postLikes": 0,
      "follows": 0,
      "messagesSent": 845,
      "totalMessageStarted": 581,
      "totalMessageReplies": 140,
      "inmailMessagesSent": 0,
      "totalInmailStarted": 0,
      "totalInmailReplies": 0,
      "connectionsSent": 4929,
      "connectionsAccepted": 539,
      "messageReplyRate": 0.24096386,
      "inMailReplyRate": 0,
      "connectionAcceptanceRate": 0.10935281
    }
  },
  "overallStats": {
    "profileViews": 0,
    "postLikes": 0,
    "follows": 0,
    "messagesSent": 2601,
    "totalMessageStarted": 1766,
    "totalMessageReplies": 395,
    "inmailMessagesSent": 0,
    "totalInmailStarted": 0,
    "totalInmailReplies": 0,
    "connectionsSent": 14740,
    "connectionsAccepted": 1828,
    "messageReplyRate": 0.2236693,
    "inMailReplyRate": 0,
    "connectionAcceptanceRate": 0.124016285
  }
}
```