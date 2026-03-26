# Set Global WARP override state

`POST /accounts/{account_id}/devices/resilience/disconnect`

Sets the Global WARP override state.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **disconnect** (boolean, required): Disconnects all devices on the account using Global WARP override.
- **justification** (string, optional): Reasoning for setting the Global WARP override state. This will be surfaced in the audit log.

## Response

### 200

Set Global WARP override state response.

_Empty object_

### 4XX

Set Global WARP override state response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
