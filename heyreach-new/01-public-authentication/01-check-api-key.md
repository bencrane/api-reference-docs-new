# GET CheckApiKey

**Endpoint:** `https://api.heyreach.io/api/public/auth/CheckApiKey`

Check if your API key is working.

## Headers

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | `<YOUR_API_KEY>` | API key header using this scheme. Example: `X-API-KEY: {API_KEY}` |
| `Accept` | `text/plain` | |

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/auth/CheckApiKey' \
--header 'X-API-KEY: <string>'
```