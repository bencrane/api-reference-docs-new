# Get Version Detail

`GET /accounts/{account_id}/workers/scripts/{script_name}/versions/{version_id}`

Retrieves detailed information about a specific version of a Workers script.

## Parameters

- **account_id** (string, required) [path]: 
- **script_name** (string, required) [path]: 
- **version_id** (string, required) [path]: 

## Response

### 200

Get Version Detail response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Get Version Detail response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
