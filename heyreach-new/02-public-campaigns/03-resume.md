# POST Resume

**Endpoint:** `https://api.heyreach.io/api/public/campaign/Resume?campaignId=<long>`

Resumes the specified campaign.

## Headers

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | `<string>` | API key header using this scheme. Example: `X-API-KEY: {API_KEY}` |
| `Accept` | `text/plain` | |

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `campaignId` | `<long>` | Yes | The id of the campaign to be resumed |

## Example Request

```bash
curl --location --request POST 'https://api.heyreach.io/api/public/campaign/Resume?campaignId=%3Clong%3E' \
--header 'X-API-KEY: <string>' \
--header 'Accept: text/plain'
```