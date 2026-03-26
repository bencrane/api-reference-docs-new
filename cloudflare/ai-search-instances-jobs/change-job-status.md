# Change Job Status

`PATCH /accounts/{account_id}/ai-search/instances/{id}/jobs/{job_id}`

Updates the status of an AI Search indexing job.

## Parameters

- **id** (string, required) [path]: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.
- **job_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **action** (string, required):  Values: `cancel`

## Response

### 200

Returns the updated AI Search Job.

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
