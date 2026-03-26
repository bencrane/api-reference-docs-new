# Add an IP to an Address Map

`PUT /accounts/{account_id}/addressing/address_maps/{address_map_id}/ips/{ip_address}`

Add an IP from a prefix owned by the account to a particular address map.

## Parameters

- **ip_address** (string, required) [path]: 
- **address_map_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Add an IP to an Address Map response

_Empty object_

### 4XX

Add an IP to an Address Map response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
