# List Job Logs

`GET /accounts/{account_id}/ai-search/instances/{id}/jobs/{job_id}/logs`

Lists log entries for an AI Search indexing job.

## Parameters

- **id** (string, required) [path]: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.
- **job_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **page** (integer, optional) [query]: 
- **per_page** (integer, optional) [query]: 

## Response

### 200

Returns a list of AI Search Job Logs.

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
