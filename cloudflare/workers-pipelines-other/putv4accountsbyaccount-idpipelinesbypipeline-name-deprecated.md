# [DEPRECATED] Update Pipeline

`PUT /accounts/{account_id}/pipelines/{pipeline_name}`

> **Deprecated**

[DEPRECATED] Update an existing pipeline. Use the new /pipelines/v1/pipelines endpoint instead.

## Parameters

- **account_id** (string, required) [path]: 
- **pipeline_name** (string, required) [path]: 

## Request Body

- **destination** (object, required): 
- **name** (string, required): Defines the name of the pipeline.
- **source** (array, required): 

## Response

### 200

[DEPRECATED] Indicates a successfully updated pipeline.

- **result** (object): [DEPRECATED] Describes the configuration of a pipeline. Use the new streams/sinks/pipelines API instead.
- **success** (boolean): Indicates whether the API call was successful.

### 4XX

Indicates an error updating pipeline.

- **errors** (array): 
- **results** (object): 
- **success** (object):
