# Add Custom Scan Expressions

`POST /zones/{zone_id}/content-upload-scan/payloads`

Add custom scan expressions for Content Scanning.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

Array of object

## Response

### 200

Add custom scan expressions for Content Scanning.

- **result** (array, optional): 

### 4XX

List existing Content Scan custom scan expressions failure response.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
