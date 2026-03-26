# List SCIM Users

`GET /accounts/{account_id}/scim/v2/Users`

Lists account members as SCIM User resources. Supports optional filtering by `userName` (email) using the SCIM filter syntax (e.g. `userName eq "user@example.com"`). Pagination is controlled via `startIndex` and `count` query parameters per RFC 7644 Section 3.4.2.4.


## Parameters

- **account_id** (string, required) [path]: 
- **startIndex** (integer, optional) [query]: 
- **count** (integer, optional) [query]: 
- **filter** (string, optional) [query]: 

## Response

### 200

List SCIM Users response

### 4XX

List SCIM Users response failure
