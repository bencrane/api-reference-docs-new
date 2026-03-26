# Create a group member

`POST /accounts/{account_id}/cloudforce-one/events/dataset/-/groups/{group_id}/members`

Create a group member

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **group_id** (string, required) [path]: 

## Request Body

- **accountId** (string, optional): 
- **accountTag** (string, optional): 

## Response

### 200

Returns the created group member.

- **accountId** (string): 
- **accountTag** (string): 
- **createdAt** (string): 
- **updatedAt** (string): 
- **uuid** (string): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
