# Change status of instance

`PATCH /accounts/{account_id}/workflows/{workflow_name}/instances/{instance_id}/status`

Changes the execution status of a workflow instance (e.g., pause, resume, terminate).

## Parameters

- **workflow_name** (string, required) [path]: 
- **instance_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **status** (string, required): Apply action to instance. Values: `resume`, `pause`, `terminate`, `restart`

## Response

### 200

Change status of instance - it can be paused, resumed or terminated.

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

Instance not found.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): 

### 409

Instance not in a restartable state.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
