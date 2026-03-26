# Get device certificate provisioning status

`GET /zones/{zone_id}/devices/policy/certificates`

Fetches device certificate provisioning.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Get WARP client provision certificates enabled status response.

- **result** (object, optional): 

### 4XX

Get WARP client provision certificates enabled status failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
