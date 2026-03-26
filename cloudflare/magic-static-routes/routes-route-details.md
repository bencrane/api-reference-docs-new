# Route Details

`GET /accounts/{account_id}/magic/routes/{route_id}`

Get a specific Magic static route.

## Parameters

- **route_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Route Details response

- **result** (object, optional): 

### 4XX

Route Details response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
