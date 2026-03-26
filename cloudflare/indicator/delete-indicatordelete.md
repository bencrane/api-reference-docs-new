# Deletes an indicator

`DELETE /accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/indicators/{indicator_id}`

Deletes a specific indicator by its UUID.

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **dataset_id** (string, required) [path]: Dataset ID.
- **indicator_id** (string, required) [path]: Indicator UUID.

## Response

### 200

Indicator deleted successfully.

- **message** (string): 
- **success** (boolean): 

### 404

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
