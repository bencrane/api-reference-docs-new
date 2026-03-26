# Delete a tag

`DELETE /accounts/{account_id}/access/tags/{tag_name}`

Delete a tag

## Parameters

- **account_id** (string, required) [path]: 
- **tag_name** (string, required) [path]: 

## Response

### 202

Delete a tag response

_Empty object_

### 4XX

Delete a tag response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
