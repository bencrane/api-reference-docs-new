# Delete a user

`DELETE /accounts/{account_id}/access/users/{user_id}`

Deletes a specific user for an account. This will also revoke any active seats and tokens for the user.

## Parameters

- **user_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 202

Delete user response

_Empty object_

### 4XX

Delete user response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
