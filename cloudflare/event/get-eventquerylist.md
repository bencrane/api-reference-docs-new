# List all saved event queries

`GET /accounts/{account_id}/cloudforce-one/events/queries`

Retrieve all saved event queries for the account

## Parameters

- **account_id** (string, required) [path]: Account ID.

## Response

### 200

Returns a list of event queries.

Type: array

### 500

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
