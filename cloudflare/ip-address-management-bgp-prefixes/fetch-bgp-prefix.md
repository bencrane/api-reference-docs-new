# Fetch BGP Prefix

`GET /accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes/{bgp_prefix_id}`

Retrieve a single BGP Prefix according to its identifier

## Parameters

- **account_id** (string, required) [path]: 
- **prefix_id** (string, required) [path]: 
- **bgp_prefix_id** (string, required) [path]: 

## Response

### 200

Fetch BGP Prefix response

- **result** (object, optional): 

### 4XX

Fetch BGP Prefix response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
