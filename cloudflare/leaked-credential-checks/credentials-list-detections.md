# List Leaked Credential Checks Custom Detections

`GET /zones/{zone_id}/leaked-credential-checks/detections`

List user-defined detection patterns for Leaked Credential Checks.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

List Leaked Credential Checks custom detections response.

- **result** (array, optional): 

### 4XX

List Leaked Credential Checks custom detections failure response.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
