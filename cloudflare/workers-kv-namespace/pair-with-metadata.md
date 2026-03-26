# Write key-value pair with optional metadata

`PUT /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}`

Write a value identified by a key. Use URL-encoding to use special characters (for example, `:`, `!`, `%`) in the key name. Body should be the value to be stored. If JSON metadata to be associated with the key/value pair is needed, use `multipart/form-data` content type for your PUT request (see dropdown below in `REQUEST BODY SCHEMA`). Existing values, expirations, and metadata will be overwritten. If neither `expiration` nor `expiration_ttl` is specified, the key-value pair will never expire. If both are set, `expiration_ttl` is used and `expiration` is ignored.

## Parameters

- **key_name** (string, required) [path]: 
- **namespace_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **expiration** (string, optional) [query]: 
- **expiration_ttl** (string, optional) [query]: 


## Response

### 200

Write key-value pair with metadata response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Write key-value pair with metadata response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
