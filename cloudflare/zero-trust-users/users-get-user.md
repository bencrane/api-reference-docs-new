# Get a user

`GET /accounts/{account_id}/access/users/{user_id}`

Gets a specific user for an account.

## Parameters

- **user_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get user response

_Empty object_

### 4XX

Get user response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
