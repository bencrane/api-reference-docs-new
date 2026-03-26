# Delete Deployment

`DELETE /accounts/{account_id}/workers/scripts/{script_name}/deployments/{deployment_id}`

Delete a Worker Deployment. The latest deployment, which is actively serving traffic, cannot be deleted. All other deployments can be deleted.

## Parameters

- **account_id** (string, required) [path]: 
- **script_name** (string, required) [path]: 
- **deployment_id** (string, required) [path]: 

## Response

### 200

Delete Deployment response.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Delete Deployment response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
