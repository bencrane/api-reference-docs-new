# Get a Job Details

`GET /accounts/{account_id}/autorag/rags/{id}/jobs/{job_id}`



## Parameters

- **id** (string, required) [path]: rag id
- **job_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Returns a AutoRAG Job Details

- **result** (object): 
- **success** (boolean): 

### 404

job_not_found

- **errors** (array): 
- **success** (boolean): 

### 503

unable_to_connect_to_autorag

- **errors** (array): 
- **success** (boolean):
