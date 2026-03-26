# Delete Leaked Credential Checks Custom Detection

`DELETE /zones/{zone_id}/leaked-credential-checks/detections/{detection_id}`

Remove user-defined detection pattern for Leaked Credential Checks.

## Parameters

- **zone_id** (string, required) [path]: 
- **detection_id** (string, required) [path]: 

## Response

### 200

Delete Leaked Credential Checks custom detection response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Defines whether the API call was successful.

### 4XX

Delete Leaked Credential Checks custom detection failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Defines whether the API call was successful.
