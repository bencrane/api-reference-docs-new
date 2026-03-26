# List Scripts in Namespace

`GET /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts`

Fetch a list of scripts uploaded to a Workers for Platforms namespace.

## Parameters

- **account_id** (string, required) [path]: 
- **dispatch_namespace** (string, required) [path]: 
- **tags** (string, optional) [query]: Filter scripts by tags. Format: comma-separated list of tag:allowed pairs where allowed is 'yes' or 'no'.

## Response

### 200

List scripts in namespace response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 

### 4XX

List scripts in namespace response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
