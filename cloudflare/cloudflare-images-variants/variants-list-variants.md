# List variants

`GET /accounts/{account_id}/images/v1/variants`

Lists existing variants.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List variants response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

List variants response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
