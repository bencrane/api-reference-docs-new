# Abort all jobs

`PUT /accounts/{account_id}/slurper/jobs/abortAll`

Cancels all running R2 Super Slurper migration jobs for the account. Any objects in the middle of a transfer will finish, but no new objects will start transferring.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

All jobs aborted

_Empty object_

### 4XX

Failure response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
