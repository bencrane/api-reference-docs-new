# Write multiple key-value pairs

`PUT /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk`

Write multiple keys and values at once. Body should be an array of up to 10,000 key-value pairs to be stored, along with optional expiration information. Existing values and expirations will be overwritten. If neither `expiration` nor `expiration_ttl` is specified, the key-value pair will never expire. If both are set, `expiration_ttl` is used and `expiration` is ignored. The entire request size must be 100 megabytes or less.

## Parameters

- **namespace_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

Array of object

## Response

### 200

Write multiple key-value pairs response.

- **result** (object, optional): 

### 4XX

Write multiple key-value pairs response failure.

- **result** (object, optional):
