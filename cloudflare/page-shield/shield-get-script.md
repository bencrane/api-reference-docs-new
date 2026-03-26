# Get a Page Shield script

`GET /zones/{zone_id}/page_shield/scripts/{script_id}`

Fetches a script detected by Page Shield by script ID.

## Parameters

- **zone_id** (string, required) [path]: 
- **script_id** (string, required) [path]: 

## Response

### 200

Get a Page Shield script response

- **result** (object, optional): 

### 4XX

Get a Page Shield script response failure

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
