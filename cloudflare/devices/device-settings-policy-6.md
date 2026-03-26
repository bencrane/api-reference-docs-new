# Set the Split Tunnel exclude list for a device settings profile

`PUT /accounts/{account_id}/devices/policy/{policy_id}/exclude`

Sets the list of routes excluded from the WARP client's tunnel for a specific device settings profile.

## Parameters

- **policy_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

Array of object

## Response

### 200

Set the Split Tunnel exclude list for a device settings profile response.

- **result** (array, optional): 

### 4XX

Set the Split Tunnel exclude list for a device settings profile response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
