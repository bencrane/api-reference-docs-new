# Get device settings for a Zero Trust account

`GET /accounts/{account_id}/devices/settings`

Describes the current device settings for a Zero Trust account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Get device settings for a Zero Trust account response.

_Empty object_

### 4XX

Get device settings for a Zero Trust account response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
