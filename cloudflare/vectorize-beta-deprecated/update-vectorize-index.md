# Update Vectorize Index (Deprecated)

`PUT /accounts/{account_id}/vectorize/indexes/{index_name}`

> **Deprecated**

Updates and returns the specified Vectorize Index.

## Parameters

- **account_id** (string, required) [path]: 
- **index_name** (string, required) [path]: 

## Request Body

- **description** (string, required): Specifies the description of the index.

## Response

### 200

Update Vectorize Index Response

- **result** (object, optional): 

### 4XX

Update Vectorize Index Failure Response

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
