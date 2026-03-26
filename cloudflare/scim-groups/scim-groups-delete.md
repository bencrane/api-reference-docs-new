# Delete SCIM Group

`DELETE /accounts/{account_id}/scim/v2/Groups/{group_id}`

Deletes a SCIM Group (custom user groups only). System groups backed by Cloudflare permission groups cannot be deleted via SCIM. Returns 204 No Content on success.


## Parameters

- **account_id** (string, required) [path]: 
- **group_id** (string, required) [path]: 

## Response

### 204

Delete SCIM Group response (no content)

### 4XX

Delete SCIM Group response failure
