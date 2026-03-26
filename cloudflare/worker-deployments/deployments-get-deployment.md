# Get Deployment

`GET /accounts/{account_id}/workers/scripts/{script_name}/deployments/{deployment_id}`

Get information about a Worker Deployment.

## Parameters

- **account_id** (string, required) [path]: 
- **script_name** (string, required) [path]: 
- **deployment_id** (string, required) [path]: 

## Response

### 200

Get Deployment response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Get Deployment response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
