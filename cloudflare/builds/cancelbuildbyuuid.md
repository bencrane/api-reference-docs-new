# Cancel build

`PUT /accounts/{account_id}/builds/builds/{build_uuid}/cancel`

Cancel a running or queued build

## Parameters

- **account_id** (string, required) [path]: 
- **build_uuid** (string, required) [path]: 

## Response

### 200

Build canceled successfully

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
