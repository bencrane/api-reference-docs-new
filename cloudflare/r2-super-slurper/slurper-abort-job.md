# Abort a job

`PUT /accounts/{account_id}/slurper/jobs/{job_id}/abort`

Cancels a specific R2 Super Slurper migration job. Any objects in the middle of a transfer will finish, but no new objects will start transferring.

## Parameters

- **account_id** (string, required) [path]: 
- **job_id** (string, required) [path]: 

## Response

### 200

Job aborted

_Empty object_

### 4XX

Failure response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
