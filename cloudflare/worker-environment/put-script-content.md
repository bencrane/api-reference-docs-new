# Put script content

`PUT /accounts/{account_id}/workers/services/{service_name}/environments/{environment_name}/content`

Put script content from a worker with an environment.

## Parameters

- **account_id** (string, required) [path]: 
- **service_name** (string, required) [path]: 
- **environment_name** (string, required) [path]: 
- **CF-WORKER-BODY-PART** (string, optional) [header]: The multipart name of a script upload part containing script content in service worker format. Alternative to including in a metadata part.
- **CF-WORKER-MAIN-MODULE-PART** (string, optional) [header]: The multipart name of a script upload part containing script content in es module format. Alternative to including in a metadata part.


## Response

### 200

Put script content.

- **result** (object, optional): 

### 4XX

Put script content failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
