# Get deployment info

`GET /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}`

Fetch information about a deployment.

## Parameters

- **deployment_id** (string, required) [path]: 
- **project_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get deployment info response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Get deployment info response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
