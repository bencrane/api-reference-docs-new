# Get target

`GET /accounts/{account_id}/infrastructure/targets/{target_id}`



## Parameters

- **account_id** (string, required) [path]: 
- **target_id** (string, required) [path]: 

## Response

### 200

Successfully retrieved the target

- **result** (object, optional): 

### 4XX

Failed to retrieve the target

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
