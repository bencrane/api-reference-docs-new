# List Existing Custom Scan Expressions

`GET /zones/{zone_id}/content-upload-scan/payloads`

Get a list of existing custom scan expressions for Content Scanning.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

List existing Content Scan custom scan expressions response.

- **result** (array, optional): 

### 4XX

List existing Content Scan custom scan expressions failure response.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
