# Delete a list

`DELETE /accounts/{account_id}/rules/lists/{list_id}`

Deletes a specific list and all its items.

## Parameters

- **list_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete a list response.

_Empty object_

### 4XX

Delete a list response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
