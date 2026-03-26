# Create SCIM User

`POST /accounts/{account_id}/scim/v2/Users`

Provisions a new account member via SCIM. The `userName` field must be a valid email address and must match the primary email in `emails`. The account must be an Enterprise account with SCIM entitlements enabled.


## Parameters

- **account_id** (string, required) [path]: 


## Response

### 201

Create SCIM User response

### 4XX

Create SCIM User response failure
