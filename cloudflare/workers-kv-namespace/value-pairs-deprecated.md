# Delete multiple key-value pairs

`DELETE /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk`

> **Deprecated**

Remove multiple KV pairs from the namespace. Body should be an array of up to 10,000 keys to be removed.

## Parameters

- **namespace_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

Array of string

## Response

### 200

Delete multiple key-value pairs response.

- **result** (object, optional): 

### 4XX

Delete multiple key-value pairs response failure.

- **result** (object, optional):
