# List Resource Groups

`GET /accounts/{account_id}/iam/resource_groups`

List all the resource groups for an account.

## Parameters

- **account_id** (string, required) [path]: 
- **id** (string, optional) [query]: 
- **name** (string, optional) [query]: 

## Response

### 200

List Resource Groups response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 

### 4XX

List Resource Groups response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
