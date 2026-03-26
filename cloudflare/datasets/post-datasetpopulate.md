# Populate dataset-specific lookup tables from existing Events data with batch processing

`POST /accounts/{account_id}/cloudforce-one/events/datasets/populate`



## Parameters

- **account_id** (string, required) [path]: Account ID.

## Response

### 200

Returns population results with counts and any errors

- **properties** (object): 
- **type** (string): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
