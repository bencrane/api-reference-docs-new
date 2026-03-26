# Deletes a Workflow

`DELETE /accounts/{account_id}/workflows/{workflow_name}`

Deletes a Workflow. This only deletes the Workflow and does not delete or modify any Worker associated to this Workflow or bounded to it.

## Parameters

- **workflow_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Deletes a Workflow.

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
