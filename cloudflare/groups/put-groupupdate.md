# Update a group

`PUT /accounts/{account_id}/cloudforce-one/events/dataset/-/groups/{group_id}`

Update a group

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **group_id** (string, required) [path]: 

## Request Body

- **description** (string, required): 
- **name** (string, required): 

## Response

### 200

Returns the updated group.

- **createdAt** (string): 
- **description** (string): 
- **name** (string): 
- **updatedAt** (string): 
- **uuid** (string): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
