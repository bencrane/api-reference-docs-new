# List mirrored tags for an indicator dataset

`GET /accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/indicators/tags`

Returns all mirrored tags from the indicator dataset (DO mirror table). No pagination.

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **dataset_id** (string, required) [path]: Dataset ID.

## Response

### 200

Returns an array of mirrored tags.

Type: array

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean): 

### 404

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean): 

### 500

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
