# Replace SCIM User

`PUT /accounts/{account_id}/scim/v2/Users/{user_id}`

Replaces a SCIM User resource (RFC 7644 Section 3.5.1). Fully replaces the mutable attributes of the user. Supports updating `userName`, `name`, `emails`, and `active`.


## Parameters

- **account_id** (string, required) [path]: 
- **user_id** (string, required) [path]: 


## Response

### 200

Replace SCIM User response

### 4XX

Replace SCIM User response failure
