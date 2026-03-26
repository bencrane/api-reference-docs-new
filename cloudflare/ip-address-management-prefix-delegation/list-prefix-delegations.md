# List Prefix Delegations

`GET /accounts/{account_id}/addressing/prefixes/{prefix_id}/delegations`

List all delegations for a given account IP prefix.

## Parameters

- **prefix_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

List Prefix Delegations response

- **result** (array, optional): 

### 4XX

List Prefix Delegations response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
