# Get Leaked Credential Checks Status

`GET /zones/{zone_id}/leaked-credential-checks`

Retrieves the current status of Leaked Credential Checks.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Get Leaked Credential Checks status response.

- **result** (object, optional): Defines the overall status for Leaked Credential Checks.

### 4XX

Get Leaked Credential Checks status failure response.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
