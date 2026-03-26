# List Vectorize Indexes

`GET /accounts/{account_id}/vectorize/v2/indexes`

Returns a list of Vectorize Indexes

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List Vectorize Index Response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

List Vectorize Index Failure Response

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
