# Lists all target industries for a specific dataset

`GET /accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/targetIndustries`



## Parameters

- **account_id** (string, required) [path]: Account ID.
- **dataset_id** (string, required) [path]: Dataset UUID.

## Response

### 200

Returns a list of target industries for the dataset.

- **items** (object): 
- **type** (string): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
