# Create a job

`POST /accounts/{account_id}/slurper/jobs`

Creates a new R2 Super Slurper migration job to transfer objects from a source bucket (e.g. S3, GCS, R2) to R2.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **overwrite** (boolean, optional): 
- **source** (object, optional): 
- **target** (object, optional): 

## Response

### 201

Job created

_Empty object_

### 409

Maximum number of concurrent jobs has been reached

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.

### 4XX

Failure response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
