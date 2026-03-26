# Read a group for an account

`GET /accounts/{account_id}/cloudforce-one/events/dataset/-/groups/{group_id}`

Read a group for an account

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **group_id** (string, required) [path]: 

## Response

### 200

Return the group.

- **createdAt** (string): 
- **description** (string): 
- **members** (array): 
- **name** (string): 
- **updatedAt** (string): 
- **uuid** (string): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
