# Patch domain

`PATCH /accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}`

Retry the validation status of a single domain.

## Parameters

- **domain_name** (string, required) [path]: 
- **project_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Patch domain response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Patch domain response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
