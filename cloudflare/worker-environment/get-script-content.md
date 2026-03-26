# Get script content

`GET /accounts/{account_id}/workers/services/{service_name}/environments/{environment_name}/content`

Get script content from a worker with an environment.

## Parameters

- **account_id** (string, required) [path]: 
- **service_name** (string, required) [path]: 
- **environment_name** (string, required) [path]: 

## Response

### 200

Get script content.

### 4XX

Get script content failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
