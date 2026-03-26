# List Vectors

`GET /accounts/{account_id}/vectorize/v2/indexes/{index_name}/list`

Returns a paginated list of vector identifiers from the specified index.

## Parameters

- **account_id** (string, required) [path]: 
- **index_name** (string, required) [path]: 
- **count** (integer, optional) [query]: 
- **cursor** (string, optional) [query]: 

## Response

### 200

List Vectors Response

- **result** (object, optional): 

### 4XX

List Vectors Failure Response

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
