# Delete a Request

`DELETE /accounts/{account_id}/cloudforce-one/requests/{request_id}`



## Parameters

- **account_id** (string, required) [path]: 
- **request_id** (string, required) [path]: 

## Response

### 200

Delete request response.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Delete request response failure.

- **errors** (object, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional):
