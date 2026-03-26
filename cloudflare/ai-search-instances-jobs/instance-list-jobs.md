# List Jobs

`GET /accounts/{account_id}/ai-search/instances/{id}/jobs`

Lists indexing jobs for an AI Search instance.

## Parameters

- **id** (string, required) [path]: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.
- **account_id** (string, required) [path]: 
- **page** (integer, optional) [query]: 
- **per_page** (integer, optional) [query]: 

## Response

### 200

Returns a list of AI Search Jobs.

- **result** (array): 
- **result_info** (object): 
- **success** (boolean): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean): 

### 500

Internal Error.

- **errors** (array): 
- **success** (boolean):
