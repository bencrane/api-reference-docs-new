# [DEPRECATED] List Pipelines

`GET /accounts/{account_id}/pipelines`

> **Deprecated**

[DEPRECATED] List, filter, and paginate pipelines in an account. Use the new /pipelines/v1/pipelines endpoint instead.

## Parameters

- **account_id** (string, required) [path]: 
- **search** (string, optional) [query]: 
- **page** (string, optional) [query]: 
- **per_page** (string, optional) [query]: 

## Response

### 200

[DEPRECATED] Lists the pipelines. Use /pipelines/v1/pipelines instead.

- **result_info** (object): 
- **results** (array): 
- **success** (boolean): Indicates whether the API call was successful.

### 4XX

Indicates the error trying to list pipelines.

- **errors** (array): 
- **results** (object): 
- **success** (object):
