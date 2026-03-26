# Delete a Request Asset

`DELETE /accounts/{account_id}/cloudforce-one/requests/{request_id}/asset/{asset_id}`



## Parameters

- **account_id** (string, required) [path]: 
- **request_id** (string, required) [path]: 
- **asset_id** (string, required) [path]: 

## Response

### 200

Delete request asset response.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Delete request asset response failure.

- **errors** (object, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional):
