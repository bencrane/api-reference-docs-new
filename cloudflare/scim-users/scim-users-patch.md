# Patch SCIM User

`PATCH /accounts/{account_id}/scim/v2/Users/{user_id}`

Partially updates a SCIM User via PATCH operations (RFC 7644 Section 3.5.2). Supports updating `userName`, `name.givenName`, `name.familyName`, and `active`. Setting `active: false` deprovisions the user (removes them from the account). For IdP compatibility, `emails[type eq "work"].value` is also accepted as an alias for `userName`.


## Parameters

- **account_id** (string, required) [path]: 
- **user_id** (string, required) [path]: 


## Response

### 200

Patch SCIM User response

### 4XX

Patch SCIM User response failure
