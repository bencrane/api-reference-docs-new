# Remove Resource Group

`DELETE /accounts/{account_id}/iam/resource_groups/{resource_group_id}`

Remove a resource group from an account.

## Parameters

- **account_id** (string, required) [path]: 
- **resource_group_id** (string, required) [path]: 


## Response

### 200

Remove Resource Group response

_Empty object_

### 4XX

Remove Member response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
