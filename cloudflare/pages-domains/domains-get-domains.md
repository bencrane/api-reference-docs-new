# Get domains

`GET /accounts/{account_id}/pages/projects/{project_name}/domains`

Fetch a list of all domains associated with a Pages project.

## Parameters

- **project_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get domains response.

- **result** (array, optional): 

### 4XX

Get domains response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
