# List Members

`GET /accounts/{account_id}/members`

List all members of an account.

## Parameters

- **account_id** (string, required) [path]: 
- **order** (string, optional) [query]: 
- **status** (string, optional) [query]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **direction** (string, optional) [query]: 

## Response

### 200

List Members response

- **result** (array, optional): 

### 4XX

List Members response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
