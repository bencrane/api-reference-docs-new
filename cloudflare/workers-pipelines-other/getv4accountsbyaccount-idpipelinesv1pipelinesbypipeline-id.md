# Get Pipeline Details

`GET /accounts/{account_id}/pipelines/v1/pipelines/{pipeline_id}`

Get Pipelines Details.

## Parameters

- **account_id** (string, required) [path]: 
- **pipeline_id** (string, required) [path]: 

## Response

### 200

Indicates a successfully retrieved Pipeline.

- **result** (object): 
- **success** (boolean): Indicates whether the API call was successful.

### 4XX

Indicates an error in retrieving Pipelines.
