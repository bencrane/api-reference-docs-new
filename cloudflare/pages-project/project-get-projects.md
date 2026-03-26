# Get projects

`GET /accounts/{account_id}/pages/projects`

Fetch a list of all user projects.

## Parameters

- **account_id** (string, required) [path]: 
- **page** (integer, optional) [query]: 
- **per_page** (integer, optional) [query]: 

## Response

### 200

Get projects response.

- **result** (array, optional): 

### 4XX

Get projects response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
