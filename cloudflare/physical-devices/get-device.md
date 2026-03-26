# Get device

`GET /accounts/{account_id}/devices/physical-devices/{device_id}`

Fetches a single WARP device.

## Parameters

- **device_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **include** (string, optional) [query]: Comma-separated list of additional information that should be included in the device response. Supported values are: "last_seen_registration.policy".


## Response

### 200

Returns a Device.

- **errors** (array): 
- **messages** (array): 
- **result** (object): A WARP Device.
- **success** (boolean): Whether the API call was successful.
