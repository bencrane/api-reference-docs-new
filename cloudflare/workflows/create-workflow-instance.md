# Batch create new Workflow instances

`POST /accounts/{account_id}/workflows/{workflow_name}/instances/batch`

Creates multiple workflow instances in a single batch operation.

## Parameters

- **workflow_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

Array of object

## Response

### 200

Batch create workflow instances. Body is a JSON list that contain all payloads and ids that are passed into the new instance as the event payload.

- **errors** (array): 
- **messages** (array): 
- **result** (array): 
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
