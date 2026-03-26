# Delete key-value pair

`DELETE /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}`

Remove a KV pair from the namespace. Use URL-encoding to use special characters (for example, `:`, `!`, `%`) in the key name.

## Parameters

- **key_name** (string, required) [path]: 
- **namespace_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete key-value pair response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Delete key-value pair response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
