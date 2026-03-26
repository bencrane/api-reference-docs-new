# Delete Script Tag

`DELETE /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags/{tag}`

Delete script tag for a script uploaded to a Workers for Platforms namespace.

## Parameters

- **account_id** (string, required) [path]: 
- **dispatch_namespace** (string, required) [path]: 
- **script_name** (string, required) [path]: 
- **tag** (string, required) [path]: 

## Response

### 200

Delete script tag.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional):  Values: ``

### 4XX

Delete script tag failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
