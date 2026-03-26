# Get application By Id

`GET /accounts/{accountId}/resource-library/applications/{id}`

Get application by ID.

## Parameters

- **accountId** (string, required) [path]: Account ID.
- **id** (string, required) [path]: Application ID.

## Response

### 200

Get the application response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Indicates whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Get application by id response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Indicates whether the API call was successful. Values: `false`
