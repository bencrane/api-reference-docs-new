# Delete Address Map

`DELETE /accounts/{account_id}/addressing/address_maps/{address_map_id}`

Delete a particular address map owned by the account. An Address Map must be disabled before it can be deleted.

## Parameters

- **address_map_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete Address Map response

_Empty object_

### 4XX

Delete Address Map response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
