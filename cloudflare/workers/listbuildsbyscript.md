# List builds by script

`GET /accounts/{account_id}/builds/workers/{external_script_id}/builds`

Get all builds for a specific worker script with pagination

## Parameters

- **account_id** (string, required) [path]: 
- **external_script_id** (string, required) [path]: 
- **page** (integer, optional) [query]: Page number for pagination
- **per_page** (integer, optional) [query]: Number of items per page

## Response

### 200

Builds retrieved successfully

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (array, optional): 
- **result_info** (object, optional): 
- **success** (boolean, optional):
