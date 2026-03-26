# Get multiple key-value pairs

`POST /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/get`

Retrieve up to 100 KV pairs from the namespace. Keys must contain text-based values. JSON values can optionally be parsed instead of being returned as a string value. Metadata can be included if `withMetadata` is true.

## Parameters

- **namespace_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **keys** (array, required): Array of keys to retrieve (maximum of 100).
- **type** (string, optional): Whether to parse JSON values in the response. Values: `text`, `json`
- **withMetadata** (boolean, optional): Whether to include metadata in the response.

## Response

### 200

Get multiple key-value pairs response.

- **result** (object, optional): 

### 4XX

Get multiple key-value pairs response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
