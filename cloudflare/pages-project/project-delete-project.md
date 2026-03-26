# Delete project

`DELETE /accounts/{account_id}/pages/projects/{project_name}`

Delete a project by name.

## Parameters

- **project_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Delete project response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Delete project response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
