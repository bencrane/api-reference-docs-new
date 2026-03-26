# Permission Group Details

`GET /accounts/{account_id}/iam/permission_groups/{permission_group_id}`

Get information about a specific permission group in an account.

## Parameters

- **account_id** (string, required) [path]: 
- **permission_group_id** (string, required) [path]: 

## Response

### 200

Permission Group Details response

- **result** (object, optional): A named group of permissions that map to a group of operations against resources.

### 4XX

Permission Group Details response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
