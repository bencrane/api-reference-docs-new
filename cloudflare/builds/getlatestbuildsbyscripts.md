# Get latest builds by script IDs

`GET /accounts/{account_id}/builds/builds/latest`

Retrieve the most recent builds for multiple worker scripts

## Parameters

- **account_id** (string, required) [path]: 
- **external_script_ids** (string, required) [query]: 

## Response

### 200

Latest builds retrieved successfully

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **result_info** (object, optional): 
- **success** (boolean, optional):
