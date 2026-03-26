# Create a New Request Asset

`POST /accounts/{account_id}/cloudforce-one/requests/{request_id}/asset/new`



## Parameters

- **account_id** (string, required) [path]: 
- **request_id** (string, required) [path]: 


## Response

### 200

Create request asset response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Create request asset response failure.

- **errors** (object, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional):
