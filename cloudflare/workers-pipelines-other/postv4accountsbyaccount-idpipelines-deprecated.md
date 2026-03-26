# [DEPRECATED] Create Pipeline

`POST /accounts/{account_id}/pipelines`

> **Deprecated**

[DEPRECATED] Create a new pipeline. Use the new /pipelines/v1/pipelines endpoint instead.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **destination** (object, required): 
- **name** (string, required): Defines the name of the pipeline.
- **source** (array, required): 

## Response

### 200

[DEPRECATED] Indicates a successfully created pipeline. Use /pipelines/v1/pipelines instead.

- **result** (object): [DEPRECATED] Describes the configuration of a pipeline. Use the new streams/sinks/pipelines API instead.
- **success** (boolean): Indicates whether the API call was successful.

### 4XX

Indicates an error in creating a pipeline.

- **errors** (array): 
- **results** (object): 
- **success** (object):
