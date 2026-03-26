# Get a Request

`GET /accounts/{account_id}/cloudforce-one/requests/{request_id}`



## Parameters

- **account_id** (string, required) [path]: 
- **request_id** (string, required) [path]: 

## Response

### 200

Get request response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Get request response failure.

- **errors** (object, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional):
