# Upsert environment variables

`PATCH /accounts/{account_id}/builds/triggers/{trigger_uuid}/environment_variables`

Create or update environment variables for a trigger

## Parameters

- **account_id** (string, required) [path]: 
- **trigger_uuid** (string, required) [path]: 

## Request Body

_Empty object_

## Response

### 200

Environment variables updated successfully

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
