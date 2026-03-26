# Create trigger

`POST /accounts/{account_id}/builds/triggers`

Create a new CI/CD trigger

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **branch_excludes** (array, required): 
- **branch_includes** (array, required): 
- **build_caching_enabled** (boolean, optional): 
- **build_command** (string, required): 
- **build_token_uuid** (string, required): Build token UUID.
- **deploy_command** (string, required): 
- **external_script_id** (string, required): External script identifier.
- **path_excludes** (array, required): 
- **path_includes** (array, required): 
- **repo_connection_uuid** (string, required): Repository connection UUID.
- **root_directory** (string, required): Root directory path.
- **trigger_name** (string, required): 

## Response

### 200

Trigger created successfully

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **result_info** (object, optional): 
- **success** (boolean, optional):
