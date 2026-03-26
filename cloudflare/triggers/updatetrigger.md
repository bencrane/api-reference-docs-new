# Update trigger

`PATCH /accounts/{account_id}/builds/triggers/{trigger_uuid}`

Update an existing CI/CD trigger

## Parameters

- **account_id** (string, required) [path]: 
- **trigger_uuid** (string, required) [path]: 

## Request Body

- **branch_excludes** (array, optional): 
- **branch_includes** (array, optional): 
- **build_caching_enabled** (boolean, optional): 
- **build_command** (string, optional): 
- **build_token_uuid** (string, optional): Build token UUID.
- **deploy_command** (string, optional): 
- **path_excludes** (array, optional): 
- **path_includes** (array, optional): 
- **root_directory** (string, optional): Root directory path.
- **trigger_name** (string, optional): 

## Response

### 200

Trigger updated successfully

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **result_info** (object, optional): 
- **success** (boolean, optional): 

### 404

Resource not found

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
