# List deployed Workflow versions

`GET /accounts/{account_id}/workflows/{workflow_name}/versions`

Lists all deployed versions of a workflow.

## Parameters

- **workflow_name** (string, required) [path]: 
- **per_page** (number, optional) [query]: 
- **page** (number, optional) [query]: 
- **account_id** (string, required) [path]: 

## Response

### 200

List deployed workflow versions.

- **errors** (array): 
- **messages** (array): 
- **result** (array): 
- **result_info** (object): 
- **success** (boolean): 

### 400

Bad Request.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
