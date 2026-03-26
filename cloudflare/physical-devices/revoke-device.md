# Revoke device registrations

`POST /accounts/{account_id}/devices/physical-devices/{device_id}/revoke`

Revokes all WARP registrations associated with the specified device.

## Parameters

- **account_id** (string, required) [path]: 
- **device_id** (string, required) [path]: 

## Response

### 200

Revoke device registrations response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
