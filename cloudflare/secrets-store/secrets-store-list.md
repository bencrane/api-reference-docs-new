# List account stores

`GET /accounts/{account_id}/secrets_store/stores`

Lists all the stores in an account

## Parameters

- **account_id** (string, required) [path]: 
- **direction** (string, optional) [query]: Direction to sort objects
- **page** (integer, optional) [query]: Page number
- **per_page** (integer, optional) [query]: Number of objects to return per page
- **order** (string, optional) [query]: Order secrets by values in the given field

## Response

### 200

List account stores response

- **result** (array, optional): 

### 4XX

List account stores response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
