# Add a zone membership to an Address Map

`PUT /accounts/{account_id}/addressing/address_maps/{address_map_id}/zones/{zone_id}`

Add a zone as a member of a particular address map.

## Parameters

- **zone_id** (string, required) [path]: 
- **address_map_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Add a zone membership to an Address Map response

_Empty object_

### 4XX

Add a zone membership to an Address Map response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
