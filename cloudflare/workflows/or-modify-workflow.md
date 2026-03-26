# Create/modify Workflow

`PUT /accounts/{account_id}/workflows/{workflow_name}`

Creates a new workflow or updates an existing workflow definition.

## Parameters

- **workflow_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **class_name** (string, required): 
- **limits** (object, optional): 
- **script_name** (string, required): 

## Response

### 200

Create/modify a Workflow based on a deployed script with an existing `WorkflowEntrypoint` class. Must be done after deploying the corresponding script.

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
