# List SCIM Schemas

`GET /accounts/{account_id}/scim/v2/Schemas`

Returns the list of SCIM schemas supported by the Cloudflare SCIM service (RFC 7643 Section 7, RFC 7644 Section 4). Clients use this to introspect the attributes of each resource type. Query parameters are not supported on this endpoint.


## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List SCIM Schemas response

### 4XX

List SCIM Schemas response failure
