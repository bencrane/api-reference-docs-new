# Create a Namespace

`POST /accounts/{account_id}/storage/kv/namespaces`

Creates a namespace under the given title. A `400` is returned if the account already owns a namespace with this title. A namespace must be explicitly deleted to be replaced.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **title** (string, required): A human-readable string name for a Namespace.

## Response

### 200

Create a Namespace response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Create a Namespace response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
