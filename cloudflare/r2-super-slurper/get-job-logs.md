# Get job logs

`GET /accounts/{account_id}/slurper/jobs/{job_id}/logs`

Gets log entries for an R2 Super Slurper migration job, showing migration status changes, errors, etc.

## Parameters

- **account_id** (string, required) [path]: 
- **job_id** (string, required) [path]: 
- **limit** (integer, optional) [query]: 
- **offset** (integer, optional) [query]: 

## Response

### 200

Job logs

_Empty object_

### 4XX

Failure response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
