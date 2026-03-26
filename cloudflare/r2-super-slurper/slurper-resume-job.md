# Resume a job

`PUT /accounts/{account_id}/slurper/jobs/{job_id}/resume`

Resumes a paused R2 Super Slurper migration job, continuing the transfer from where it stopped.

## Parameters

- **account_id** (string, required) [path]: 
- **job_id** (string, required) [path]: 

## Response

### 200

Job resumed

_Empty object_

### 4XX

Failure response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
