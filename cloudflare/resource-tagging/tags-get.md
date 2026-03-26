# Get tags for an account-level resource

`GET /accounts/{account_id}/tags`

Retrieves tags for a specific account-level resource.

## Parameters

- **account_id** (string, required) [path]: 
- **resource_id** (string, required) [query]: The ID of the resource to retrieve tags for.
- **resource_type** (string, required) [query]: The type of the resource.
- **worker_id** (string, optional) [query]: Worker identifier. Required for worker_version resources.

## Response

### 200

Get tags for single resource response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Get tags for single resource response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

### 5XX

Get tags for single resource response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
