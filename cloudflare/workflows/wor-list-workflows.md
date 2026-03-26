# List all Workflows

`GET /accounts/{account_id}/workflows`

Lists all workflows configured for the account.

## Parameters

- **per_page** (number, optional) [query]: 
- **page** (number, optional) [query]: 
- **search** (string, optional) [query]: Allows filtering workflows` name.
- **account_id** (string, required) [path]: 

## Response

### 200

List of all Workflows belonging to a account.

- **errors** (array): 
- **messages** (array): 
- **result** (array): 
- **result_info** (object): 
- **success** (boolean): 

### 400

Input Validation Error.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
