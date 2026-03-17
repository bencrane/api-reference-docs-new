# POST GetTags

**Endpoint:** `https://api.heyreach.io/api/public/lead/GetTags`

Get Tags for a Lead.

Gets the tags for a lead. The tags are alphabetically sorted.

## Headers

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | `<string>` | API key header using this scheme. Example: `X-API-KEY: {API_KEY}` |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

## Body Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `profileUrl` | string | Yes | The LinkedIn profile URL of the lead (e.g. `https://www.linkedin.com/in/john-doe/`) |

## Body (raw JSON)

```json
{
  "profileUrl": "https://www.linkedin.com/in/john_doe/"
}
```

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/lead/GetTags' \
--header 'X-API-KEY: <string>' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "profileUrl": "https://www.linkedin.com/in/john_doe/"
}'
```

## Example Response

```json
{
  "tags": [
    "atag1",
    "btag2",
    "ctag3"
  ]
}
```