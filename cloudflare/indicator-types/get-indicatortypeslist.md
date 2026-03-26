# Lists indicator types across multiple datasets

`GET /accounts/{account_id}/cloudforce-one/events/indicator-types`



## Parameters

- **account_id** (string, required) [path]: Account ID.
- **datasetIds** (array, optional) [query]: Array of dataset IDs to query indicator types from. If not provided, queries all datasets for the account.

## Response

### 200

Returns a list of indicator types.

- **items** (object): 
- **type** (string): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
