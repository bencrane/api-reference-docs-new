# Delete an Access group

`DELETE /accounts/{account_id}/access/groups/{group_id}`

Deletes an Access group.

## Parameters

- **group_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 202

Delete an Access group response

_Empty object_

### 4XX

Delete an Access group response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
