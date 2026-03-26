# Delete a Custom Scan Expression

`DELETE /zones/{zone_id}/content-upload-scan/payloads/{expression_id}`

Delete a Content Scan Custom Expression.

## Parameters

- **zone_id** (string, required) [path]: 
- **expression_id** (string, required) [path]: 

## Response

### 200

Delete Content Scan custom scan expressions response.

- **result** (array, optional): 

### 4XX

Delete Content Scan custom scan expressions failure response.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
