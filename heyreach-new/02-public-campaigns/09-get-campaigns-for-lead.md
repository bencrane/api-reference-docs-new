# POST GetCampaignsForLead

**Endpoint:** `https://api.heyreach.io/api/public/campaign/GetCampaignsForLead`

Gets Campaigns for a Lead.

Retrieves the list of campaigns where the specified lead is. The response will contain campaigns that match the provided lead information, such as email, LinkedIn ID, or profile URL.

## Headers

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | `<string>` | API key header using this scheme. Example: `X-API-KEY: {API_KEY}` |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

## Body Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `email` | string | Optional | The email address of the lead |
| `linkedinId` | string | Optional | The LinkedIn ID of the lead |
| `profileUrl` | string | Optional | The LinkedIn profile URL of the lead (e.g. `https://www.linkedin.com/in/john_doe/`) |
| `offset` | integer | | The number of records to skip (for pagination) |
| `limit` | integer | | The maximum number of records to return |

## Response Enums

### LeadStatus

- `Pending`
- `InSequence`
- `Finished`
- `Paused`
- `Failed`
- `Excluded`
- `PendingOrExcludedToBeCalculated`

### CampaignStatus

- `DRAFT`
- `IN_PROGRESS`
- `PAUSED`
- `FINISHED`
- `CANCELED`
- `FAILED`
- `STARTING`

## Body (raw JSON)

```json
{
  "email": "string",
  "linkedinId": "string",
  "profileUrl": "string",
  "offset": 0,
  "limit": 100
}
```

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/campaign/GetCampaignsForLead' \
--header 'X-API-KEY: <string>' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data-raw '{
  "email": "john_doe@example.com",
  "linkedinId": "1254asd3",
  "profileUrl": "https://www.linkedin.com/in/john_doe",
  "offset": 0,
  "limit": 100
}'
```

## Example Response

```json
{
  "leadFullName": "John Doe",
  "totalCount": 2,
  "items": [
    {
      "campaignId": 1082,
      "campaignName": "Campaign For Veterans",
      "campaignStatus": "PAUSED",
      "creationTime": "2025-11-12T13:22:29.96342Z",
      "leadStatus": "Finished"
    },
    {
      "campaignId": 1451,
      "campaignName": "Campaign 5",
      "campaignStatus": "CANCELED",
      "creationTime": "2025-10-12T13:22:29.96342Z",
      "leadStatus": "Finished"
    }
  ]
}
```