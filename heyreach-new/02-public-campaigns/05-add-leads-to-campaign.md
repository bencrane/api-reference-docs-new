# POST AddLeadsToCampaign

**Endpoint:** `https://api.heyreach.io/api/public/campaign/AddLeadsToCampaign`

Add leads to a campaign. Add up to 100 leads per request. If a LinkedIn account Id is specified in the `AccountLeadPairs`, that lead will be mapped to the account in the campaign.

The `name` field in the `customUserFields` array of the leads you are importing must contain only alpha-numeric characters or underscores `_`. An error will be returned in the case the `name` field does not follow this format.

## Headers

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | `<string>` | API key header using this scheme. Example: `X-API-KEY: {API_KEY}` |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

## Body (raw JSON)

```json
{
    "campaignId": 235,
    "accountLeadPairs": [
        {
            "linkedInAccountId": 123,
            "lead": {
                "firstName": "John",
                "lastName": "Doe",
                "location": "USA",
                "summary": "SDR @ HeyReach",
                "companyName": "HeyReach",
                "position": "SDR",
                "about": "I like LinkedIn",
                "emailAddress": "john_doe@example.com",
                "customUserFields": [
                    {
                        "name": "favorite_color",
                        "value": "blue"
                    }
                ],
                "profileUrl": "https://www.linkedin.com/in/john-doe"
            }
        }
    ],
    "resumeFinishedCampaign": false,
    "resumePausedCampaign": true
}
```

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/campaign/AddLeadsToCampaign' \
--header 'X-API-KEY: <string>' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "accountLeadPairs": [
    {
      "lead": {
        "firstName": "<string>",
        "lastName": "<string>",
        "profileUrl": "<string>",
        "location": "<string>",
        "summary": "<string>",
        "companyName": "<string>",
        "position": "<string>",
        "about": "<string>",
        "emailAddress": "<string>",
        "customUserFields": [
          {
            "name": "<string>",
            "value": "<string>"
          },
          {
            "name": "<string>",
            "value": "<string>"
          }
        ]
      },
      "linkedInAccountId": "<integer>"
    }
  ],
  "campaignId": "<long>",
  "resumeFinishedCampaign": "<boolean>",
  "resumePausedCampaign": "<boolean>"
}'
```

## Example Response

```
0
```