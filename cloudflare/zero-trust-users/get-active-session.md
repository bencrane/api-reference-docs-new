# Get single active session

`GET /accounts/{account_id}/access/users/{user_id}/active_sessions/{nonce}`

Get an active session for a single user.

## Parameters

- **user_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **nonce** (string, required) [path]: 

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
