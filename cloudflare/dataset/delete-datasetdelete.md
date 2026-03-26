# Delete a dataset

`DELETE /accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}`

Deletes a dataset given a datasetId.

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **dataset_id** (string, required) [path]: Dataset ID to delete

## Response

### 200

Returns the uuid and name of the deleted dataset.

- **name** (string): 
- **uuid** (string): 

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
