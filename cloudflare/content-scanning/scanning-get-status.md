# Get Content Scanning Status

`GET /zones/{zone_id}/content-upload-scan/settings`

Retrieve the current status of Content Scanning.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Get Content Scanning status response.

- **result** (object, optional): Defines the status for Content Scanning.

### 4XX

Get Content Scanning status failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
