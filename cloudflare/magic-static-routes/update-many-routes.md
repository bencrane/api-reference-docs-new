# Update Many Routes

`PUT /accounts/{account_id}/magic/routes`

Update multiple Magic static routes. Use `?validate_only=true` as an optional query parameter to run validation only without persisting changes. Only fields for a route that need to be changed need be provided.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **routes** (array, required): 

## Response

### 200

Update Many Routes response

- **result** (object, optional): 

### 4XX

Update Many Routes response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
