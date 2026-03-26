# Get Worker subdomain

`GET /accounts/{account_id}/workers/scripts/{script_name}/subdomain`

Get if the Worker is available on the workers.dev subdomain.

## Parameters

- **account_id** (string, required) [path]: 
- **script_name** (string, required) [path]: 

## Response

### 200

Get subdomain response.

_Empty object_

### 4XX

Get subdomain response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
