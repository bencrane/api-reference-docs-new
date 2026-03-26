# List all event query alerts

`GET /accounts/{account_id}/cloudforce-one/events/queries/alerts`

Retrieve all event query alerts for the account

## Parameters

- **account_id** (string, required) [path]: Account ID.

## Response

### 200

Returns a list of event query alerts.

Type: array

### 500

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
