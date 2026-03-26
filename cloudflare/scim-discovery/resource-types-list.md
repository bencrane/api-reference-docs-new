# List SCIM Resource Types

`GET /accounts/{account_id}/scim/v2/ResourceTypes`

Returns the list of SCIM resource types supported by the Cloudflare SCIM service (RFC 7643 Section 6, RFC 7644 Section 4). Clients use this to discover available resource categories (e.g. Users, Groups) and their associated schemas. Query parameters are not supported on this endpoint.


## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List SCIM Resource Types response

### 4XX

List SCIM Resource Types response failure
