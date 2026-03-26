# Retry deployment

`POST /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/retry`

Retry a previous deployment.

## Parameters

- **deployment_id** (string, required) [path]: 
- **project_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Retry deployment response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Retry deployment response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
