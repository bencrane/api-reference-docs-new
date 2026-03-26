# Update Content Scanning Status

`PUT /zones/{zone_id}/content-upload-scan/settings`

Update the Content Scanning status.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **value** (string, required): The status value for Content Scanning. Values: `enabled`, `disabled`

## Response

### 200

Update Content Scanning settings response.

- **result** (object, optional): Defines the status for Content Scanning.

### 4XX

Update Content Scanning settings failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
