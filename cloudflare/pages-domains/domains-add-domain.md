# Add domain

`POST /accounts/{account_id}/pages/projects/{project_name}/domains`

Add a new domain for the Pages project.

## Parameters

- **project_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **name** (string, required): The domain name.

## Response

### 200

Add domain response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Add domain response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
