# Get Script Content

`GET /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/content`

Fetch script content from a script uploaded to a Workers for Platforms namespace.

## Parameters

- **account_id** (string, required) [path]: 
- **dispatch_namespace** (string, required) [path]: 
- **script_name** (string, required) [path]: 

## Response

### 200

Get script content.

### 4XX

Get script content failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
