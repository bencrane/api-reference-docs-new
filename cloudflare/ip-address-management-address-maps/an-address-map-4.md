# Remove a zone membership from an Address Map

`DELETE /accounts/{account_id}/addressing/address_maps/{address_map_id}/zones/{zone_id}`

Remove a zone as a member of a particular address map.

## Parameters

- **zone_id** (string, required) [path]: 
- **address_map_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Remove a zone membership from an Address Map response

_Empty object_

### 4XX

Remove a zone membership from an Address Map response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
