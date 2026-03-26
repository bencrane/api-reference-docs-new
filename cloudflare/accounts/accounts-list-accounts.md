# List Accounts

`GET /accounts`

List all accounts you have ownership or verified access to.

## Parameters

- **name** (string, optional) [query]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **direction** (string, optional) [query]: 

## Response

### 200

List Accounts response

- **result** (array, optional): 

### 4XX

List Accounts response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
