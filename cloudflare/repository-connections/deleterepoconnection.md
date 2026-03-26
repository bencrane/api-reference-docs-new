# Delete repository connection

`DELETE /accounts/{account_id}/builds/repos/connections/{repo_connection_uuid}`

Remove a repository connection

## Parameters

- **account_id** (string, required) [path]: 
- **repo_connection_uuid** (string, required) [path]: 

## Response

### 200

Operation successful

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **result_info** (object): 
- **success** (boolean): 

### 404

Resource not found

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
