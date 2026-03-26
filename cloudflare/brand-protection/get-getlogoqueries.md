# Get logo queries

`GET /accounts/{account_id}/cloudforce-one/v2/brand-protection/logo/queries`

Get all saved brand protection logo queries for an account. Optionally specify id to get a single query. Set download=true to include base64-encoded image data.

## Parameters

- **account_id** (string, required) [path]: 
- **id** (string, optional) [query]: Optional query ID to retrieve a specific logo query
- **download** (string, optional) [query]: If true, include base64-encoded image data in the response

## Response

### 200

Successfully retrieved logo queries

Type: array
