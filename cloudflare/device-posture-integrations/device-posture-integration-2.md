# Update a device posture integration

`PATCH /accounts/{account_id}/devices/posture/integration/{integration_id}`

Updates a configured device posture integration.

## Parameters

- **integration_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **config** (object, optional): The configuration object containing third-party integration information.
- **interval** (string, optional): The interval between each posture check with the third-party API. Use `m` for minutes (e.g. `5m`) and `h` for hours (e.g. `12h`).
- **name** (string, optional): The name of the device posture integration.
- **type** (string, optional): The type of device posture integration. Values: `workspace_one`, `crowdstrike_s2s`, `uptycs`, `intune`, `kolide`, `tanium_s2s`, `sentinelone_s2s`, `custom_s2s`

## Response

### 200

Update a device posture integration response.

- **result** (object, optional): 

### 4XX

Update a device posture integration response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
