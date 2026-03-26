# Remove User Group Member

`DELETE /accounts/{account_id}/iam/user_groups/{user_group_id}/members/{member_id}`

Remove a member from User Group

## Parameters

- **account_id** (string, required) [path]: 
- **user_group_id** (string, required) [path]: 
- **member_id** (string, required) [path]: 

## Response

### 200

Delete User Group Member response

- **result** (object, optional): Member attached to a User Group.

### 4XX

Delete User Group response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
