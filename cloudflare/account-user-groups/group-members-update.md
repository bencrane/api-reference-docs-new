# Update User Group Members

`PUT /accounts/{account_id}/iam/user_groups/{user_group_id}/members`

Replace the set of members attached to a User Group.

## Parameters

- **account_id** (string, required) [path]: 
- **user_group_id** (string, required) [path]: 

## Request Body

Array of object

## Response

### 200

Update User Group Members response

- **result** (array, optional): 

### 4XX

Update User Group response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
