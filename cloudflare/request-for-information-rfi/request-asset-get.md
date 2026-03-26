# Get a Request Asset

`GET /accounts/{account_id}/cloudforce-one/requests/{request_id}/asset/{asset_id}`



## Parameters

- **account_id** (string, required) [path]: 
- **request_id** (string, required) [path]: 
- **asset_id** (string, required) [path]: 

## Response

### 200

Get request asset response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 

### 4XX

Get request asset response failure.

- **errors** (object, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional):
