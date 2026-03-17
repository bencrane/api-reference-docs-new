# POSTCreateEmptyList

## Endpoint

```
POST https://api.heyreach.io/api/public/list/CreateEmptyList
```

Create an empty lead or company list. You pass the list name and the list type (`USER_LIST` or `COMPANY_LIST`). If the type value is left empty, a Lead list will be created by default.

## Headers

| Header | Value | Description |
|---|---|---|
| `X-API-KEY` | `<string>` | API key header using this scheme. Example: `"X-API-KEY: {API_KEY}"` |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

## Body (raw JSON)

```json
{
  "name": "<string>",
  "type": "<COMPANY_LIST|USER_LIST>"
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | `<string>` | Yes | The name of the list |
| `type` | `<string>` | No | List type: `COMPANY_LIST` or `USER_LIST`. Defaults to `USER_LIST` (lead list) if left empty |

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/list/CreateEmptyList' \
--header 'X-API-KEY: <string>' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "name": "<string>",
  "type": "<COMPANY_LIST|USER_LIST>"
}'
```

## Example Response

```json
{
  "id": 123,
  "name": "My List",
  "count": 0,
  "listType": "<COMPANY_LIST|USER_LIST>",
  "creationTime": "2024-08-29T09:34:56.5417789Z",
  "isDeleted": false,
  "campaigns": null,
  "search": null,
  "status": "UNKNOWN"
}
```