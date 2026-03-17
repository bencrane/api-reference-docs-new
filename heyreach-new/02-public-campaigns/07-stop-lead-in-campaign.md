# POST StopLeadInCampaign

**Endpoint:** `https://api.heyreach.io/api/public/campaign/StopLeadInCampaign`

Stops a lead in a campaign. Call this method if you want to stop the progression of a lead in a campaign.

## Headers

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | `<string>` | API key header using this scheme. Example: `X-API-KEY: {API_KEY}` |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

## Body Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `campaignId` | integer | The ID of the campaign |
| `leadMemberId` | string | The lead member Id. You can get the member Id from the field `linkedin_id` in the method `GetLeadsFromCampaign` or from `GetLeadsFromList` |
| `leadUrl` | string | The LinkedIn URL for the lead |

## Body (raw JSON)

```json
{
  "campaignId": 123,
  "leadMemberId": "123123123",
  "leadUrl": "https://www.linkedin.com/in/john-doe"
}
```