# Create Resource Group

`POST /accounts/{account_id}/iam/resource_groups`

Create a new Resource Group under the specified account.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **name** (string, required): Name of the resource group
- **scope** (object, required): A scope is a combination of scope objects which provides additional context.

## Response

### 200

Add Resource Group response

- **result** (object, optional): A group of scoped resources.

### 4XX

Add Resource Group response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
