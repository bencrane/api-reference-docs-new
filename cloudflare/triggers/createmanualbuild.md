# Create manual build

`POST /accounts/{account_id}/builds/triggers/{trigger_uuid}/builds`

Trigger a manual build for a specific trigger

## Parameters

- **account_id** (string, required) [path]: 
- **trigger_uuid** (string, required) [path]: 

## Request Body

- **branch** (object, optional): Git branch name (required if commit_hash not provided)
- **commit_hash** (object, optional): Git commit hash (required if branch not provided)
- **seed_repo** (object, optional): 

## Response

### 200

Build created successfully

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **result_info** (object, optional): 
- **success** (boolean, optional):
