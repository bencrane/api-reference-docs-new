# List triggers by script

`GET /accounts/{account_id}/builds/workers/{external_script_id}/triggers`

Get all triggers for a specific worker script

## Parameters

- **account_id** (string, required) [path]: 
- **external_script_id** (string, required) [path]: 

## Response

### 200

Triggers retrieved successfully

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (array, optional): 
- **result_info** (object, optional): 
- **success** (boolean, optional):
