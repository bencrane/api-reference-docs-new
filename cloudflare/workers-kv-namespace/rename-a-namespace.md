# Rename a Namespace

`PUT /accounts/{account_id}/storage/kv/namespaces/{namespace_id}`

Modifies a namespace's title.

## Parameters

- **namespace_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **title** (string, required): A human-readable string name for a Namespace.

## Response

### 200

Rename a Namespace response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Rename a Namespace response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
