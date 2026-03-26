# Get last seen identity

`GET /accounts/{account_id}/access/users/{user_id}/last_seen_identity`

Get last seen identity for a single user.

## Parameters

- **user_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get active session response

_Empty object_

### 4XX

Get active session response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
