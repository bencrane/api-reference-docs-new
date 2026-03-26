# Delete Prefix

`DELETE /accounts/{account_id}/addressing/prefixes/{prefix_id}`

Delete an unapproved prefix owned by the account.

## Parameters

- **prefix_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete Prefix response

_Empty object_

### 4XX

Delete Prefix response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
