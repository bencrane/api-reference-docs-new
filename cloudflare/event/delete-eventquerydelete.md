# Delete a saved event query

`DELETE /accounts/{account_id}/cloudforce-one/events/queries/{query_id}`

Delete a saved event query by its ID

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **query_id** (integer, required) [path]: Event query ID

## Response

### 200

Event query deleted successfully.

### 404

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
