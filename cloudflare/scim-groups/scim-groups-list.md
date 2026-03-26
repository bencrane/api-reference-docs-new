# List SCIM Groups

`GET /accounts/{account_id}/scim/v2/Groups`

Lists SCIM Group resources for the account. Returns both system groups (backed by Cloudflare permission groups, prefixed `cloudflare-v1-`) and custom user groups. Supports filtering by `displayName` using SCIM filter syntax.


## Parameters

- **account_id** (string, required) [path]: 
- **startIndex** (integer, optional) [query]: 
- **count** (integer, optional) [query]: 
- **filter** (string, optional) [query]: 

## Response

### 200

List SCIM Groups response

### 4XX

List SCIM Groups response failure
