# Show application category by ID

`GET /accounts/{accountId}/resource-library/categories/{id}`

Get application category by ID.

## Parameters

- **accountId** (string, required) [path]: Account ID.
- **id** (string, required) [path]: Application category ID.

## Response

### 200

Get application category by id response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Indicates whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Get application category by id response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Indicates whether the API call was successful. Values: `false`
