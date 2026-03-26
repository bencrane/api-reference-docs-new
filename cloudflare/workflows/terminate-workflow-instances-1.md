# Get status of the job responsible for terminate all instances of a workflow

`GET /accounts/{account_id}/workflows/{workflow_name}/instances/terminate`

Gets the status of a bulk workflow instance termination job.

## Parameters

- **workflow_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get status of the job responsible for terminate all instances of a workflow.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **result_info** (object): 
- **success** (boolean): 

### 400

Input Validation Error.

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
