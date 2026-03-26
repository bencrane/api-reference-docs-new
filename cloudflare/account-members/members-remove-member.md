# Remove Member

`DELETE /accounts/{account_id}/members/{member_id}`

Remove a member from an account.

## Parameters

- **member_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Remove Member response

_Empty object_

### 4XX

Remove Member response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
