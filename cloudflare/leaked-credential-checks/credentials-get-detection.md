# Get Leaked Credential Checks Custom Detection

`GET /zones/{zone_id}/leaked-credential-checks/detections/{detection_id}`

Get user-defined detection pattern for Leaked Credential Checks.

## Parameters

- **zone_id** (string, required) [path]: 
- **detection_id** (string, required) [path]: 

## Response

### 200

Get Leaked Credential Checks custom detection response.

- **result** (object, optional): Defines a custom set of username/password expressions to match Leaked Credential Checks on.

### 4XX

Update Leaked Credential Checks custom detection failure response.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
