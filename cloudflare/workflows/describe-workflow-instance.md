# Get logs and status from instance

`GET /accounts/{account_id}/workflows/{workflow_name}/instances/{instance_id}`

Retrieves logs and execution status for a specific workflow instance.

## Parameters

- **workflow_name** (string, required) [path]: 
- **instance_id** (string, required) [path]: 
- **simple** (string, optional) [query]: When true, omits step details and returns only metadata with step_count.
- **order** (string, optional) [query]: Step ordering: "asc" (default, oldest first) or "desc" (newest first).
- **account_id** (string, required) [path]: 

## Response

### 200

Get all logs and status from the instance.

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
