# Delete a device posture integration

`DELETE /accounts/{account_id}/devices/posture/integration/{integration_id}`

Delete a configured device posture integration.

## Parameters

- **integration_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete a device posture integration response.

- **result** (object, optional): 

### 4XX

Delete a device posture integration response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
