# List User Group Members

`GET /accounts/{account_id}/iam/user_groups/{user_group_id}/members`

List all the members attached to a user group.

## Parameters

- **account_id** (string, required) [path]: 
- **user_group_id** (string, required) [path]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 

## Response

### 200

List User Group Members

- **result** (array, optional): 

### 4XX

User Group Details response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
