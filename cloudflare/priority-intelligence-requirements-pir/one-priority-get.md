# Get a Priority Intelligence Requirement

`GET /accounts/{account_id}/cloudforce-one/requests/priority/{priority_id}`



## Parameters

- **account_id** (string, required) [path]: 
- **priority_id** (string, required) [path]: 

## Response

### 200

Get priority response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Get priority response failure.

- **errors** (object, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional):
