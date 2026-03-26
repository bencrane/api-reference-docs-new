# Purge build cache

`POST /accounts/{account_id}/pages/projects/{project_name}/purge_build_cache`

Purge all cached build artifacts for a Pages project

## Parameters

- **project_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Purge build cache response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Purge build cache failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
