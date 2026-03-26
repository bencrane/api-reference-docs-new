# Resource Group Details

`GET /accounts/{account_id}/iam/resource_groups/{resource_group_id}`

Get information about a specific resource group in an account.

## Parameters

- **account_id** (string, required) [path]: 
- **resource_group_id** (string, required) [path]: 

## Response

### 200

Resource Group Details response

- **result** (object, optional): A group of scoped resources.

### 4XX

Resource Group Details response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
