# Get all application categories

`GET /accounts/{accountId}/resource-library/categories`

Get all application categories.

## Parameters

- **accountId** (string, required) [path]: Account ID.

## Response

### 200

Get all application categories response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Indicates whether the API call was successful. Values: `true`
- **result** (array, optional): Returns the list of categories.

### 4XX

Get application categories response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Indicates whether the API call was successful. Values: `false`
