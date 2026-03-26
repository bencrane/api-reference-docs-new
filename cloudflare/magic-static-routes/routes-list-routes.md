# List Routes

`GET /accounts/{account_id}/magic/routes`

List all Magic static routes.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List Routes response

- **result** (object, optional): 

### 4XX

List Routes response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
