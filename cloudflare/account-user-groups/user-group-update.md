# Update User Group

`PUT /accounts/{account_id}/iam/user_groups/{user_group_id}`

Modify an existing user group.

## Parameters

- **account_id** (string, required) [path]: 
- **user_group_id** (string, required) [path]: 

## Request Body

- **name** (string, optional): Name of the User group.
- **policies** (array, optional): Policies attached to the User group

## Response

### 200

Update User Group response

- **result** (object, optional): A group of policies resources.

### 4XX

Update User Group response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
