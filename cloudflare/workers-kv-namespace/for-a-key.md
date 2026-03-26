# Read the metadata for a key

`GET /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/metadata/{key_name}`

Returns the metadata associated with the given key in the given namespace. Use URL-encoding to use special characters (for example, `:`, `!`, `%`) in the key name.

## Parameters

- **key_name** (string, required) [path]: 
- **namespace_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Read the metadata for a key response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Read the metadata for a key response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
