# Delete an event query alert

`DELETE /accounts/{account_id}/cloudforce-one/events/queries/alerts/{alert_id}`

Delete an event query alert subscription by its ID

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **alert_id** (integer, required) [path]: Event query alert ID

## Response

### 200

Event query alert deleted successfully.

### 404

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
