# GETGetById

## Endpoint

```
GET https://api.heyreach.io/api/public/list/GetById?listId=<integer>
```

Get a lead or company list by Id

## Headers

| Header | Value | Description |
|---|---|---|
| `X-API-KEY` | `<string>` | API key header using this scheme. Example: `"X-API-KEY: {API_KEY}"` |
| `Accept` | `text/plain` | |

## Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `listId` | `<integer>` | Yes | The Id of the list to be retrieved |

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/list/GetById?listId=%3Cinteger%3E' \
--header 'X-API-KEY: <string>' \
--header 'Accept: text/plain'
```

## Example Response

```json
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
```