# Get Version

`GET /accounts/{account_id}/workers/workers/{worker_id}/versions/{version_id}`

Get details about a specific version.

## Parameters

- **account_id** (string, required) [path]: 
- **worker_id** (string, required) [path]: 
- **version_id** (string, required) [path]: 
- **include** (string, optional) [query]: 

## Response

### 200

Get version success.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Get version failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
