# Get script content

`GET /accounts/{account_id}/workers/scripts/{script_name}/content/v2`

Fetch script content only.

## Parameters

- **account_id** (string, required) [path]: 
- **script_name** (string, required) [path]: 

## Response

### 200

Fetch script content.

### 4XX

Fetch script content failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
