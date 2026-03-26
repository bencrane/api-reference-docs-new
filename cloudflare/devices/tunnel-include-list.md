# Get the Split Tunnel include list

`GET /accounts/{account_id}/devices/policy/include`

Fetches the list of routes included in the WARP client's tunnel.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Get the Split Tunnel include list response.

- **result** (array, optional): 

### 4XX

Get the Split Tunnel include list response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
