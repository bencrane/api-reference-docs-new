# Patch Script Settings

`PATCH /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/settings`

Patch script metadata, such as bindings.

## Parameters

- **account_id** (string, required) [path]: 
- **dispatch_namespace** (string, required) [path]: 
- **script_name** (string, required) [path]: 


## Response

### 200

Patch script settings.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): Script and version settings for Workers for Platforms namespace scripts. Same as script-and-version-settings-item but without annotations, which are not supported for namespace scripts.


### 4XX

Patch script settings failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
