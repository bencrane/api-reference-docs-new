# Add User Group Members

`POST /accounts/{account_id}/iam/user_groups/{user_group_id}/members`

Add members to a User Group.

## Parameters

- **account_id** (string, required) [path]: 
- **user_group_id** (string, required) [path]: 

## Request Body

Array of object

## Response

### 200

Add User Group Member response

- **result** (object, optional): Member attached to a User Group.

### 4XX

Add User Group Member response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
