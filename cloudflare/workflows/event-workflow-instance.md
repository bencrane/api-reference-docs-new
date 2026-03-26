# Send event to instance

`POST /accounts/{account_id}/workflows/{workflow_name}/instances/{instance_id}/events/{event_type}`

Sends an event to a running workflow instance to trigger state transitions.

## Parameters

- **workflow_name** (string, required) [path]: 
- **instance_id** (string, required) [path]: 
- **event_type** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

_Empty object_

## Response

### 200

Send an event to an instance.

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

Workflow not found.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
