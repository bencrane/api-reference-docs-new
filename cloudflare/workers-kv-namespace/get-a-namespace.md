# Get a Namespace

`GET /accounts/{account_id}/storage/kv/namespaces/{namespace_id}`

Get the namespace corresponding to the given ID.

## Parameters

- **namespace_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get a Namespace response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Get a Namespace response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
