# Get zone setting

`GET /zones/{zone_id}/settings/{setting_id}`

Fetch a single zone setting by name

## Parameters

- **zone_id** (string, required) [path]: 
- **setting_id** (string, required) [path]: 

## Response

### 200

Get zone setting response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful
- **result** (object, optional): 

### 4XX

Get zone setting response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
