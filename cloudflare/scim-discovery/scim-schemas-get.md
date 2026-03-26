# Get SCIM Schema

`GET /accounts/{account_id}/scim/v2/Schemas/{schema_id}`

Returns a single SCIM schema definition by schema URI ID (RFC 7643 Section 7). Valid IDs are `urn:ietf:params:scim:schemas:core:2.0:User` and `urn:ietf:params:scim:schemas:core:2.0:Group`.


## Parameters

- **account_id** (string, required) [path]: 
- **schema_id** (string, required) [path]: 

## Response

### 200

Get SCIM Schema response

### 4XX

Get SCIM Schema response failure
