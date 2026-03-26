# List of workflow instances

`GET /accounts/{account_id}/workflows/{workflow_name}/instances`

Lists all instances of a workflow with their execution status.

## Parameters

- **workflow_name** (string, required) [path]: 
- **page** (number, optional) [query]: `page` and `cursor` are mutually exclusive, use one or the other.
- **per_page** (number, optional) [query]: 
- **cursor** (string, optional) [query]: `page` and `cursor` are mutually exclusive, use one or the other.
- **direction** (string, optional) [query]: should only be used when `cursor` is used, defines a new direction for the cursor
- **status** (string, optional) [query]: 
- **date_start** (string, optional) [query]: Accepts ISO 8601 with no timezone offsets and in UTC.
- **date_end** (string, optional) [query]: Accepts ISO 8601 with no timezone offsets and in UTC.
- **account_id** (string, required) [path]: 

## Response

### 200

List of workflow instances.

- **errors** (array): 
- **messages** (array): 
- **result** (array): 
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
