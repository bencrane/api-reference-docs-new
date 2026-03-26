# Create a device posture integration

`POST /accounts/{account_id}/devices/posture/integration`

Create a new device posture integration.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **config** (object, required): The configuration object containing third-party integration information.
- **interval** (string, required): The interval between each posture check with the third-party API. Use `m` for minutes (e.g. `5m`) and `h` for hours (e.g. `12h`).
- **name** (string, required): The name of the device posture integration.
- **type** (string, required): The type of device posture integration. Values: `workspace_one`, `crowdstrike_s2s`, `uptycs`, `intune`, `kolide`, `tanium_s2s`, `sentinelone_s2s`, `custom_s2s`

## Response

### 200

Create a device posture integration response.

- **result** (object, optional): 

### 4XX

Create a device posture integration response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
