# Get repository configuration autofill

`GET /accounts/{account_id}/builds/repos/{provider_type}/{provider_account_id}/{repo_id}/config_autofill`

Analyze repository for automatic configuration detection

## Parameters

- **account_id** (string, required) [path]: 
- **provider_type** (string, required) [path]: SCM provider type
- **provider_account_id** (string, required) [path]: 
- **repo_id** (string, required) [path]: 
- **branch** (string, required) [query]: 
- **root_directory** (string, optional) [query]: 

## Response

### 200

Configuration autofill data retrieved successfully

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **result_info** (object, optional): 
- **success** (boolean, optional):
