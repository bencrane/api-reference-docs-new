# Remove User Group

`DELETE /accounts/{account_id}/iam/user_groups/{user_group_id}`

Remove a user group from an account.

## Parameters

- **account_id** (string, required) [path]: 
- **user_group_id** (string, required) [path]: 

## Response

### 200

Remove User Group response

_Empty object_

### 4XX

Remove User Group response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
