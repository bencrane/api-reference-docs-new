# Create SCIM Group

`POST /accounts/{account_id}/scim/v2/Groups`

Creates a new SCIM Group (user group) for the account. The `displayName` must not be empty and must not begin with `CF` (reserved for system groups).


## Parameters

- **account_id** (string, required) [path]: 


## Response

### 201

Create SCIM Group response

### 4XX

Create SCIM Group response failure
