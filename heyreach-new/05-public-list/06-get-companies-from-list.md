# POSTGetCompaniesFromList

## Endpoint

```
POST https://api.heyreach.io/api/public/list/GetCompaniesFromList
```

Get a paginated collection of companies from a company list. Get up to 1000 companies per request.

## Headers

| Header | Value | Description |
|---|---|---|
| `X-API-KEY` | `<string>` | API key header using this scheme. Example: `"X-API-KEY: {API_KEY}"` |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

## Body (raw JSON)

```json
{
  "listId": 123,
  "offset": 0,
  "keyword": "HeyReach",
  "limit": 10
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `listId` | `<long>` | Yes | The ID of the company list |
| `offset` | `<integer>` | No | Pagination offset |
| `keyword` | `<string>` | No | Search term to filter companies |
| `limit` | `<integer>` | No | Number of companies to return (max 1000) |

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/list/GetCompaniesFromList' \
--header 'X-API-KEY: <string>' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "listId": "<long>",
  "offset": "<integer>",
  "keyword": "<string>",
  "limit": "<integer>"
}'
```

## Example Response

```json
{
  "totalCount": "<integer>",
  "items": [
    {
      "name": "<string>",
      "description": "<string>",
      "industry": "<string>",
      "imageUrl": "<string>",
      "companySize": "<string>",
      "employeesOnLinkedIn": "<integer>",
      "location": "<string>",
      "specialities": "<string>",
      "website": "<string>"
    },
    {
      "name": "<string>",
      "description": "<string>",
      "industry": "<string>",
      "imageUrl": "<string>",
      "companySize": "<string>",
      "employeesOnLinkedIn": "<integer>",
      "location": "<string>",
      "specialities": "<string>",
      "website": "<string>"
    }
  ]
}
```