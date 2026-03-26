# Delete device

`DELETE /accounts/{account_id}/devices/physical-devices/{device_id}`

Deletes a WARP device.

## Parameters

- **device_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Device was successfully deleted.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
