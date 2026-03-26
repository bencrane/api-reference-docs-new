# Create a new workflow instance

`POST /accounts/{account_id}/workflows/{workflow_name}/instances`

Creates a new instance of a workflow, starting its execution.

## Parameters

- **workflow_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **instance_id** (string, optional): 
- **instance_retention** (object, optional): 
- **params** (object, optional): 

## Response

### 200

Create workflow instance. Body is a JSON parsable string that it's passed into the new instance as the event payload.

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
