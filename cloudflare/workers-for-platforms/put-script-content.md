# Put Script Content

`PUT /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/content`

Put script content for a script uploaded to a Workers for Platforms namespace.

## Parameters

- **account_id** (string, required) [path]: 
- **dispatch_namespace** (string, required) [path]: 
- **script_name** (string, required) [path]: 
- **CF-WORKER-BODY-PART** (string, optional) [header]: The multipart name of a script upload part containing script content in service worker format. Alternative to including in a metadata part.
- **CF-WORKER-MAIN-MODULE-PART** (string, optional) [header]: The multipart name of a script upload part containing script content in es module format. Alternative to including in a metadata part.


## Response

### 200

Put script content (Workers for Platforms).

- **result** (object, optional): 

### 4XX

Put script content failure (Workers for Platforms).

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
