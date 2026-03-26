# List Tokens

`GET /accounts/{account_id}/tokens`

List all Account Owned API tokens created for this account.

## Parameters

- **account_id** (string, required) [path]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **direction** (string, optional) [query]: 

## Response

### 200

List Tokens response

- **result** (array, optional): 

### 4XX

List Tokens response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
