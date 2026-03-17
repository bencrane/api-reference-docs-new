# POST ReplaceTags

**Endpoint:** `https://api.heyreach.io/api/public/lead/ReplaceTags`

Replaces Tags on Lead.

Removes the existing tags and replaces with the new tags.

## Headers

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | `<string>` | API key header using this scheme. Example: `X-API-KEY: {API_KEY}` |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

## Body Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `leadProfileUrl` | string | Optional | The LinkedIn profile URL of the lead (e.g. `https://www.linkedin.com/in/john-doe/`) |
| `leadLinkedInId` | string | Optional | The LinkedIn ID of the lead. You can find this ID as `linkedin_id` in the response of many endpoints, for example in `/api/public/lead/GetLead` |
| `tags` | string[] | Yes | The tags to be added to the lead |
| `createTagIfNotExisting` | boolean | Yes | If `true`, creates tags that don't exist. If `false` and there is a tag that does not exist, "Bad Request" will be returned |

## Body (raw JSON)

```json
{
  "leadProfileUrl": "https://www.linkedin.com/in/john_doe/",
  "leadLinkedInId": "",
  "tags": [
    "tag1",
    "tag2"
  ],
  "createTagIfNotExisting": false
}
```

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/lead/ReplaceTags' \
--header 'X-API-KEY: <string>' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "leadProfileUrl": "https://www.linkedin.com/in/john_doe/",
  "leadLinkedInId": "",
  "tags": [
    "tag1",
    "tag2"
  ],
  "createTagIfNotExisting": false
}'
```

## Example Response

```json
{
  "newAssignedTags": [
    "tag1",
    "tag2"
  ]
}
```