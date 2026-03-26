# User Group Details

`GET /accounts/{account_id}/iam/user_groups/{user_group_id}`

Get information about a specific user group in an account.

## Parameters

- **account_id** (string, required) [path]: 
- **user_group_id** (string, required) [path]: 

## Response

### 200

User Group Details response

- **result** (object, optional): A group of policies resources.

### 4XX

User Group Details response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
