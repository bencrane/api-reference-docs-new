# Get Workflow details

`GET /accounts/{account_id}/workflows/{workflow_name}`

Retrieves configuration and metadata for a specific workflow.

## Parameters

- **workflow_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get Workflow details.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **result_info** (object): 
- **success** (boolean): 

### 400

Workflow has no deployed versions.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): 

### 404

Workflow not found.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
