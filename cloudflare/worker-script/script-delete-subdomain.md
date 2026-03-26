# Delete Worker subdomain

`DELETE /accounts/{account_id}/workers/scripts/{script_name}/subdomain`

Disable all workers.dev subdomains for a Worker.

## Parameters

- **account_id** (string, required) [path]: 
- **script_name** (string, required) [path]: 

## Response

### 200

Delete subdomain response.

_Empty object_

### 4XX

Delete subdomain response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
