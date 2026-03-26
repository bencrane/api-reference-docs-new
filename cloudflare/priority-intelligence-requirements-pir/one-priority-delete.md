# Delete a Priority Intelligence Requirement

`DELETE /accounts/{account_id}/cloudforce-one/requests/priority/{priority_id}`



## Parameters

- **account_id** (string, required) [path]: 
- **priority_id** (string, required) [path]: 

## Response

### 200

Delete priority response.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Delete priority response failure.

- **errors** (object, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional):
