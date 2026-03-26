# List Versions

`GET /accounts/{account_id}/workers/workers/{worker_id}/versions`

List all versions for a Worker.

## Parameters

- **account_id** (string, required) [path]: 
- **worker_id** (string, required) [path]: 
- **page** (integer, optional) [query]: Current page.
- **per_page** (integer, optional) [query]: Items per-page.

## Response

### 200

List versions success.

- **result** (array, optional): 

### 4XX

List versions failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
