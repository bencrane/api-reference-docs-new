# Delete Many Routes

`DELETE /accounts/{account_id}/magic/routes`

Delete multiple Magic static routes.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **routes** (array, required): 

## Response

### 200

Delete Many Routes response

- **result** (object, optional): 

### 4XX

Delete Many Routes response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
