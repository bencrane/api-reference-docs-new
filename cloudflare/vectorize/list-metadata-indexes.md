# List Metadata Indexes

`GET /accounts/{account_id}/vectorize/v2/indexes/{index_name}/metadata_index/list`

List Metadata Indexes for the specified Vectorize Index.

## Parameters

- **account_id** (string, required) [path]: 
- **index_name** (string, required) [path]: 

## Response

### 200

List Metadata Index Response

- **result** (object, optional): 

### 4XX

List Metadata Index Failure Response

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
