# Retrieve Global WARP override state

`GET /accounts/{account_id}/devices/resilience/disconnect`

Fetch the Global WARP override state.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Fetch Global WARP override state response.

_Empty object_

### 4XX

Fetch Global WARP override state failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
