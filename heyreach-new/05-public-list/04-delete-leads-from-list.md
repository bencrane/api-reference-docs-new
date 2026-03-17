# DELETEDeleteLeadsFromList

## Endpoint

```
DELETE https://api.heyreach.io/api/public/list/DeleteLeadsFromList
```

Deletes the specified leads from a lead list.

## Headers

| Header | Value | Description |
|---|---|---|
| `X-API-KEY` | `<string>` | API key header using this scheme. Example: `"X-API-KEY: {API_KEY}"` |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

## Body (raw JSON)

```json
{
  "listId": 3672,
  "leadMemberIds": ["1111", "222"]
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `listId` | `integer` | Yes | The ID of the list |
| `leadMemberIds` | `string[]` | Yes | Array of LinkedIn IDs of the leads to be deleted. In API responses, this MemberId can also be named as `linkedin_id` |

## Example Request

```bash
curl --location --request DELETE 'https://api.heyreach.io/api/public/list/DeleteLeadsFromList' \
--header 'X-API-KEY: <string>' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "listId": 3672,
  "leadMemberIds": ["1111", "222"]
}'
```

## Example Response

No response body. This request doesn't return any response body.