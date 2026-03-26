# Update project

`PATCH /accounts/{account_id}/pages/projects/{project_name}`

Set new attributes for an existing project. Modify environment variables. To delete an environment variable, set the key to null.

## Parameters

- **project_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **build_config** (object, optional): Configs for the project build process.
- **deployment_configs** (object, optional): Configs for deployments in a project.
- **name** (string, optional): Name of the project.
- **production_branch** (string, optional): Production branch of the project. Used to identify production deployments.
- **source** (object, optional): Configs for the project source control.

## Response

### 200

Update project response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Update project response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
