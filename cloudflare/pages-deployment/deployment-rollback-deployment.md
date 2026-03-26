# Rollback deployment

`POST /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/rollback`

Rollback the production deployment to a previous deployment. You can only rollback to succesful builds on production.

## Parameters

- **deployment_id** (string, required) [path]: 
- **project_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Rollback deployment response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Rollback deployment response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
