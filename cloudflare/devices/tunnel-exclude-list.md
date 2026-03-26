# Get the Split Tunnel exclude list

`GET /accounts/{account_id}/devices/policy/exclude`

Fetches the list of routes excluded from the WARP client's tunnel.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Get the Split Tunnel exclude list response.

- **result** (array, optional): 

### 4XX

Get the Split Tunnel exclude list response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
