# List Roles

`GET /accounts/{account_id}/roles`

Get all available roles for an account.

## Parameters

- **account_id** (string, required) [path]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 

## Response

### 200

List Roles response

- **result** (array, optional): 

### 4XX

List Roles response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
