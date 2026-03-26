# Set the Split Tunnel include list

`PUT /accounts/{account_id}/devices/policy/include`

Sets the list of routes included in the WARP client's tunnel.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

Array of object

## Response

### 200

Set the Split Tunnel include list response.

- **result** (array, optional): 

### 4XX

Set the Split Tunnel include list response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
