# Deletes one or more events

`DELETE /accounts/{account_id}/cloudforce-one/events/{dataset_id}/delete`



## Parameters

- **account_id** (string, required) [path]: Account ID.
- **dataset_id** (string, required) [path]: Dataset UUID.
- **eventIds** (array, required) [query]: Array of Event IDs to delete.

## Response

### 200

Returns the number of deleted events.

Type: number

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
