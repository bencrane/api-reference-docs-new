# List Prefixes

`GET /accounts/{account_id}/addressing/prefixes`

List all prefixes owned by the account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List Prefixes response

- **result** (array, optional): 

### 4XX

List Prefixes response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
