# Post Worker subdomain

`POST /accounts/{account_id}/workers/scripts/{script_name}/subdomain`

Enable or disable the Worker on the workers.dev subdomain.

## Parameters

- **account_id** (string, required) [path]: 
- **script_name** (string, required) [path]: 

## Request Body

- **enabled** (boolean, required): Whether the Worker should be available on the workers.dev subdomain.
- **previews_enabled** (boolean, optional): Whether the Worker's Preview URLs should be available on the workers.dev subdomain.

## Response

### 200

Post subdomain response.

_Empty object_

### 4XX

Post subdomain response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
