# Delete Version

`DELETE /accounts/{account_id}/workers/workers/{worker_id}/versions/{version_id}`

Delete a version.

## Parameters

- **account_id** (string, required) [path]: 
- **worker_id** (string, required) [path]: 
- **version_id** (string, required) [path]: 

## Response

### 200

Delete version success.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Delete version failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
