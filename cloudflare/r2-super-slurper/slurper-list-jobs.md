# List jobs

`GET /accounts/{account_id}/slurper/jobs`

Lists all R2 Super Slurper migration jobs for the account with their status.

## Parameters

- **account_id** (string, required) [path]: 
- **limit** (integer, optional) [query]: 
- **offset** (integer, optional) [query]: 

## Response

### 200

A list of jobs

_Empty object_

### 4XX

Failure response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
