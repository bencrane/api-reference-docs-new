# Get Script Settings

`GET /accounts/{account_id}/workers/services/{service_name}/environments/{environment_name}/settings`

Get script settings from a worker with an environment.

## Parameters

- **account_id** (string, required) [path]: 
- **service_name** (string, required) [path]: 
- **environment_name** (string, required) [path]: 

## Response

### 200

Fetch script settings.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Fetch script settings failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
