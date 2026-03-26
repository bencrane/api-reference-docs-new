# Get the Split Tunnel include list for a device settings profile

`GET /accounts/{account_id}/devices/policy/{policy_id}/include`

Fetches the list of routes included in the WARP client's tunnel for a specific device settings profile.

## Parameters

- **policy_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get the Split Tunnel include list for a device settings profile response.

- **result** (array, optional): 

### 4XX

Get the Split Tunnel include list for a device settings profile response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
