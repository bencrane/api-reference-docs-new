# List group members

`GET /accounts/{account_id}/cloudforce-one/events/dataset/-/groups/{group_id}/members`

List group members

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **group_id** (string, required) [path]: 

## Response

### 200

Returns the group members.

Type: array

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
