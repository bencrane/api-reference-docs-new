# Get tunnel route

`GET /accounts/{account_id}/teamnet/routes/{route_id}`

Get a private network route in an account.

## Parameters

- **account_id** (string, required) [path]: 
- **route_id** (string, required) [path]: 

## Response

### 200

Get a tunnel route response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Get a tunnel route response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
