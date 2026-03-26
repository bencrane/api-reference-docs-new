# Remove an IP from an Address Map

`DELETE /accounts/{account_id}/addressing/address_maps/{address_map_id}/ips/{ip_address}`

Remove an IP from a particular address map.

## Parameters

- **ip_address** (string, required) [path]: 
- **address_map_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Remove an IP from an Address Map response

_Empty object_

### 4XX

Remove an IP from an Address Map response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
