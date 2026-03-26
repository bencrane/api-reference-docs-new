# Delete a group member

`DELETE /accounts/{account_id}/cloudforce-one/events/dataset/-/groups/{group_id}/members/{member_id}`

Delete a group member

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **group_id** (string, required) [path]: 
- **member_id** (string, required) [path]: 

## Response

### 200

Returns the created group member.

- **message** (string): 
- **success** (boolean): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
