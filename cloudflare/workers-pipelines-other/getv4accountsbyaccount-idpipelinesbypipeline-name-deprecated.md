# [DEPRECATED] Get Pipeline

`GET /accounts/{account_id}/pipelines/{pipeline_name}`

> **Deprecated**

[DEPRECATED] Get configuration of a pipeline. Use the new /pipelines/v1/pipelines endpoint instead.

## Parameters

- **account_id** (string, required) [path]: 
- **pipeline_name** (string, required) [path]: 

## Response

### 200

[DEPRECATED] Describes the configuration of a pipeline.

- **result** (object): [DEPRECATED] Describes the configuration of a pipeline. Use the new streams/sinks/pipelines API instead.
- **success** (boolean): Indicates whether the API call was successful.

### 404

Indicates that the pipeline was not found.

- **errors** (array): 
- **results** (object): 
- **success** (object):
