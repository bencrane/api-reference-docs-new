# Get Workflow version details

`GET /accounts/{account_id}/workflows/{workflow_name}/versions/{version_id}`

Retrieves details for a specific deployed workflow version.

## Parameters

- **workflow_name** (string, required) [path]: 
- **version_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get specific version details.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **result_info** (object): 
- **success** (boolean): 

### 400

Bad Request.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): 

### 404

Version not found.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
