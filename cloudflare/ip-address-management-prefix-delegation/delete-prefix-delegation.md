# Delete Prefix Delegation

`DELETE /accounts/{account_id}/addressing/prefixes/{prefix_id}/delegations/{delegation_id}`

Delete an account delegation for a given IP prefix.

## Parameters

- **delegation_id** (string, required) [path]: 
- **prefix_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete Prefix Delegation response

- **result** (object, optional): 

### 4XX

Delete Prefix Delegation response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
