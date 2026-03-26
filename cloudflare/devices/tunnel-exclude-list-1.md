# Set the Split Tunnel exclude list

`PUT /accounts/{account_id}/devices/policy/exclude`

Sets the list of routes excluded from the WARP client's tunnel.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

Array of object

## Response

### 200

Set the Split Tunnel exclude list response.

- **result** (array, optional): 

### 4XX

Set the Split Tunnel exclude list response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
