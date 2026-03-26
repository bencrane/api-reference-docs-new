# Delete Vectorize Index (Deprecated)

`DELETE /accounts/{account_id}/vectorize/indexes/{index_name}`

> **Deprecated**

Deletes the specified Vectorize Index.

## Parameters

- **account_id** (string, required) [path]: 
- **index_name** (string, required) [path]: 

## Response

### 200

Delete Vectorize Index Response

- **result** (object, optional): 

### 4XX

Delete Vectorize Index Failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
