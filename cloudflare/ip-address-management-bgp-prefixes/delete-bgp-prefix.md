# Delete BGP Prefix

`DELETE /accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes/{bgp_prefix_id}`

Delete a BGP Prefix associated with the specified IP Prefix. A BGP Prefix must be withdrawn before it can be deleted.

## Parameters

- **account_id** (string, required) [path]: 
- **prefix_id** (string, required) [path]: 
- **bgp_prefix_id** (string, required) [path]: 

## Response

### 200

Delete BGP Prefix response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Delete BGP Prefix response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
