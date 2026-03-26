# List domains

`GET /accounts/{account_id}/registrar/domains`

List domains handled by Registrar.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List domains response

- **result** (array, optional): 

### 4XX

List domains response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
