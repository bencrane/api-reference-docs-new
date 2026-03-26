# Get Workflow version graph

`GET /accounts/{account_id}/workflows/{workflow_name}/versions/{version_id}/graph`

Retrieves the graph visualization of a workflow version.

## Parameters

- **workflow_name** (string, required) [path]: 
- **version_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get the parsed graph for a specific workflow version.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **result_info** (object): 
- **success** (boolean): 

### 404

Version not found.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
