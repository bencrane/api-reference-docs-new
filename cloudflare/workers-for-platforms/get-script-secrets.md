# Get secret binding

`GET /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets/{secret_name}`

Get a given secret binding (value omitted) on a script uploaded to a Workers for Platforms namespace.

## Parameters

- **account_id** (string, required) [path]: 
- **dispatch_namespace** (string, required) [path]: 
- **script_name** (string, required) [path]: 
- **secret_name** (string, required) [path]: 
- **url_encoded** (string, optional) [query]: 

## Response

### 200

Get script secret (Workers for Platforms).

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): A secret value accessible through a binding.

### 4XX

Get script secret failure (Workers for Platforms).

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
