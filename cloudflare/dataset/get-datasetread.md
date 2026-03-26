# Reads a dataset

`GET /accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}`



## Parameters

- **account_id** (string, required) [path]: Account ID.
- **dataset_id** (string, required) [path]: Dataset ID.

## Response

### 200

Returns a dataset.

- **isPublic** (boolean): 
- **name** (string): 
- **uuid** (string): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
