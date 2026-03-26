# Create project

`POST /accounts/{account_id}/pages/projects`

Create a new project.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **build_config** (object, optional): Configs for the project build process.
- **deployment_configs** (object, optional): Configs for deployments in a project.
- **name** (string, required): Name of the project.
- **production_branch** (string, required): Production branch of the project. Used to identify production deployments.
- **source** (object, optional): Configs for the project source control.

## Response

### 200

Create project response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Create project response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
