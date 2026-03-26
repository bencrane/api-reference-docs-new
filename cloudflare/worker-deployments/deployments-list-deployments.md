# List Deployments

`GET /accounts/{account_id}/workers/scripts/{script_name}/deployments`

List of Worker Deployments. The first deployment in the list is the latest deployment actively serving traffic.

## Parameters

- **account_id** (string, required) [path]: 
- **script_name** (string, required) [path]: 

## Response

### 200

List Deployments response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

List Deployments response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
