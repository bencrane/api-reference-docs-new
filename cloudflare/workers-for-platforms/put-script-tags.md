# Put Script Tags

`PUT /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags`

Put script tags for a script uploaded to a Workers for Platforms namespace.

## Parameters

- **account_id** (string, required) [path]: 
- **dispatch_namespace** (string, required) [path]: 
- **script_name** (string, required) [path]: 

## Request Body

Array of string

## Response

### 200

Fetch script tags.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 

### 4XX

Fetch script tags failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
