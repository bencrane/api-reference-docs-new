# List User Groups

`GET /accounts/{account_id}/iam/user_groups`

List all the user groups for an account.

## Parameters

- **account_id** (string, required) [path]: 
- **id** (string, optional) [query]: ID of the user group to be fetched.
- **name** (string, optional) [query]: 
- **fuzzyName** (string, optional) [query]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **direction** (string, optional) [query]: 

## Response

### 200

List User Group response

- **result** (array, optional): A list of user groups for the account.

### 4XX

List User Group response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
