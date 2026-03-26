# Read key-value pair

`GET /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}`

Returns the value associated with the given key in the given namespace. Use URL-encoding to use special characters (for example, `:`, `!`, `%`) in the key name. If the KV-pair is set to expire at some point, the expiration time as measured in seconds since the UNIX epoch will be returned in the `expiration` response header.

## Parameters

- **key_name** (string, required) [path]: 
- **namespace_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Read key-value pair response.

### 4XX

Read key-value pair response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
