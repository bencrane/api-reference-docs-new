# Delete Regional Hostname

`DELETE /zones/{zone_id}/addressing/regional_hostnames/{hostname}`

Delete the region configuration for a specific Regional Hostname.

## Parameters

- **zone_id** (string, required) [path]: 
- **hostname** (string, required) [path]: 

## Response

### 200

Delete hostname response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`

### 4XX

Failure to delete hostname

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
