# List environment variables

`GET /accounts/{account_id}/builds/triggers/{trigger_uuid}/environment_variables`

Get all environment variables for a trigger

## Parameters

- **account_id** (string, required) [path]: 
- **trigger_uuid** (string, required) [path]: 

## Response

### 200

Environment variables retrieved successfully

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **result_info** (object, optional): 
- **success** (boolean, optional):
