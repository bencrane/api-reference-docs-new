# Get secret binding

`GET /accounts/{account_id}/workers/scripts/{script_name}/secrets/{secret_name}`

Get a given secret binding (value omitted) on a script.

## Parameters

- **account_id** (string, required) [path]: 
- **script_name** (string, required) [path]: 
- **secret_name** (string, required) [path]: 
- **url_encoded** (string, optional) [query]: 

## Response

### 200

Get script secret binding.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): A secret value accessible through a binding.

### 4XX

Get script secret failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
