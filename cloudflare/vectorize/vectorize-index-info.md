# Get Vectorize Index Info

`GET /accounts/{account_id}/vectorize/v2/indexes/{index_name}/info`

Get information about a vectorize index.

## Parameters

- **account_id** (string, required) [path]: 
- **index_name** (string, required) [path]: 

## Response

### 200

Get Vectorize Index Info Response

- **result** (object, optional): 

### 4XX

Get Vectorize Index Info Failure Response

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
