# Get build logs

`GET /accounts/{account_id}/builds/builds/{build_uuid}/logs`

Retrieve logs for a specific build with cursor-based pagination

## Parameters

- **account_id** (string, required) [path]: 
- **build_uuid** (string, required) [path]: 
- **cursor** (string, optional) [query]: 

## Response

### 200

Build logs retrieved successfully

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **result_info** (object, optional): 
- **success** (boolean, optional): 

### 404

Resource not found

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
