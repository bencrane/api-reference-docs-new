# Get a Job Details

`GET /accounts/{account_id}/ai-search/instances/{id}/jobs/{job_id}`

Retrieves details for a specific AI Search indexing job.

## Parameters

- **id** (string, required) [path]: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.
- **job_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Returns a AI Search Job Details.

- **result** (object): 
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
