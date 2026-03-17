# POSTAddLeadsToListV2

## Endpoint

```
POST https://api.heyreach.io/api/public/list/AddLeadsToListV2
```

Add leads to a lead list. Add up to 100 leads per request. Same as the `AddLeadsToList` request, however this request returns counts for how many of the leads were added, how many were updated, and how many failed to be added.

**NOTE:** The `name` field in the `customUserFields` array of the leads you are importing must contain only alpha-numeric characters or underscores (`_`). An error will be returned if the `name` field does not follow this format.

**IMPORTANT:** Adding leads to a list is not the same as adding them to a campaign. If the campaign is in a finished state or has already used all the leads in it, then leads added to the list will not be started in the campaign. If you want to add leads to a specific campaign, use the `AddLeadsToCampaign` or `AddLeadsToCampaignV2` methods instead.

## Headers

| Header | Value | Description |
|---|---|---|
| `X-API-KEY` | `<string>` | API key header using this scheme. Example: `"X-API-KEY: {API_KEY}"` |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

## Body (raw JSON)

```json
{
  "leads": [
    {
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
  ],
  "listId": 123
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `listId` | `<long>` | Yes | The ID of the list to add leads to |
| `leads` | `array` | Yes | Array of lead objects (max 100) |
| `leads[].firstName` | `<string>` | No | Lead's first name |
| `leads[].lastName` | `<string>` | No | Lead's last name |
| `leads[].profileUrl` | `<string>` | No | LinkedIn profile URL |
| `leads[].location` | `<string>` | No | Lead's location |
| `leads[].summary` | `<string>` | No | Lead's summary/headline |
| `leads[].companyName` | `<string>` | No | Lead's company name |
| `leads[].position` | `<string>` | No | Lead's position/title |
| `leads[].about` | `<string>` | No | Lead's about section |
| `leads[].emailAddress` | `<string>` | No | Lead's email address |
| `leads[].customUserFields` | `array` | No | Array of custom field objects |
| `leads[].customUserFields[].name` | `<string>` | Yes | Field name (alpha-numeric and underscores only) |
| `leads[].customUserFields[].value` | `<string>` | Yes | Field value |

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/list/AddLeadsToListV2' \
--header 'X-API-KEY: <string>' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "leads": [
    {
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
    }
  ],
  "listId": "<long>"
}'
```

## Example Response

```json
{
  "addedLeadsCount": 10,
  "updatedLeadsCount": 1,
  "failedLeadsCount": 0
}
```