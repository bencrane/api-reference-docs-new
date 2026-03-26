# List permissions for dataset

`GET /accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/permissions`

List permissions

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **dataset_id** (string, required) [path]: Dataset UUID.

## Response

### 200

Returns the list of permissions.

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
