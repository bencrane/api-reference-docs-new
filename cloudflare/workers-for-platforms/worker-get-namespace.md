# Get dispatch namespace

`GET /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}`

Get a Workers for Platforms namespace.

## Parameters

- **account_id** (string, required) [path]: 
- **dispatch_namespace** (string, required) [path]: 

## Response

### 200

Get a Workers for Platforms namespace.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Failure to get Workers for Platforms namespace.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
