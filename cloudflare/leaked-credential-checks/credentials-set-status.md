# Set Leaked Credential Checks Status

`POST /zones/{zone_id}/leaked-credential-checks`

Updates the current status of Leaked Credential Checks.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **enabled** (boolean, optional): Determines whether or not Leaked Credential Checks are enabled.

## Response

### 200

Set Leaked Credential Checks status response.

- **result** (object, optional): Defines the overall status for Leaked Credential Checks.

### 4XX

Set Leaked Credential Checks status failure response.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
