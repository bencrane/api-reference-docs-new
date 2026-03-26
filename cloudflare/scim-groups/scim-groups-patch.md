# Patch SCIM Group

`PATCH /accounts/{account_id}/scim/v2/Groups/{group_id}`

Partially updates a SCIM Group via PATCH operations (RFC 7644 Section 3.5.2). Supports add, remove, and replace operations on `members`, `displayName`, and `externalId`. For system groups (prefixed `cloudflare-v1-`), only member management operations are supported.


## Parameters

- **account_id** (string, required) [path]: 
- **group_id** (string, required) [path]: 


## Response

### 200

Patch SCIM Group response

### 4XX

Patch SCIM Group response failure
