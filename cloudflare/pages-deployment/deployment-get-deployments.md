# Get deployments

`GET /accounts/{account_id}/pages/projects/{project_name}/deployments`

Fetch a list of project deployments.

## Parameters

- **project_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **env** (string, optional) [query]: 
- **page** (integer, optional) [query]: 
- **per_page** (integer, optional) [query]: 

## Response

### 200

Get deployments response.

- **result** (array, optional): 

### 4XX

Get deployments response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
