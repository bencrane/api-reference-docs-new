# Update a Request Asset

`PUT /accounts/{account_id}/cloudforce-one/requests/{request_id}/asset/{asset_id}`



## Parameters

- **account_id** (string, required) [path]: 
- **request_id** (string, required) [path]: 
- **asset_id** (string, required) [path]: 

## Request Body

- **source** (string, optional): Asset file to upload.

## Response

### 200

Update request asset response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Update request asset response failure.

- **errors** (object, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional):
