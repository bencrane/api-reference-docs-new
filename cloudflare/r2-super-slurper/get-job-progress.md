# Get job progress

`GET /accounts/{account_id}/slurper/jobs/{job_id}/progress`

Retrieves current progress metrics for an R2 Super Slurper migration job

## Parameters

- **account_id** (string, required) [path]: 
- **job_id** (string, required) [path]: 

## Response

### 200

Job progress

_Empty object_

### 4XX

Failure response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
