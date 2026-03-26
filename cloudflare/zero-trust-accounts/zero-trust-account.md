# Reset device settings for a Zero Trust account with defaults. This turns off all proxying.

`DELETE /accounts/{account_id}/devices/settings`

Resets the current device settings for a Zero Trust account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Reset response for device settings for a Zero Trust account.

_Empty object_

### 4XX

Reset failure response device settings for a Zero Trust account.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
