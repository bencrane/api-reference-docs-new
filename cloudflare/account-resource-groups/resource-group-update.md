# Update Resource Group

`PUT /accounts/{account_id}/iam/resource_groups/{resource_group_id}`

Modify an existing resource group.

## Parameters

- **account_id** (string, required) [path]: 
- **resource_group_id** (string, required) [path]: 

## Request Body

- **name** (string, optional): Name of the resource group
- **scope** (object, optional): A scope is a combination of scope objects which provides additional context.

## Response

### 200

Update Resource Group response

- **result** (object, optional): A group of scoped resources.

### 4XX

Update Resource Group response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
