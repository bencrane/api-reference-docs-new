# POSTGetAll

## Endpoint

```
POST https://api.heyreach.io/api/public/list/GetAll
```

Get a paginated collection of all company and lead lists. Get up to 100 lists per request.

## Headers

| Header | Value | Description |
|---|---|---|
| `X-API-KEY` | `<string>` | API key header using this scheme. Example: `"X-API-KEY: {API_KEY}"` |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

## Body (raw JSON)

```json
{
  "offset": 0,
  "keyword": "my list name",
  "listType": "USER_LIST",
  "campaignIds": [123, 125],
  "limit": 10
}
```

| Field | Type | Description |
|---|---|---|
| `offset` | `<integer>` | Pagination offset |
| `keyword` | `<string>` | Filter lists by name |
| `listType` | `<string>` or `null` | Filter by list type (e.g. `"USER_LIST"`) |
| `campaignIds` | `<long[]>` | Filter by associated campaign Ids |
| `limit` | `<integer>` | Number of lists to return (max 100) |

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/list/GetAll' \
--header 'X-API-KEY: <string>' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "offset": "<integer>",
  "keyword": "<string>",
  "listType": null,
  "campaignIds": [
    "<long>",
    "<long>"
  ],
  "limit": "<integer>"
}'
```

## Example Response

```json
{
  "totalCount": "<integer>",
  "items": [
    {
      "id": "<long>",
      "name": "<string>",
      "totalItemsCount": "<integer>",
      "listType": null,
      "creationTime": "<dateTime>",
      "campaignIds": [
        "<long>",
        "<long>"
      ]
    },
    {
      "id": "<long>",
      "name": "<string>",
      "totalItemsCount": "<integer>",
      "listType": null,
      "creationTime": "<dateTime>",
      "campaignIds": [
        "<long>",
        "<long>"
      ]
    }
  ]
}
```