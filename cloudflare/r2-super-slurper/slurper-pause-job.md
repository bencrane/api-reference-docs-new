# Pause a job

`PUT /accounts/{account_id}/slurper/jobs/{job_id}/pause`

Pauses a running R2 Super Slurper migration job. The job can be resumed later to continue transferring.

## Parameters

- **account_id** (string, required) [path]: 
- **job_id** (string, required) [path]: 

## Response

### 200

Job paused

_Empty object_

### 409

Job is not paused

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.

### 4XX

Failure response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
