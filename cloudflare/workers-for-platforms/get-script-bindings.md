# Get Script Bindings

`GET /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/bindings`

Fetch script bindings from a script uploaded to a Workers for Platforms namespace.

## Parameters

- **account_id** (string, required) [path]: 
- **dispatch_namespace** (string, required) [path]: 
- **script_name** (string, required) [path]: 

## Response

### 200

Fetch script bindings (Workers for Platforms).

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): List of bindings attached to a Worker. You can find more about bindings on our docs: https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/#bindings.

### 4XX

Fetch script bindings failure (Workers for Platforms).

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
