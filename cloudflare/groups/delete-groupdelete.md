# Delete a group for an account

`DELETE /accounts/{account_id}/cloudforce-one/events/dataset/-/groups/{group_id}`

Delete a group for an account

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **group_id** (string, required) [path]: 

## Response

### 200

Group deleted successfully.

- **message** (string): 
- **success** (boolean): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
