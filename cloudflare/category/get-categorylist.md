# Lists categories across multiple datasets

`GET /accounts/{account_id}/cloudforce-one/events/categories`



## Parameters

- **account_id** (string, required) [path]: Account ID.
- **datasetIds** (array, optional) [query]: Array of dataset IDs to query categories from. If not provided, uses the default dataset.

## Response

### 200

Returns a list of categories.

Type: array

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
