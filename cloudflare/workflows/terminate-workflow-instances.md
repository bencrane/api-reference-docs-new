# Batch terminate instances of a workflow

`POST /accounts/{account_id}/workflows/{workflow_name}/instances/batch/terminate`

Terminates multiple workflow instances in a single batch operation.

## Parameters

- **workflow_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

Array of string

## Response

### 200

Batch terminate instances of a workflow, via a async job. Body is a JSON list that contain the ids of the instances to terminate.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **result_info** (object): 
- **success** (boolean): 

### 400

Provided Workflow ID is not valid.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): 

### 404

Workflow Name not found.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
