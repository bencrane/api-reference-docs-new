# List dispatch namespaces

`GET /accounts/{account_id}/workers/dispatch/namespaces`

Fetch a list of Workers for Platforms namespaces.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Fetch a list of Workers for Platforms namespaces.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 

### 4XX

Failure to get list of Workers for Platforms namespaces.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
