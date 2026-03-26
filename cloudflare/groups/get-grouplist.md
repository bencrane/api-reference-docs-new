# List groups for an account

`GET /accounts/{account_id}/cloudforce-one/events/dataset/-/groups`

List groups for an account

## Parameters

- **account_id** (string, required) [path]: Account ID.

## Response

### 200

Returns the list of groups.

Type: array

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
